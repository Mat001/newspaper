from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

# Create your views here.

# view for title_aaa
def title_aaa(request):
    title = 'Treasure found at the base of the rainbow.'
    return HttpResponse(title)

# view, but using a template
def title_aaa_template(request):
    part = 'Treasure found at the base of the rainbow.'
    # load template
    t = get_template('title_template.html')
    # render template
    title = t.render(Context({'part':part}))
    # send template back to the browser
    return HttpResponse(title)