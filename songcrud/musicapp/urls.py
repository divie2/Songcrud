from django.urls import path

# from musicapp import views
from .views import index

urlpatterns = [
    path ("" , index, name= 'index')
]
