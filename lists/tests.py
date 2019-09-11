# from django.urls import resolve
from django.test import TestCase
# from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_ndles_post_request(self):
        response = self.client.post('/', {'item_text': 'a list item'})
        self.assertIn('a list item', response.content.decode())
