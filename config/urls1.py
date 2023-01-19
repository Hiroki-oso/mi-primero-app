from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView, UserLoginView, UserLogoutView
from accounts import views
from lifemanage import views

app_name = 'accounts'
urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', top, name='top'),
    # path('', include('accounts.urls')),
    # path('', include('lifemanage.urls')),
    
    # Accounts
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    # lifemanage
        # path('', views.top, name='top'),
    path('', views.TopView.as_view(), name='top'),
    path('list/', views.IndexListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.IndexDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.IndexDeleteView.as_view(), name='delete'),
    # path('delete_done/<int:pk>', views.DeleteDoneView.as_view(), name='delete_done'),
    path('firstinput/', views.FirstInputView.as_view(), name='firstinput'),
    # path('update/<int:pk>', views.IndexUpdateView.as_view(), name='update'),
]
