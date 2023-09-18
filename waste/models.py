from django.db import models
from accounts.models import Driver, User
from django.urls import reverse


class Bin(models.Model):
    """
    The collection bin model.
    Foreign key with Driver model.
    Ease allocation of bin.
    """

    area = models.CharField(
        max_length=200,
    )
    locality = models.CharField(
        max_length=200,
    )
    landmark = models.CharField(
        max_length=200,
    )
    city = models.CharField(
        max_length=200,
    )
    driveremail = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    LOAD_TYPE = (
        ("h", "High"),
        ("m", "Medium"),
        ("l", "Low"),
    )
    loadtype = models.CharField(
        max_length=1,
        choices=LOAD_TYPE,
        blank=True,
        default="l",
        help_text="Type of Load",
    )
    best_route = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse("bin-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return self.area


class Complaint(models.Model):
    """
    Customer can create complaint
    Complaint has to be related to bin
    """

    bin = models.ForeignKey(Bin, on_delete=models.SET_NULL, null=True)
    email = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    complaint = models.TextField(max_length=1000)

    COMPLAINT_STATUS = (
        ("p", "Pending"),
        ("i", "InProgress"),
        ("a", "Approved"),
    )
    status = models.CharField(
        max_length=1,
        choices=COMPLAINT_STATUS,
        blank=True,
        default="p",
        help_text="Status",
    )

    def get_absolute_url(self):
        return reverse("complaint-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return self.bin
