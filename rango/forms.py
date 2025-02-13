from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User
from rango.models import UserProfile

class CategoryForm(forms.ModelForm):
    # We can reuse the model's NAME_MAX_LENGTH constant
    name = forms.CharField(
        max_length=Category.NAME_MAX_LENGTH,
        help_text="Please enter the category name."
    )
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        # Only want to show the name field to the user
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=Page.TITLE_MAX_LENGTH,
        help_text="Please enter the title of the page."
    )
    url = forms.URLField(
        max_length=Page.URL_MAX_LENGTH,
        help_text="Please enter the URL of the page."
    )
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        # Exclude the category field since we'll set it in the view
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is provided and doesn't start with "http://"
        # or "https://", prepend "http://"
        if url:
            if not (url.startswith('http://') or url.startswith('https://')):
                url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
 class Meta:
        model = UserProfile
        fields = ('website', 'picture',)
