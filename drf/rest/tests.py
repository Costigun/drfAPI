from django.test import TestCase
from .models import Ezone
from django.utils import timezone
from django.urls import reverse

class EzoneTestCase(TestCase):
    def setUp(self):
        self.name = "Tests"
        self.description = "tests for app"
        self.category = "tested"
        Ezone.objects.create(name=self.name,
                             description=self.description,
                             category=self.category
                             )


    def test_max_length(self):
        name = Ezone.objects.get(id=1)
        max_length = name._meta.get.field('name').max_length
        self.assertEqual(max_length,15)


    def test_create_notes(self):
        number = 5
        for new_notes in range (number):
            Ezone.objects.create(name="test" % new_notes,
                                 description="lorem ipsum dolore" % new_notes,
                                 category="categoryyyyyyyyyy" % new_notes
                                 )


