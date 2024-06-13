from captcha.fields import CaptchaField
from django import forms

from blogApp.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["post", "name", "email", "subject", "message"]
