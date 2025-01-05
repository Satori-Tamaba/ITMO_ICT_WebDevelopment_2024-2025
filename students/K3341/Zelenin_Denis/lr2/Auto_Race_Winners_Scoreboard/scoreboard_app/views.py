from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import User
from .models import Driver
from .models import Race
from .models import Truck
from .models import Comments


# Create your views here.

def show_user(request, user_slug):
    user = get_object_or_404(User, slug=user_slug)
    return render(request, 'score/show_user.html', {'user': user})


def show_driver(request, driver_slug):
    driver = get_object_or_404(Driver, slug=driver_slug)
    car = driver.car_id
    return render(request, 'score/driver_details.html', {'driver': driver, 'car': car})

def detail_race(request, race_id):

    context_race = (
        Race.objects.filter(truck_id=race_id)
        .select_related('Driver_id', 'truck_id')
        .order_by('-end_position')
    )

    return render(request, 'score/race_details.html', {'races': context_race})
