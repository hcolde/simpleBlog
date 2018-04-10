from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.PageView, name = 'index'),
	path('<int:page>/', views.PageView, name = 'page'),
	path('<int:pk>/detail/', views.DetailView.as_view(), name = 'detail'),
	path('post/', views.PostView, name = 'post_new'),
	path('<int:blog_id>/modify/', views.ModifyView, name = 'modify'),
	path('<int:blog_id>/remove/', views.RemoveView, name = 'remove'),
	path('search/', views.SearchView, name = 'search'),
]