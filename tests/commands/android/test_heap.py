import unittest
from unittest import mock

from objection.commands.android.heap import live_instances
from tests.helpers import capture


class TestHeap(unittest.TestCase):
    @mock.patch('objection.state.connection.state_connection.get_api')
    def test_print_love_instances_validates_command(self, mock_api):
        with capture(live_instances, []) as o:
            output = o

        self.assertEqual('Usage: android heap print_instances <class> (eg: com.example.test)\n', output)
        self.assertFalse(mock_api.return_value.android_live_print_class_instances.called)

    @mock.patch('objection.state.connection.state_connection.get_api')
    def test_print_love_instances_validates_command(self, mock_api):
        live_instances(['java.io.File'])

        self.assertTrue(mock_api.return_value.android_live_print_class_instances.called)
