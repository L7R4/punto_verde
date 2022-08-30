from .views import homePage, encuestaPage,admin
from django.urls import path

app_name = "market"

urlpatterns = [
    path("", homePage.as_view(), name ="home"),
    path("encuesta/", encuestaPage.as_view(), name = "encuesta"),
    path("admin/",admin.as_view(), name ="admin"),
]

