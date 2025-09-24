from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit
from django.utils.timezone import localtime


def storage_information_view(request):
    visit_objects = Visit.objects.all()
    print(visit_objects)
    unleaved_objects = Visit.objects.filter(leaved_at=None)
    for unleaved_object in unleaved_objects:
        print(Passcard.objects.get(owner_name=unleaved_object.passcard))
    duration = Visit.get_duration(unleaved_objects[0])
    non_closed_visits = [
        {
            "who_entered": unleaved_objects[0].passcard,
            "entered_at": localtime(unleaved_objects[0].entered_at),
            "duration": Visit.format_duration(duration),
        }
    ]
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
