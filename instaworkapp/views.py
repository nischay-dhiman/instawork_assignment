from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import TeamMember
from .forms import TeamMemberForm

class TeamMemberListView(ListView):
    model = TeamMember
    context_object_name = 'team_members'

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('teammember-index')



class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('teammember-index')

class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('teammember-index')
