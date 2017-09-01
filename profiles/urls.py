from django.conf.urls import url

# importing views
from . import views

app_name = 'profiles'

urlpatterns = [
    # Default homepage (index)
    url(r'^$', views.Home, name='Home'),
]
