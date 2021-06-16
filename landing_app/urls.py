from django.urls import path
from landing_app.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name = 'landing_page'),
]