"""거리와 시간을 바꾸며 위치·속도·가속도·저크를 비교합니다."""

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
    distance = mo.ui.slider(5, 20, value=12, step=1, label="이동 거리 D (m)", show_value=True)
    duration = mo.ui.slider(3, 8, value=5, step=0.5, label="이동 시간 T (s)", show_value=True)
    progress = mo.ui.slider(0, 1, value=0.5, step=0.05, label="관찰 시점 t/T", show_value=True)
    mo.vstack([distance, duration, progress, reset])
    return distance, duration, progress


@app.cell
def _(distance, duration, mo, progress):
    from calculus_plot import chart
    from trajectory_model import state

    d, total_time = distance.value, duration.value
    observed_time = progress.value * total_time
    observed = state(d, total_time, observed_time)
    samples = [(total_time * i / 120, state(d, total_time, total_time * i / 120)) for i in range(121)]
    series = (
        ("위치 s", "m", (0, 20), (0, 5, 10, 15, 20)),
        ("속도 v", "m/s", (0, 14), (0, 3, 6, 9, 12)),
        ("가속도 a", "m/s²", (-14, 14), (-12, -6, 0, 6, 12)),
        ("저크 j", "m/s³", (-50, 50), (-40, -20, 0, 20, 40)),
    )
    graphs = []
    for index, (name, unit, y_range, y_ticks) in enumerate(series):
        graph = chart(
            [(t, values[index]) for t, values in samples],
            x_range=(0, 8),
            y_range=y_range,
            x_ticks=(0, 2, 4, 6, 8),
            y_ticks=y_ticks,
            x_label="시간 t (s)",
            y_label=f"{name} ({unit})",
            tooltip=lambda t, value, unit=unit: f"t={t:.2f} s, y={value:.2f} {unit}",
            marker=(observed_time, observed[index]),
        )
        graphs.extend((mo.md(f"**{name}**"), mo.Html(graph)))

    mo.vstack([
        mo.md(
            f"**관찰 시각:** {observed_time:.2f} s　"
            f"**위치:** {observed[0]:.2f} m　**속도:** {observed[1]:.2f} m/s　"
            f"**가속도:** {observed[2]:.2f} m/s²　**저크:** {observed[3]:.2f} m/s³"
        ),
        mo.md(f"**최대 저크 크기:** {60 * d / total_time**3:.2f} m/s³ (이 가상 궤적)"),
        *graphs,
    ])


if __name__ == "__main__":
    app.run()
