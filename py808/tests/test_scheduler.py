import datetime
from unittest import TestCase, mock

from py808.scheduler import Scheduler


class TestScheduler(TestCase):

    def test_seconds_per_step_calc_works_correctly(self):
        sut = Scheduler(bpm=96)
        self.assertEqual(sut.seconds_per_step, 0.625)

    @mock.patch.object(Scheduler, '_now')
    def test_seconds_until_next_step_gives_remainder_time_until_next_step(self, now):
        start = datetime.datetime(2018, 2, 14, 5, 10, 0, 0)  # Baseline timestamp
        end = datetime.datetime(2018, 2, 14, 5, 10, 0, 1000) # 1000 microseconds later
        now.side_effect = [start, end]
        sut = Scheduler(bpm=96)
        sut.start_step()
        sut.stop_step()
        
        self.assertEqual(sut.seconds_per_step, 0.625)
        self.assertEqual(sut.seconds_until_next_step, 0.624) # Time left until next cycle

    def test_seconds_until_next_step_raises_exception_without_invoking_start_step(self):
        sut = Scheduler(bpm=96)
        sut.start_step()
        with self.assertRaises(Exception) as e:
            sut.seconds_until_next_step

    def test_seconds_until_next_step_raises_exception_without_invoking_stop_step(self):
        sut = Scheduler(bpm=96)
        sut.stop_step()
        with self.assertRaises(Exception) as e:
            sut.seconds_until_next_step

    def test_seconds_until_next_step_will_clear_existing_intervals(self):
        sut = Scheduler(bpm=96)
        sut.start_step()
        sut.stop_step()
        eta = sut.seconds_until_next_step
        self.assertEqual(None, sut.start_interval)
        self.assertEqual(None, sut.stop_interval)
