from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='challenges-index'),
    path("<int:month>",views.monthly_challenge_number),
    path("<str:month>",views.monthly_challenge_name, name='month-challenge')
]
