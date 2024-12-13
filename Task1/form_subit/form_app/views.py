from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

# Create your views here.
def render_form(request):
    return render(request, 'form.html')


@csrf_exempt
def form_submit(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            name = data.get("name")
            email = data.get("email")

            # Save data to the database
            FormData.objects.create(name=name, email=email)

            print(f"Received Data: {data}")  # Logs the data in the terminal
            return JsonResponse({"message": "Data saved successfully!"})
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    return JsonResponse({"error": "Invalid request method!"}, status=400)

