from django import forms

class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(max_length=5)

    GENDER = (
        ('P', 'Pria'),
        ('W', 'Wanita')
    )
    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER
    )

    TAHUN = range(1945, 2020, 1)
    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(years=TAHUN)
    )
    email = forms.EmailField(label='Alamat Email')
    alamat = forms.CharField(
        widget=forms.Textarea,
        required=False
    )
    agree = forms.BooleanField()
