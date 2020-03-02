
from django.urls import path
from .views import index, redirect_view

urlpatterns = [
    path('', index, name='urlsorter'),
    path('link/<str:link>/', redirect_view, name='redirect_url'),

]