from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse # Importa HttpResponse para una vista simple de prueba

# Una vista simple para la raíz
def home_view(request):
    return HttpResponse("¡Bienvenido a tu aplicación Django en Elastic Beanstalk!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginapp.urls')),
    path('', home_view), # ¡Añade esta línea para la raíz!
]   