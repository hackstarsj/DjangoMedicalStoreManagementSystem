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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from DjangoMedicalApp import views
from DjangoMedicalApp.views import CompanyNameViewSet, CompanyOnlyViewSet,MedicineByNameViewSet
from DjangoMedicalStoreManagementSystem import settings

router=routers.DefaultRouter()
router.register("company",views.CompanyViewSet,basename="company")
router.register("companybank",views.CompanyBankViewset,basename="companybank")
router.register("medicine",views.MedicineViewSet,basename="medicine")
router.register("companyaccount",views.CompanyAccountViewset,basename="companyaccount")
router.register("employee",views.EmployeeViewset,basename="employee")
router.register("employee_all_bank",views.EmployeeBankViewset,basename="employee_all_bank")
router.register("employee_all_salary",views.EmployeeSalaryViewset,basename="employee_all_salary")
router.register("generate_bill_api",views.GenerateBillViewSet,basename="generate_bill_api")
router.register("customer_request",views.CustomerRequestViewset,basename="customer_request")
router.register("home_api",views.HomeApiViewset,basename="home_api")

import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name="gettoken"),
    path('api/resfresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/companybyname/<str:name>',CompanyNameViewSet.as_view(),name="companybyname"),
    path('api/medicinebyname/<str:name>',MedicineByNameViewSet.as_view(),name="medicinebyname"),
    path('api/companyonly/',CompanyOnlyViewSet.as_view(),name="companyonly"),
    path('api/employee_bankby_id/<str:employee_id>',views.EmployeeBankByEIDViewSet.as_view(),name="employee_bankby_id"),
    path('api/employee_salaryby_id/<str:employee_id>',views.EmployeeSalaryByEIDViewSet.as_view(),name="employee_salaryby_id"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
