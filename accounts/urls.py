from django.urls import path
from accounts.views import (
    SignUpView,
    DriverDeleteView,
    DriverDetailView,
    DriverSignUpView,
    DriverUpdateView,
    CustomerDeleteView,
    CustomerDetailView,
    CustomerSignUpView,
    CustomerUpdateView,
    UserDetailView,
    UserListView,
    UserDeleteView,
    UserUpdateView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/driver/", DriverSignUpView.as_view(), name="driver-signup"),
    path("signup/customer/", CustomerSignUpView.as_view(), name="customer-signup"),
    path("users/", UserListView.as_view(), name="users"),
    path("user/<int:pk>/detail/", UserDetailView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("profile/<int:pk>/driver/", DriverDetailView.as_view(), name="driver-profile"),
    path("update/<int:pk>/driver/", DriverUpdateView.as_view(), name="driver-update"),
    path("delete/<int:pk>/driver/", DriverDeleteView.as_view(), name="driver-delete"),
    path(
        "profile/<int:pk>/customer/",
        CustomerDetailView.as_view(),
        name="customer-profile",
    ),
    path(
        "update/<int:pk>/customer/",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "delete/<int:pk>/customer/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
]
