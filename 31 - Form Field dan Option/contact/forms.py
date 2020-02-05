from django import forms

class ContactForm(forms.Form):
    GENDER = (
        ('P', 'Pria'),
        ('W', 'Wanita')
    )
    nama_lengkap = forms.CharField(max_length=5)
    jenis_kelamin = forms.ChoiceField(choices=GENDER)
    email = forms.EmailField(label='Alamat Email')
    alamat = forms.CharField(required=False)
    kode_pos = forms.IntegerField(required=False)
    kota = forms.CharField(required=True)
    provinsi = forms.CharField(required=False)
    agree = forms.BooleanField()
