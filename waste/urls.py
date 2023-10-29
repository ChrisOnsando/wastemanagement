from django.urls import path
from waste import views
from waste.views import (
    BinCreate,
    BinDelete,
    BinDetailView,
    BinListView,
    BinUpdate,
    ComplaintDelete,
    ComplaintDetailView,
    ComplaintListView,
    ComplaintUpdate,
    AllComplaintsListView,
    BinDriverListView,
    DriverComplaintListView,
)
from waste.views import download_receipt_as_pdf

urlpatterns = [
    path("bins/", BinListView.as_view(), name="bins"),
    path("bin/<int:pk>/", BinDetailView.as_view(), name="bin-detail"),
    path('bin_receipt/<int:bin_id>/', download_receipt_as_pdf, name='bin-receipt-pdf'),
    path("bin/create/", BinCreate.as_view(), name="bin-create"),
    path("bin/<int:pk>/update/", BinUpdate.as_view(), name="bin-update"),
    path("bin/<int:pk>/delete/", BinDelete.as_view(), name="bin-delete"),
    path("bin/driver/", BinDriverListView.as_view(), name="driver-bin"),
    path("complaints/", ComplaintListView.as_view(), name="complaints"),
    path("complaint/<int:pk>/", ComplaintDetailView.as_view(), name="complaint-detail"),
    path("complaint/create/", views.new, name="complaint-create"),
    path(
        "complaint/<int:pk>/update/", ComplaintUpdate.as_view(), name="complaint-update"
    ),
    path(
        "complaint/<int:pk>/delete/", ComplaintDelete.as_view(), name="complaint-delete"
    ),
    path("allcomplaints/", AllComplaintsListView.as_view(), name="all-complaints"),
    path("complaints/driver/", DriverComplaintListView.as_view(), name="driver-complaints"),
]
