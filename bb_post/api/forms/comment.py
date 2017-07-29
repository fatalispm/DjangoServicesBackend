from django import forms


class CreateForm(forms.Form):
    text = forms.CharField()
    post = forms.IntegerField()
