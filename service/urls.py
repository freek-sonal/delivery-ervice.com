from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('homepage/',views.firstPage),
    path('restaurants/',views.restaurantPage),
    path('signup/',views.signup),
    path('login/',TemplateView.as_view(template_name="login.html")),
]
