from elevators import rest_views
from django.urls import path

urlpatterns = [
    path(
        "api/elevator-system/initialize/", rest_views.ElevatorInitializeView.as_view()
    ),
    path(
        "api/elevators/<elevator_id>/requests/",
        rest_views.ElevatorRequestsView.as_view(),
    ),
    path(
        "api/elevators/<elevator_id>/next-destination/",
        rest_views.ElevatorStatusRequestView.as_view(),
    ),
    path(
        "api/elevators-maintenance/{elevator_id}/",
        rest_views.ElevatorMaintenanceStatusView.as_view(),
    ),
]
