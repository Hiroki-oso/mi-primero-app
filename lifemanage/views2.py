from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Personal
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import FirstForm
from django.contrib import messages

# top page
class TopView(TemplateView):
    template_name = 'top.html'

# List page ログイン後、レンダリング R
class IndexListView(LoginRequiredMixin, ListView):
    model = Personal
    template_name = 'pages/list.html'
    contaxt_object_name = "personal_list"
    queryset = Personal.objects.order_by(-created_at)
    paginate_by = 7

    def get_queryset(self):
    
# @login_required   
# def IndexDetail(request, personal_id):
#     personal = get_object_or_404(Personal, pk=personal_id)
#     return render(request, "pages/detail.html", {
#         'personal.weight': personal.weight,
#     })
      

# detail page listpageのdetail buttonをクリック後、」遷移 R

class IndexDetailView(ListView):
    template_name = 'pages/detail.html'
    model = Personal
    context_object_name = "personal_list"
    queryset = Personal.objects.all()
    paginate_by = 7
    
# delete_doneの前の確認クラス
class DeleteIndicateView(TemplateView):
    template_name = 'pages/delete.html'
    
    
class FirstInputView(FormView):
    template_name = 'pages/firstinput.html'
    form_class = FirstForm
    success_url = reverse_lazy('pages:secondinput')
    
    def form_valid(self, form):
        if form.is_valid():
            sex = form.cleaned_data['sex']
            sex = '1' and '2'
        else:
            messages.error(self.request, 'エラーです。1または２を入力してください')
            height = form.cleaned_data['height']
            Personal.save()
        return super().form_valid(form)
    
    
       
# BMI参考
from .forms import BMIForm

def index(request):
    contaxt = {
        'forms':FirstForm(),
    }
    if (request.method == 'POST'):
        height = int(request.POST['height'])
        weight = int(request.POST['weight'])

        contaxt['bmi'] = weight / ((height/100) * (height/100))
        contaxt['optimal'] = (height/100) * (height/100) * 22

    return render(request, 'pages/detail.html', contaxt)

#top page(関数定義)
# def top(request):
#     person = Person.objects.all()
#     context = {
#         "person": person,
#     }
#     return render(request, "top.html", context)

# 詳細ページ
# @login_required
# def life_detail(request, person_id):
#     person = get_object_or_404(Person, pk=person_id)
#     return render(request, 'pages/detail.html', {
#         'person': person,
#     })

# 削除ページ
# class DeleteDoneView(DeleteView):
#     model = Person
#     template_name = 'pages/delete_done.html'
#     success_url = reverse_lazy('lifemanage:detail')

# def get_queryset(self):
    
    # object['bmi_1'] = int(object['height'] / 100)
    # object['bmi_2'] = object['bmi_1'] * object['bmi_1']
    # object['bmi'] = int(object['weight']) / object['bmi_2']
    # return Person.objects.filter(user=self.request.user)
    
# @login_required
# def index(request):
#     person = Person.objects.all()
#     context = {"person": person}
#     return render(request, "pages/list.html", context)


    def index(request, **kwargs):
        
    #     context = {
    #     'forms':FirstForm(),
    # }
        if (request.method == 'POST'):
            
            weight = request.POST.get("weight")
            height = request.POST.get("height")
            # height = int(request.POST.get['height'])
            # weight = int(request.POST.get['weight'])

            bmi = weight / ((height/100) * (height/100))
            appr_w = (height/100) * (height/100) * 22
            
            form = FirstForm(request.POST)
                
            context = {
                # 'bmi': bmi,
                # 'appr_w': appr_w,
            }
            
            context['bmi'] = round(bmi)
            context['appr_w'] = round(appr_w)

            if form.is_valid():
                form.save()
            else:
                form = FirstForm()
            return render(request, 'pages/firstinput.html', context, **kwargs)
        
# def detail(request, id):
#     person = get_object_or_404(person, pk=id)
#     return render(request, 'pages/detail.html')

# def get_queryset(self):
#     person = Person.objects.filter(user=self.request.user).order_by('-created_at')[:5]
#     return person

# def index(request):
#     contaxt = {
#         'forms':FirstForm(),
#     }
#     if (request.method == 'POST'):
#         height = float(request.POST['height'])
#         weight = float(request.POST['weight'])
# height = height / 100
# bmi = (weight / (height**2))
# appr_w = (height**2)*22
#         context['bmi'] = round(bmi)
# context['appr_w'] = round(appr_w)
# return render(request, '', context) 


      
    # def get_queryset(self):
    #     return Person.objects.filter(user=self.request.user)

    # def get_queryset(self):
    #     return Person.objects.filter(user=self.request.user)
