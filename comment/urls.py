from . import views
from django.urls import path

urlpatterns = [
    path('confession/<int:cf_id>', views.view, name='viewcomment'),
    path('confession/<int:cf_id>/create', views.create, name='createcomment'),
]