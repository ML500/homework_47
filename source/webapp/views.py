from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Goal, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


# from webapp.forms import GoalForm


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
        return redirect('goal_view', pk=goal.pk)


def goal_update_view(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'GET':
        return render(request, 'goal_update.html', context={'status_choices': STATUS_CHOICES,
                                                            'goal': goal})
    elif request.method == 'POST':
        errors = {}
        goal.describe = request.POST.get('describe')
        if not goal.describe:
            errors['describe'] = 'This field is required'
        goal.detail = request.POST.get('detail')
        if not goal.detail:
            errors['detail'] = 'This field is required'
        goal.status = request.POST.get('status')
        if errors:
            return render(request, 'goal_update.html', context={'status_choices': STATUS_CHOICES,
                                                                'goal': goal,
                                                                'errors': errors})
        goal.save()
        return redirect('goal_view', pk=goal.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
