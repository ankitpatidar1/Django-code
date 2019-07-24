from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','price']

class RawProductForm(forms.Form):
    title = forms.CharField(required = True, label='', widget=forms.TextInput(
        attrs={"placeholder":"your title"}
        
    ))
    description = forms.CharField(required = False,widget=forms.Textarea(
        attrs={"placeholder":"your description",
        "class":"new-class-name two","id": "id-for-textarea",
        "rows": 20,
        "cols":100}))
    price = forms.DecimalField(required = True,initial=109.00)
