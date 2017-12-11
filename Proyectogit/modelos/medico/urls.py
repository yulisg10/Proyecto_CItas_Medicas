from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from modelos.medico.views import index, registro_success
from modelos.medico.views import MedicoCreate, MedicoUpdate
# #CRUD por funciones 
# urlpatterns = [ 
#     url(r'^inicio$', index, name='inicio'),
#     url(r'^nuevo$', usuario_view, name='crear_usuario'),
#     url(r'^listar$', usuario_list, name='listar_usuario'),
#     url(r'^editar/(?P<id_usuario>\d+)/$', usuario_edit, name='editar_usuario'),
#     url(r'^eliminar/(?P<id_usuario>\d+)/$', usuario_delete, name='eliminar_usuario'),
# ]

#CRUD por clases
# urlpatterns = [ 
#     url(r'^inicio$', index, name='inicio'),
#     url(r'^nuevo$', MedicoCreate.as_view(), name='crear_usuario'),
#     url(r'^listar$', UsuarioList.as_view(), name='listar_usuario'),
#     url(r'^editar/(?P<pk>\d+)/$', MedicoUpdate.as_view(), name='editar_usuario'),
#     url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='eliminar_usuario'),


urlpatterns = [ 
#           ruta url usuario   
     url(r'^inicio$', login_required(index) , name='inicio'),
     url(r'^nuevo$', MedicoCreate.as_view(), name='registrar'),
     url(r'^registro_success$', registro_success, name='success'),
     url(r'^editar/(?P<pk>\d+)/$',login_required(MedicoUpdate.as_view()) , name='editar'),
#     url(r'^listar$', UsuarioList.as_view(), name='listar_usuario'),
#     url(r'^nuevo_usuario$', MedicoCreate.as_view(), name='crear_usuario'),
#     url(r'^validar/(?P<id_usuario>\d+)/$', validar, name='validarform'),
]