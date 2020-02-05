from django import forms

class ContactForm(forms.Form):
    nama_lengkap    = forms.CharField(
        label='Nama Lengkap',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'masukkan nama lengkap anda',
            }
        )
    )

    jenis_kelamin   = forms.ChoiceField(
        choices=[
            ('P', 'Pria'),
            ('W', 'Wanita'),
        ],
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-check-input',
            }
        )
    )

    tanggal_lahir   = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class': 'form-control col-sm-2',
            },
            years=range(1945, 2020, 1)
        )
    )

    email           = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'isi dengan email anda',
            }
        )
    )

    alamat          = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'isi dengan alamat lengkap',
            }
        )
    )

    agree           = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
            }
        )
    )