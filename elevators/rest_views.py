from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from elevator_system import responses
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer


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
            Elevator.objects.create(
                current_floor=0, direction="", maintenance_status=""
            )
        return responses.SuccessResponse(
            data={
                "num_elevators": num_elevators,
                "elevators": [e.id for e in Elevator.objects.all()],
            },
            message="Elevators",
        )
