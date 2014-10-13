#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Article, Categorie
from blog.forms import ContactForm, ArticleForm


# Create your views here.

def home(request):
	return render(request, 'blog/home.html', {'current_date': datetime.now()})

def article(request, id, slug):
	# try:
	#     article = Article.objects.get(Article, id=id, slug=slug)
	# except Article.DoesNotExist:
	#     raise Http404
	article = get_object_or_404(Article, id=id, slug=slug)
	return render(request, 'blog/article.html', {'article':article})

def article_new(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ArticleForm()
	return render(request, 'blog/article_form.html', locals())

def accueil(request):
	derniers_articles = Article.objects.all()
	return render(request, 'blog/accueil.html', {'derniers_articles':derniers_articles})

def contact(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = ContactForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides

			# Ici nous pouvons traiter les données du formulaire
			sujet = form.cleaned_data['sujet']
			message = form.cleaned_data['message']
			envoyeur = form.cleaned_data['envoyeur']
			renvoi = form.cleaned_data['renvoi']

			# Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

			envoi = True

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = ContactForm()  # Nous créons un formulaire vide

	return render(request, 'blog/contact.html', locals())