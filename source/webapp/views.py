from django.shortcuts import render
from webapp.models import Goal


def index_view(request):
    data = Goal.objects.all()
    return render(request, 'index.html', context={
        'goals': data
    })
