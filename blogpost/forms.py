from django import forms
from blogpost.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        #fields = ('post','name','comment',)
        
    def __init__(self,postid,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        #self.fields['post'].queryset = Post.objects.filter(id=postid) #filter post fk/dropdown in comment model
        self.fields['post'].initial = postid
        self.fields['post'].widget.attrs['class'] = 'invisible'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'
    """
    def save(self,commit=True):
        comment = Comment.objects.create(self.cleaned_data['post'],self.cleaned_data['name'],self.cleaned_data['comment']) 
        return comment
    """
