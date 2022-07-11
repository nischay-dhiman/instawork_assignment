from django.core.validators import RegexValidator
from django.db import models


class TeamMember(models.Model):
    ROLE_CHOICES = [
        (0, "Regular - Can't delete members"),
        (1, "Admin - Can delete members")
    ]

    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    assigned_role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=False, blank=False)

    def role_text(self):
        if self.assigned_role == 1:
            return " (admin) "
        else:
            return ""
