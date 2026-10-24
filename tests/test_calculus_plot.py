"""모든 미적분 시뮬레이터가 공유하는 그래프의 좌표 표시를 확인합니다."""

import unittest

from simulations.calculus_plot import chart


class CalculusPlotTests(unittest.TestCase):
    def test_coordinates_and_readable_hover(self):
        graph = chart(
            [(0, 0), (1, 1)],
            x_range=(0, 1),
            y_range=(0, 1),
            x_ticks=(0, 1),
            y_ticks=(0, 1),
            x_label="시간 t (s)",
            y_label="높이 y (m)",
            tooltip=lambda x, y: f"x={x:.1f} & y={y:.1f}",
        )
        self.assertIn('points="62.0,330.0 662.0,32.0"', graph)
        self.assertIn('x=0.5 &amp; y=0.5', graph)
        self.assertIn('font-size="22"', graph)


if __name__ == "__main__":
    unittest.main()
