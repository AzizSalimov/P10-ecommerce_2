# from django.contrib.auth.views import LogoutView
# from django.urls import path
#
# from account.views import AccountLoginView, profile
#
# app_name = "account"
#
# urlpatterns = [
#     path("login/", AccountLoginView.as_view(), name="login"),
#     path("logout/", LogoutView.as_view(), name="logout"),
#     path("profile/", profile, name = 'profile')
#]

from django.urls import path
from .views import login_view, profile_view, logout_view, AccountLoginView

app_name = 'account'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
    path('account', logout_view, name='account'),
    path('logout/', logout_view, name='logout'),
]


