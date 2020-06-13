from django.shortcuts import render
from mptt_practice.models import Mptt_file


def index(request):
    return render(request, 'index.html', {'nodes': Mptt_file.objects.all()})
