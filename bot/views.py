from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .eliza import el


def home(request):    
    return render(request, 'bot/home.html')

@require_http_methods(['POST'])
@csrf_exempt
def bot(request):
    message = request.POST['message']
    if message in el.initials:
        response = el.initial()
    else:
        response = el.respond(message)
    
    if response:
        return JsonResponse({"reply": response})
    return JsonResponse({"reply": el.final()})