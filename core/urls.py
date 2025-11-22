from django.contrib import admin
from django.urls import path
from uploads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal (Home) para subir fotos
    path('', views.upload_view, name='home'),
    
    # Ruta dinámica: captura cualquier cosa (ej: 'Ab3x') y la manda a la vista
    path('<str:short_code>/', views.image_view, name='image_detail'),
]
