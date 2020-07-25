from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Goal, STATUS_CHOICES

from django.urls import reverse


def index_view(request):
    data = Goal.objects.all()
    return render(request, 'index.html', context={
        'goals': data
    })


def goal_view(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    context = {'goal': goal}
    return render(request, 'goal_view.html', context)


def goal_create_view(request):
    if request.method == 'GET':
        return render(request, 'create_goal.html', context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        describe = request.POST.get('describe')
        detail = request.POST.get('detail')
        status = request.POST.get('status')
        if request.POST.get('execute_at') == '':
            execute_at = None
        else:
            execute_at = request.POST.get('execute_at')
        goal = Goal.objects.create(describe=describe, status=status, detail=detail, execute_at=execute_at)
        context = {'goal': goal}
        return render(request, 'goal_view.html', context)


def delete_goal(request):
    if request.method == 'GET':
        data = Goal.objects.all()
        return render(request, 'delete_form.html', context={
            'goals': data
        })
    elif request.method == 'POST':
        id_goal = request.POST.get('id')
        goal = Goal.objects.get(pk=id_goal)
        goal.delete()
        data = Goal.objects.all()
        return render(request, 'index.html', context={
            'goals': data
        })
