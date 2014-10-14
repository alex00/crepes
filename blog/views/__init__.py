#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Article, Categorie
from blog.forms import ContactForm, ArticleForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate