from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^emprego/(?P<post_id>\w+)$', views.emprego_by_idList.as_view(), name='emprego-list'),
    url(r'^utilizador/(?P<post_id>\w+)$', views.utilizador_by_idList.as_view(), name='emprego-list'),
    url(r'^empresa/(?P<post_id>\w+)$', views.empresa_by_idList.as_view(), name='emprego-list'),
    url(r'^emprego/$', views.empregoList.as_view(), name='emprego-list'),
    url(r'^utilizador/$', views.utilizadorList.as_view(), name='emprego-list'),
    url(r'^empresa/$', views.empresaList.as_view(), name='emprego-list'),
    
    url(r'^auth/login_user', views.login_user, name='login_user'),
    url(r'^auth/login_empresa', views.login_empresa, name='login_empresa'),

    url(r'^auth/register_user', views.register_user, name='register_user'),
    url(r'^auth/register_empresa', views.register_empresa, name='register_empresa'),
]