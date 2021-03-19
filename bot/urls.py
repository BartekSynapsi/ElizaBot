from django.urls import path
from .views import home, bot
urlpatterns = [
    path('', home),
    path('bot/', bot)
]
