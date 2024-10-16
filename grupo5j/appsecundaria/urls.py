from django.urls import path,include
from appsecundaria import views

urlpatterns = [
    path('',views.Index_lista,name="Index_lista"),
]