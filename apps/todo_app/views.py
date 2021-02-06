from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from apps.todo_app.models import Todo
# Create your views here.

def index(request):
    items = Todo.objects.all()
    return render(request, 'todo_app/index.html', {'items':items})

@csrf_exempt
def agregar_item(request):

    texto_obtenido = request.POST['texto']
    fecha_actual = timezone.now() 
    item = Todo.objects.create(
        fecha_ingreso = fecha_actual,
        texto = texto_obtenido,
    )
    print(item)
    item.save()
    return HttpResponseRedirect('/todo_app/inicio')
    
@csrf_exempt
def eliminar_item(request, id_borrar):

    item_por_borrar = Todo.objects.get(id = id_borrar)
    item_por_borrar.delete()

    return HttpResponseRedirect('/todo_app/inicio')
    