# 극좌표계: 거리와 방향으로 위치 표현하기

> 벡터와 좌표계 3/7 · 약 25~35분 · 선수 지식: [직교좌표계](cartesian-plane.md), 삼각함수

## 극좌표의 두 숫자

극좌표계(Polar coordinates)는 원점에서의 **거리** $r$와 기준 방향에서 잰 **각도** $\theta$로 점을 나타냅니다.

\[
(r,\theta),\qquad r\ge0.
\]

이 단원에서는 각도를 **양의 $x$축에서 반시계 방향**으로 측정합니다. 동쪽으로 3m, 북쪽으로 4m인 점의 표현은

\[
(x,y)=(3,4)\,\mathrm m,\qquad
(r,\theta)=(5\,\mathrm m,\ 53.13^\circ)
\]

입니다.

## 그림으로 이해하기

![극좌표의 반지름 5m와 양의 x축에서 반시계 방향으로 잰 53.13도 각도가 직교좌표 (3,4)와 같은 위치를 가리키는 그래프](../../assets/figures/mathematics/coordinate-systems/cartesian-polar-345.svg)

*동일한 물리적 위치라도 사용하는 좌표 변수가 달라질 수 있습니다.*

## 각도의 단위와 사분면

$180^\circ=\pi$ rad입니다. 미분·회전속도 계산에는 라디안을 사용합니다. $\theta$에 $360^\circ$를 더하거나 빼도 같은 방향입니다. $r=0$에서는 방향각이 정의되지 않습니다.

각도 계산에서 $\tan\theta=y/x$만 사용하면 사분면 정보가 부족합니다. 두 성분의 부호를 함께 고려하는 **atan2(y,x)**를 사용합니다.

## 문제 예시: 2사분면의 목표 위치

점 $Q=(-3,3\sqrt3)$ m를 극좌표로 바꿔 보세요. 각도는 $0^\circ\le\theta<360^\circ$로 씁니다.

**풀이.** 거리는

\[
r=\sqrt{(-3)^2+(3\sqrt3)^2}=6\,\mathrm m.
\]

$x<0,y>0$이므로 2사분면이고,

\[
\cos\theta=-\frac12,\quad\sin\theta=\frac{\sqrt3}{2}
\quad\Rightarrow\quad\theta=120^\circ=\frac{2\pi}{3}.
\]

$\arctan(y/x)$만 계산하면 사분면을 잘못 판단할 수 있습니다.

## 확인 문제

$P=(0,-4)$ m의 극좌표 $(r,\theta)$를 $0^\circ\le\theta<360^\circ$로 나타내 보세요.

## 확인 문제 풀이

$r=4$ m이며 아래 방향이므로 $\theta=270^\circ=3\pi/2$ rad입니다. 같은 방향을 $-90^\circ$라고 표현할 수도 있습니다.

**다음:** [직교·극좌표 변환](coordinate-conversion.md) · [이전](cartesian-plane.md)
