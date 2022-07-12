from django.urls import path
from instaworkapp import views

urlpatterns = [
    path(r'', views.TeamMemberListView.as_view(), name="teammember-index"),
    path(r'create/', views.TeamMemberCreateView.as_view(), name="teammember-create"),
    path(r'update/<pk>', views.TeamMemberUpdateView.as_view(), name="teammember-update"),
    path(r'delete/<pk>', views.TeamMemberDeleteView.as_view(), name="teammember-delete"),
]
