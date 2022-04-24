from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('login_page', views.login_page, name='login_page'),
    path('registration', views.registration, name='registration'),
    path('get_data', views.home, name='home'),
    path('post_data', views.entry, name='entry'),
    path('home-page', views.index_page, name='index_page')
]
