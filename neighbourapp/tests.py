from django.test import TestCase
from models import *
# Create your tests here.

class NeighbourHoodTest(TestCase):
    def setup(self):
        self.new= NeighbourHood(name= 'new',location='maragi')

    def test_instances(self):
        self.assertTrue(isinstance(self.new,NeighbourHood))    

    def test_save_image(self):
        self.new.save_neighbour()
        after = NeighbourHood.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.new.delete_neighbour()
        neighbourhood_tests = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhood_tests) == 0)

    def test_update_neighborhood(self):
        self.new.save_neighbour()
        self.new.update_neighborhood(self.new.id )
        changed_neighburhood = NeighbourHood.objects.filter(neighbourhood='new')
        self.assertTrue(len(changed_neighburhood) > 0)    


class PosterTestClass(TestCase):
    def setUp(self):
        self.kimani= Business(name ='kimani', user='dennis',email='kimani@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.kimani, Business))

    def test_save_method(self):
        self.kimani.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses)>0)

    def test_delete_method(self):
        self.kimani.save_business()
        business = Business.objects.all()
        self.kimani.delete_business()
        self.assertTrue(len(business)==0) 

        