"""
To render HTML web pages
"""
from django.http import HttpResponse
import random

from django.shortcuts import render

from articles.models import Article

def home_view(request, *args, **kwargs):
  number = random.randint(1, 5)
  article_obj = Article.objects.get(id=number)
  all_articles = Article.objects.all()
  
  context = {
    "all_articles" : all_articles,
    "object" : article_obj,
    "id" : article_obj.id,
    "title" : article_obj.title,
    "content" : article_obj.content,
  }
  
  # NON TEMPLATE(s)
  # HTML_STRING = """
  # <h1>{title} - (id: {id})!</h1>
  # <p>{content}</p>
  # """.format(**context)
  
  print(args, kwargs)
  
  return render(request, template_name="home-view.html", context=context)