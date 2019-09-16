# from django.urls import resolve
from django.test import TestCase
from lists.models import Item
# from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_ndles_post_request(self):
        response = self.client.post('/', {'item_text': 'a list item'})
        self.assertIn('a list item', response.content.decode())

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'Item the first (ever) list item'
        first_item.save()


        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Item the first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


