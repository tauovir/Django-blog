from django import forms

class Subscribe(forms.Form):
    email = forms.EmailField(
        max_length = 100,
        label=None,
        widget=forms.TextInput(attrs={'class': "form-control mr-md-1 semail",'placeholder' :'Enter email','name' : 'email'}),
        )
    