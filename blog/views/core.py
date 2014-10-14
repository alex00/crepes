#-*- coding: utf-8 -*-
from django.shortcuts import render
from blog.forms import ContactForm
from datetime import datetime

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

	return render(request, 'blog/core/contact.html', locals())