"""초기 속력과 발사 각도를 바꾸며 포물선 운동을 관찰합니다."""

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    speed = mo.ui.slider(5, 40, value=20, step=1, label="초기 속력 (m/s)", show_value=True)
    angle = mo.ui.slider(5, 85, value=45, step=1, label="발사 각도 (°)", show_value=True)
    mo.vstack([speed, angle])
    return speed, angle


@app.cell
def _(angle, mo, speed):
    from projectile import trajectory

    points, flight_time, max_height, horizontal_range = trajectory(speed.value, angle.value)

    # 슬라이더의 전체 범위에서 동일한 축을 사용해야 궤적 변화를 비교할 수 있습니다.
    def to_screen(x, y):
        return 52 + x / 170 * 600, 330 - y / 85 * 300

    screen_points = [to_screen(x, y) for x, y in points]
    path = " ".join(f"{x:.1f},{y:.1f}" for x, y in screen_points)
    reference_points, _, _, _ = trajectory(20, 45)
    reference_path = " ".join(
        f"{x:.1f},{y:.1f}" for x, y in (to_screen(x, y) for x, y in reference_points)
    )

    ticks = []
    for value in (0, 50, 100, 150):
        x, _ = to_screen(value, 0)
        ticks.append(
            f'<line x1="{x:.1f}" y1="30" x2="{x:.1f}" y2="330" stroke="#e2e8f0" />'
            f'<text x="{x:.1f}" y="350" text-anchor="middle" font-size="12">{value}</text>'
        )
    for value in (0, 20, 40, 60, 80):
        _, y = to_screen(0, value)
        ticks.append(
            f'<line x1="52" y1="{y:.1f}" x2="652" y2="{y:.1f}" stroke="#e2e8f0" />'
            f'<text x="43" y="{y + 4:.1f}" text-anchor="end" font-size="12">{value}</text>'
        )

    hover_areas = []
    for (x1, y1), (x2, y2), (sx1, sy1), (sx2, sy2) in zip(
        points, points[1:], screen_points, screen_points[1:]
    ):
        x = (x1 + x2) / 2
        y = max(0, (y1 + y2) / 2)
        label = f"x={x:.2f} m, y={y:.2f} m"
        tooltip_x = min((sx1 + sx2) / 2 + 10, 510)
        tooltip_y = max((sy1 + sy2) / 2 - 38, 20)
        hover_areas.append(
            f'<g class="sample">'
            f'<line x1="{sx1:.1f}" y1="{sy1:.1f}" x2="{sx2:.1f}" y2="{sy2:.1f}" '
            f'stroke="transparent" stroke-width="18" pointer-events="stroke" cursor="crosshair">'
            f'<title>{label}</title></line>'
            f'<g class="sample-tooltip">'
            f'<rect x="{tooltip_x:.1f}" y="{tooltip_y:.1f}" width="180" height="28" '
            f'rx="5" fill="#0f172a" />'
            f'<text x="{tooltip_x + 8:.1f}" y="{tooltip_y + 19:.1f}" '
            f'fill="white" font-size="13">{label}</text>'
            f'</g></g>'
        )

    graph = f"""
    <svg viewBox="0 0 700 390" width="100%" role="img"
         aria-label="초기 속력 {speed.value}미터 매초, 발사 각도 {angle.value}도의 포물선 궤적">
      <style>
        .sample-tooltip {{ visibility: hidden; pointer-events: none; }}
        .sample:hover .sample-tooltip {{ visibility: visible; }}
      </style>
      {''.join(ticks)}
      <line x1="52" y1="330" x2="652" y2="330" stroke="#64748b" stroke-width="2" />
      <line x1="52" y1="330" x2="52" y2="30" stroke="#64748b" stroke-width="2" />
      <polyline points="{reference_path}" fill="none" stroke="#94a3b8"
                stroke-width="3" stroke-dasharray="6 5" />
      <polyline points="{path}" fill="none" stroke="#2563eb" stroke-width="4" />
      {''.join(hover_areas)}
      <line x1="320" y1="18" x2="344" y2="18" stroke="#94a3b8"
            stroke-width="3" stroke-dasharray="6 5" />
      <text x="350" y="22" font-size="12">기준: 20 m/s, 45°</text>
      <line x1="512" y1="18" x2="536" y2="18" stroke="#2563eb" stroke-width="4" />
      <text x="542" y="22" font-size="12">현재 설정</text>
      <text x="650" y="377" font-size="14" text-anchor="end">수평 거리 x (m)</text>
      <text x="16" y="25" font-size="14">높이 y (m)</text>
    </svg>
    """
    mo.vstack([
        mo.Html(graph),
        mo.md(
            f"**비행 시간:** {flight_time:.2f} s　"
            f"**최고 높이:** {max_height:.2f} m　"
            f"**도달 거리:** {horizontal_range:.2f} m"
        ),
    ])


if __name__ == "__main__":
    app.run()
