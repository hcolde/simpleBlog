from django.shortcuts import render
from django.views import generic
from .models import Post

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'blog_list'

	def get_queryset(self):
		return Post.objects.order_by('-publish_date')[:5]

def PageView(request):
	pageNum = request.Get('page')
	blogCount = Post.objects.all().count() # the total number of blogs
	allPage_ = blogCount/5 # each page shows 5
	allPage = allPage_ > int(allPage_) or int(allPage_)+1 and int(allPage_)
	pageNum = pageNum > allPage or allPage and pageNum # could not exceed total number of pages
	start = pageNum * 5 - 5
	blog_list = Post.objects.order_by('-publish_date')[start:5]
	return render(request, 'page.html', blog_list)