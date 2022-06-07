from django.urls import path
from .views import account_regis, account_login, account_logout

app_name = "account"

urlpatterns = [
    path('regis/', account_regis, name="regis"),
    path('login/', account_login, name="login"),
    path('logout/', account_logout, name="logout"),
]
