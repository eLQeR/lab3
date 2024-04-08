from django.urls import path
from shop.views import HomePageView, about, about_company

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('^about/$', about, name='about'),
    path('^about/company/$', about_company, name='about_company'),
    ]