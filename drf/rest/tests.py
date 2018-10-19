from django.test import TestCase
from .models import Ezone
# Create your tests here.
class EzoneTestCase(TestCase):
    def setUp(self):
        Ezone.objects.create(name="Like")

    def test_ezone_can_add(self):
        like = Ezone.objects.get(name='lice')
        self.assertEqual(like.speak(),'Like is good')