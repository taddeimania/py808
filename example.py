"""This is an example use of the drum sequencer `py808` module.

The interface follows the following psuedocode
- Create a few patterns for a track
- Create an instrument for that track
- Create a track that combines the instrument and patterns
--- repeat as many times as you like ---

- Create a song that contains the following information:
 - BPM
 - Loop?
 - and each Track as a positional argument.
   - Caveat: Make sure all tracks are the same length or you'll raise an exception

- Run the "start" method on the song and awaayyyyyyyy we gooooo!
"""


from py808.pattern import Pattern, Rest
from py808.instrument import Instrument
from py808.track import Track
from py808.song import Song

pattern_1 = Pattern(136)
pattern_2 = Pattern(136)
kick = Instrument('Boots', 'boots', 400)
track_1 = Track(kick, pattern_1, pattern_2)

pattern_3 = Pattern(85)
pattern_4 = Pattern(85)
n = Instrument('And', 'n', 400)
track_2 = Track(n, pattern_3, pattern_4)

pattern_5 = Pattern(34)
pattern_6 = Pattern(34)
cats = Instrument('Cats', 'cats', 400)
track_3 = Track(cats, pattern_5, pattern_5)

pattern_7 = Pattern(99)
pattern_8 = Pattern(99)
dan = Instrument('Dan', 'dan', 400)
track_4 = Track(cats, pattern_7, pattern_8)

song = Song(220, True, track_1, track_2, track_3, track_4)
song.start()
