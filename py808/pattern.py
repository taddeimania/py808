

class Pattern:
    """A pattern represents a single vector of 8 steps in the drum sequencer. A user
    will define multiple patterns and compose them into a Track along with an Instrument.
    A pattern defines the ON / OFF state for a step.

    Attributes
    ----------
    pattern_value : int
        The 8 bit unsigned integer in decimal form that will be translated into the steps.
    bin_pattern : str
        A string containing the 1's and 0's from the pattern_value
    current_step : int
        Pointer for looking at the current step

    Methods
    -------
    - Static
    convert_val_to_binary(val) : str
        Converts a decimal value into it's 8 bit binary string.

    - Method
    increment_step() : int
        Increment the current step pointer by one or roll it over if it's at the end of a pattern.
    get_tick() : int
        Returns a 1 or a 0 for the given step.
    _clear_intervals() : void
        Resets intervals to None.
    _now() : datetime.datetime
        Helper to provide "now" datetime. Makes it easier for testing.
    """

    def __init__(self, pattern=0):
        if pattern < 0 or pattern > 255:
            raise Exception("Pattern Value must be between 0-255")
        self.pattern_value = pattern
        self.bin_pattern = self._convert_val_to_binary(pattern)
        self.current_step = 0

    def increment_step(self) -> int:
        if self.current_step == 7:
            self.current_step = 0
        else:
            self.current_step += 1
        return self.current_step

    def get_tick(self) -> int:
        # I originally had an overly complicated bitwise shift implementation below but realized
        # a much less complex way. I'm leaving it here for discussions sake and it was kind of clever

        # return int(self._convert_val_to_binary(self.pattern_value >> 7 - self.current_step)[-1])
        return int(self._convert_val_to_binary(self.pattern_value)[self.current_step])
    
    def get_flattened_bits(self) -> tuple:
        return tuple(map(lambda _: int(_), self.bin_pattern))
    
    @staticmethod
    def _convert_val_to_binary(val) -> str:
        return '{0:08b}'.format(val)

    def __str__(self) -> str:
        return "|{}|{}|{}|{}|{}|{}|{}|{}".format(*self.bin_pattern)


class Rest(Pattern):

    def __init__(self):
        super().__init__()


class Slam(Pattern):

    def __init__(self):
        super().__init__(255)
