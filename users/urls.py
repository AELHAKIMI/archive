from django.conf.urls import url, re_path
from . import views
urlpatterns = [
    url(r'^changepassword/$', views.change_password, name='change_password')
]