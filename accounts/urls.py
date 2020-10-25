from django.urls import path
from accounts import views

app_name = 'accounts'


urlpatterns = [
    path('', views.index_page),
    path('api/users/', views.UserCreate.as_view(), name='account-create'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]