# 역함수의 미분법

[역함수](../functions/inverse-functions.md) $f^{-1}(y)$는 출력 $y$를 만드는 **입력 자체**를 구합니다. 역함수의 도함수 $(f^{-1})'(y)$는 그 출력이 조금 변할 때 필요한 **입력 변화의 민감도**를 구합니다. 입력 $x$에서 $y=f(x)$이고 $f$가 그 근방에서 일대일이며 $f'(x)\ne0$이면

\[
f(f^{-1}(y))=y
\quad\Longrightarrow\quad
f'(f^{-1}(y))(f^{-1})'(y)=1
\quad\Longrightarrow\quad
(f^{-1})'(y)=\frac1{f'(x)}.
\]

가운데 식은 합성함수의 미분인 연쇄법칙입니다. $f'(x)=0$이면 이 공식으로 유한한 역함수 변화율을 구할 수 없습니다. 역함수의 미분은 국소적인 관계이고, 큰 변화에는 역함수를 직접 계산해야 합니다.

## 회전 속도와 추력

모터·프로펠러가 일정 조건에서 내는 추력을 단순히 $T=k\omega^2$로 모델링합니다. $T$는 추력(N), $\omega>0$는 각속도(rad/s), $k>0$는 이 장치와 조건에 맞춰 정할 계수입니다. 역함수와 그 도함수는

\[
\omega(T)=\sqrt{\frac{T}{k}},\qquad
\frac{d\omega}{dT}=\frac1{2k\omega}=\frac1{2\sqrt{kT}}.
\]

단위는 $k$가 $\mathrm{N\,s^2/rad^2}$, $d\omega/dT$가 $\mathrm{rad/(s\,N)}$입니다. 예시 계수 $k=10^{-5}\,\mathrm{N\,s^2/rad^2}$에서 $T=2.5\,\mathrm N$을 내려면 $\omega=500\,\mathrm{rad/s}$입니다. 목표를 $2.6\,\mathrm N$으로 올릴 때 미분으로 얻은 **근사 변화량**은 $\Delta\omega\approx(d\omega/dT)\Delta T=100\times0.1=10\,\mathrm{rad/s}$입니다. 실제 모델의 역함수로 계산한 입력은 $\sqrt{2.6/10^{-5}}\approx509.90\,\mathrm{rad/s}$, 곧 약 $9.90\,\mathrm{rad/s}$ 증가입니다. 모델 밖의 실제 추력은 회전 속도만으로 결정되지 않으며 공기 밀도·프로펠러·유동에 영향을 받습니다.

<details>
<summary>역함수 미분 시뮬레이션: 목표 추력에 필요한 입력 비교하기</summary>

목표 추력을 바꾸며 각속도의 역함수값과 미분 근사값을 비교해 보세요. 파란 곡선은 추력이 각속도 제곱에 비례하는 이상화 모델입니다.

<iframe src="../../../../simulations/inverse-thrust/index.html?v=calculus-1" title="역함수 미분 시뮬레이터" width="100%" height="640" loading="lazy" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>

<p><a href="../../../../simulations/inverse-thrust/index.html?v=calculus-1" target="_blank" rel="noopener">시뮬레이터 새 창에서 열기</a> · <a href="https://github.com/koosco/applied-science/blob/main/simulations/inverse_thrust.py">Python 원본 코드</a></p>
</details>

## 기압으로 고도 추정

온도와 중력가속도 등이 일정한 이상화 조건에서는 기준 기압 $p_0>0$, 척도높이 $H>0$로 $p(h)=p_0e^{-h/H}$라 놓을 수 있습니다. 역함수로 고도를 구하고 이를 미분하면

\[
h(p)=-H\ln\frac{p}{p_0},\qquad
\frac{dh}{dp}=-\frac Hp.
\]

따라서 기압 변화 $\Delta p$가 작을 때 고도 변화는 $\Delta h\approx-H\Delta p/p$입니다. 기압이 낮아지면 추정 고도는 올라갑니다. 이 모델의 $H$와 $p_0$는 환경에 맞게 정해야 하며 날씨와 온도 변화, 센서 오차는 고도 추정 오차로 이어집니다.

## 역삼각함수의 변화율

$y=\arcsin x$에서 $x=\sin y$를 미분하면 $1=\cos y\,dy/dx$입니다. $y\in(-\pi/2,\pi/2)$에서는 $\cos y=\sqrt{1-x^2}>0$이므로

\[
\frac{d}{dx}\arcsin x=\frac1{\sqrt{1-x^2}}\quad(-1<x<1).
\]

같은 방법으로 $y=\arccos x$에서는 $1=-\sin y\,dy/dx$, $\sin y=\sqrt{1-x^2}$이고, $y=\arctan x$에서는 $1=(1+\tan^2y)dy/dx$입니다. 따라서 $(\arccos x)'=-1/\sqrt{1-x^2}$ ($-1<x<1$), $(\arctan x)'=1/(1+x^2)$ ($x\in\mathbb R$)입니다. 사인·코사인의 끝점 부근에서 분모가 0에 가까워지는 것은 **비율의 작은 오차가 큰 각도 오차로 이어질 수 있음**을 보여줍니다.
