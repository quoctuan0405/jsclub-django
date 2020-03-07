from . import views
from django.urls import path

urlpatterns = [
	path('', views.home, name='homeconfession'),
    path('create', views.create, name='createconfession'),
    path('<int:cf_id>', views.detail, name='detailconfession')
]