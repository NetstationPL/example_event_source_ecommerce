from django.urls import path

from . import views

app_name = "customers"
urlpatterns = [
    path("", views.CustomerListView.as_view(), name="index"),
    path("new/", views.CustomerCreateView.as_view(), name="new"),
]
