from django import forms


class UserForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'style': 'height: 400px;width:800px'}), required=False)
    filename = forms.FileField(required=False)