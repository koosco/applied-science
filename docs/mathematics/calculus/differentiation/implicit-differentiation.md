# 음함수의 미분법

좌표 사이 관계가 $y=f(x)$로 풀려 있지 않아도 $F(x,y)=0$으로 주어질 수 있습니다. $F_x$와 $F_y$는 다른 변수를 고정한 채 각각 $x$와 $y$에 대해 미분한 편도함수입니다. 이 식을 따라 $y$가 $x$의 함수처럼 변한다고 보고 양변을 $x$로 미분하면 $F_x+F_y\,dy/dx=0$입니다. 따라서 $F_y\ne0$인 점에서

\[
\frac{dy}{dx}=-\frac{F_x}{F_y}.
\]

이 식은 해당 점의 **국소적인 기울기**입니다. $F_y=0$에서는 $y$를 $x$의 함수로 나타내기 어려울 수 있으며, 기울기 공식을 그대로 쓰지 않습니다.

**원형 비행 경로.** 지름이 $5\,\mathrm m$인 원은 반지름이 $2.5\,\mathrm m$이므로 $x^2+y^2=6.25\,\mathrm{m^2}$입니다. $x^2+y^2=25$라면 **반지름 5 m, 지름 10 m**인 원입니다. 미분하면 $2x+2y\,dy/dx=0$, 즉 $dy/dx=-x/y$입니다. 원 위의 점 $(1.5,2.0)\,\mathrm m$에서 기울기는 $-0.75$이므로, 이 점 근처에서 $x$가 $0.1\,\mathrm m$ 늘면 $y$는 약 $0.075\,\mathrm m$ 줄어듭니다. 실제 원 위의 유한한 이동은 $y=\sqrt{6.25-x^2}$로 다시 계산해야 하며, $(\pm2.5,0)$에서는 수직 접선입니다.

<details>
<summary>음함수 미분 시뮬레이션: 원 위의 위치와 접선 비교하기</summary>

위쪽 반원에서 수평 위치를 바꾸며 접선 기울기를 확인해 보세요. 양 끝에 가까워질수록 기울기의 절댓값이 커집니다.

<iframe src="../../../../simulations/implicit-circle/index.html?v=calculus-1" title="음함수 미분 시뮬레이터" width="100%" height="640" loading="lazy" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>

<p><a href="../../../../simulations/implicit-circle/index.html?v=calculus-1" target="_blank" rel="noopener">시뮬레이터 새 창에서 열기</a> · <a href="https://github.com/koosco/applied-science/blob/main/simulations/implicit_circle.py">Python 원본 코드</a></p>
</details>

**두 변수의 비선형 관계.** $x^3+y^3=2xy$를 미분하면

\[
3x^2+3y^2\frac{dy}{dx}=2y+2x\frac{dy}{dx},
\qquad
\frac{dy}{dx}=\frac{2y-3x^2}{3y^2-2x}.
\]

$(1,1)$은 원래 식을 만족하고 분모가 1이므로 그 점의 기울기는 $-1$입니다. 이 식은 변수 관계를 연습하기 위한 수학적 예이며 특정 비행 물리 법칙을 뜻하지 않습니다.

## 문제 예시: 드론의 타원형 수평 경로

드론의 수평 비행 경로를 $x^2/16+y^2/9=1$로 계획했다고 가정합니다. $x,y$는 좌표를 미터 단위로 나타낸 수치입니다. 위쪽 경로의 점 $(2,3\sqrt3/2)\,\mathrm m$에서 접선 기울기를 구하고, 그 근처에서 $x$가 $0.2\,\mathrm m$ 증가할 때 필요한 $y$의 변화량을 근사해 보세요.

**풀이.** 점을 대입하면 $2^2/16+(3\sqrt3/2)^2/9=1/4+3/4=1$이므로 경로 위에 있습니다. 관계식을 $x$로 미분하면

\[
\frac{x}{8}+\frac{2y}{9}\frac{dy}{dx}=0,
\qquad
\frac{dy}{dx}=-\frac{9x}{16y}.
\]

따라서 해당 점의 기울기는 $-9\cdot2/[16(3\sqrt3/2)]=-\sqrt3/4\approx-0.433$입니다. 국소 근사로 $\Delta y\approx(dy/dx)\Delta x=-\sqrt3/20\approx-0.0866\,\mathrm m$를 얻습니다. 이는 타원 경로의 **접선 방향**을 이용한 작은 이동 근사이며, 실제 제어에는 경로 추종 오차와 기체 동역학도 고려해야 합니다.
