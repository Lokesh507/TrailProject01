from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index')
    path('', views.home, name='home'),
    path('data_form', views.entry, name='entry'),
    path('post_data', views.entry, name='entry')
]
