"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.reg, name='reg'),
    path('login/',views.login, name='login'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('pulsar',views.pulsar,name='pulsar'),
    path('ktm',views.ktm,name='ktm'),
    path('passion',views.passion,name='passion'),
    path('sucessfully_regr',views.sucessfully_regr,name='sucessfully_regr'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('thankyou',views.thankyou,name='thankyou')

]
