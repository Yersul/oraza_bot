from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

class BroadcastForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    broadcast_text = forms.CharField(widget=forms.Textarea)
    broadcast_date = forms.DateTimeField(widget=AdminSplitDateTime)
