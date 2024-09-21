"""
To render HTML web pages
"""
from django.http import HttpResponse
import random

def home_view(request):
  name = "Anas"
  number = random.randint(10, 1233123)
  
  # Django templates
  H1_STRING = f"<h1>HELLO {name} - {number}!</h1>"
  P_STRING = f"<p>Hi {name} - {number}!</p>"
  
  HTML_STRING = H1_STRING + P_STRING
  
  return HttpResponse(HTML_STRING)