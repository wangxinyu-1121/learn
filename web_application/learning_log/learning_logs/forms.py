from django import forms

from .models import Topic

class TopicFrom(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels ={'text': ''}

