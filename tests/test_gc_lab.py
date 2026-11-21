import unittest

from main import run_demo


class GarbageCollectorLabTests(unittest.TestCase):
    def test_demo_reclaims_self_cycles(self):
        result = run_demo(25)
        self.assertEqual(result["created_cycles"], 25)
        self.assertEqual(result["tracked_before_release"], 25)
        self.assertEqual(result["reclaimed_cycles"], 25)
        self.assertGreaterEqual(result["collected_objects"], 25)

    def test_zero_cycles_is_valid(self):
        result = run_demo(0)
        self.assertEqual(result["created_cycles"], 0)
        self.assertEqual(result["reclaimed_cycles"], 0)

    def test_cycle_limit_is_enforced(self):
        with self.assertRaises(ValueError):
            run_demo(100001)


if __name__ == "__main__":
    unittest.main()
