import random
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from waste.models import Bin, Complaint
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from waste.forms import NewComplaintForm
from random import randint
from django.template.loader import get_template
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.admin.views.decorators import staff_member_required

class BinCreate(UserPassesTestMixin, CreateView):
    model = Bin
    template_name = "waste/bin_create.html"
    success_url = reverse_lazy("bins")
    fields = ['area', 'locality', 'landmark', 'city', 'loadtype', 'best_route', 'price']  # Define the fields you want in your form

    def test_func(self):
        # Check if the user is authenticated
        return self.request.user.is_authenticated

    def calculate_price(self, load_type):
        if load_type == 'low':
            return randint(0, 100)
        elif load_type == 'medium':
            return randint(101, 300)
        elif load_type == 'high':
            return randint(301, 500)

    def form_valid(self, form):
        # Calculate the price based on the selected load type
        load_type = form.cleaned_data['loadtype']
        price = self.calculate_price(load_type)

        # Save the price to the Bin instance
        bin = form.save(commit=False)
        bin.price = price
        bin.save()

        return super().form_valid(form)

class BinListView(generic.ListView):
    model = Bin
    paginate_by = 6
    template_name = "waste/bin_list.html"

class BinDriverListView(LoginRequiredMixin, generic.ListView):
    """
    Show drivers their bins
    """

    model = Bin
    paginate_by = 5
    template_name = "waste/driver_bin_list.html"

    def get_queryset(self):
        return Bin.objects.filter(driveremail=self.request.user.id)


class BinDetailView(generic.DetailView):
    """
    See detail of a single bin
    """

    model = Bin
    template_name = "waste/bin_detail.html"

def download_receipt_as_pdf(request, bin_id):
    bin = Bin.objects.get(pk=bin_id)
    context = {'bin': bin}
    
    # Render the HTML template with the context
    template = get_template('waste/bin_detail.html')  # Replace 'your_template.html' with the actual path to your HTML template
    html_template = template.render(context)
    
    # Create a PDF response
    pdf_response = HttpResponse(content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename="bin_receipt_{bin.id}.pdf"'
    
    # Generate the PDF from the HTML template
    HTML(string=html_template).write_pdf(pdf_response)
    
    return pdf_response

class BinUpdate(UserPassesTestMixin, UpdateView):
    """
    Updating bin by staff
    """

    model = Bin
    fields = [
        "area",
        "locality",
        "landmark",
        "city",
        "driveremail",
        "loadtype",
        "best_route",
    ]
    template_name = "waste/bin_update.html"

    def test_func(self):
        return self.request.user.is_staff


class BinDelete(UserPassesTestMixin, DeleteView):
    """Staff deleting a bin"""

    model = Bin
    success_url = reverse_lazy("bins")
    template_name = "waste/bin_delete.html"

    def test_func(self):
        return self.request.user.is_staff


@login_required
def new(request):
    if request.method == "POST":
        form = NewComplaintForm(request.POST)

        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.email = request.user
            complaint.save()

            return redirect("complaint-detail", pk=complaint.id)
    else:
        form = NewComplaintForm()

    return render(request, "waste/complaint_create.html", {"form": form})


class ComplaintListView(LoginRequiredMixin, generic.ListView):
    """List all complaints created by user"""

    model = Complaint
    template_name = "waste/complaint_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Complaint.objects.filter(email=self.request.user)


class AllComplaintsListView(UserPassesTestMixin, generic.ListView):
    """Staff sees all complaints"""

    model = Complaint
    template_name = "waste/complaints_list.html"
    paginate_by = 6

    def test_func(self):
        return self.request.user.is_staff


class ComplaintDetailView(LoginRequiredMixin, generic.DetailView):
    """Details about a single complaint"""

    model = Complaint
    template_name = "waste/complaint_detail.html"


class ComplaintUpdate(UserPassesTestMixin, UpdateView):
    """Only staff can update the complaint"""

    model = Complaint
    fields = [
        "status",
    ]
    read_only_fields = ["email", "complaint", "bin"]
    template_name = "waste/complaint_update.html"
    def test_func(self):
        return self.request.user.is_staff

   
class ComplaintDelete(LoginRequiredMixin, DeleteView):
    """Deleting a complaint"""

    model = Complaint
    template_name = "waste/complaint_delete.html"
    success_url = reverse_lazy("complaints")

class DriverComplaintListView(LoginRequiredMixin, generic.ListView):
    """
    Driver sees the complaints of bins allocated to them
    """
    model = Complaint
    template_name = "waste/driver_complaint_list.html"
    context_object_name = 'complaints' 

    def get_queryset(self):
        driver_id = self.request.user.id
        return Complaint.objects.filter(bin__driveremail=driver_id)

