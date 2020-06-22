from django import forms
from .models import Comment

# This class is used for sharing the posts by email
class EmailPostForm(forms.Form):
	"""docstring for EmailPostForm"""
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)	



# This class is used for creating the form for submiting the comments to the post
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')


# For implementing the search function in the blog posts
class SearchForm(forms.Form):
	query = forms.CharField()