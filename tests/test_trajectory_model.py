"""5차 궤적의 경계 조건과 도함수 관계를 확인합니다."""

import unittest

from simulations.trajectory_model import state


class TrajectoryModelTests(unittest.TestCase):
    def test_boundaries_and_derivatives(self):
        distance, duration = 12, 5
        self.assertEqual(state(distance, duration, 0), (0, 0, 0, 60 * distance / duration**3))
        end = state(distance, duration, duration)
        self.assertAlmostEqual(end[0], distance)
        self.assertAlmostEqual(end[1], 0)
        self.assertAlmostEqual(end[2], 0)

        time, step = 1.7, 1e-4
        before, now, after = (state(distance, duration, t) for t in (time - step, time, time + step))
        for index in range(3):
            self.assertAlmostEqual((after[index] - before[index]) / (2 * step), now[index + 1], places=5)


if __name__ == "__main__":
    unittest.main()
