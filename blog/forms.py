from django import forms
from blog.models import Contactus

class Subscribe(forms.Form):
    email = forms.EmailField(
        max_length = 100,
        label=None,
        widget=forms.TextInput(attrs={'class': "form-control mr-md-1 semail",'placeholder' :'Enter email','name' : 'email'}),
        )
    

# class ContactusForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': "input2"}),
#         )
#     email = forms.EmailField(
#         max_length = 150,
#         widget=forms.TextInput(attrs={'class': "input2"}),
        
#         )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'class': "input2"}),
        
#         )

# This is Modelform, so we do not have to redeclare field in the form,it take field from model class
class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields  = ['name','email','message']
        # Add Widgets to Model form
        widgets = {
           'name':forms.TextInput(attrs={'class': "input2"}),
           'email': forms.TextInput(attrs={'class': "input2"}),
            'message': forms.Textarea(attrs={'class': "input2"}),
        }

    
    