from datetime import date, datetime
import pytz
from django.test import TestCase
from django.urls import reverse
from ..models import House, Task


class StatsListViewTest(TestCase):

    def test_stats_view_url_exists(self):
        resp = self.client.get('/stats/')
        self.assertEqual(resp.status_code, 200)

    def test_stats_view_uses_correct_template(self):
        resp = self.client.get(reverse('brick_counter:stats'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'brick_counter/base_page.html')

    def test_building_view_url_exists(self):
        resp = self.client.get('/building/')
        self.assertEqual(resp.status_code, 200)

    def test_building_view_uses_correct_template(self):
        resp = self.client.get(reverse('brick_counter:building'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'brick_counter/building.html')







