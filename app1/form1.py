from django import forms
from app1.models import hostel

class hostel_form1(forms.ModelForm):
    class Meta:
        model=hostel
        fields='__all__'