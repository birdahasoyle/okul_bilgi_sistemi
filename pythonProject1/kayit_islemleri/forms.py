from django import forms
from .models import Okul


class kayit_formu(forms.ModelForm):

    class Meta:
        model = Okul
        fields = ('sehir', 'kayit_turu', 'isim_soyisim', 'telefon')

    def __init__(self, *args, **kwargs):
        super(kayit_formu, self).__init__(*args, **kwargs)
        self.fields['kayit_turu'].empty_label = "Seciniz"
        self.fields['sehir'].empty_label = "Seciniz"

    def __str__(self):
        return self.isim_soyisim
