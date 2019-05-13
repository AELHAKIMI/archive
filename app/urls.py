from django.conf.urls import url
from . import views
urlpatterns = [
    ######################  Archive
    url(r'^index/$', views.ArchiveListView.as_view(), name='index-view' ),
    url(r'^add/$', views.ArchiveCreateView.as_view(), name='create-view'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ArchiveDetailView.as_view(), name='detail-view'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ArchiveDeleteView.as_view(), name='delete-view'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ArchiveUpdateView.as_view(), name='update-view'),
    ######################  WorkList

    url(r'^worklist/index/$', views.WorklistListView.as_view(), name='worklist-index-view'),
    url(r'^worklist/add/$', views.WorkListCreateView.as_view(), name='worklist-create-view'),
    url(r'^worklist/detail/(?P<pk>[0-9]+)/$', views.WorkListDetailView.as_view(), name='worklist-detail-view'),
]