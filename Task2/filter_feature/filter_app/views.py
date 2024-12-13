from django.shortcuts import render
from .models import *
# Create your views here.

def filter_boxes(request):
    location_filter = request.GET.get('location', 'All')
    if location_filter and location_filter != 'All Locations':
        boxes = Box.objects.filter(location=location_filter)
    else:
        boxes = Box.objects.all()

    locations = Box.objects.values_list('location', flat=True).distinct()
    return render(request, 'filter_boxes.html', {
        'boxes': boxes,
        'locations': ['All Locations'] + list(locations),
        'selected_location': location_filter,
    })
