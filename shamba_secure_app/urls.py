from django.urls import path, include
from . import views
# from django.contrib.auth.views import LoginView,LogoutView
# from django.conf import settings
# from django.conf.urls.static import static



urlpatterns = [
    path('', views.home),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('real-estate-dash/', views.real_estate_dash, name='real-estate-dash'),

]