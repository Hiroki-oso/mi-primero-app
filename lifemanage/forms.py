from django import forms
from .models import Person

class FirstForm(forms.ModelForm):
    username = forms.CharField(label='お名前')
    height = forms.FloatField(label='身長')
    weight = forms.IntegerField(label='体重')
    bmi = forms.FloatField(label='BMI')
    appr_w = forms.FloatField(label='適正体重')
    memo = forms.CharField(label='memo')
    
    class Meta:
        model = Person
        fields = ('username', 'height', 'weight', 'bmi', 'appr_w', 'memo')
        widgets = {
            'username' : forms.TextInput(attrs={
                'class': "form-control",
            }),
            'height' : forms.TextInput(attrs={
                'class': "form-control",
            }),
            'weight' : forms.TextInput(attrs={
                'class': "form-control",
            }),
            'bmi' : forms.TextInput(attrs={
                'class': "form-control",
            }),
            'appr_w' : forms.TextInput(attrs={
                'class': "form-control",
            }),
            'memo' : forms.TextInput(attrs={
                'class': "form-control",
            }),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.wedget.attrs['class'] = 'form-control'

        

    
# class SecondForm(forms.Form):
#     weight = forms.IntegerField(label='体重: ')
#     s_jikan = forms.IntegerField(label='睡眠時間: ')
#     m_cal = forms.IntegerField(label='食事のカロリー: ')
#     e_cal = forms.IntegerField(label='運動カロリー: ')
#     total_cal = forms.IntegerField(label='トータルカロリー: ')
#     bmi = forms.FloatField(label='BMI: ')


# class BMIForm(forms.Form):
#     height = forms.IntegerField(label='Height: ')
#     weight = forms.IntegerField(label='Weight: ')
