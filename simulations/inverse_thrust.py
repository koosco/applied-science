"""목표 추력에 필요한 각속도와 국소 입력 민감도를 살펴봅니다."""

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
    thrust = mo.ui.slider(0.5, 5, value=2.5, step=0.1, label="목표 추력 T (N)", show_value=True)
    mo.vstack([thrust, reset])
    return (thrust,)


@app.cell
def _(mo, thrust):
    from math import sqrt
    from calculus_plot import chart

    k = 1e-5
    omega = sqrt(thrust.value / k)
    sensitivity = 1 / (2 * k * omega)
    points = [(750 * i / 150, k * (750 * i / 150) ** 2) for i in range(151)]
    graph = chart(
        points,
        x_range=(0, 750),
        y_range=(0, 5.7),
        x_ticks=(0, 150, 300, 450, 600, 750),
        y_ticks=(0, 1, 2, 3, 4, 5),
        x_label="각속도 ω (rad/s)",
        y_label="추력 T (N)",
        tooltip=lambda x, y: f"ω={x:.1f} rad/s, T={y:.2f} N",
        overlays=(([(0, thrust.value), (750, thrust.value)], "#d97706", True),),
        marker=(omega, thrust.value),
    )
    exact_change = sqrt((thrust.value + 0.1) / k) - omega
    mo.vstack([
        mo.Html(graph),
        mo.md(
            f"**필요 각속도:** {omega:.2f} rad/s　"
            f"**dω/dT:** {sensitivity:.2f} rad/(s·N)　"
            f"**추력 +0.1 N:** 미분 근사 +{0.1 * sensitivity:.2f}, "
            f"역함수 계산 +{exact_change:.2f} rad/s"
        ),
    ])


if __name__ == "__main__":
    app.run()
