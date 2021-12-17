from django.urls import path
from .import views


urlpatterns = [

    path('addlaptop/', views.addLaptop, name='add_laptop'),
    path('showlaptop/', views.showLaptop, name='show_laptop'),
    path('updatelaptop/<int:i>', views.updateLaptop, name='update_laptop'),
    path('deletelaptop/<int:i>', views.deleteLaptop, name='delete_laptop'),



]