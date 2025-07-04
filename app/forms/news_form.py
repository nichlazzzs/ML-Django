from django import forms
from app.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
