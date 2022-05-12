from django.urls import path
  
# importing views from views..py
from .views import signup_view, login_view
  
urlpatterns = [
    path('signup', signup_view, name="signup"),
    path('login', login_view, name='login')
]