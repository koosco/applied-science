"""미적분 시뮬레이터의 고정 축 SVG 그래프."""

from html import escape


def chart(
    points,
    *,
    x_range,
    y_range,
    x_ticks,
    y_ticks,
    x_label,
    y_label,
    tooltip,
    overlays=(),
    marker=None,
):
    left, right, top, bottom = 62, 662, 32, 330

    def screen(x, y):
        return (
            left + (x - x_range[0]) / (x_range[1] - x_range[0]) * (right - left),
            bottom - (y - y_range[0]) / (y_range[1] - y_range[0]) * (bottom - top),
        )

    def polyline(values, color, dashed=False):
        coordinates = " ".join(f"{sx:.1f},{sy:.1f}" for sx, sy in map(lambda p: screen(*p), values))
        dash = ' stroke-dasharray="7 5"' if dashed else ""
        return f'<polyline points="{coordinates}" fill="none" stroke="{color}" stroke-width="3"{dash} />'

    ticks = []
    for x in x_ticks:
        sx, _ = screen(x, y_range[0])
        ticks.append(
            f'<line x1="{sx:.1f}" y1="{top}" x2="{sx:.1f}" y2="{bottom}" stroke="#e2e8f0" />'
            f'<text x="{sx:.1f}" y="350" text-anchor="middle" font-size="14">{x:g}</text>'
        )
    for y in y_ticks:
        _, sy = screen(x_range[0], y)
        ticks.append(
            f'<line x1="{left}" y1="{sy:.1f}" x2="{right}" y2="{sy:.1f}" stroke="#e2e8f0" />'
            f'<text x="52" y="{sy + 5:.1f}" text-anchor="end" font-size="14">{y:g}</text>'
        )

    hover = []
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        sx1, sy1 = screen(x1, y1)
        sx2, sy2 = screen(x2, y2)
        x, y = (x1 + x2) / 2, (y1 + y2) / 2
        label = escape(tooltip(x, y))
        bx = min((sx1 + sx2) / 2 + 12, 370)
        by = max(min((sy1 + sy2) / 2 - 62, 310), 8)
        hover.append(
            f'<g class="sample"><line x1="{sx1:.1f}" y1="{sy1:.1f}" '
            f'x2="{sx2:.1f}" y2="{sy2:.1f}" stroke="transparent" '
            f'stroke-width="18" pointer-events="stroke" cursor="crosshair" '
            f'aria-label="{label}" />'
            f'<g class="sample-tooltip"><rect x="{bx:.1f}" y="{by:.1f}" '
            f'width="320" height="52" rx="8" fill="#0f172a" />'
            f'<text x="{bx + 14:.1f}" y="{by + 34:.1f}" fill="white" '
            f'font-size="22">{label}</text></g></g>'
        )

    marker_svg = ""
    if marker is not None:
        sx, sy = screen(*marker)
        marker_svg = (
            f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="7" '
            f'fill="#e11d48" stroke="white" stroke-width="2" pointer-events="none" />'
        )

    return f"""
    <div style="overflow-x:auto"><svg viewBox="0 0 700 390" width="700" height="390"
         role="img" aria-label="{escape(y_label)} 변화 그래프">
      <style>
        .sample-tooltip {{ visibility: hidden; pointer-events: none; }}
        .sample:hover .sample-tooltip {{ visibility: visible; }}
      </style>
      <defs><clipPath id="plot-area"><rect x="{left}" y="{top}" width="600" height="298" /></clipPath></defs>
      {''.join(ticks)}
      <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#64748b" stroke-width="2" />
      <line x1="{left}" y1="{bottom}" x2="{left}" y2="{top}" stroke="#64748b" stroke-width="2" />
      <g clip-path="url(#plot-area)">
        {''.join(polyline(values, color, dashed) for values, color, dashed in overlays)}
        {polyline(points, '#2563eb')}
        {marker_svg}
      </g>
      {''.join(hover)}
      <text x="660" y="379" text-anchor="end" font-size="15">{escape(x_label)}</text>
      <text x="16" y="22" font-size="15">{escape(y_label)}</text>
    </svg></div>
    """
