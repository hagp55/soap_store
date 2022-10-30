from django import forms


class TeleBotSendMessageForm(forms.Form):
    # name = forms.CharField(max_length=150)
    # email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField()