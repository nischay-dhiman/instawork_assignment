from django.test import TestCase

from instaworkapp.models import TeamMember

class TeamMemberTestCase(TestCase):
    def setUp(self):
        TeamMember.objects.create(first_name="lion", last_name="king", email="lionking@gmail.com", phone_number="+19998887776", assigned_role=1)
        TeamMember.objects.create(first_name="cow", last_name="mammal", email="cowmammal@gmail.com", phone_number="+19998887776")

    def test_team_member_role_text(self):
        king = TeamMember.objects.get(email="lionking@gmail.com")
        mammal = TeamMember.objects.get(email="cowmammal@gmail.com")
        self.assertEqual(king.role_text(), ' (admin) ')
        self.assertEqual(mammal.role_text(), '')


    def test_team_member_default_role(self):
        team_member = TeamMember.objects.create(first_name="lion", last_name="king", email="email@gmail.com", phone_number="+19989987886")
        self.assertEqual(team_member.assigned_role, 0)
