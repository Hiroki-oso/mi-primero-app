from accounts.models import User
from django.db import models

class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='ユーザー', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='お名前', max_length=50)
    height = models.FloatField(verbose_name='身長', blank=False)
    weight = models.IntegerField(verbose_name='体重', blank=True, null=True)
    bmi = models.FloatField(verbose_name='BMI', blank=True, null=True)
    appr_w = models.FloatField(verbose_name='適正体重', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    memo = models.TextField(verbose_name='メモ', blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'person'
        
    def __str__(self):
        return str(self.user)
        

    


