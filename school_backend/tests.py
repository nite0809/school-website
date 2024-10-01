from django.test import TestCase
from django.urls import reverse

class MainPageTests(TestCase):
    def test_homepage_status_code(self):
        """
        Test that the homepage returns a status code of 200 (OK).
        """
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of your URL pattern
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_template(self):
        """
        Test that the homepage uses the correct template (index.html).
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_contains_static_image(self):
        """
        Test that the homepage contains a reference to the static image.
        """
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'src="img\genesis-image1.jpg"')  # Adjust to match your image path
