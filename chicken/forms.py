from django import forms
from captcha.fields import CaptchaField
from .models import *


class ContactEnquiryForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactEnquiry
        fields = [
            'full_name',
            'email',
            'phone_number',
            'subject',
            'message',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5
            }),
        }


class ContactEnquiryUpdateForm(forms.ModelForm):
    class Meta:
        model = ContactEnquiry
        fields = '__all__'

class OfferForm(forms.ModelForm):

    class Meta:

        model = Offer

        fields = [
            'title',
            'image',
            'discount',
            'description',
            'start_date',
            'end_date',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),


            'discount': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),

            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class LatestUpdateForm(forms.ModelForm):

    class Meta:

        model = LatestUpdate

        fields = [
            'title',
            'image',
            'short_description',
            'description',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
        }