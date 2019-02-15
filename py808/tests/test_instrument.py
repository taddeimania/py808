from unittest import TestCase

from py808.instrument import Instrument


class TestInstrument(TestCase):

    def test_name_cannot_be_longer_than_10_char(self):
        with self.assertRaises(Exception) as e:
            Instrument('My Kick is awesome', 'boom')
