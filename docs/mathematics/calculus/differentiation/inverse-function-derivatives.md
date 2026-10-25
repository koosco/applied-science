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

<a id="inverse-trig-derivatives"></a>
## 역삼각함수의 도함수

역삼각함수의 **값**은 주값 범위에서 원래 각도를 찾습니다. 여기서 구하는 **도함수**는 입력 비율이 조금 달라질 때 그 각도가 변하는 정도입니다. 아래 계산은 사인·코사인·탄젠트의 도함수와 연쇄법칙을 사용합니다. $x$는 무차원 비율이고 각도 $y$는 라디안으로 나타냅니다.

### $\arcsin x$

$y=\arcsin x$라 두면 $\sin y=x$, $y\in[-\pi/2,\pi/2]$입니다. 양변을 $x$로 미분하고 $\sin^2y+\cos^2y=1$을 이용하면

\[
\cos y\,\frac{dy}{dx}=1,
\qquad
\cos y=\sqrt{1-\sin^2y}=\sqrt{1-x^2}.
\]

이 범위 안쪽에서는 $\cos y>0$이므로

\[
\boxed{\frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^2}}}
\qquad(-1<x<1).
\]

### $\arccos x$

$y=\arccos x$라 두면 $\cos y=x$, $y\in[0,\pi]$입니다. 같은 방법으로

\[
-\sin y\,\frac{dy}{dx}=1,
\qquad
\sin y=\sqrt{1-\cos^2y}=\sqrt{1-x^2}.
\]

범위 안쪽에서는 $\sin y>0$이므로

\[
\boxed{\frac{d}{dx}\arccos x=-\frac{1}{\sqrt{1-x^2}}}
\qquad(-1<x<1).
\]

### $\arctan x$

$y=\arctan x$라 두면 $\tan y=x$, $y\in(-\pi/2,\pi/2)$입니다. 탄젠트를 미분하고 $\sec^2y=1+\tan^2y$를 대입하면

\[
\sec^2y\,\frac{dy}{dx}=1,
\qquad
\sec^2y=1+\tan^2y=1+x^2.
\]

따라서 모든 실수 $x$에서

\[
\boxed{\frac{d}{dx}\arctan x=\frac{1}{1+x^2}}.
\]

예를 들어 입력 비율 $x=1/2$에서 $\arcsin x$와 $\arccos x$의 도함수는 각각 $2/\sqrt3$, $-2/\sqrt3$이고, $x=1$에서 $\arctan x$의 도함수는 $1/2$입니다. $\arcsin$과 $\arccos$는 $x=\pm1$에서 함수값은 정의되지만 유한한 도함수는 없습니다. 센서 비율이 이 끝점에 가까우면 **작은 비율 오차가 큰 각도 오차**로 이어질 수 있습니다.

### 문제 예시: 기울기 추정값의 민감도 비교

드론이 거의 정지한 상태에서 한 축의 기울기 $\theta$를 $r=\sin\theta$로 모델링하고 $\theta\in[-\pi/2,\pi/2]$라 둡니다. 센서 비율 $r$이 $0.60$일 때와 $0.80$일 때 각각 $+0.01$만큼 달라지면, 추정 각도가 얼마나 변할지 미분으로 근사해 보세요. 두 경우에 같은 비율 오차가 다른 각도 오차를 만드는 이유도 설명해 보세요. 다른 가속도와 센서 오차는 제외합니다.

**풀이.** $\theta=\arcsin r$이고 두 기준값 모두 $(-1,1)$에 있으므로 $d\theta/dr=1/\sqrt{1-r^2}$를 적용할 수 있습니다. $\Delta r=0.01$에 대해

\[
\begin{aligned}
r=0.60:&\quad \Delta\theta\approx\frac{0.01}{\sqrt{1-0.60^2}}=0.0125\,\mathrm{rad},\\
r=0.80:&\quad \Delta\theta\approx\frac{0.01}{\sqrt{1-0.80^2}}\approx0.0167\,\mathrm{rad}.
\end{aligned}
\]

$r$이 1에 가까울수록 분모가 작아져 같은 비율 변화에도 각도 변화가 커집니다. 이 값은 해당 기준점의 **국소 근사**입니다. 역함수값을 직접 계산한 정확한 변화는 각각 $\arcsin(0.61)-\arcsin(0.60)\approx0.01256\,\mathrm{rad}$와 $\arcsin(0.81)-\arcsin(0.80)\approx0.01686\,\mathrm{rad}$로, 근사값과 조금 다릅니다.

## 문제 예시: 드론 기압 고도의 입력값과 민감도

기압 고도 모델 $p(h)=p_0e^{-h/H}$에서 가상의 척도높이를 $H=8000\,\mathrm m$로 둡니다. 드론의 센서가 $p=0.9p_0$를 읽었을 때 모델 고도를 구하고, 그 기압에서 센서값이 추가로 **현재 기압의 1%**만큼 낮아지면 추정 고도가 얼마나 늘어나는지 미분 근사와 정확한 역함수값으로 비교해 보세요. 날씨와 온도 변화는 무시합니다.

**풀이.** 역함수로 입력 고도를 계산하면

\[
h(0.9p_0)=-8000\ln(0.9)\approx842.88\,\mathrm m.
\]

$dh/dp=-8000/p$이고 $\Delta p=-0.01p$이므로 미분 근사는 $\Delta h\approx(-8000/p)(-0.01p)=80\,\mathrm m$입니다. 새 기압은 $0.99p$이므로 정확한 모델 변화량은

\[
h(0.99p)-h(p)=-8000\ln(0.99)\approx80.40\,\mathrm m.
\]

역함수는 **현재 고도값**을, 그 도함수는 **기압 오차가 고도 추정에 미치는 민감도**를 구합니다. 실제 드론이 상승하지 않아도 날씨 때문에 기압이 변하면 이 모델은 고도가 변한 것으로 해석할 수 있습니다.
