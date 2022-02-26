from django.urls import path
from signup import views

app_name = 'home'

urlpatterns = [
    path('', views.signup, name='signup'),
]