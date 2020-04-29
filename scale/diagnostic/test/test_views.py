from __future__ import unicode_literals

import json

import django
from django.test import TransactionTestCase
from rest_framework import status
from mock import patch

import storage.test.utils as storage_test_utils
import util.rest as rest_util
from rest_framework.test import APITransactionTestCase
from util import rest


class TestQueueScaleBakeView(APITransactionTestCase):

    fixtures = ['diagnostic_job_types.json', 'diagnostic_recipe_types.json']

    def setUp(self):
        django.setup()

        rest.login_client(self.client, is_staff=True)

    def test_bad_num(self):
        """Tests calling the view with a num of 0 (which is invalid)."""

        json_data = {
            'num': 0
        }

        url = rest_util.get_url('/diagnostics/job/bake/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    @patch('queue.models.CommandMessageManager')
    def test_successful(self, mock_msg_mgr):
        """Tests calling the view to create Scale Bake jobs."""

        json_data = {
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/job/bake/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED, response.content)


class TestQueueScaleCasinoView(APITransactionTestCase):

    fixtures = ['diagnostic_job_types.json', 'diagnostic_recipe_types.json']

    def setUp(self):
        django.setup()

        rest.login_client(self.client, is_staff=True)

    def test_bad_num(self):
        """Tests calling the view with a num of 0 (which is invalid)."""

        json_data = {
            'num': 0
        }

        url = rest_util.get_url('/diagnostics/recipe/casino/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    @patch('queue.models.CommandMessageManager')
    def test_successful(self, mock_msg_mgr):
        """Tests calling the view to create Scale Casino recipes."""

        json_data = {
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/recipe/casino/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED, response.content)

class TestQueueScaleHelloView(APITransactionTestCase):

    fixtures = ['diagnostic_job_types.json', 'diagnostic_recipe_types.json']

    def setUp(self):
        django.setup()

        rest.login_client(self.client, is_staff=True)

    def test_bad_num(self):
        """Tests calling the view with a num of 0 (which is invalid)."""

        json_data = {
            'num': 0
        }

        url = rest_util.get_url('/diagnostics/job/hello/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    @patch('queue.models.CommandMessageManager')
    def test_successful(self, mock_msg_mgr):
        """Tests calling the view to create Scale Hello jobs."""

        json_data = {
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/job/hello/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED, response.content)


class TestQueueScaleRouletteView(APITransactionTestCase):

    fixtures = ['diagnostic_job_types.json', 'diagnostic_recipe_types.json']

    def setUp(self):
        django.setup()

        rest.login_client(self.client, is_staff=True)

    def test_bad_num(self):
        """Tests calling the view with a num of 0 (which is invalid)."""

        json_data = {
            'num': 0
        }

        url = rest_util.get_url('/diagnostics/job/roulette/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    @patch('queue.models.CommandMessageManager')
    def test_successful(self, mock_msg_mgr):
        """Tests calling the view to create Scale Roulette jobs."""

        json_data = {
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/job/roulette/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED, response.content)


class TestQueueScaleIfView(APITransactionTestCase):
    fixtures = ['diagnostic_job_types.json', 'diagnostic_recipe_types.json']

    def setUp(self):
        django.setup()

        rest.login_client(self.client, is_staff=True)
        self.workspace = storage_test_utils.create_workspace()

    def test_bad_args(self):
        """Tests calling the view with an invalid workpace and a num of 0 (which is invalid)."""

        json_data = {
            'workspace': 'nonexistant',
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/recipe/if/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

        json_data = {
            'workspace': self.workspace.name,
            'num': 0
        }

        url = rest_util.get_url('/diagnostics/recipe/if/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    @patch('queue.models.CommandMessageManager')
    def test_successful(self, mock_msg_mgr):
        """Tests calling the view to create Scale If recipes."""
        json_data = {
            'workspace': self.workspace.name,
            'num': 10
        }

        url = rest_util.get_url('/diagnostics/recipe/if/')
        response = self.client.generic('POST', url, json.dumps(json_data), 'application/json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED, response.content)



class MockCommandMessageManager():

    def send_messages(self, commands):
        new_commands = []
        while True:
            for command in commands:
                command.execute()
                new_commands.extend(command.new_messages)
            commands = new_commands
            if not new_commands:
                break
            new_commands = []