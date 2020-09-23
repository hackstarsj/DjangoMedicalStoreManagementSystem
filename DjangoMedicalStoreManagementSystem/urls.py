"""DjangoMedicalStoreManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from DjangoMedicalApp import views
from DjangoMedicalApp.views import CompanyNameViewSet, CompanyOnlyViewSet

router=routers.DefaultRouter()
router.register("company",views.CompanyViewSet,basename="company")
router.register("companybank",views.CompanyBankViewset,basename="companybank")
router.register("medicine",views.MedicineViewSet,basename="medicine")
router.register("companyaccount",views.CompanyAccountViewset,basename="companyaccount")
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name="gettoken"),
    path('api/resfresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/companybyname/<str:name>',CompanyNameViewSet.as_view(),name="companybyname"),
    path('api/companyonly/',CompanyOnlyViewSet.as_view(),name="companyonly"),
]
