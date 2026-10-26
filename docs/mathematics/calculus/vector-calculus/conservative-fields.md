# 보존장과 퍼텐셜: 경로 독립적 적분

> 벡터 미적분 3/5 · 선수 지식: [선적분](line-integrals.md), 그래디언트

## 언제 경로가 중요하지 않을까?

어떤 스칼라 함수 $\phi$가 있어 $\mathbf F=\nabla\phi$로 표현되면 $\mathbf F$는 **퍼텐셜을 가진 보존장(conservative field)**입니다. 매끄러운 경로를 따라 퍼텐셜을 미분한 값을 누적하면 양 끝값의 차이만 남습니다.

\[
\boxed{\int_C\mathbf F\cdot d\mathbf r
=\phi(B)-\phi(A).}
\]

여기서는 힘이 **양의 그래디언트**인 수학적 정의를 사용합니다. 물리학에서 위치에너지 $U$로 표현한 보존력은 흔히 $\mathbf F=-\nabla U$로 쓰므로 부호가 다릅니다.

## 그래프로 이해하기

![퍼텐셜 φ=x²+y²의 동심원 등위선과 두 끝점 사이 여러 경로를 나타낸 그림](../../../assets/figures/calculus/vector-calculus/conservative-potential.svg)

*경로 모양이 달라도 같은 시작점과 도착점을 가지면 퍼텐셜 차이는 같습니다.*

## 문제 예시: 두 경로의 일 비교

$\phi(x,y)=x^2+y^2$이고 $\mathbf F=\nabla\phi=(2x,2y)$입니다. $A=(0,0)$에서 $B=(3,4)$까지 이동할 때의 선적분을 구하세요. 모든 값은 무차원 수학적 예시입니다.

**풀이.** 퍼텐셜 차이만 계산하면

\[
\int_C\mathbf F\cdot d\mathbf r
=\phi(3,4)-\phi(0,0)
=3^2+4^2-0=25.
\]

직선이든 두 축을 따라 꺾어서 가든 같은 결과입니다. 폐곡선에서는 시작점과 끝점이 같으므로 $\oint_C\mathbf F\cdot d\mathbf r=0$입니다(이 장의 보존장 가정 아래에서).

## 확인 문제

$\phi(x,y)=x+2y$인 보존장에서 $A=(1,1)$에서 $B=(2,3)$으로 이동할 때의 선적분을 구하세요.

## 확인 문제 풀이

$\phi(B)=2+6=8$, $\phi(A)=1+2=3$이므로 적분값은 $8-3=5$입니다.

[← 이전: 선적분](line-integrals.md) · [다음: 발산과 회전](divergence-and-curl.md)
