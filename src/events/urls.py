from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
        path('', views.events, name='events'),
        path('<str:event_slug>', views.event, name='event_info'),
        path('<str:event_slug>/challenge/<str:chall_slug>', views.chall_event_info, name='event_chall_info'),
        path('pwd/<str:event_slug>', views.submit_pwd, name='submit_pwd'),
        path('submitEventFlag/<str:event_slug>/<str:chall_slug>', views.submit_event_flag, name='submit_event_flag'),
        path('subscribe/<str:event_slug>', views.subscribe_to_event, name='subscribe_event'),
        path('create_team/<str:event_slug>', views.create_team, name='create_team'),
         path('join_team/<str:event_slug>', views.join_team, name='join_team'),
]
