from django.urls import path,include
from .views import dashboard_view,register_user
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('register/',register_user, name='register'),
    path('oauth/',include('social_django.urls'))
]