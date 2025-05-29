# 열손실 및 열획득 (Heat Loss and Heat Gain)

존의 열손실/열획득은 서로 대차 대조된 후, 난방부하 또는 냉방부하가 계산됩니다. 다음과 같은 열손실 및 열획득이 부하 분석 시 고려됩니다:

- 관류에 의한 열손실/열획득
- 환기에 의한 열손실/열획득 (침기, 창문환기, 이웃 존과의 환기)
- 존의 부하와 무관하게 온도 처리된 급기에 의한 열손실/열획득
- 투명한 창호를 통한 태양열 획득
- 불투명한 벽체의 외피에서 태양열흡수와 열방사에 의한 열손실/열획득
- 전자기기, 인공조명, 인체발열(사람, 동물), 건물 존으로 온기나 냉기를 가진 물건 유입/반출, 존 내부에 열/냉열 배관이 지나가 발생하는 내부 열손실/열획득

## 열손실

전도와 자연환기에 의한 열손실, 기계환기에 의한 냉열유입, 존 내부의 냉열원 그리고 복사손실에 의한 존의 총 열손실이 결정됩니다. 

<body>
    <details>
        <summary>열손실</summary>
        <p>
            열손실 계산식은 다음과 같습니다:
        </p>
        <p style="margin-left:20px;">
            <code>Q_{sink} = Q_T + Q_V + Q_{I,sink} + Q_S</code>
        </p>
    </details>
<body>

<div style="display: flex; gap: 2em;">

  <!-- 왼쪽 단: 열손실 (기본 열림 상태) -->
  <div style="flex: 1;">
    <details open>
      <summary><strong>열손실</strong></summary>
      <p>\( Q_{sink} = Q_T + Q_V + Q_{I,sink} + Q_S \)</p>
      {{ include_equations("2", 11, 11) }}
    </details>
  </div>

  <!-- 오른쪽 단: 여러 개의 접힌 details -->
  <div style="flex: 1; display: flex; flex-direction: column; gap: 1em;">

    <details>
      <summary><strong>전도 열손실</strong></summary>
      <p>\( Q_{source} = Q_{solar} + Q_{internal} + Q_{gain} \)</p>
      {{ include_equations("2", 11, 12) }}
    </details>

    <details>
      <summary><strong>외기에 접한 벽체를 통한 전도</strong></summary>
      <p>각 열량 항목은 보정계수를 곱하여 평가합니다.</p>
      <ul>
        <li>계수 1</li>
        <li>계수 2</li>
      </ul>
    </details>

    <details>
      <summary><strong>🔹 기타 조건</strong></summary>
      <p>기타 조건 설명 또는 표 삽입 가능.</p>
    </details>

  </div>

</div>
