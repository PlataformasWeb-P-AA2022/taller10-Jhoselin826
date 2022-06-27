from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('parroquia/<int:id>', views.obtenerParroquia, 
            name='obtenerParroquia'),
        path('crear/parroquia', views.crearParroquia, 
            name='crearParroquia'),
        path('editarParroquia/<int:id>', views.editarParroquia, 
            name='editarParroquia'),
        
        path('barrios', views.obtenerBarrio, 
            name='obtenerBarrio'),
        path('editar/barrio/<int:id>', views.editarBarrio, 
            name='editarBarrio'),
        path('crear/barrio/<int:id>', 
            views.crearBarrioParroquia, 
            name='crearBarrioParroquia'),
 ]