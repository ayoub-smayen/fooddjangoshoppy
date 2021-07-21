from django.urls import path
from customers import views

app_name="customers"
urlpatterns = [
    path('', views.myprofile, name='myprofile'),
    path('profile', views.ProfileView.as_view(), name='profile'),
]
#profile/myprofile