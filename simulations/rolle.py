"""같은 높이를 지나는 두 시각 사이의 수직 속도 0인 지점을 보여줍니다."""

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
    speed = mo.ui.slider(20, 40, value=30, step=1, label="초기 수직 속도 (m/s)", show_value=True)
    mo.vstack([speed, reset])
    return (speed,)


@app.cell
def _(mo, speed):
    from calculus_plot import chart

    gravity = 9.8

    def trajectory(initial_speed):
        end = 2 * initial_speed / gravity
        points = []
        for i in range(121):
            t = end * i / 120
            points.append((t, initial_speed * t - gravity * t**2 / 2))
        return points

    stationary_time = speed.value / gravity
    max_height = speed.value**2 / (2 * gravity)
    return_time = 2 * stationary_time
    graph = chart(
        trajectory(speed.value),
        x_range=(0, 9),
        y_range=(0, 85),
        x_ticks=(0, 2, 4, 6, 8),
        y_ticks=(0, 20, 40, 60, 80),
        x_label="시간 t (s)",
        y_label="높이 s (m)",
        tooltip=lambda t, height: f"t={t:.2f} s, s={height:.2f} m",
        overlays=((trajectory(30), "#94a3b8", True),),
        marker=(stationary_time, max_height),
    )
    mo.vstack([
        mo.Html(graph),
        mo.md(
            f"**같은 높이인 시각:** 0 s, {return_time:.2f} s　"
            f"**수직 속도 0인 시각:** {stationary_time:.2f} s　"
            f"**그때 높이:** {max_height:.2f} m"
        ),
        mo.md("회색 점선은 초기 수직 속도 30 m/s의 기준 궤적입니다."),
    ])


if __name__ == "__main__":
    app.run()
