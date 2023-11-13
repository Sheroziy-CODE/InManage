from django.urls import path
from authy.views import login_view, profile_view, workers_view, login_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', login_page, name='login'),
    path('login/', login_view, name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>', profile_view, name='profile'),
    path('workers/', workers_view, name='workers'),
]
