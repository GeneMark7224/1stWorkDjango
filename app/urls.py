from django.urls import path
from .views import (HomePageView, AboutPageView,
                    ContactPageView, MyprojectPageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),path('contact/', ContactPageView.as_view(), name='contact'),
path('myproject/', MyprojectPageView.as_view(), name='myproject'),
]
