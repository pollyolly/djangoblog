from django import forms

class ChatForm(forms.Form):
    name = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control',
                                                                                    'id':'chat-name'}))
    chat = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class':'form-control',
                                                                        'id':'chat-input',
                                                                       'placeholder':'Messages...'}))
