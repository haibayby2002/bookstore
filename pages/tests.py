from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView
# Create your tests here.

class HomepageTest(SimpleTestCase):
    def setUp(self): # new
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        # response = self.client.get("/")
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        # response = self.client.get(reverse("home"))
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # response = self.client.get("/")
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self): # new
        # response = self.client.get("/")
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self): # new
        # response = self.client.get("/")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve("/")
        # print(view.func.__name__, HomePageView.as_view().__name__)
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )    