from django import forms

from qrgen.models import File

class PdfUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']

