
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from sonakshi import views

urlpatterns = [
path('',views.index,name="index"),
path('contact/',views.contact,name="contact"),
path('act/',views.act, name="act"),
path('about/',views.about, name="about"),
path('services/',views.services,name="services"),
path('team/',views.team,name="team"),
]
