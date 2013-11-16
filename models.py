from django.db import models

import re
import string

from general.functions import parse_post_content, parse_wiki_title

class Article(models.Model):
    title = models.CharField(max_length=200, primary_key=True, default='Index')
    subtitle = models.CharField(max_length=1000, default="")
    last_edited = models.DateTimeField(auto_now=True)
    content = models.TextField(default='Fill me with content')

    def __unicode__(self):
        return self.title

    def build_article_dict(self, mode=''):
        article_dict = {}
        article_dict['title'] = self.title
        article_dict['display_title'] = parse_wiki_title(self.title)
        article_dict['last_edited'] = self.last_edited
        article_dict['subtitle'] = self.subtitle
        if mode:
            article_dict['content'] = parse_post_content(self.content, mode)
        else:
            article_dict['content'] = self.content
        return article_dict
