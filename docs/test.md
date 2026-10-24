# 시뮬레이터 동작 확인

아래 시뮬레이터에서 초기 속력과 발사 각도를 바꾸면 파란 궤적과 계산값이 함께 갱신됩니다. 회색 점선은 처음 설정인 20 m/s, 45°의 기준 궤적입니다. [포물선 운동 문서](mechanics/projectile-motion.md)에서 모델의 가정과 수식을 확인할 수 있습니다.

<iframe src="../simulations/projectile/index.html?v=reset-3" title="포물선 운동 시뮬레이터 동작 확인" width="100%" height="640" loading="lazy" style="border: 1px solid #ddd; border-radius: 8px;"></iframe>

<a href="../simulations/projectile/index.html?v=reset-3" target="_blank" rel="noopener">시뮬레이터 새 창에서 열기</a>

## 확인 방법

1. 기본값인 **초기 속력 20 m/s, 발사 각도 45°**에서 도달 거리 약 **40.77 m**를 확인합니다.
2. 초기 속력을 **30 m/s**로 바꾸고 궤적이 달라지는지 확인합니다. 같은 각도에서 도달 거리는 약 **91.74 m**입니다.
3. 각도를 바꾸고 최고 높이와 도달 거리가 다시 계산되는지 확인합니다.
4. 궤적 위에 마우스를 올려 해당 지점의 수평 거리(x)와 높이(y)를 확인합니다.
5. 초기화 버튼을 누르고 속력 20 m/s, 각도 45°, 도달 거리 약 40.77 m로 돌아가는지 확인합니다.

이상적인 모델의 결과이며 공기 저항은 포함하지 않습니다.
