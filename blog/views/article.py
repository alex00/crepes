#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie
from blog.forms import ArticleForm

def accueil(request, num="1"):
	derniers_articles = Article.objects.all().order_by('-date')
	return render(request, 'blog/article/accueil.html', {'derniers_articles':derniers_articles})

def lire(request, id, slug):
	# try:
	#     article = Article.objects.get(Article, id=id, slug=slug)
	# except Article.DoesNotExist:
	#     raise Http404
	article = get_object_or_404(Article, id=id, slug=slug)
	return render(request, 'blog/article/lire.html', {'article':article})

def new(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = ArticleForm()
	return render(request, 'blog/article/form.html', locals())
