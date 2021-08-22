from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('login/', views.login, name='login_page'),
    path('register/', views.register, name='register_page'),
    path('logout/', views.logout, name='logout_page'),
    path('tours/', views.tours_list, name='tours_list'),
    # path('tours/<int:pk>/', views.ToursDetail.as_view(), name='tours_detail'),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('creaete/', views.rev_create, name='rev_create'),


]
