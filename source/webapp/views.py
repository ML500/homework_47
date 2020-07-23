from django.shortcuts import render
from webapp.models import Goal, STATUS_CHOICES


def index_view(request):
    data = Goal.objects.all()
    return render(request, 'index.html', context={
        'goals': data
    })


def goal_create_view(request):
    if request.method == 'GET':
        return render(request, 'create_goal.html', context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        describe = request.POST.get('describe')
        status = request.POST.get('status')
        if request.POST.get('execute_at') == '':
            execute_at = None
        else:
            execute_at = request.POST.get('execute_at')
        goal = Goal.objects.create(describe=describe, status=status, execute_at=execute_at)
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
