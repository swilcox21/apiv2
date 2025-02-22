from django.urls import path
from .views import ActivityTypeView, ActivityMeView, ActivityClassroomView

app_name = 'activity'
urlpatterns = [
    path('me', ActivityMeView.as_view(), name='root'),
    path('type/', ActivityTypeView.as_view(), name='type'),
    path('type/<str:activity_slug>',
         ActivityTypeView.as_view(),
         name='type_slug'),
    path('academy/cohort/<str:cohort_id>',
         ActivityClassroomView.as_view(),
         name='academy_cohort_id'),
    path('academy/student/<str:student_id>',
         ActivityClassroomView.as_view(),
         name='academy_student_id'),
]
