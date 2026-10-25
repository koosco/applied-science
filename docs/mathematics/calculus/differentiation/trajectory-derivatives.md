# 비행 궤적의 고계도함수

드론의 위치 하나만 보면 다음 순간의 움직임을 알기 어렵습니다. 위치의 시간 변화율은 속도, 속도의 변화율은 가속도, 가속도의 변화율은 **저크(jerk)**입니다. PX4의 [멀티콥터 제어 구조](https://docs.px4.io/main/en/flight_stack/controller_diagrams)는 위치·속도·가속도 목표값을 사용하며, [저크 제한 궤적](https://docs.px4.io/main/en/config_mc/mc_jerk_limited_type_trajectory)으로 급격한 가속도 변화를 제한합니다.

## 한 축에서 여러 번 미분하기

한 축의 위치 $s(t)$가 세 번 미분 가능하면

\[
v(t)=s'(t),\qquad a(t)=v'(t)=s''(t),\qquad
j(t)=a'(t)=s'''(t).
\]

$s,v,a,j$의 단위는 각각 m, m/s, m/s², m/s³입니다. $a=0$인 순간에도 $v$는 0이 아닐 수 있고, $j=0$은 가속도가 그 순간 변하지 않는다는 뜻이지 가속도가 0이라는 뜻은 아닙니다. 그래프의 극값 해석은 [도함수로 극값 찾기](extrema.md)에서 이어집니다.

3차원 위치 $\mathbf r(t)=(x(t),y(t),z(t))$는 각 성분을 미분합니다.

\[
\mathbf v(t)=\mathbf r'(t)=(x',y',z'),\qquad
\mathbf a(t)=\mathbf r''(t)=(x'',y'',z'').
\]

예를 들어 $\mathbf r(t)=(2t,\sin t,5)\,\mathrm m$라면 $\mathbf v(t)=(2,\cos t,0)\,\mathrm{m/s}$, $\mathbf a(t)=(0,-\sin t,0)\,\mathrm{m/s^2}$입니다. $t$는 초 단위 수치이며 사인 함수의 입력은 라디안입니다. 이 예에서는 고도가 일정해도 수평 방향의 가속도가 생깁니다. 일반적으로 속력만 일정해도 운동 방향이 바뀌면 가속도가 생길 수 있습니다. 실제 비행 데이터를 해석할 때는 축이 지면 기준인지 기체 기준인지도 구분해야 합니다.

## 정지 상태를 잇는 예시 궤적

한 축을 따라 거리 $D>0$만큼 $T>0$초에 이동하고 시작과 끝의 속도·가속도를 0으로 두겠습니다. $u=t/T$라 놓고 $s(t)=D(Au^3+Bu^4+Cu^5)$로 가정합니다. 처음 조건은 자동으로 만족하고, 끝 조건 $s(T)=D$, $s'(T)=s''(T)=0$을 적용하면

\[
A+B+C=1,\qquad 3A+4B+5C=0,\qquad 6A+12B+20C=0.
\]

이를 풀면 $A=10$, $B=-15$, $C=6$입니다. [연쇄법칙](basic-rules.md#chain-rule)으로 $du/dt=1/T$를 매번 곱하면

\[
\begin{aligned}
s(t)&=D(10u^3-15u^4+6u^5),\\
v(t)&=\frac DT(30u^2-60u^3+30u^4),\\
a(t)&=\frac D{T^2}(60u-180u^2+120u^3),\\
j(t)&=\frac D{T^3}(60-360u+360u^2),\qquad 0\le u\le1.
\end{aligned}
\]

중간 시각 $u=1/2$에는 $s=D/2$, $v=15D/(8T)$, $a=0$, $j=-30D/T^3$입니다. 이 모델에서 $|j|$의 최댓값은 양 끝의 $60D/T^3$이므로 같은 거리에서 시간을 줄이면 최대 저크가 세제곱에 반비례해 커집니다. 이는 **제한값을 자동으로 지키는 제어기**가 아니라 변화율을 살펴보기 위한 다항식 예시입니다. 정지 구간과 연결하면 끝점에서 저크가 불연속일 수 있으며, 실제 비행에는 추력·자세·속도 제한도 필요합니다.

<details>
<summary>궤적 시뮬레이션: 거리와 시간을 바꾸며 네 도함수 확인하기</summary>

거리와 이동 시간을 바꾸면 위치·속도·가속도·저크 곡선과 계산값이 함께 바뀝니다. 관찰 시각 슬라이더는 네 그래프에서 같은 시점을 가리킵니다. 각 축의 범위와 단위는 고정되어 있으며, 곡선에 마우스를 올리면 시간과 해당 값을 볼 수 있습니다.

<iframe src="../../../../simulations/trajectory-derivatives/index.html?v=calculus-1" title="비행 궤적의 도함수 시뮬레이터" width="100%" height="2100" loading="lazy" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>

<p><a href="../../../../simulations/trajectory-derivatives/index.html?v=calculus-1" target="_blank" rel="noopener">시뮬레이터 새 창에서 열기</a> · <a href="https://github.com/koosco/applied-science/blob/main/simulations/trajectory_derivatives.py">Python 원본 코드</a></p>
</details>

## 문제 예시: 제한된 시간 안의 이동 계획

위 모델로 드론의 한 축을 $D=12\,\mathrm m$ 이동시키며 $T=5\,\mathrm s$를 사용한다고 가정합니다. 중간 시각의 위치·속도·가속도·저크를 계산하고, 전체 구간의 최대 저크 크기가 $6\,\mathrm{m/s^3}$라는 가상의 계획 한계를 지키는지 판단해 보세요. 같은 거리를 이동하면서 이 한계를 지키려면 $T$를 최소 얼마로 잡아야 할까요?

**풀이.** $t=2.5\,\mathrm s$에서는 $u=1/2$이므로 $s=6\,\mathrm m$, $v=15(12)/(8\cdot5)=4.5\,\mathrm{m/s}$, $a=0$, $j=-30(12)/5^3=-2.88\,\mathrm{m/s^3}$입니다. 위에서 유도한 최대 저크 크기는 양 끝점에서 $60D/T^3$이므로 $T=5$일 때 $60(12)/5^3=5.76\,\mathrm{m/s^3}$로 한계 안입니다. 일반적인 $T$에는

\[
\frac{60(12)}{T^3}\le6
\quad\Longleftrightarrow\quad
T\ge\sqrt[3]{120}\approx4.93\,\mathrm s.
\]

따라서 $5\,\mathrm s$ 계획은 허용되지만 더 짧은 시간을 택할 때는 저크 한계를 다시 확인해야 합니다. 중간에 $a=0$이라고 해서 드론이 멈춘 것은 아닙니다. 실제 운용 한계는 기체와 제어 설정에 따라 따로 정해야 합니다.
