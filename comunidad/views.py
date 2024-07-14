from django.shortcuts import render
from .models import Leyend

# Create your views here.

def history (request):
    projects = Leyend.objects.all()
    return render(request,"comunidad/history.html",{'projects':projects})