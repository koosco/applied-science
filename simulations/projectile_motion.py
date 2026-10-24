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
    path = " ".join(
        f"{40 + x / horizontal_range * 620:.1f},{320 - y / max_height * 280:.1f}"
        for x, y in points
    )
    graph = f"""
    <svg viewBox="0 0 700 365" width="100%" role="img"
         aria-label="초기 속력 {speed.value}미터 매초, 발사 각도 {angle.value}도의 포물선 궤적">
      <line x1="40" y1="320" x2="660" y2="320" stroke="#64748b" stroke-width="2" />
      <line x1="40" y1="320" x2="40" y2="40" stroke="#64748b" stroke-width="2" />
      <polyline points="{path}" fill="none" stroke="#2563eb" stroke-width="4" />
      <text x="650" y="350" font-size="15" text-anchor="end">수평 거리 (m)</text>
      <text x="48" y="34" font-size="15">높이 (m)</text>
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
