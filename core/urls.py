from django.contrib import admin
from django.urls import path
from uploads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shiny/', views.admin_shiny_view, name='shiny_admin'),
    path('admin/', admin.site.urls),
    # Home
    path('', views.upload_view, name='home'),
    #dinamically generated image view
    path('<str:short_code>/', views.image_view, name='image_detail'),
    
]
