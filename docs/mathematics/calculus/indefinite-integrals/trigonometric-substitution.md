# 삼각치환

제곱근 안에 $a^2-x^2$ 같은 이차식이 있으면 삼각함수 항등식으로 제곱근을 없앨 수 있습니다. **삼각치환(trigonometric substitution)**은 [일반 치환적분](substitution.md)의 한 종류이지만, 치환하는 각도의 범위를 정해 제곱근의 부호까지 맞추는 점이 중요합니다.

## 어떤 식에 어떤 치환을 쓰는가

$a>0$일 때 대표적인 선택은 다음과 같습니다.

| 제곱근의 형태 | 치환 | 사용하는 항등식 |
| --- | --- | --- |
| $\sqrt{a^2-x^2}$ | $x=a\sin\theta$ | $1-\sin^2\theta=\cos^2\theta$ |
| $\sqrt{a^2+x^2}$ | $x=a\tan\theta$ | $1+\tan^2\theta=\sec^2\theta$ |
| $\sqrt{x^2-a^2}$ | $x=a\sec\theta$ | $\sec^2\theta-1=\tan^2\theta$ |

표만으로 부호가 자동 결정되지는 않습니다. 예를 들어 $|x|<a$에서 $\theta=\arcsin(x/a)\in(-\pi/2,\pi/2)$로 정하면 $\cos\theta\ge0$이어서 $\sqrt{a^2-x^2}=a\cos\theta$입니다. 다른 치환에서도 허용 구간을 먼저 정하고 $\sqrt{z^2}=|z|$를 확인합니다.

## 원형 경계의 원시함수 유도

$|x|<a$에서 $x=a\sin\theta$를 쓰면 $dx=a\cos\theta\,d\theta$입니다. [반각 공식](trigonometric-integrals.md#trig-identities)을 적용하면

\[
\begin{aligned}
\int\sqrt{a^2-x^2}\,dx
&=a^2\int\cos^2\theta\,d\theta\\
&=\frac{a^2}{2}\left(\theta+\sin\theta\cos\theta\right)+C\\
&=\frac12\left[a^2\arcsin\frac xa+x\sqrt{a^2-x^2}\right]+C.
\end{aligned}
\]

마지막 줄은 $\sin\theta=x/a$, $\cos\theta=\sqrt{a^2-x^2}/a$로 원래 변수에 되돌린 결과입니다. 최종 식을 미분하면 $\sqrt{a^2-x^2}$가 나옵니다. 끝점 $x=\pm a$에서는 도함수를 포함한 조건을 별도로 살펴야 합니다.

제곱근이 분모에 있는 더 간단한 형태는 같은 치환으로 $\int dx/\sqrt{a^2-x^2}=\arcsin(x/a)+C$입니다. [역삼각함수의 도함수](../differentiation/inverse-function-derivatives.md)를 미분해도 같은 결과를 확인할 수 있습니다.

## 문제 예시: 원형 허용 영역의 경계식

반지름 $3\,\mathrm m$인 원형 영역의 윗경계를 $y(x)=\sqrt{9-x^2}\,\mathrm m$로 나타냅니다. $|x|<3\,\mathrm m$에서 $F'(x)=y(x)$이고 $F(0)=0$인 원시함수를 구한 뒤 $F(1\,\mathrm m)$을 계산해 보세요. 이는 경계식을 적분하는 가상 기하 모델이며 실제 비행 가능 영역의 판정은 아닙니다.

**풀이.** $a=3$을 위 결과에 넣고 $F(0)=0$으로 상수를 정하면

\[
F(x)=\frac12\left[x\sqrt{9-x^2}+9\arcsin\left(\frac x3\right)\right].
\]

따라서 $F(1\,\mathrm m)=\tfrac12[\sqrt8+9\arcsin(1/3)]\,\mathrm{m^2}\approx2.943\,\mathrm{m^2}$입니다. 결과의 단위는 $y\,dx$에 대응하는 m²이며, 미분하면 처음 경계식으로 돌아옵니다.

## 참고 자료

- [OpenStax Calculus Volume 2, Trigonometric Substitution](https://openstax.org/books/calculus-volume-2/pages/3-3-trigonometric-substitution)
