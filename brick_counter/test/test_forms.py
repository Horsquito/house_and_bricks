from django.test import TestCase
from ..forms import HouseForm, TaskForm

from datetime import datetime, date

class HouseFormTest(TestCase):

    def test_normal_addreess_length(self):
        address = 'ул. Северодвинская 11к1'
        year_of_constructions = date(1991, 3, 12)
        form_data = {'address': address, 'year_of_construction': year_of_constructions}
        form = HouseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_too_big_addreess_length(self):
        address = 'ул. Северодвинская 11к1' * 100
        form_data = {'address': address}
        form = HouseForm(data=form_data)
        self.assertFalse(form.is_valid())

class TaskFormTest:

    def test_normal_number_of_bricks(self):
        form_data = {'number_of_bricks': 123456}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid_number_of_bricks(self):
        form_data = {'number_of_bricks': -123456}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

