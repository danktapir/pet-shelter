from django import forms

class ReportForm(forms.Form):
    reason = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tell me why!',
        'required': True,
    }))