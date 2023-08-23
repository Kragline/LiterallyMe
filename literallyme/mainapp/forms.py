from django import forms
from django.core.exceptions import ValidationError

from .models import *


name_attrs = {'type': 'text', 'class': 'form-control', 'placeholder': 'Actor name'}
bio_attrs = {'type': 'text', 'class': 'form-control', 'cols': 70, 'placeholder': 'Actor bio'}
slug_attrs = {'type': 'text', 'class': 'form-control', 'placeholder': 'Slug for URL'}
photo_attrs = {'type': 'file', 'class': 'form-control'}

title_attrs = {'type': 'text', 'class': 'form-control', 'placeholder': 'Movie name'}
plot_attrs = {'type': 'text', 'class': 'form-control', 'cols': 70, 'placeholder': 'Movie plot'}
release_date_attrs = {'type': 'text', 'class': 'form-control', 'placeholder': 'Release date'}
rating_attrs = {'type': 'number', 'class': 'form-control', 'placeholder': 'Movie rating (1-10)'}
select_attrs = {'class': 'form-select'}

category_name_attrs = {'type': 'text', 'class': 'form-control', 'placeholder': 'Category name'}

comment_attrs = {'type': 'text', 'class': 'form-control', 'cols': 70, 'rows': 1, 'placeholder': 'Add your comment'}


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'bio', 'photo', 'slug']

        widgets = {
            'name': forms.TextInput(attrs=name_attrs),
            'bio': forms.Textarea(attrs=bio_attrs),
            'slug': forms.TextInput(attrs=slug_attrs),
            'photo': forms.FileInput(attrs=photo_attrs),
        }


class MovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Choose category'

    def clean_rating(self):
        data = self.cleaned_data['rating']
        if data < 1 or data > 10:
            raise ValidationError('Rating must be from 1 to 10')

        return data

    class Meta:
        model = Movie
        fields = ['title', 'plot', 'release_date', 'poster', 'actors', 'rating', 'category', 'slug']

        widgets = {
            'title': forms.TextInput(attrs=title_attrs),
            'plot': forms.Textarea(attrs=plot_attrs),
            'release_date': forms.TextInput(attrs=release_date_attrs),
            'poster': forms.FileInput(attrs=photo_attrs),
            'slug': forms.TextInput(attrs=slug_attrs),
            'actors': forms.SelectMultiple(attrs=select_attrs),
            'rating': forms.NumberInput(attrs=rating_attrs),
            'category': forms.Select(attrs=select_attrs)
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

        widgets = {
            'name': forms.TextInput(attrs=category_name_attrs),
            'slug': forms.TextInput(attrs=slug_attrs)
        }


class CommentForm(forms.ModelForm):
    def clean_text(self):
        new_comment_text = self.cleaned_data['text']
        return new_comment_text.capitalize()

    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs=comment_attrs)
        }
