from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news' : news})

class NewsDetail(DetailView):
    model = Article
    template_name = "news/details_view.html"
    context_object_name = "article"

class NewsUpdateView(UpdateView):
    model = Article
    template_name = "news/create.html"
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = "/news/"
    context_object_name = "article"
    template_name = "news/news-delete.html"

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid(): #is_valid in ModelForm
            form.save()
            return redirect('news_home')
        else:
            error = "Форма была не верной"

    form = ArticleForm()

    data = {
        "form":form,
        "error" : error,
    }

    return render(request, 'news/create.html', data)
