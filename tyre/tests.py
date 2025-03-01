from django.test import TestCase
from .models import Tyre

class TyreModelTest(TestCase):

    def setUp(self):
        """Create a sample tyre record for testing."""
        self.tyre = Tyre.objects.create(rfid="123ABC", status="In")

    def test_tyre_creation(self):
        """Test if a tyre object is created successfully."""
        self.assertEqual(self.tyre.rfid, "123ABC")
        self.assertEqual(self.tyre.status, "In")

    def test_str_representation(self):
        """Test the string representation of Tyre model."""
        self.assertEqual(str(self.tyre), "123ABC")
