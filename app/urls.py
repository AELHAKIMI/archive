from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'index/$', views.ArchiveListView.as_view(), name='index-view' ),
    url(r'^add/$', views.ArchiveCreateView.as_view(), name='create-view'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ArchiveDetailView.as_view(), name='detail-view'),
]