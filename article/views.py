from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context

from django.shortcuts import render_to_response
from article.models import Article

from django.shortcuts import render

# Create your views here.

# view for title_aaa
# def article_1(request):
#     title = 'This is article number 1.'
#     return HttpResponse(title)

# with 'render' function
def article_1(request):
    art = Article.objects.get()
    return render(request, 'article1.html', {'art': art})





def article_2(request):
    title = 'This is article number 2.'
    return HttpResponse(title)

def article_3(request):
    title = 'This is article number 3.'
    return HttpResponse(title)

# view, but using a template
def article_aaa_template(request):
    part = 'Treasure found at the base of the rainbow.'
    # load template
    t = get_template('article_template.html')
    # render template
    title = t.render(Context({'part':part}))
    # send template back to the browser
    return HttpResponse(title)

def articles(request):
    return render_to_response(
        'articles.html',
        { 'articles': Article.objects.all() })

# get method pulls out information from DB
def article(request, article_id=1):
    return render_to_response('article1.html',
                              { 'article': Article.objects.get(id=article_id) })

