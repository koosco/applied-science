# 부분적분

두 함수의 곱에서 한쪽은 **미분하면 단순해지고** 다른 쪽은 **원시함수를 구하기 쉬울 때** 부분적분을 살펴봅니다. [곱의 미분법](../differentiation/basic-rules.md)을 거꾸로 적용한 방법입니다.

## 공식의 유도와 선택 기준

$(uv)'=u'v+uv'$이므로 양변의 원시함수를 비교하면

\[
uv=\int u'v\,dx+\int uv'\,dx
\quad\Longrightarrow\quad
\boxed{\int u\,dv=uv-\int v\,du}.
\]

여기서 $dv=v'(x)\,dx$입니다. $u$를 고를 때는 $du$가 더 단순해지는지, $dv$를 고를 때는 $v$를 실제로 구할 수 있는지 확인합니다. 공식은 적분을 없애는 것이 아니라 **더 쉬운 적분으로 바꾸는 것**입니다. 바뀐 적분이 더 어렵다면 다른 분리를 시도합니다.

예를 들어 $x>0$에서 $\int\ln x\,dx$는 $u=\ln x$, $dv=dx$로 두면 $du=dx/x$, $v=x$입니다. 따라서 $\int\ln x\,dx=x\ln x-\int1\,dx=x\ln x-x+C$입니다. 미분하면 다시 $\ln x$가 됩니다.

## 문제 예시: 감쇠 신호의 시간 가중 원시함수

정규화한 가상 센서 응답을 $r(t)=e^{-t/\tau}$로 두고 $\tau=2\,\mathrm s$라고 합시다. $t\ge0$에서 $W'(t)=t\,r(t)$를 만족하고 $W(0)=0$인 함수를 구한 뒤 $W(2\,\mathrm s)$를 계산해 보세요. $W$는 시간으로 가중한 신호의 원시함수이며 단위는 s²입니다.

**풀이.** $u=t$, $dv=e^{-t/\tau}dt$로 선택하면 $du=dt$, $v=-\tau e^{-t/\tau}$입니다. 그러므로

\[
\begin{aligned}
W(t)&=-\tau t e^{-t/\tau}+\tau\int e^{-t/\tau}dt\\
&=-\tau(t+\tau)e^{-t/\tau}+C.
\end{aligned}
\]

$W(0)=0$에서 $C=\tau^2$입니다. $\tau=2\,\mathrm s$를 넣으면 $W(2\,\mathrm s)=(4-8/e)\,\mathrm{s^2}\approx1.057\,\mathrm{s^2}$입니다. 결과를 미분하면 $t e^{-t/\tau}$가 나오므로 곱의 부호와 $\tau$ 계수를 확인할 수 있습니다. 실제 센서의 감쇠가 이 지수 모델을 따른다는 뜻은 아닙니다.

## 참고 자료

- [OpenStax Calculus Volume 2, Integration by Parts](https://openstax.org/books/calculus-volume-2/pages/3-1-integration-by-parts)
