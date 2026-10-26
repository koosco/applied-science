# 직교좌표와 극좌표 사이의 변환

> 벡터와 좌표계 4/7 · 약 30~40분 · 선수 지식: [극좌표계](polar-coordinates.md)

## 두 표현 사이를 왕복하기

극좌표 $(r,\theta)$에서 직교좌표 $(x,y)$로 바꾸는 공식은 직각삼각형의 삼각함수 정의에서 나옵니다.

\[
\boxed{x=r\cos\theta,\qquad y=r\sin\theta.}
\]

반대 방향에서는 피타고라스 정리로 $r$을, **사분면을 고려하는** 함수로 $\theta$를 구합니다.

\[
\boxed{r=\sqrt{x^2+y^2},\qquad \theta=\operatorname{atan2}(y,x).}
\]

여기서 $\operatorname{atan2}(y,x)$는 보통 $(-\pi,\pi]$ 또는 $[-\pi,\pi)$와 같은 구간의 각도를 반환하며, 언어별 구간의 끝점 규약은 조금 다를 수 있습니다. 원하는 범위가 $[0,2\pi)$이면 음수 각도에 $2\pi$를 더하면 됩니다. **첫 번째 인수는 $y$, 두 번째 인수는 $x$**라는 순서에 주의합니다.

## 그래프로 이해하기

![좌표 (3,4)를 반지름 5와 53.13도 각도로 나타낸 직교·극좌표 변환 그림](../../assets/figures/mathematics/coordinate-systems/cartesian-polar-345.svg)

*성분을 합치면 길이·각도가 되고, 길이와 각도를 분해하면 다시 $x,y$가 됩니다. 그림의 원점은 좌표계의 기준점입니다.*

## 문제 예시: 목표점의 직교·극좌표 변환

평면 지도에서 목표점 $P=(3,4)$ m입니다. 극좌표로 바꾼 뒤 다시 직교좌표로 복원해 보세요.

**풀이.** 거리는 $r=\sqrt{3^2+4^2}=5$ m입니다. 두 성분이 양수이므로 1사분면이고 $\theta=\operatorname{atan2}(4,3)\approx53.13^\circ$입니다.

\[
5\cos\theta=3,\qquad 5\sin\theta=4
\]

이므로 원래 좌표 $(3,4)$ m로 복원됩니다. 실제 수치 계산에서는 $\theta$를 소수 둘째 자리까지 반올림하면 아주 작은 오차가 생길 수 있습니다.

## 문제 예시: 극좌표에서 위치 계산

거리 10m, 방향각 $150^\circ$인 점의 직교좌표를 구해 보세요.

**풀이.** 각도는 2사분면이므로

\[
x=10\cos150^\circ=-5\sqrt3\,\mathrm m,\qquad
y=10\sin150^\circ=5\,\mathrm m.
\]

$x$가 음수이고 $y$가 양수라는 조건으로 부호를 검산합니다.

## Python에서 각도 다루기

아래는 표준 라이브러리를 사용한 예시입니다. Python의 삼각함수·atan2는 **라디안**을 반환하거나 받습니다.

~~~python
import math

x, y = 3.0, 4.0
r = math.hypot(x, y)
theta = math.atan2(y, x)

print(r)                    # 5.0
print(math.degrees(theta))  # 약 53.1301 도
print(r * math.cos(theta), r * math.sin(theta))  # (3.0, 4.0)에 근접
~~~

## 확인 문제

$P=(-\sqrt2,\sqrt2)$ m를 $0^\circ\le\theta<360^\circ$의 극좌표로 나타내세요.

## 확인 문제 풀이

$r=2$ m이고 2사분면이므로 $\theta=135^\circ=3\pi/4$ rad입니다.

**다음:** [극좌표에서의 운동](polar-motion.md) · [이전](polar-coordinates.md)
