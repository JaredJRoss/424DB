from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.model_form_upload, name='home'),
    url(r'^mult$',views.FileFieldView.as_view(), name = 'multiple')
]
