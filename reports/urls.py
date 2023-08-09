from django.urls import path
from .views import insertDataForDB,combinaterPaternOfFileToExcel

urlpatterns = [
    path("",insertDataForDB),
    path("transform/",combinaterPaternOfFileToExcel),
]
