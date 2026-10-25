# 미적분 학습 목차

센서값으로 상태를 추정하고 물리량의 변화를 계산하는 데 필요한 내용을 **함수**, **미분법**, **부정적분**으로 나눴습니다. 각 문서에는 성립 조건, 유도 또는 증명, 공학적 문제와 풀이를 담았습니다. 그래프를 조작할 수 있는 주제에는 시뮬레이터를 연결했습니다.

## 함수

| 순서 | 문서 | 다루는 질문 |
| --- | --- | --- |
| 1 | [합성함수](functions/composition.md) | 측정과 단위 변환을 연달아 적용하면 어떤 함수가 되는가? |
| 2 | [단사·전사와 역함수](functions/inverse-functions.md) | 출력에서 입력을 유일하게 되찾으려면 어떤 조건이 필요한가? |
| 3 | [함수의 극한과 연속](functions/limits-and-continuity.md) | 값이 가까워질 때의 결과와 목표값의 존재를 어떻게 판단하는가? |
| 응용 | [주기 함수와 신호 시스템](functions/periodic-signals.md) | 반복되는 진동에서 주파수·진폭·위상을 어떻게 읽는가? |

## 미분법

| 순서 | 문서 | 다루는 질문 |
| --- | --- | --- |
| 1 | [미분계수와 도함수](differentiation/derivatives-and-tangents.md) | 순간속도와 접선·법선은 어떻게 구하는가? |
| 2 | [기본 미분법](differentiation/basic-rules.md) | 여러 함수가 결합된 운동·센서 모델의 변화율을 어떻게 계산하는가? |
| 3 | [비행 궤적의 고계도함수](differentiation/trajectory-derivatives.md) | 위치·속도·가속도·저크는 어떻게 이어지고 이동 시간에 따라 달라지는가? |
| 4 | [도함수로 극값 찾기](differentiation/extrema.md) | 허용 범위에서 가장 큰 값이나 작은 값을 어떻게 찾는가? |
| 5 | [롤의 정리](differentiation/theorems/rolle.md) | 같은 출력값 사이에 변화율이 0인 순간이 있는가? |
| 6 | [코시의 평균값 정리](differentiation/theorems/cauchy-mean-value.md) | 두 출력의 전체 변화량 비율과 순간 변화율 비율은 어떻게 연결되는가? |
| 7 | [로피탈의 정리](differentiation/theorems/lhopital.md) | $0/0$형과 $\infty/\infty$형 극한을 언제 도함수로 계산할 수 있는가? |
| 8 | [역함수의 미분법](differentiation/inverse-function-derivatives.md) | 출력 목표의 변화와 $\arcsin$, $\arccos$, $\arctan$의 도함수는 어떻게 구하는가? |
| 9 | [음함수의 미분법](differentiation/implicit-differentiation.md) | 두 변수가 하나의 관계식에 묶여 있을 때 기울기는 무엇인가? |

## 부정적분

| 순서 | 문서 | 다루는 질문 |
| --- | --- | --- |
| 1 | [부정적분 개요](indefinite-integrals/index.md) | 변화율에서 원래 함수의 가족을 어떻게 찾고 계산 기법을 고르는가? |
| 2 | [기본 공식](indefinite-integrals/basic-rules.md) | 선형성, 거듭제곱, 지수·로그 공식은 어떻게 검산하는가? |
| 3 | [합성함수와 치환적분](indefinite-integrals/substitution.md) | 안쪽 함수와 그 도함수를 어떻게 알아보는가? |
| 4 | [삼각함수 적분](indefinite-integrals/trigonometric-integrals.md) | 주기 함수의 거듭제곱과 곱을 어떻게 바꾸는가? |
| 5 | [부분적분](indefinite-integrals/integration-by-parts.md) | 곱의 미분법을 어떻게 거꾸로 적용하는가? |
| 6 | [유리함수와 부분분수](indefinite-integrals/partial-fractions.md) | 다항식의 비를 어떤 기본형으로 분해하는가? |
| 7 | [삼각치환](indefinite-integrals/trigonometric-substitution.md) | 이차식의 제곱근을 어떻게 단순한 삼각함수로 바꾸는가? |

함수의 합성·역함수와 기본 미분법을 먼저 읽으면 적분 공식을 유도하고 검산하기 쉽습니다. 부정적분 문서는 원시함수를 구하는 데 집중하며, 필요한 주제만 골라 읽어도 적용 조건과 계산 과정을 확인할 수 있습니다.
