from django.forms import ModelForm, RadioSelect, TextInput
from instaworkapp.models import TeamMember


class TeamMemberForm(ModelForm):
    # role_choices = [('0', "Regular - Can't delete members"), ('1', "Admin - Can delete members")]
    # assigned_role = forms.CharField(label='Role', widget=forms.RadioSelect(choices=role_choices))
    # first_name = forms.CharField(label='First Name', widget=forms.TextInput(), required=True)
    # last_name = forms.CharField(label='Last Name', widget=forms.TextInput(), required=True)
    # email = forms.EmailField(label='Email', widget=forms.TextInput(), required=True)
    # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        role_choices = [('0', "Regular - Can't delete members"), ('1', "Admin - Can delete members")]
        model = TeamMember
        fields = '__all__'
        widgets = {
            'assigned_role': RadioSelect(),
            'first_name': TextInput(attrs={'required': False, 'class':'form-control', 'placeholder':'First Name'}),
            'last_name': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Phone Number'}),
        }


