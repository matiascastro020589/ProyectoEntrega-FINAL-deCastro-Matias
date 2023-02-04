from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Producto, Cliente, Vendedor,Avatar
from AppCoder.forms import ProductoFormulario, ClienteFormulario, VendedorFormulario

# Create your views here.

def producto(request):

      producto =  Producto(nombre="ResmaA4", precio=1800)
      producto.save()
      documentoDeTexto = f"--->Producto: {producto.nombre}   Precio: {producto.precio}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def acercade(request):

      return render(request, "AppCoder/acercade.html")

def buscadores(request):

      return render(request, "AppCoder/Buscadores.html")      



def vendedores(request):

      return render(request, "AppCoder/vendedores.html")



def productos(request):

      if request.method == 'POST':

            miFormulario = ProductoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  producto = Producto(nombre=informacion['nombre'], precio=informacion['precio']) 

                  producto.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProductoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/productos.html", {"miFormulario":miFormulario})




def clientes(request):

      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], localidad=informacion['localidad']) 

                  cliente.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ClienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/clientes.html", {"miFormulario":miFormulario})


def vendedores(request):

      if request.method == 'POST':

            miFormulario = VendedorFormulario (request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  vendedor = Vendedor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email']) 

                  vendedor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= VendedorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/vendedores.html", {"miFormulario":miFormulario})



def buscar(request):

      if  request.GET["precio"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            precio = request.GET['precio'] 
            productos = Producto.objects.filter(precio__icontains=precio)

            return render(request, "AppCoder/Buscadores.html", {"productos":productos, "precio":precio})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)


def buscarcliente(request):

      if  request.GET["nombre"]:

	    
            nombre = request.GET['nombre'] 
            clientes = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/Buscadores.html", {"clientes":clientes, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def buscarvendedor(request):

      if  request.GET["nombre"]:

	       
            nombre = request.GET['nombre'] 
            vendedores = Vendedor.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/Buscadores.html", {"vendedores":vendedores, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def leerClientes(request):

      clientes = Cliente.objects.all() 

      contexto= {"clientes":clientes} 

      return render(request, "AppCoder/leerClientes.html",contexto)

def leerVendedores(request):

      vendedores = Vendedor.objects.all() 

      contexto= {"vendedores":vendedores} 

      return render(request, "AppCoder/leerVendedores.html",contexto)


def eliminarClientes(request, cliente_nombre):

    cliente = Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()

    # vuelvo al menú
    cliente = Cliente.objects.all()  

    contexto = {"clientes": clientes}

    return render(request, "AppCoder/leerClientes.html", contexto)

def eliminarVendedores(request, vendedor_nombre):

    vendedor = Vendedor.objects.get(nombre=vendedor_nombre)
    vendedor.delete()

    # vuelvo al menú
    vendedor = Vendedor.objects.all()  

    contexto = {"vendedores": vendedores}

    return render(request, "AppCoder/leerVendedores.html", contexto)

def editarCliente(request, cliente_nombre):

    
    cliente = Cliente.objects.get(nombre=cliente_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = ClienteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.email = informacion['email']
            cliente.localidad = informacion['localidad']

            cliente.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ClienteFormulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido,
                                                   'email': cliente.email, 'localidad': cliente.localidad})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarCliente.html", {"miFormulario": miFormulario, "cliente_nombre": cliente_nombre})

def editarVendedor(request, vendedor_nombre):

    
    vendedor = Vendedor.objects.get(nombre=vendedor_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = VendedorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            vendedor.nombre = informacion['nombre']
            vendedor.apellido = informacion['apellido']
            vendedor.email = informacion['email']
           

            vendedor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = VendedorFormulario(initial={'nombre': vendedor.nombre, 'apellido': vendedor.apellido,
                                                   'email': vendedor.email})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarVendedor.html", {"miFormulario": miFormulario, "vendedor_nombre": vendedor_nombre})


from django.views.generic import ListView

class ProductoList(ListView):

    model = Producto
    template_name = "AppCoder/productos_list.html"


from django.views.generic.detail import DetailView


class ProductoDetalle(DetailView):

    model = Producto
    template_name = "AppCoder/producto_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ProductoCreacion(CreateView):

    model = Producto
    success_url = "/AppCoder/producto/list"
    fields = ['nombre', 'precio']

from django.views.generic.edit import UpdateView

class ProductoUpdate(UpdateView):

    model = Producto
    success_url = "/AppCoder/producto/list"
    fields = ['nombre', 'precio']


from django.views.generic.edit import DeleteView

class ProductoDelete(DeleteView):

    model = Producto
    success_url = "/AppCoder/producto/list"

from django.views.generic import ListView

class ClienteList(ListView):

    model = Cliente
    template_name = "AppCoder/clientes_list.html"


from django.views.generic.detail import DetailView


class ClienteDetalle(DetailView):

    model = Cliente
    template_name = "AppCoder/cliente_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ClienteCreacion(CreateView):

    model = Cliente
    success_url = "/AppCoder/cliente/list"
    fields = ['nombre', 'apellido', 'email', 'localidad']

from django.views.generic.edit import UpdateView

class ClienteUpdate(UpdateView):

    model = Cliente
    success_url = "/AppCoder/cliente/list"
    fields = ['nombre', 'apellido', 'email', 'localidad']


from django.views.generic.edit import DeleteView

class ClienteDelete(DeleteView):

    model = Cliente
    success_url = "/AppCoder/cliente/list"

from django.views.generic import ListView

class VendedorList(ListView):

    model = Vendedor
    template_name = "AppCoder/vendedores_list.html"


from django.views.generic.detail import DetailView


class VendedorDetalle(DetailView):

    model = Vendedor
    template_name = "AppCoder/vendedor_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class VendedorCreacion(CreateView):

    model = Vendedor
    success_url = "/AppCoder/vendedor/list"
    fields = ['nombre', 'apellido', 'email']

from django.views.generic.edit import UpdateView

class VendedorUpdate(UpdateView):

    model = Vendedor
    success_url = "/AppCoder/vendedor/list"
    fields = ['nombre', 'apellido', 'email']


from django.views.generic.edit import DeleteView

class VendedorDelete(DeleteView):

    model = Vendedor
    success_url = "/AppCoder/vendedor/list"

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

from AppCoder.forms import  UserRegisterForm,UserEditForm


# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

#LOGIN EN INICIO

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request): 
    
    return  render(request, "AppCoder/inicio.html")

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


