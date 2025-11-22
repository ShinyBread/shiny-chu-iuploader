from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.management import call_command
from .forms import ImageUploadForm
from .models import Image

def upload_view(request):
    url_resultado = None
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            #full url
            host = request.get_host()
            protocol = 'https' if request.is_secure() else 'http'
            url_resultado = f"{protocol}://{host}/{img.short_code}"
            print(f"DEBUG: url_resultado generated: {url_resultado}")
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form, 'url_resultado': url_resultado})

def image_view(request, short_code):
    img = get_object_or_404(Image, short_code=short_code)
    
    # img context for discord
    context = {
        'image_url': img.image.url,
        'short_code': short_code
    }
    return render(request, 'view_image.html', context)

def admin_shiny_view(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
            return redirect('shiny_admin') 
        
        if 'cleanup' in request.POST:
            if not request.user.is_authenticated:
                return redirect('shiny_admin')
            
            try:
                call_command('cleanup_images')
                return render(request, 'admin_shiny.html', {
                    'message': 'Imágenes viejas eliminadas.', 
                    'user': request.user
                })
            except Exception as e:
                return render(request, 'admin_shiny.html', {
                    'error': f'Error: {str(e)}', 
                    'user': request.user
                })

        #login
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('shiny_admin')
    
    else:
        form = AuthenticationForm()

    return render(request, 'admin_shiny.html', {'form': form})