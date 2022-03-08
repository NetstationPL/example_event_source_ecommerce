from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path("", views.OrdersListView.as_view(), name="index"),
    path("new/", views.OrdersCreateView.as_view(), name="new"),
    path(
        "<uuid:order_id>/add_item/", views.OrdersAddItemView.as_view(), name="add_item"
    ),
    path(
        "<uuid:order_id>/remove_item/",
        views.OrdersRemoveItemView.as_view(),
        name="remove_item",
    ),
    path("<uuid:order_id>/edit/", views.OrdersEditView.as_view(), name="edit"),
]
