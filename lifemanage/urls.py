from django.urls import path
from .import views

app_name = 'lifemanage'
urlpatterns = [
    # path('', views.top, name='top'),
    path('', views.TopView.as_view(), name='top'),
    # path('list/', views.index, name='list'),
    path('list/', views.IndexListView.as_view(), name='list'),
    # path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/', views.IndexDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.IndexDeleteView.as_view(), name='delete'),
    # path('delete_done/<int:pk>', views.DeleteDoneView.as_view(), name='delete_done'),
    path('firstinput/', views.FirstInputView.as_view(), name='firstinput'),
    path('update/<int:pk>', views.IndexUpdateView.as_view(), name='update'),
]