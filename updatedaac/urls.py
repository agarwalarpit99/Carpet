from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
    path('about',views.about,name="about"),
    path('custom',views.custom,name='custom'),
    path('infrastructure',views.infrastructure,name="infrastructure"),
    path('contact',views.contact,name="contact"),
]
#class="container"  data-spy="scroll" data-target="#navbar-example2" data-offset="0" id="about"