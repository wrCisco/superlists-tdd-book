from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.content.decode('utf8')
#         expected_html = render_to_string('lists/home.html')
#         self.assertEqual(html, expected_html)
        response = self.client.get('/')
#         html = response.content.decode('utf-8')
#         self.assertTrue(html.startswith('<html>'))
#         self.assertIn('<title>To-Do lists</title>', html)
#         self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')

