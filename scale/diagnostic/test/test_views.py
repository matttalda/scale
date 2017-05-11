from __future__ import unicode_literals

import json

import django
from django.test import TransactionTestCase
from rest_framework import status

import util.rest as rest_util


class TestQueueScaleHelloView(TransactionTestCase):

    fixtures = ['diagnostic_job_types.json']

    def setUp(self):
        django.setup()

    def test_bad_num(self):
        """Tests calling the view with a num of 0 (which is invalid)."""

        json_data = {
            'num': 0
        }

        url = rest_util.get_url('/diagnostics/job/hello/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    def test_successful(self):
        """Tests calling the view to create Scale Hello jobs."""

        json_data = {
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/job/hello/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED, response.content)
