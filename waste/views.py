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


class BinCreate(UserPassesTestMixin, CreateView):
    """
    Creation a bin by staff
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
    template_name = "waste/bin_create.html"
    success_url = reverse_lazy("bins")

    def test_func(self):
        return self.request.user.is_staff


class BinListView(generic.ListView):
    """
    List all bins
    """

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
