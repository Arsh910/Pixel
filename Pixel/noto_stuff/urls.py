from .views import Bugs_in,team_view
from django.urls import path

urlpatterns = [
        path('',team_view,name='home'),
        path('report_bugs/',Bugs_in,name='Bug_in'),
]