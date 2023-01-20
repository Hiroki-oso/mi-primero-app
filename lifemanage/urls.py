from django.urls import path
from .import views

app_name = 'lifemanage'
urlpatterns = [
    path('top/', views.TopView.as_view(), name='top'),
    path('second/', views.IndexSecondView.as_view(), name='second'),
    path('detail/<int:pk>/', views.IndexDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.IndexDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.IndexUpdateView.as_view(), name='update'),
    path('list/', views.IndexListView.as_view(), name='list'),
    path('firstinput/', views.FirstInputView.as_view(), name='firstinput'),
]