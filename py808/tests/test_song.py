from unittest import TestCase

from py808.pattern import Pattern
from py808.instrument import Instrument
from py808.track import Track
from py808.song import Song


class TestSong(TestCase):

    def test_song_displays_correctly(self):
        # Track 1
        pattern_1 = Pattern(170)
        pattern_2 = Pattern(120)
        kick = Instrument('Kick', 'boom')
        track_1 = Track(kick, pattern_1, pattern_2)

        # Track 2
        pattern_3 = Pattern(14)
        pattern_4 = Pattern(200)
        beep = Instrument('Random', 'beep')
        track_2 = Track(beep, pattern_3, pattern_4)

        song = Song(120, False, track_1, track_2)
        self.assertEqual(
            song.__str__(), 
            'Kick       |1|0|1|0|1|0|1|0|0|1|1|1|1|0|0|0\nRandom     |0|0|0|0|1|1|1|0|1|1|0|0|1|0|0|0\n'
         )

    def test_song_raises_exception_if_tracks_arent_all_the_same_length(self):
        # Track 1
        pattern_1 = Pattern(170)
        pattern_2 = Pattern(120)
        kick = Instrument('Kick', 'boom')
        track_1 = Track(kick, pattern_1, pattern_2)

        # Track 2
        pattern_3 = Pattern(14)
        beep = Instrument('Random', 'beep')
        track_2 = Track(beep, pattern_3)
        with self.assertRaises(Exception) as e:
            Song(120, False, track_1, track_2)

    def test_song_get_all_sounds_at_pointer_return_all_current_sounds(self):
        # Track 1
        pattern_1 = Pattern(170)
        pattern_2 = Pattern(120)
        kick = Instrument('Kick', 'boom')
        track_1 = Track(kick, pattern_1, pattern_2)

        # Track 2
        pattern_3 = Pattern(14)
        pattern_4 = Pattern(200)
        beep = Instrument('Random', 'beep')
        track_2 = Track(beep, pattern_3, pattern_4)

        sut = Song(120, False, track_1, track_2)
        self.assertEqual(sut.get_all_sounds_at_pointer(), 'boom')
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        self.assertEqual(sut.get_all_sounds_at_pointer(), 'boom+beep')

