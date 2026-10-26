"""Regression tests for the documented SVG figure contract."""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_figures import validate_repo


SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" role="img"
    aria-labelledby="fig-title fig-desc">
<title id="fig-title">속도 그래프</title>
<desc id="fig-desc">시간에 비례해 속도가 증가하는 그래프</desc>
<path d="M0 400 L800 0" fill="none" stroke="blue"/>
</svg>'''


class FigureConventionsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.figure = self.root / "docs/assets/figures/calculus/speed-graph.svg"
        self.figure.parent.mkdir(parents=True)
        self.figure.write_text(SVG, encoding="utf-8")
        self.markdown = self.root / "docs/mathematics/example.md"
        self.markdown.parent.mkdir(parents=True)
        self.markdown.write_text(
            "# 예시\n\n![시간별 속도 곡선](../assets/figures/calculus/speed-graph.svg)\n\n"
            "*속도가 선형 증가하는 예시입니다.*\n", encoding="utf-8"
        )

    def assert_issue(self, keyword):
        issues = validate_repo(self.root)
        self.assertTrue(any(keyword in issue for issue in issues), issues)

    def test_valid_figure_and_markdown(self):
        self.assertEqual(validate_repo(self.root), [])

    def test_broken_image_path(self):
        text = self.markdown.read_text(encoding="utf-8").replace("speed-graph.svg", "unknown.svg")
        self.markdown.write_text(text, encoding="utf-8")
        self.assert_issue("image not found")

    def test_missing_alt_text(self):
        text = self.markdown.read_text(encoding="utf-8").replace("[시간별 속도 곡선]", "[]")
        self.markdown.write_text(text, encoding="utf-8")
        self.assert_issue("alt text")

    def test_missing_caption(self):
        text = self.markdown.read_text(encoding="utf-8").replace("*속도가 선형 증가하는 예시입니다.*", "해석이 없습니다.")
        self.markdown.write_text(text, encoding="utf-8")
        self.assert_issue("explanatory caption")

    def test_invalid_svg_xml(self):
        self.figure.write_text("<svg><title>broken", encoding="utf-8")
        self.assert_issue("invalid SVG XML")

    def test_svg_accessibility(self):
        self.figure.write_text(SVG.replace('role="img"', 'role="presentation"'), encoding="utf-8")
        self.assert_issue("role=img")

    def test_unreferenced_svg(self):
        another = self.figure.with_name("unused-figure.svg")
        another.write_text(SVG, encoding="utf-8")
        self.assert_issue("not referenced")

    def test_external_image_path_is_rejected(self):
        text = self.markdown.read_text(encoding="utf-8").replace(
            "../assets/figures/calculus/speed-graph.svg", "https://example.com/figure.svg"
        )
        self.markdown.write_text(text, encoding="utf-8")
        self.assert_issue("relative local image path")

    def test_svg_script_is_rejected(self):
        self.figure.write_text(SVG.replace("</svg>", "<script>alert(1)</script></svg>"), encoding="utf-8")
        self.assert_issue("not allowed")


if __name__ == "__main__":
    unittest.main()
