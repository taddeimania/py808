
import itertools
import subprocess
import sys


class Track:
    """A Track is a grouping of a singular Instrument and one or many patterns.
    It can be easiest understood as a horizontal line on a drum sequencer.

    Attributes
    ----------
    instrument : Instrument
        Instrument to use for this track.
    pattern_list : List<Pattern>
        List containing all patterns.
    pattern_count : int
        How many patterns are in this arrangement.
    pattern_bits : Tuple<int>
        The pattern groups as a flat tuple of 1's and 0's.
    step_pointer : int
        Current location of the song.

    Methods
    -------
    making_sound() : int
        Returns a 1 if the current track is making a sound, 0 if not.
    get_sound() : str
        Gives the sound the track's instrument is currently playing, also play it audibly.
    reset_steps() : void
        Resets step_pointer to 0.
    increment_step() : void
        Increment track's step_pointer by 1.
    get_flattened_pattern_bits() : Tuple<int>
        Return a tuple containing 0's and 1's of a track's sound state.
    """

    def __init__(self, instrument, *pattern_list):
        self.instrument = instrument
        self.pattern_list = pattern_list
        self.pattern_count = len(pattern_list)
        self.pattern_bits = self.get_flattened_pattern_bits()
        self.step_pointer = 0

    def making_sound(self) -> int:
        sound = self.pattern_bits[self.step_pointer]
        return sound

    def get_sound(self) -> str:
        if self.making_sound() and sys.platform == "darwin": # Only play sound for OSX-macOS
            # Popen will start a non-blocking subprocess that will play our sound and not block
            # other sounds from happening. Pretty cool when you layer 10 voices.
            subprocess.Popen(['say', '-v', 'victoria', self.instrument.sound, '-r', str(self.instrument.speed)])
        return self.instrument.sound if self.making_sound() else ''

    def reset_steps(self):
        self.step_pointer = 0

    def increment_step(self):
        self.step_pointer += 1

    def get_flattened_pattern_bits(self) -> tuple:
        return tuple(itertools.chain(*map(lambda _: _.get_flattened_bits(), self.pattern_list)))

    def __str__(self) -> str:
        track_template = ("{}" * self.pattern_count).format(*self.pattern_list)
        return "{:10} {}".format(self.instrument.name, track_template)
