from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {'message': "Welcome my BBS",
               'members':["AAAさん","BBBさん","CCCさん"],
               'articles':articles,
               }
    return render(request, 'bbs/index.html', context)

def detail(request, id):

    article = get_object_or_404(Article, pk=id)

    context = {

        'message': 'ページID:'+ str(id),

        'article': article,

    }

    return render(request, 'bbs/detail.html', context)

def create(request):

    article = Article(content='追加したよ',user_name='わたし')

    article.save()


    articles = Article.objects.all()

    context = {'message': "Articleに追加",

                'articles': articles,

                }

    return render(request, 'bbs/index.html', context)

def delete(request, id):

    article = get_object_or_404(Article, pk=id)

    article.delete()


    articles = Article.objects.all()

    context = {

        'message': 'ページID:'+ str(id) + 'を削除しました',

        'articles': articles,

    }

    return render(request, 'bbs/index.html', context)