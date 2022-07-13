from django.forms import ModelForm, RadioSelect, TextInput
from instaworkapp.models import TeamMember


class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        widgets = {
            'assigned_role': RadioSelect(),
            'first_name': TextInput(attrs={'required': False, 'class':'form-control', 'placeholder':'First Name'}),
            'last_name': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Phone Number'}),
        }


