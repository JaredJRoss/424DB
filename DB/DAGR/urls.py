from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^upload$', views.model_form_upload, name='home'),
    url(r'^Category$', views.add_cat, name='Category'),
    url(r'^mult$',views.FileFieldView.as_view(), name = 'multiple'),
    url(r'^basic_search/$', views.basic_search, name= 'basic search'),
    url(r'^search/', include("watson.urls", namespace="watson"), {'template_name' : 'DAGR/search_results.html',}),
    url(r'^DAGR/(?P<pk>[0-9]+)/$',views.DAGR_Detailview.as_view(),name='dagr_detail'),
    url(r'^$',views.DAGRListView.as_view(),name='home'),
    url(r'^update/(?P<pk>[0-9]+)/$',views.DAGR_Update.as_view(),name='dagr_update'),
    url(r'^reach/(?P<pk>[0-9]+)/$',views.DAGR_Reach,name = 'dagr_reach'),
    url(r'^orphans$',views.DAGR_Sterile,name='dagr_sterile'),
    url(r'^delete/(?P<pk>[0-9]+)/',views.DAGR_Delete,name='delete_page'),
    url(r'^deleteCon/(?P<pk>[0-9]+)/',views.delete,name='delete_confirm')
]
