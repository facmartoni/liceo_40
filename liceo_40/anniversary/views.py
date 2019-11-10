from django.shortcuts import render
from django.http import HttpResponse

# path('admin/', admin.site.urls),
# path('', views.home, name='home'),
# path('fotos', views.photos, name="photos"),
# path('historia', views.history, name="history"),
# path('inscripcion', views.register, name="register"),
# path('asistentes', views.attendees, name="attendees"),


def home(request):
    return render(request, 'home.html')


def photos(request):
    return render(request, 'photos.html')


def history(request):
    return render(request, 'history.html')


def register(request):
    return render(request, 'register.html')


def attendees(request):
    return render(request, 'attendees.html')
