from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('<int:page>/', views.PageView, name = 'page'),
	#path('[int:pk]/view/', views.ViewView.as_view(), name = 'view'),
	#path('post/', views.PostView.as_view(), name = 'post'),
	#path('[int:pk]/remove/', views.RemoveView.as_view(), name = 'remove'),
	#path('[int:pk]/modify/', views.ModifyView.as_view(), name = 'modify'),
]