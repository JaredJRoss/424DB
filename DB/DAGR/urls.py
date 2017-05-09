from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^upload$', views.model_form_upload, name='home'),
    url(r'^Category$', views.add_cat, name='Category'),
    url(r'^mult$',views.FileFieldView.as_view(), name = 'multiple'),
    url(r'^basic_search/$', views.basic_search, name= 'basic search'),
    url(r'^search/', include("watson.urls", namespace="watson"), {'template_name' : 'DAGR/search_results.html',}),
    url(r'^$',views.tables,name='home'),
    url(r'DAGR/(?P<pk>[0-9]+)/$',views.DAGR_Detailview.as_view(),name='dagr_detail'),
    url(r'DAGR/',views.DAGRListView.as_view(),name='DAGR List View'),
    url(r'update/(?P<pk>[0-9]+)/$',views.DAGR_Update.as_view(),name='dagr_update'),

]
