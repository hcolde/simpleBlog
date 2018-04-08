from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm
from django.utils import timezone

def PageView(request, page = 1):
	showNum = 3 # each page shows 3
	pageNum = page
	blogCount = Post.objects.all().count() # the total number of blogs
	allPage_ = blogCount/showNum
	allPage = int(allPage_)+1 if allPage_>int(allPage_) else int(allPage_) # the max number of pages
	pageNum = allPage if pageNum>allPage else pageNum # could not exceed total number of pages
	start = pageNum * showNum - showNum
	blog_list = Post.objects.order_by('-publish_date')[start:start+showNum]
	dir_list = [x for x in request.path.split('/') if x!='']
	home = '../' if len(dir_list)>1 else ''
	info_list = {
		'blog_list': blog_list,
		'page': pageNum,
		'home': home,
		'homePage': home if pageNum!=1 else None,
		'previousPage': home+str(pageNum-1) if pageNum>1 else None,
		'nextPage': home+str(pageNum+1) if pageNum!=allPage else None,
		'lastPage': home+str(allPage) if pageNum!=allPage else None,
	}
	return render(request, 'blog/page.html', info_list)


class DetailView(generic.DetailView):
	model = Post
	template_name = 'blog/detail.html'


def PostView(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('blog:detail', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})