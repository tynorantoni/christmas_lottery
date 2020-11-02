from django.contrib.auth import  logout
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from lottery.views import index, CustomLoginView


class TestUrls(SimpleTestCase):

    def test_is_index_resolved(self):
        url = reverse('lottery:index')
        self.assertEquals(resolve(url).func, index)

    def test_is_login_resolved(self):
        url = reverse('login')
        url2 = reverse('logout')
        self.assertEquals(resolve(url).func, resolve(url).func)
        self.assertEquals(resolve(url2).func, logout)



