from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.PageView, name = 'index'),
	path('<int:page>/', views.PageView, name = 'page'),
	path('<int:pk>/detail/', views.DetailView.as_view(), name = 'detail'),
	path('post/', views.PostView, name = 'post_new'),
	#path('[int:pk]/remove/', views.RemoveView.as_view(), name = 'remove'),
	#path('[int:pk]/modify/', views.ModifyView.as_view(), name = 'modify'),
]