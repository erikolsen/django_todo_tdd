# from django.urls import resolve
from django.test import TestCase
# from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertIn(
            '<title>To-Do Lists</title>',
            response.content.decode()
        )
        # found = resolve('/')
        # self.assertEqual(found.func, home_page)
