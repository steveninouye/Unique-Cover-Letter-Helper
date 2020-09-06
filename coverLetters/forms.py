from django import forms
from django.forms import ModelForm
from .models import Job, UserDetail
from django.forms.models import model_to_dict

class CoverLetterForm(ModelForm):

    class Meta:
        model = Job
        # fields = [
        #     'template_choices',
        #     'job_posting_website',
        #     'company', 
        #     'city',
        #     'title', 
        #     'link', 
        #     'recruiter',
        #     'description',
        #     'pre_bullet_point_paragraph_one',
        #     'pre_bullet_point_paragraph_two',
        #     'top_skills',
        #     'bullet_point_one',
        #     'bullet_point_two',
        #     'bullet_point_three',
        #     'bullet_point_four',
        #     'bullet_point_five',
        #     'bullet_point_six',
        #     'bullet_point_seven',
        #     'bullet_point_eight',
        #     'post_bullet_point_paragraph_one',
        #     'post_bullet_point_paragraph_two',
        # ]
        fields = '__all__'
        labels = {'position_title': 'Position title'}
        widgets = {
            # 'bullet_point_one': forms.TextInput,
            'template_choices': forms.RadioSelect(), 
        }
        
        formId = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].initial = 'San Francisco'
        

class UserDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['first_name',
            'middle_name',
            'last_name',
            'preferred_name',
            'email',
            'linkedin',
            'github',
            'portfolio_website',
            'street_address',
            'city_address',
            'state_address',
            'zip_code',
        ]

