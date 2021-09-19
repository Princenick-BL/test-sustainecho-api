from django.urls import path
from .views import EmployeeView,PaysView,MarqueView,VilleView


urlpatterns = [
    path('employes', EmployeeView.as_view()),
    path('pays', PaysView.as_view()),
    path('ville', VilleView.as_view()),
    path('marques', MarqueView.as_view()),
]
