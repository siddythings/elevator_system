from elevators import rest_views
from django.urls import path

urlpatterns = [
    path(
        "api/elevator-system/initialize/", rest_views.ElevatorInitializeView.as_view()
    ),
]
