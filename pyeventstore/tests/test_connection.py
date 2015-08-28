import unittest

import mock

from .. import connection


class TestConnection(unittest.TestCase):

    @mock.patch('pyeventstore.connection.socket')
    def test_default_behaviour(self, fake_socket):
        fake_connection = mock.Mock()
        fake_socket.socket.Mock(return_value=fake_connection)
        with connection.connect('example.com') as s:
            self.assertIsInstance(s, mock.Mock)
            s.connect.assert_called_with(('example.com', 1113))
        s.close.assert_called_with()

    @mock.patch('pyeventstore.connection.socket')
    def test_closed_even_any_error(self, fake_socket):
        fake_connection = mock.Mock()
        fake_socket.socket.Mock(return_value=fake_connection)
        try:
            with connection.connect('example.com') as s:
                raise TestException()
        except TestException:
            pass
        s.close.assert_called_with()


class TestException(Exception):
    pass
