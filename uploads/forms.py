from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'file-input', 'accept': 'image/*'})
        }
