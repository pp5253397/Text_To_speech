from django.urls import path
from .views import LoginView,RegisterView,IndexView,logout

urlpatterns = [
    path('', LoginView,name = 'login'),
    path('register/',RegisterView,name = 'register'),
    path('index/',IndexView,name = 'index'),
    path('logout/',logout,name = 'logout')

]