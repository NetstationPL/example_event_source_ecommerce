from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<uuid:pk>/", views.DetailView.as_view(), name="detail"),
    path("new/", views.ProductFormView.as_view(), name="new"),
    path("create/", views.ProductCreateView.as_view(), name="create"),
]
