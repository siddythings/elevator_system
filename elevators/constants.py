class Enum:
    def __contains__(self, item: str) -> bool:
        if hasattr(self, "_value_set"):
            return item in self._value_set
        self._value_set = set()
        for key in dir(self):
            if (key.endswith("__") and key.startswith("__")) or key == "_value_set":
                pass
            else:
                self._value_set.add(getattr(self, key))
        return item in self._value_set


def instantiate(cls):
    return cls()


@instantiate
class ElevatorUpdateType(Enum):
    Increase = 1
    Decrease = 0


@instantiate
class ElevatorMaintenanceUpdateType(Enum):
    Available = True
    OnMaintenance = False
