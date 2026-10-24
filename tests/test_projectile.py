"""포물선 운동 계산의 대표값과 입력 범위를 확인합니다."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "simulations"))
from projectile import trajectory  # noqa: E402


class ProjectileTests(unittest.TestCase):
    def test_45_degrees(self):
        points, flight_time, max_height, horizontal_range = trajectory(20, 45)
        self.assertAlmostEqual(flight_time, 2.8832, places=3)
        self.assertAlmostEqual(max_height, 10.1937, places=3)
        self.assertAlmostEqual(horizontal_range, 40.7747, places=3)
        self.assertAlmostEqual(points[0][1], 0)
        self.assertAlmostEqual(points[-1][1], 0)

    def test_invalid_inputs(self):
        for args in ((0, 45), (20, 0), (20, 90), (20, 45, 0)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                trajectory(*args)


if __name__ == "__main__":
    unittest.main()
