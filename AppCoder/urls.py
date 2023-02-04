from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('acercade', views.acercade, name="Acerca de"),
    path('buscadores', views.buscadores, name="Buscadores"), 
    path('productos', views.productos, name="Productos"),
    path('clientes', views.clientes, name="Clientes"),
    path('vendedores', views.vendedores, name="Vendedores"),
    path('buscar/', views.buscar),
    path('buscarcliente/', views.buscarcliente),
    path('buscarvendedor/', views.buscarvendedor),
    path('leerClientes', views.leerClientes, name = "LeerClientes"),
    path('leerVendedores', views.leerVendedores, name = "LeerVendedores"),
    path('eliminarCliente/<cliente_nombre>/', views.eliminarClientes, name="EliminarCliente"),
    path('editarCliente/<cliente_nombre>/', views.editarCliente, name="EditarCliente"),
    path('eliminarVendedor/<vendedor_nombre>/', views.eliminarVendedores, name="EliminarVendedor"),
    path('editarVendedor/<vendedor_nombre>/', views.editarVendedor, name="EditarVendedor"),    

    path('producto/list', views.ProductoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='Delete'),

    path('cliente/list', views.ClienteList.as_view(), name='Listcliente'),
    path(r'^(?P<pk>\dcliente+)$', views.ClienteDetalle.as_view(), name='Detailcliente'),
    path(r'^nuevocliente$', views.ClienteCreacion.as_view(), name='Newcliente'),
    path(r'^editarcliente/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='Editcliente'),
    path(r'^borrarcliente/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='Deletecliente'),

    path('vendedor/list', views.VendedorList.as_view(), name='Listvendedor'),
    path(r'^(?P<pk>\dvendedor+)$', views.VendedorDetalle.as_view(), name='Detailvendedor'),
    path(r'^nuevovendedor$', views.VendedorCreacion.as_view(), name='Newvendedor'),
    path(r'^editarvendedor/(?P<pk>\d+)$', views.VendedorUpdate.as_view(), name='Editvendedor'),
    path(r'^borrarvendedor/(?P<pk>\d+)$', views.VendedorDelete.as_view(), name='Deletevendedor'),


    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name ="EditarPerfil")


]

