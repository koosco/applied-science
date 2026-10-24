"""높이 그래프의 접선과 순간속도를 확인합니다."""

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
    time = mo.ui.slider(0, 6, value=5, step=0.1, label="시각 t (s)", show_value=True)
    mo.vstack([time, reset])
    return (time,)


@app.cell
def _(mo, time):
    from calculus_plot import chart

    def height(t):
        return 30 * t - 4.9 * t**2

    t = time.value
    speed = 30 - 9.8 * t
    tangent = [(x, height(t) + speed * (x - t)) for x in (max(0, t - 1), min(6.1, t + 1))]
    points = [(6.1 * i / 122, height(6.1 * i / 122)) for i in range(123)]
    graph = chart(
        points,
        x_range=(0, 6.1),
        y_range=(0, 48),
        x_ticks=(0, 1, 2, 3, 4, 5, 6),
        y_ticks=(0, 10, 20, 30, 40),
        x_label="시간 t (s)",
        y_label="높이 s (m)",
        tooltip=lambda x, y: f"t={x:.2f} s, s={y:.2f} m",
        overlays=((tangent, "#d97706", True),),
        marker=(t, height(t)),
    )
    mo.vstack([mo.Html(graph), mo.md(f"**높이:** {height(t):.2f} m　**순간속도:** {speed:.2f} m/s")])


if __name__ == "__main__":
    app.run()
