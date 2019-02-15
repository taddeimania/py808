from unittest import TestCase

from py808.pattern import Pattern
from py808.instrument import Instrument
from py808.track import Track


class TestTrack(TestCase):

    def test_track_displays_correctly(self):
        pattern_1 = Pattern(170)
        pattern_2 = Pattern(120)
        instrument = Instrument('Kick', 'boom')
        sut = Track(instrument, pattern_1, pattern_2)
        self.assertEqual(sut.__str__(), 'Kick       |1|0|1|0|1|0|1|0|0|1|1|1|1|0|0|0')

    def test_track_get_flattened_pattern_bits_flattens_all_pattern_bits(self):
        pattern_1 = Pattern(170)
        pattern_2 = Pattern(120)
        instrument = Instrument('Kick', 'boom')
        sut = Track(instrument, pattern_1, pattern_2)
        self.assertEqual(sut.get_flattened_pattern_bits(), (1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0))

    def test_track_get_sound_returns_instruments_sound_based_on_current_pointer_in_track(self):
        pattern_1 = Pattern(170)
        pattern_2 = Pattern(120)
        instrument = Instrument('Kick', 'boom')
        sut = Track(instrument, pattern_1, pattern_2)
        self.assertEqual(sut.get_sound(), 'boom')
        sut.increment_step()
        self.assertEqual(sut.get_sound(), '')
