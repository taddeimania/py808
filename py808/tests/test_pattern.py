from unittest import TestCase

from py808.pattern import Pattern, Slam, Rest


class TestPattern(TestCase):

    def test_pattern_pattern_value_must_be_between_0_and_255(self):
        with self.assertRaises(Exception) as e:
            sut = Pattern(-1)
        with self.assertRaises(Exception) as e:
            sut = Pattern(256)

        with self.assertRaises(AssertionError):  # Python's weird way of writing "assert not raises"
            with self.assertRaises(Exception) as e:
                sut = Pattern(255)

        with self.assertRaises(AssertionError):
            with self.assertRaises(Exception) as e:
                sut = Pattern(0)

    def test_pattern_current_step_initializes_to_0(self):
        sut = Pattern()
        self.assertEqual(sut.current_step, 0)

    def test_pattern_current_step_can_be_incremented(self):
        sut = Pattern()
        sut.increment_step()
        self.assertEqual(sut.current_step, 1)

    def test_pattern_current_step_rolls_over_at_8(self):
        sut = Pattern()
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        sut.increment_step()
        self.assertEqual(sut.current_step, 7)
        sut.increment_step()
        self.assertEqual(sut.current_step, 0)

    def test_pattern_gets_its_pattern_from_binary_numbers(self):
        # This imposes a limit on patterns only being able to
        # support 8 bit unsigned ints. If someone wanted a longer pattern 
        # perhaps we could create a collection class and call it CompoundPattern.
        sut = Pattern(170)
        self.assertEqual(sut.__str__(), '|1|0|1|0|1|0|1|0')

    def test_pattern_get_tick_will_reveal_if_current_step_is_a_1_or_0(self):
        sut = Pattern(120)
        self.assertEqual(sut.get_tick(), 0)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 1)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 1)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 1)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 1)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 0)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 0)
        sut.increment_step()
        self.assertEqual(sut.get_tick(), 0)

    def test_pattern_get_flattened_bits_returns_tuple_of_bits(self):
        sut = Pattern(120)
        self.assertEqual(sut.get_flattened_bits(), (0, 1, 1, 1, 1, 0, 0, 0))
        
    def test_rest_pattern_is_a_helper_for_an_empty_pattern(self):
        sut = Rest()
        self.assertEqual(sut.__str__(), '|0|0|0|0|0|0|0|0')

    def test_slam_pattern_is_a_helper_for_a_full_pattern(self):
        sut = Slam()
        self.assertEqual(sut.__str__(), '|1|1|1|1|1|1|1|1')
