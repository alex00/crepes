#-*- coding: utf-8 -*-
from django import forms
from models import Article
from django.db.models import Q
from django.contrib.auth.models import User

class ContactForm(forms.Form):

	#css input error
	error_css_class = 'has-warning'

	sujet = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(attrs={'class' : 'form-control'}),
		label= "Suuuuuujet"
	)
	message = forms.CharField(
		widget=forms.Textarea(attrs={'class' : 'form-control'})
	)
	envoyeur = forms.EmailField(
		widget=forms.EmailInput(attrs={'class' : 'form-control'}),
		label=u"Votre adresse mail"
	)
	renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		sujet = cleaned_data.get('sujet')
		message = cleaned_data.get('message')

		if sujet and message:  # Est-ce que sujet et message sont valides ?
			if "pizza" in sujet and "pizza" in message:
				msg = u"Vous parlez déjà de pizzas dans le sujet, n'en parlez plus dans le message !"
				self._errors["message"] = self.error_class([msg])

				del cleaned_data["message"]

		return cleaned_data

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):   

	login = forms.CharField(
		label = 'Email ou Pseudo', 
		widget=forms.TextInput(attrs={'class' : 'form-control'}),
		required=True
	)                                         
	password  = forms.CharField(
		label = 'Mot de passe', 
		widget = forms.PasswordInput(attrs={'class' : 'form-control'}),
		required = True
	)

	   
	def clean(self):                                     
		login = self.cleaned_data.get('login', '')         
		password = self.cleaned_data.get('password', '')
		self.user = None
		users = User.objects.filter(Q(username=login)|Q(email=login))
		for user in users:
			if user.is_active and user.check_password(password):
				self.user = user
			if self.user is None:
				msg = u"Login ou mot de passe invalide"
				self._errors["message"] = self.error_class([msg])
		return self.cleaned_data


