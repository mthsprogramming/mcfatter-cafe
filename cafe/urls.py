from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

# URLconf for the McFater Cafe app

app_name = 'cafe'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^menu/', views.MenuView.as_view(), name='menu'),
    url(r'^order/', views.OrderView.as_view(), name='order'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^login/', auth_views.LoginView.as_view(template_name="cafe/login.html"), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^update-profile/', views.update_profile, name='update-profile')
]