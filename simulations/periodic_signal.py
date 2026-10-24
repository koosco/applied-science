"""정현파의 진폭, 주파수, 위상에 따른 변화를 관찰합니다."""

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
    amplitude = mo.ui.slider(0.5, 2, value=1, step=0.25, label="진폭 A (임의 단위)", show_value=True)
    frequency = mo.ui.slider(0.5, 3, value=1, step=0.25, label="주파수 f (Hz)", show_value=True)
    phase = mo.ui.slider(-180, 180, value=0, step=15, label="위상 φ (°)", show_value=True)
    mo.vstack([amplitude, frequency, phase, reset])
    return amplitude, frequency, phase


@app.cell
def _(amplitude, frequency, mo, phase):
    from math import pi, radians, sin
    from calculus_plot import chart

    def signal(t):
        return amplitude.value * sin(2 * pi * frequency.value * t + radians(phase.value))

    times = [4 * i / 240 for i in range(241)]
    graph = chart(
        [(t, signal(t)) for t in times],
        x_range=(0, 4),
        y_range=(-2.2, 2.2),
        x_ticks=(0, 1, 2, 3, 4),
        y_ticks=(-2, -1, 0, 1, 2),
        x_label="시간 t (s)",
        y_label="신호 x (임의 단위)",
        tooltip=lambda x, y: f"t={x:.2f} s, x={y:.2f}",
        overlays=(([(t, sin(2 * pi * t)) for t in times], "#94a3b8", True),),
    )
    mo.vstack([
        mo.Html(graph),
        mo.md(
            f"**진폭:** {amplitude.value:.2f}　**주기:** {1/frequency.value:.2f} s　"
            f"**위상:** {phase.value}°　**초기 신호값:** {signal(0):.2f}"
        ),
        mo.md("회색 점선은 A=1, f=1 Hz, φ=0°의 기준 신호입니다."),
    ])


if __name__ == "__main__":
    app.run()
