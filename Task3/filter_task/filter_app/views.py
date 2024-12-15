from django.shortcuts import render
from .models import Box
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

def filter_boxes(request):
    location_filter = request.GET.get('location', 'All Locations')
    category_filter = request.GET.get('category', 'All categories')

    boxes = Box.objects.all()
    if location_filter != 'All Locations':
        boxes = boxes.filter(location=location_filter)
    if category_filter != 'All categories':
        boxes = boxes.filter(category=category_filter)

    locations = Box.objects.values_list('location', flat=True).distinct()
    categories = Box.objects.values_list('category', flat=True).distinct()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # If it's an AJAX request, return only the boxes content
        html = render_to_string('partials/boxes.html', {'boxes': boxes})
        return HttpResponse(html)

    # Otherwise, render the full page
    return render(request, 'filter.html', {
        'boxes': boxes,
        'locations': ['All Locations'] + list(locations),
        'categories': ['All categories'] + list(categories),
        'selected_location': location_filter,
        'selected_category': category_filter,
    })
