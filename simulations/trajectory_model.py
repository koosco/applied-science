"""한 축에서 정지 상태를 잇는 5차 다항식 궤적의 변화율."""


def state(distance: float, duration: float, time: float) -> tuple[float, float, float, float]:
    if duration <= 0 or not 0 <= time <= duration:
        raise ValueError("duration은 양수이고 time은 [0, duration] 안에 있어야 합니다")

    u = time / duration
    position = distance * (10 * u**3 - 15 * u**4 + 6 * u**5)
    velocity = distance / duration * (30 * u**2 - 60 * u**3 + 30 * u**4)
    acceleration = distance / duration**2 * (60 * u - 180 * u**2 + 120 * u**3)
    jerk = distance / duration**3 * (60 - 360 * u + 360 * u**2)
    return position, velocity, acceleration, jerk
