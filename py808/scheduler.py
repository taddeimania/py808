
import datetime


class Scheduler:
    """The scheduler is responsible for keeping time for the sequencer. It's primary
    function is to track the start of the step and the end of the step to account for
    CPU processing time between instructions. Then it subtracts that time from the total
    time between steps so that the Song can delay the correct amount to maintain a steady beat
    regardless of CPU/Memory latency.

    Attributes
    ----------
    bpm : int
        How many beats per minute to schedule

    Properties
    ----------
    seconds_per_step : float
        Calculate how many seconds per step given the BPM.
    seconds_until_next_step : float
        Calculate the delay amount before the next step has to happen.

    Methods
    -------
    start_step() : void
        Sets the start interval to the time it is called.
    stop_step() : void
        Sets the stop interval to the time it is called.
    _clear_intervals() : void
        Resets intervals to None.
    _now() : datetime.datetime
        Helper to provide "now" datetime. Makes it easier for testing.
    """

    def __init__(self, bpm=120):
        self._clear_intervals()
        self.bpm = bpm

    @property
    def seconds_per_step(self) -> float:
        return ((60 / self.bpm) * 4) / 4

    def start_step(self):
        self.start_interval = self._now()

    def stop_step(self):
        self.stop_interval = self._now()

    @property
    def seconds_until_next_step(self) -> float:
        """The purpose of this property is to provide the interpreter with how many fractions of a second
        to delay prior to the next scheduled step.
        """
        if self.stop_interval == None or self.start_interval == None:
            raise Exception("You must call both the 'start_step' and 'stop_step' method prior to calling this method.")
        delta = self.stop_interval - self.start_interval
        self._clear_intervals()
        return (datetime.timedelta(seconds=self.seconds_per_step) - delta).microseconds / 1000000
        
    # Private

    def _clear_intervals(self):
        self.start_interval = None
        self.stop_interval = None

    def _now(self) -> datetime.datetime:
        """This is a helper method to make writing unit tests more friendly.
        """
        return datetime.datetime.now()
