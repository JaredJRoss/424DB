from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.model_form_upload, name='home'),
    url(r'^Category$', views.add_cat, name='Category'),
    url(r'^mult$',views.FileFieldView.as_view(), name = 'multiple'),
    url(r'^basic_search/$', views.basic_search, name= 'basic search'),
    url(r'^search/', include("watson.urls", namespace="watson"), {'template_name' : 'DAGR/search_results.html',})

]
