import pdb

from django.test import TestCase
from django.core.urlresolvers import reverse

from wiki.models import Article

from general.functions import parse_post_content

class WikiViewTests(TestCase):
    def test_new_index_view(self):
        """
        When accessing the index for the first time, it should redirect to an
        edit page
        """
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response['location'], 'http://testserver/wiki/edit/Index/')

    def test_old_index_view(self):
        """
        When accessing the index page after the first time, it should return an
        article object.
        """
        Article.objects.create()
        article = self.client.get(reverse('wiki:index')).context['article']
        self.assertEqual(article['title'], 'Index')
        self.assertEqual(article['content'], 'Fill me with content')

    def test_edit_post_view(self):
        """
        When sending a post request to wiki:edit with the name of an article that
        does not exist yet, it should create a new article and redirect to that 
        article
        """
        response = self.client.get(reverse('wiki:display', args=('test',)))
        self.assertEqual(response['location'], 'http://testserver/wiki/edit/test/')
        response = self.client.post(response['location'], {'content':'test content'})
        self.assertEqual(response['location'], 'http://testserver/wiki/test/')

        article = self.client.get(reverse('wiki:display', args=('test',))).context['article']
        self.assertEqual(article['display_title'], 'Test')
        self.assertEqual(article['content'], 'test content')
