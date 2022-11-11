from django.test import TestCase

# Create your tests here.

from store.models import Catagory, Product


class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Catagory.objects.create(name='django', slug='django')

    def test_category_model_entery(self):
        '''
        Test category model data inseratoin /types/field attributes

        '''

        data = self.data1
        self.assertTrue(isinstance(data, Catagory))