# 💧 습도 조건 자동 테이블 (CSV 기반)

아래 표는 외부 CSV 파일(`humidity_data.csv`)에서 데이터를 불러와 자동으로 표시되며,  
조건에 따라 특정 값을 추출하여 아래에 보여줍니다.

---

<table id="csv-table" border="1"></table>

<p><strong>❄️ 추출값 (겨울 / 편차가 없는 습도요구):</strong>
<span id="extracted-value" style="color:blue;"></span></p>

<script>
  fetch("humidity_data.csv")
    .then(res => res.text())
    .then(text => {
      const rows = text.trim().split("\n").map(r => r.split(","));
      const header = rows[0];
      const table = document.getElementById("csv-table");

      // 표 출력
      rows.forEach((row, i) => {
        const tr = document.createElement("tr");
        row.forEach(cell => {
          const el = document.createElement(i === 0 ? "th" : "td");
          el.textContent = cell.trim();
          tr.appendChild(el);
        });
        table.appendChild(tr);
      });

      // 조건값 추출 (겨울, 편차가 없는 습도요구, hABL,Wi)
      const 계절Index = header.indexOf("계절");
      const 조건Index = header.indexOf("조건");
      const 값Index = header.indexOf("값");

      const matchRow = rows.find((row, i) =>
        i > 0 &&
        row[계절Index] === "겨울" &&
        row[조건Index] === "편차가 없는 습도요구"
      );

      const value = matchRow?.[값Index] ?? "값 없음";
      document.getElementById("extracted-value").textContent = value;
    });
</script>
