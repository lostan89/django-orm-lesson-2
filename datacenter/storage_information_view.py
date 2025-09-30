from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit
from django.utils.timezone import localtime


def storage_information_view(request):
    objects_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in objects_in_storage:
        duration = Visit.get_duration(visit)
        non_closed_visits.append(
            {
                "who_entered": visit.passcard,
                "entered_at": localtime(visit.entered_at),
                "duration": Visit.format_duration(duration),
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
