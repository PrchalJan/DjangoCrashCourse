from django.shortcuts import render


# Create your views here.
from .models import Posts

def index(request):

	context = {
		'posts': Posts.objects.all()[:10],
		'title': 'Latest Posts',
	}

	return render(request, 'posts/index.html', context)

def details(request, id):

	context = {
		'post': Posts.objects.get(id=id)
	}
	return render(request, 'posts/details.html', context)