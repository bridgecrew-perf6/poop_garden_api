from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PoopProfile
# Tests

class PoopProfileTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_poopProfile = PoopProfile.objects.create(
            user = testuser1,
            poopInfo= 54,
            nickname = 'test'
        )
        test_poopProfile.save()

    def test_pooperProfile_content(self):
        profile = PoopProfile.objects.get(id=1)
        actual_nickname = profile.nickname
        actual_info = profile.poopInfo
        self.assertEqual(actual_nickname, 'test')
        self.assertEqual(actual_info, 54)
