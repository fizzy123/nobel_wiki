import pdb
import logging
log = logging.getLogger(__name__)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404

from wiki.models import Article

from general.functions import parse_post_content

def display(request, name='Index'):
    a = Article.objects.filter(title=name)
    if a:
        a = a[0]
        context = {'article': a.build_article_dict()}
        return render(request, 'wiki/article.html', context)
    else:
        return HttpResponseRedirect(reverse('wiki:edit',args=(name,)))

def edit(request, name='Index'):
    if request.META['REQUEST_METHOD'] == 'GET':
        if request.session['logged_in'] if request.session.has_key('logged_in') else False:
            a = Article.objects.get_or_create(title=name)[0]
            context = {'article': a.build_article_dict('edit')}
            return render(request, 'wiki/edit.html', context)
        else:
            raise Http404
    elif request.META['REQUEST_METHOD'] == 'POST':
        parsed_content = parse_post_content(request.POST['content'], 'display')
        a, created = Article.objects.get_or_create(title=name)
        a.content = parsed_content
        a.subtitle = request.POST['subtitle'] if request.POST.has_key('subtitle') else ''
        a.save()
        return HttpResponseRedirect(reverse('wiki:display',args=(name,)))

