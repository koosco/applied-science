# 합성함수와 치환적분

적분할 함수에 $g(x)$가 들어 있고 그 바깥에 $g'(x)$가 곱해져 있다면 [연쇄법칙](../differentiation/basic-rules.md#chain-rule)을 거꾸로 읽습니다. 이것이 **치환적분($u$-substitution)**의 핵심입니다.

## 왜 치환할 수 있는가

$F'=f$이고 $g$가 미분 가능하면

\[
\frac{d}{dx}F(g(x))=f(g(x))g'(x).
\]

따라서 두 함수가 정의되는 구간에서

\[
\boxed{\int f(g(x))g'(x)\,dx=F(g(x))+C.}
\]

$u=g(x)$, $du=g'(x)\,dx$라는 표기는 이 식을 짧게 계산하는 방법입니다. 치환 후에는 **남은 $x$를 모두 $u$로 바꾸고**, 적분이 끝나면 원래 변수로 돌아옵니다. $g$가 구간 전체에서 역함수를 가질 필요는 없습니다. 위 연쇄법칙이 성립하고 원시함수를 미분해 확인할 수 있으면 됩니다.

## 안쪽 도함수와 상수 배율

예를 들어 $\int\cos(3t+\phi)\,dt$에서 안쪽 식을 $u=3t+\phi$로 두면 $du=3\,dt$입니다. 따라서

\[
\int\cos(3t+\phi)\,dt=\frac13\sin(3t+\phi)+C.
\]

계수 $1/3$을 빠뜨리면 미분 결과가 세 배가 됩니다. 마찬가지로 $x^2+1>0$이므로

\[
\int\frac{2x}{x^2+1}\,dx
=\ln(x^2+1)+C,
\]

이며 $u=x^2+1$, $du=2x\,dx$를 사용했습니다. 일반적으로 $g(x)\ne0$인 구간에서는 $\int g'(x)/g(x)\,dx=\ln|g(x)|+C$입니다. 반면 $\int\cos(t^2)\,dt$에는 $2t$가 없어서 같은 치환을 바로 적용할 수 없습니다. 겉모양만 보고 안쪽 도함수를 만들어 내서는 안 됩니다.

## 문제 예시: 시간에 따라 빨라지는 위상

가상 비행 시험에서 한 축의 각속도를 $\omega(t)=0.6t\cos(0.3t^2)\,\mathrm{rad/s}$로 계획했습니다. $t$는 초 단위 시간의 수치이고 $0\le t\le2$입니다. 시작 각도 $\theta(0)=0.2\,\mathrm{rad}$가 주어졌을 때 방향각 $\theta(t)$와 $\theta(2)$를 구해 보세요.

**풀이.** 사인 함수의 안쪽 위상은 $u=0.3t^2$ 라디안이고 $du=0.6t\,dt$입니다. 따라서

\[
\theta(t)=\int 0.6t\cos(0.3t^2)\,dt
=\sin(0.3t^2)+C.
\]

$\theta(0)=0.2$이므로 $C=0.2$이고, $\theta(2)=0.2+\sin(1.2)\approx1.132\,\mathrm{rad}$입니다. 미분하면 $0.6t\cos(0.3t^2)$가 다시 나옵니다. 이 식은 계획한 각속도의 원시함수이며 실제 기체 자세 측정값은 아닙니다.

## 참고 자료

- [OpenStax Calculus Volume 1, Substitution](https://openstax.org/books/calculus-volume-1/pages/5-5-substitution)
