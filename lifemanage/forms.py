from django import forms
from .models import Person

class FirstForm(forms.ModelForm):
    username = forms.CharField(label='お名前')
    height = forms.FloatField(label='身長')
    weight = forms.IntegerField(label='体重')
    # bmi = forms.FloatField(label='BMI')
    # appr_w = forms.FloatField(label='適正体重')
    memo = forms.CharField(label='memo')
    
    class Meta:
        model = Person
        fields = ('height', 'weight', 'username', 'memo',)
        # widgets = {
        #     'username' : forms.TextInput(attrs={
        #         'class': "form-control",
        #     }),
        #     'height' : forms.TextInput(attrs={
        #         'class': "form-control",
        #     }),
        #     'weight' : forms.TextInput(attrs={
        #         'class': "form-control",
        #     }),
        #     'bmi' : forms.TextInput(attrs={
        #         'class': "form-control",
        #     }),
        #     'appr_w' : forms.TextInput(attrs={
        #         'class': "form-control",
        #     }),
        #     'memo' : forms.TextInput(attrs={
        #         'class': "form-control",
        #     }),
        # }
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     for field in self.fields.values():
        #         field.wedget.attrs['class'] = 'form-control'
