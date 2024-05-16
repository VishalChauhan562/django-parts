from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='challenges-index'),
    path("month-detail/", views.month_list),
    path("month-detail/<int:pk>", views.month_detail, name='month-detail'),
    path("temp-view/<int:id>",views.monthly_challenge_name, name='month-challenge'),
    path("month-create/",views.month_create)
    
]
