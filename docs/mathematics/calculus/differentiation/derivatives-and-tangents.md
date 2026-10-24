# 미분계수와 도함수

시간 $t$에 따른 위치 $s(t)$의 평균속도는 $[s(t+\Delta t)-s(t)]/\Delta t$입니다. [함수의 극한](../functions/limits-and-continuity.md)으로 $\Delta t\to0$을 다룰 수 있으면 **순간속도**인 도함수

\[
s'(t)=\lim_{\Delta t\to0}\frac{s(t+\Delta t)-s(t)}{\Delta t}
\]

가 됩니다. 도함수가 존재하면 그 점에서 함수는 연속이지만, 연속이라고 항상 미분 가능한 것은 아닙니다. 예를 들어 $|t|$는 0에서 연속이지만 좌우 기울기가 달라 미분 불가능합니다.

**공을 위로 던진 예.** 위쪽을 양의 방향으로 잡고, 공기 저항 없이 중력가속도를 $9.8\,\mathrm{m/s^2}$로 일정하게 두면 $s(t)=30t-4.9t^2$입니다. 원래 기록의 `30ㅅ`은 $30t$로 해석합니다. 단위는 $s$가 m, $t$가 s입니다.

\[
\begin{aligned}
\frac{s(t+\Delta t)-s(t)}{\Delta t}
&=30-9.8t-4.9\Delta t,\\
s'(t)&=30-9.8t.
\end{aligned}
\]

$t=5\,\mathrm s$에서 높이는 $s(5)=27.5\,\mathrm m$, 순간속도는 $s'(5)=-19\,\mathrm{m/s}$입니다. 음수는 공이 **아래로 내려가는 중**임을 뜻합니다. 이 단순 모델에서 출발 높이로 돌아오는 때는 약 $6.12\,\mathrm s$입니다.

<details>
<summary>순간속도 시뮬레이션: 시각을 바꾸며 접선 확인하기</summary>

시각을 바꾸면 위치 곡선의 점, 접선, 순간속도가 함께 바뀝니다. 축은 고정되어 있으며 툴팁은 시간과 높이를 보여줍니다.

<iframe src="../../../../simulations/instantaneous-velocity/index.html?v=calculus-1" title="순간속도 시뮬레이터" width="100%" height="640" loading="lazy" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>

<p><a href="../../../../simulations/instantaneous-velocity/index.html?v=calculus-1" target="_blank" rel="noopener">시뮬레이터 새 창에서 열기</a> · <a href="https://github.com/koosco/applied-science/blob/main/simulations/instantaneous_velocity.py">Python 원본 코드</a></p>
</details>

## 접선과 법선의 방정식

평면에서 $y=f(x)$의 $(a,f(a))$에서 접선 기울기가 $m=f'(a)$이면 접선은 $y-f(a)=m(x-a)$입니다. 이에 수직인 **법선**은 $m\ne0$일 때 $y-f(a)=-\frac1m(x-a)$입니다. $m=0$이면 법선은 수직선 $x=a$입니다. 접선 방향 벡터 $(1,m)$과 법선 방향 벡터 $(-m,1)$의 내적은 $-m+m=0$이므로 두 방향이 수직입니다.

예를 들어 경사진 지면을 국소적으로 $y=0.2x$로 나타내면 접선 방향은 $(1,0.2)$, 위쪽을 향한 법선 방향은 $(-0.2,1)$입니다. 이를 길이 1로 만들려면 $\sqrt{1+0.2^2}$로 나눕니다. 법선은 지면의 방향이나 접촉력의 방향을 기술하는 데 도움이 됩니다. 실제 착륙 제어에는 지형 측정, 기체 자세, 속도와 오차도 함께 고려해야 합니다. 여기서 지면의 $x,y$는 거리 좌표이며 위의 높이 대 시간 그래프와 서로 다른 평면입니다.
