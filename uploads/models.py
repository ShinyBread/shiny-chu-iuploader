from django.db import models
from django.utils.crypto import get_random_string

class Image(models.Model):
   
    short_code = models.CharField(max_length=10, unique=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='shinies/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        if not self.short_code:
            self.short_code = get_random_string(5)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code
