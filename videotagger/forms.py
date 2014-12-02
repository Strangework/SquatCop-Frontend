from django import forms

class UploadVideoForm(forms.Form):
  video = forms.FileField(
    label = 'HELP ME YOU FUCK',
    help_text = 'You are beyond help.'
)
