from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer
from .constants import ElevatorUpdateType


class ElevatorsServicesCls:
    # Update elevators current floor after any operation perform
    def update_elevators_current_floor(
        self, elevator_id, current_floor, direction=ElevatorUpdateType.Increase
    ):
        if direction == ElevatorUpdateType.Increase:
            Elevator.objects.filter(id=elevator_id).update(
                current_floor=current_floor + 1, direction=direction
            )
        else:
            Elevator.objects.filter(id=elevator_id).update(
                current_floor=current_floor - 1, direction=direction
            )

    # Update request to id checked to mark completed
    def update_request_to_is_checked(self, request_id):
        Request.objects.filter(id=request_id).update(is_checked=True)

    # Next destination for the elevators
    def get_elevators_next_request(self, elevator_id, elevator_status):
        first_request = Request.objects.filter(
            elevator_id=int(elevator_id), is_checked=False
        ).order_by("created_at")[:1]
        if not first_request:
            return {
                "direction": "idel",
                "distination": False,
                "current_floor": int(elevator_status.get("current_floor")),
            }
        request_serializer_data = RequestSerializer(first_request[0]).data
        next_direction = self.get_elevators_next_direction(
            elevator_id, elevator_status, request_serializer_data.get("floor")
        )
        return next_direction

    def get_elevators_next_direction(self, elevator_id, elevator_status, floor_id):
        if int(elevator_status.get("current_floor")) == int(floor_id):
            next_request_stop = Request.objects.filter(
                elevator_id=int(elevator_id),
                floor=int(elevator_status.get("current_floor")),
                is_checked=False,
            ).order_by("created_at")[:1]
            next_request_stop_data = RequestSerializer(next_request_stop[0]).data
            next_request_stop_data.update(
                {
                    "direction": "open and close",
                    "distination": True,
                    "current_floor": int(elevator_status.get("current_floor")),
                }
            )
            self.update_request_to_is_checked(next_request_stop_data.get("id"))

        elif int(elevator_status.get("current_floor")) > int(floor_id):
            next_request_stop = Request.objects.filter(
                elevator_id=int(elevator_id),
                floor__lt=int(elevator_status.get("current_floor")),
                is_checked=False,
            ).order_by("created_at")[:1]
            next_request_stop_data = RequestSerializer(next_request_stop[0]).data
            next_request_stop_data.update(
                {
                    "direction": "down",
                    "distination": False,
                    "current_floor": int(elevator_status.get("current_floor")),
                }
            )
            self.update_elevators_current_floor(
                elevator_id,
                int(elevator_status.get("current_floor")),
                direction=ElevatorUpdateType.Decrease,
            )
        else:
            next_request_stop = Request.objects.filter(
                elevator_id=int(elevator_id),
                floor__gt=int(elevator_status.get("current_floor")),
                is_checked=False,
            ).order_by("created_at")[:1]
            next_request_stop_data = RequestSerializer(next_request_stop[0]).data
            next_request_stop_data.update(
                {
                    "direction": "up",
                    "distination": False,
                    "current_floor": int(elevator_status.get("current_floor")),
                }
            )
            self.update_elevators_current_floor(
                elevator_id,
                int(elevator_status.get("current_floor")),
                direction=ElevatorUpdateType.Increase,
            )
        return next_request_stop_data


ElevatorsServices = ElevatorsServicesCls()
