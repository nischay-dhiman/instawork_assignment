from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember
from .forms import TeamMemberForm

def index(request):
    team_members = TeamMember.objects.all().order_by('id')
    context = {'team_members': team_members, 'team_count': len(team_members)}
    return render(request, 'instaworkapp/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            context = {'form': TeamMemberForm(), 'errors': dict(form.errors) }
            return render(request, 'instaworkapp/form.html', context)
    else:
        context = {'form': TeamMemberForm()}
        return render(request, 'instaworkapp/form.html', context)

def update(request, mem_id):
    team_member = get_object_or_404(TeamMember, id=mem_id)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST or None, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            context = {'form': TeamMemberForm(instance=team_member), 'mem_id': mem_id, 'errors': dict(form.errors)}
            return render(request, 'instaworkapp/form.html', context)
    else:
        team_member = get_object_or_404(TeamMember, id=mem_id)
        context = {'form': TeamMemberForm(instance=team_member), 'mem_id': team_member.id}
        return render(request, 'instaworkapp/form.html', context)

def delete(request, mem_id):
    team_member = get_object_or_404(TeamMember, id=mem_id)
    team_member.delete()
    return redirect(index)
