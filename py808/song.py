import asyncio
import os
import time

from .scheduler import Scheduler

class Song:
    """A Song is a compilation of all of the tracks that compose a song. It manages the
    state of the playback as well as being responsible for moving the current
    pointer forward for all of the tracks.  For most intents and purposes, the Song
    is the main entry point for when you want to play your composition.

    Attributes
    ----------
    tracks : List<Track>
        All tracks in a song.
    track_count : int
        The amount of tracks in a song.
    step_pointer : int
        The current step a song is at.
    scheduler : Scheduler
        Helper responsible for providing timing information for advancing the step.
    loop : Boolean
        Repeat the song over and over.

    Methods
    -------
    start()
        Main entry point to play a song. Starts all async loop handling code.
    play()
        Primary song advancing logic and UI code.
    get_all_sounds_at_pointer()
        Responsible for combining all sounds at a given step for output.
    increment_steps()
        Move all tracks step pointer forward.
    reset_steps()
        Reset all tracks step pointer to zero (for looping).
    valid_tracks()
        Validation to make sure all tracks are the same length.
    """

    def __init__(self, bpm=96, loop=False, *tracks):

        self.tracks = tracks
        if not self.valid_tracks():
            raise Exception("All tracks must contain the same amount of patterns")
        self.track_count = len(tracks)
        self.step_pointer = 0
        self.scheduler = Scheduler(bpm)
        self.loop = loop

    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(self.play())
        )
        loop.close()

    async def play(self):
        while True:
            log = []
            for step in range(len(self.tracks[0].get_flattened_pattern_bits())):
                self.scheduler.start_step()
                os.system('clear')
                print(self)
                print(" " * 12 + " " * (step * 2) + "X")
                log.append(self.get_all_sounds_at_pointer())
                print("|".join(log))
                self.increment_step()
                self.scheduler.stop_step()
                await asyncio.sleep(self.scheduler.seconds_until_next_step)
            if not self.loop:
                return
            self.reset_steps()

    def get_all_sounds_at_pointer(self) -> str:
        return "+".join([track.get_sound() for track in self.tracks if track.making_sound()])

    def increment_step(self):
        for track in self.tracks:
            track.increment_step()
        self.step_pointer += 1

    def reset_steps(self):
        for track in self.tracks:
            track.reset_steps()
        self.step_pointer = 0


    def valid_tracks(self) -> bool:
        length = len(self.tracks[0].get_flattened_pattern_bits())
        for track in self.tracks[1:]:
            if len(track.get_flattened_pattern_bits()) != length:
                return False
        return True

    def __str__(self) -> str:
        return ("{}\n" * self.track_count).format(*self.tracks)
