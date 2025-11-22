import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from uploads.models import Image

try:
    last_img = Image.objects.last()
    if last_img:
        print(f"Last Image Code: {last_img.short_code}")
        print(f"Image URL: {last_img.image.url}")
        if 'cloudinary' in last_img.image.url:
            print("SUCCESS: Image is hosted on Cloudinary!")
        else:
            print("FAILURE: Image is NOT on Cloudinary.")
    else:
        print("No images found.")
except Exception as e:
    print(f"Error: {e}")
