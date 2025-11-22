from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from .models import Image

def upload_view(request):
    url_resultado = None
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            # Construimos la URL completa (ej: https://i.shinychu.com/Ab3x)
            host = request.get_host()
            protocol = 'https' if request.is_secure() else 'http'
            url_resultado = f"{protocol}://{host}/{img.short_code}"
            print(f"DEBUG: url_resultado generated: {url_resultado}")
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form, 'url_resultado': url_resultado})

def image_view(request, short_code):
    # Busca la imagen o lanza un error 404 si no existe
    img = get_object_or_404(Image, short_code=short_code)
    
    # Contexto para que Discord entienda la imagen
    context = {
        'image_url': img.image.url,
        'short_code': short_code
    }
    return render(request, 'view_image.html', context)
