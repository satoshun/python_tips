from . import TestCase

from mapping import reverse_mapping


class TestMapping(TestCase):
    def test_reverse_mapping(self):

        mock_data = {'key': 'value'}
        expected = {'value': ['key']}
        after_mock_data = reverse_mapping(mock_data)
        assert after_mock_data == expected
