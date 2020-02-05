from django import forms

# import model dari models.py
from .models import Artikel

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'judul',
            'isi',
            'penulis',
        ]