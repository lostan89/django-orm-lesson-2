from django.db import models
from datetime import timedelta
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(f"leaved at {self.leaved_at}" if self.leaved_at else "not leaved"),
        )

    def get_duration(visit):
        delta = localtime() - visit.entered_at
        return delta

    def format_duration(duration):
        delta_string = timedelta(seconds=int(duration.total_seconds()))
        return delta_string

    def is_visit_long(visit, minutes=60):
        delta = visit.leaved_at - visit.entered_at
        return delta.total_seconds() // 60 > minutes
