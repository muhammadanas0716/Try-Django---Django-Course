from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

def article_search_view(request):
    query_id = request.GET.get("q")  # Get 'q' from the query params
    article_obj = None
    
    if query_id:
        article_obj = get_object_or_404(Article, id=query_id)

    return render(request, "articles/search.html", {"article_obj": article_obj})

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        obj = form.save()
        return redirect('home_view')
    
    context = {"form": form} 
    return render(request, "articles/create.html", context)

def article_detail_view(request, id=None):
    # Using get_object_or_404 to handle cases where the article doesn't exist
    article_obj = get_object_or_404(Article, id=id)

    context = {
        "article_obj": article_obj
    }

    return render(request, template_name="articles/detail.html", context=context)