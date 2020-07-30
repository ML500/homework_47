from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Goal, STATUS_CHOICES
from django.http import HttpResponseNotAllowed

from webapp.forms import GoalForm


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
        return render(request, 'create_goal.html', context={
            'form': GoalForm()
        })
    elif request.method == 'POST':
        form = GoalForm(data=request.POST)
        if form.is_valid():
            goal = Goal.objects.create(
                describe=form.cleaned_data['describe'],
                detail=form.cleaned_data['detail'],
                execute_at=form.cleaned_data['execute_at'],
                status=form.cleaned_data['status'],
            )
            return redirect('goal_view', pk=goal.pk)
        else:
            return render(request, 'create_goal.html', context={
                'form': form
            })


def goal_update_view(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'GET':
        form= GoalForm(initial={
            'describe': goal.describe,
            'detail': goal.detail,
            'status': goal.status,
            'execute_at': goal.execute_at,
        })
        return render(request, 'goal_update.html', context={
            'form': form,
            'goal': goal
        })
    elif request.method == 'POST':
        form = GoalForm(data=request.POST)
        if form.is_valid():
            goal.describe = form.cleaned_data['describe']
            goal.detail = form.cleaned_data['detail']
            goal.status = form.cleaned_data['status']
            goal.execute_at = form.cleaned_data['execute_at']
            goal.save()
            return redirect('goal_view', pk=goal.pk)
        else:
            return render(request, 'goal_update.html', context={
                'goal': goal,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def goal_delete_view(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_goal.html', context={'goal': goal})
    elif request.method == 'POST':
        goal.delete()
        return redirect('index')
