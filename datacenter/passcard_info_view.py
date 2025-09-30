from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard_object = get_object_or_404(Passcard, passcode=passcode)
    visits_filtred_by_passcard = Visit.objects.filter(passcard=passcard_object)
    this_passcard_visits = []
    for visit in visits_filtred_by_passcard:
        duration = visit.leaved_at - visit.entered_at
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": Visit.format_duration(duration),
                "is_strange": Visit.is_visit_long(visit),
            }
        )
    context = {
        "passcard": passcard_object,
        "this_passcard_visits": this_passcard_visits,
    }
    return render(request, "passcard_info.html", context)
