
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from sonakshi import views

urlpatterns = [
    path('',views.index,name="index"),
    path('elements/',views.index,name="elements"),
]
