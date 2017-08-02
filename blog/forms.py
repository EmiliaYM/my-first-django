from django import forms
from .models import Post

#to create class automaticallu type"cal" enter
class PostForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Post
		fields = ('title', 'text',)


