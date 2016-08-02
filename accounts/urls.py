from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^settings/$', login_required(views.settings), name='settings')
]