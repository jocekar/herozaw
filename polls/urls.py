from django.urls import views
from polls import views

urlpatterns = [
    path('', views.index, name='indexpage')
]
