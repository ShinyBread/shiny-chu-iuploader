from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from uploads.models import Image

class Command(BaseCommand):
    help = 'Elimina imágenes antiguas (más de 7 días) de la base de datos y Cloudinary'

    def handle(self, *args, **kwargs):
        dias_vida = 7
        limite = timezone.now() - timedelta(days=dias_vida)
        imagenes_viejas = Image.objects.filter(created_at__lt=limite) #busca imagenes mas viejas
        cantidad = imagenes_viejas.count()

        if cantidad == 0:
            self.stdout.write(self.style.SUCCESS('No hay imágenes antiguas para borrar.'))
            return
        
        for img in imagenes_viejas:
            img.delete()

        self.stdout.write(self.style.SUCCESS(f'✅ Se eliminaron {cantidad} imágenes antiguas.'))