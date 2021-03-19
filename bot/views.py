from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'bot/home.html')

@require_http_methods(['POST'])
@csrf_exempt
def bot(request):
    message = request.POST['message']
    import time
    return JsonResponse({"test": message})