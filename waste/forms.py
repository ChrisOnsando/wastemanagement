from django import forms
from waste.models import Complaint


class NewComplaintForm(forms.ModelForm):
    """
    Allow customers create complaints
    """

    class Meta:
        model = Complaint
        fields = (
            "bin",
            "complaint",
        )
        widgets = {
            "bin": forms.Select(attrs={"placeholder": "select bin"}),
            "complaint": forms.Textarea(attrs={"placeholder": "Write your complaint"}),
        }
