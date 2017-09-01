"""ecommerce_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',profiles_views.Home, name='Home'),
    url(r'about/$', profiles_views.About , name="About"),
    url(r'contact/$', contact_views.Contact , name="Contact"),
    url(r'profile/$', profiles_views.UserProfile , name="Profile"),
    url(r'checkout/$', checkout_views.Checkout , name="Checkout"),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^profiles/', include('profiles.urls')),
]
