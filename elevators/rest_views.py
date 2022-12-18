from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from elevator_system import responses
from .models import Elevator, Request, MaintenanceStatus
from .serializers import ElevatorSerializer, RequestSerializer
from .services import ElevatorsServices
from .constants import ElevatorMaintenanceUpdateType


class ElevatorInitializeView(APIView):
    def post(self, request):
        requested_data = request.data
        num_elevators = int(requested_data.get("num_elevators"))
        if not num_elevators:
            return responses.BadRequestResponse(
                message="Missing parameter: num_elevators"
            )
        try:
            num_elevators = int(num_elevators)
        except ValueError:
            return responses.BadRequestResponse(
                message="Invalid value for parameter: num_elevators"
            )
        for i in range(num_elevators):
            elevator = Elevator.objects.create(
                current_floor=0, direction="", maintenance_status=""
            )

        return responses.SuccessResponse(
            data={
                "num_elevators": num_elevators,
                "elevators": [e.id for e in Elevator.objects.all()],
            },
            message="Elevators",
        )


class ElevatorRequestsView(APIView):
    def post(self, request, elevator_id):
        request_data = request.data
        floor = request_data.get("floor")
        if not floor or not str(floor) != "0":
            return responses.BadRequestResponse(message="Missing parameter: floor")
        try:
            floor = int(floor)
        except ValueError:
            return responses.BadRequestResponse(
                message="Invalid value for parameter: floor"
            )
        elevator = get_object_or_404(Elevator, id=int(elevator_id))
        requests = Request.objects.create(elevator=elevator, floor=floor)
        serializer = RequestSerializer(requests)
        return responses.SuccessResponse(data=serializer.data, message="Elevator")


class ElevatorStatusRequestView(APIView):
    def post(self, request, elevator_id):
        elevator = get_object_or_404(Elevator, id=int(elevator_id))
        elevator_serializer = ElevatorSerializer(elevator).data
        if not elevator_serializer.get("maintenance_status"):
            return {
                "direction": "Elevator On Maintence",
                "distination": False,
                "current_floor": 0,
            }
        elevator_next_request = ElevatorsServices.get_elevators_next_request(
            elevator_id, elevator_serializer
        )
        return responses.SuccessResponse(data=elevator_next_request, message="Elevator")


class ElevatorMaintenanceStatusView(APIView):
    def post(self, request, elevator_id):
        request_data = request.data
        MaintenanceStatus.objects.create(
            elevator_id=elevator_id,
            status=request_data.get("status"),
            reason=request_data.get("reason"),
        )

        if request_data.get("status") == ElevatorMaintenanceUpdateType.Available:
            Elevator.objects.filter(id=elevator_id).update(
                maintenance_status=ElevatorMaintenanceUpdateType.Available
            )
        else:
            Elevator.objects.filter(id=elevator_id).update(
                maintenance_status=ElevatorMaintenanceUpdateType.OnMaintenance
            )

        return responses.SuccessResponse(data={}, message="Elevator")
