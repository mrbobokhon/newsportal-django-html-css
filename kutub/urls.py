from django.urls import path
from .views import KutubIndex

app_name = 'kutub'

urlpatterns = [
    path('', KutubIndex.as_view(), name="index"),
]