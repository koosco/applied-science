# 삼각함수 적분

진동이나 회전 모델에는 사인·코사인 함수가 자주 나타납니다. 한 항의 원시함수는 [기본 공식](basic-rules.md)으로 구하고, 거듭제곱이나 곱은 **삼각 항등식으로 모양을 바꾼 뒤** 적분합니다. 각도의 단위는 라디안입니다. 파형 자체는 [주기 함수와 신호 시스템](../functions/periodic-signals.md)의 시뮬레이터에서 확인할 수 있습니다.

## 기본 원시함수와 안쪽 각도

\[
\int\sin x\,dx=-\cos x+C,\qquad
\int\cos x\,dx=\sin x+C,\qquad
\int\sec^2x\,dx=\tan x+C.
\]

$\cos x\ne0$인 구간에서는 $(\ln|\cos x|)'=-\tan x$이므로 $\int\tan x\,dx=-\ln|\cos x|+C$입니다. $\sin x\ne0$인 구간에서는 $\int\cot x\,dx=\ln|\sin x|+C$입니다. 로그 안의 함수가 0이 되는 지점을 가로질러 하나의 원시함수를 쓰지 않습니다.

안쪽 각도가 $\omega t+\phi$이면 [연쇄법칙과 치환적분](substitution.md)에 따라 $\omega\ne0$일 때

\[
\int\sin(\omega t+\phi)\,dt
=-\frac{\cos(\omega t+\phi)}{\omega}+C.
\]

미분하면 앞의 $1/\omega$와 안쪽 도함수 $\omega$가 서로 상쇄됩니다.

<a id="trig-identities"></a>
## 제곱과 곱을 항등식으로 바꾸기

$\cos(2x)=1-2\sin^2x=2\cos^2x-1$과 $\sin(2x)=2\sin x\cos x$에서

\[
\sin^2x=\frac{1-\cos(2x)}2,\qquad
\cos^2x=\frac{1+\cos(2x)}2,\qquad
\sin x\cos x=\frac{\sin(2x)}2
\]

를 얻습니다. 그러므로 $\int\sin^2x\,dx=x/2-\sin(2x)/4+C$입니다. 두 거듭제곱 중 하나가 홀수라면 한 인수를 떼어 내고 $\sin^2x+\cos^2x=1$을 사용해 치환할 수도 있습니다. 예를 들어 $\sin^3x\cos x=\sin^3x(\sin x)'$이므로 $\int\sin^3x\cos x\,dx=\sin^4x/4+C$입니다. 양쪽 지수가 짝수이면 반각 공식을 먼저 살펴봅니다.

## 문제 예시: 가상 주기 전류의 손실 에너지 함수

가상의 저항성 구동 회로에서 전류를 $i(t)=2\sin(\pi t)\,\mathrm A$, 저항을 $R=1\,\Omega$로 둡니다. $t$는 초 단위 시간의 수치이며 실제 BLDC 모터의 전류 파형을 뜻하지 않습니다. 손실 전력 $P(t)=i(t)^2R=4\sin^2(\pi t)\,\mathrm W$의 원시함수 $E'(t)=P(t)$를 구하고 $E(0)=0$일 때 $E(1)$을 계산해 보세요.

**풀이.** 반각 공식으로 $4\sin^2(\pi t)=2-2\cos(2\pi t)$입니다. 따라서

\[
E(t)=2t-\frac{\sin(2\pi t)}{\pi}+C\quad\mathrm J.
\]

$E(0)=0$에서 $C=0$이고 $E(1)=2\,\mathrm J$입니다. 미분하면 $2-2\cos(2\pi t)=4\sin^2(\pi t)$로 돌아갑니다. 여기서 $E$의 단위는 W·s인 J이며, 계산은 주어진 이상적인 저항 모델에만 해당합니다.

## 참고 자료

- [OpenStax Calculus Volume 2, Trigonometric Integrals](https://openstax.org/books/calculus-volume-2/pages/3-2-trigonometric-integrals)
