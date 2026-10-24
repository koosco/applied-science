"""사인 비율에서 제한된 정의역의 각도를 찾습니다."""

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
    ratio = mo.ui.slider(-1, 1, value=0.5, step=0.05, label="사인 비율", show_value=True)
    mo.vstack([ratio, reset])
    return (ratio,)


@app.cell
def _(mo, ratio):
    from math import asin, degrees, pi, sin
    from calculus_plot import chart

    points = [(-pi / 2 + pi * i / 160, sin(-pi / 2 + pi * i / 160)) for i in range(161)]
    angle = asin(ratio.value)
    graph = chart(
        points,
        x_range=(-pi / 2, pi / 2),
        y_range=(-1.1, 1.1),
        x_ticks=(-pi / 2, -pi / 4, 0, pi / 4, pi / 2),
        y_ticks=(-1, -0.5, 0, 0.5, 1),
        x_label="각도 θ (rad)",
        y_label="sin θ",
        tooltip=lambda x, y: f"θ={x:.2f} rad, sin θ={y:.2f}",
        overlays=(([(-pi / 2, ratio.value), (pi / 2, ratio.value)], "#d97706", True),),
        marker=(angle, ratio.value),
    )
    mo.vstack([mo.Html(graph), mo.md(f"**arcsin({ratio.value:.2f}) = {angle:.3f} rad = {degrees(angle):.1f}°**")])


if __name__ == "__main__":
    app.run()
