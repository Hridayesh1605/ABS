from django import forms
from .models import Tool

class ToolForm(forms.Form):
    tool = forms.ModelChoiceField(
        queryset=Tool.objects.all(),
        empty_label="Select a tool",
        widget=forms.Select(attrs={'class': 'tool-dropdown'})
    )