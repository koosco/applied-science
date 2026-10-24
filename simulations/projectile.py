"""공기 저항이 없는 포물선 운동의 위치를 계산합니다."""

from math import cos, radians, sin


def trajectory(speed: float, angle_degrees: float, gravity: float = 9.81, samples: int = 80):
    """궤적 좌표, 비행 시간, 최고 높이, 수평 도달 거리를 반환합니다."""
    if speed <= 0 or gravity <= 0 or samples < 2 or not 0 < angle_degrees < 90:
        raise ValueError("속력·중력가속도는 양수, 각도는 0~90도 사이여야 합니다.")

    angle = radians(angle_degrees)
    horizontal_speed = speed * cos(angle)
    vertical_speed = speed * sin(angle)
    flight_time = 2 * vertical_speed / gravity
    max_height = vertical_speed**2 / (2 * gravity)
    horizontal_range = horizontal_speed * flight_time
    points = [
        (horizontal_speed * t, vertical_speed * t - gravity * t**2 / 2)
        for t in (flight_time * i / samples for i in range(samples + 1))
    ]
    return points, flight_time, max_height, horizontal_range
