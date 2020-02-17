import pytz
from django.test import TestCase
from ..models import House, Task

from datetime import datetime, date


class HouseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        House.objects.create(address='ул.Пожарского 12', year_of_construction=date(1991, 3, 12))

    def test_address_label(self):
        house = House.objects.get(id=1)
        field_label = house.address
        self.assertEquals(field_label, 'ул.Пожарского 12')

    def test_year_of_construction_label(self):
        house = House.objects.get(id=1)
        field_label = house.year_of_construction
        self.assertEquals(field_label, date(1991, 3, 12))

    def test_get_absolute_url(self):
        house = House.objects.get(id=1)
        self.assertEquals(house.get_absolute_url(), '/building/1')


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        House.objects.create(address='ул.Пожарского 12', year_of_construction=datetime(1991, 3, 12).date())
        Task.objects.create(number_of_bricks=12345, date_and_time=datetime(1991, 3, 13, 13, 00, tzinfo=pytz.utc))

    def test_number_of_bricks_label(self):
        task = Task.objects.get(id=1)
        field_label = task.number_of_bricks
        self.assertEquals(field_label, 12345)

    def test_date_and_time_label(self):
        task = Task.objects.get(id=1)
        field_label = task.date_and_time
        self.assertEquals(field_label, datetime(1991, 3, 13, 13, 00, tzinfo=pytz.utc))



