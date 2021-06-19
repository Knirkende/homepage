from django.urls import path
from landing_app.views import LandingPageView, ibsen_view

urlpatterns = [
#    path('', LandingPageView.as_view(), name = 'landing_page'),
    path('', ibsen_view, name = 'landing_page'),
]