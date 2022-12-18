from django.db import models


class Elevator(models.Model):
    current_floor = models.PositiveIntegerField()
    direction = models.CharField(max_length=5)
    maintenance_status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return "%s"(self.id)


class Request(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField()
    direction = models.CharField(max_length=5)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    is_checked = models.BooleanField(default=False)
    # def __str__(self):
    #     return "%s, %s"(self.elevator, self.updated_at)


class MaintenanceStatus(models.Model):
    elevator = models.OneToOneField(Elevator, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    reason = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, %s"(self.elevator, self.updated_at)
