
from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path("", views.OrdersListView.as_view(), name="index"),
    path("new/", views.OrdersCreateView.as_view(), name="new"),
]