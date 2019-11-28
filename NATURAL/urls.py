"""NATURAL URL Configuration

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
from django.conf.urls import url
from django.urls import path,include,re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from recycler.views import CompanySignUpView,SignUpView
from recycle.views import ConsumerSignUpView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('recycle/', include('recycle.urls')),
    path('recycler/', include('recycler.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/recycle/', ConsumerSignUpView.as_view(), name='consumer_signup'),
    path('accounts/signup/recycler/', CompanySignUpView.as_view(), name='company_signup'),
    re_path(r'^', include('recycle.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)