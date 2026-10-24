"""원형 경로에서 좌표 변화에 따른 접선 기울기를 확인합니다."""

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    reset = mo.ui.button(label="초기화")
    return (reset,)


@app.cell
def _(mo, reset):
    reset.value
    x_position = mo.ui.slider(-2.4, 2.4, value=1.5, step=0.1, label="수평 위치 x (m)", show_value=True)
    mo.vstack([x_position, reset])
    return (x_position,)


@app.cell
def _(mo, x_position):
    from math import sqrt
    from calculus_plot import chart

    x = x_position.value
    y = sqrt(6.25 - x**2)
    slope = -x / y
    xs = [-2.5 + 5 * i / 160 for i in range(161)]
    upper = [(value, sqrt(max(0, 6.25 - value**2))) for value in xs]
    lower = [(value, -sqrt(max(0, 6.25 - value**2))) for value in xs]
    tangent = [(value, y + slope * (value - x)) for value in (x - 0.8, x + 0.8)]
    graph = chart(
        upper,
        x_range=(-2.8, 2.8),
        y_range=(-2.8, 2.8),
        x_ticks=(-2, -1, 0, 1, 2),
        y_ticks=(-2, -1, 0, 1, 2),
        x_label="수평 위치 x (m)",
        y_label="수직 위치 y (m)",
        tooltip=lambda x, y: f"x={x:.2f} m, y={y:.2f} m",
        overlays=((lower, "#94a3b8", True), (tangent, "#d97706", True)),
        marker=(x, y),
    )
    mo.vstack([
        mo.Html(graph),
        mo.md(f"**현재 위치:** ({x:.2f}, {y:.2f}) m　**dy/dx:** {slope:.3f}"),
        mo.md("파란 선은 위쪽 반원, 회색 점선은 아래쪽 반원, 주황 점선은 현재 위치의 접선입니다."),
    ])


if __name__ == "__main__":
    app.run()
