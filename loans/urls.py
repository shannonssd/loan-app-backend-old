from django.urls import path
from . import views

urlpatterns = [
  path("", views.get_listings_or_add_loan, name="retrieve all listings or add new loan"),
  path("<int:listing_id>/", views.get_listing_and_repayment, name="retrieve listing and repayment data")
]