# 📊 Humidity Table – Clickable Cells (편차가 허용된 습도요구)

<!-- PapaParse 라이브러리 (CSV 파싱용) -->
<script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.0/papaparse.min.js"></script>

<!-- 테이블 렌더링 위치 -->
<div id="csv-table"></div>

<script>
// CSV 파일 불러오기
fetch('humidity_data1.csv') // CSV 경로에 맞게 수정
  .then(response => response.text())
  .then(text => {
    const data = Papa.parse(text, { header: true, skipEmptyLines: true }).data;
    const tableDiv = document.getElementById('csv-table');

    const table = document.createElement('table');
    table.border = '1';
    table.style.borderCollapse = 'collapse';
    table.style.width = '100%';
    table.style.marginTop = '10px';

    // 테이블 헤더 만들기
    const headerRow = document.createElement('tr');
    for (const key in data[0]) {
      const th = document.createElement('th');
      th.textContent = key;
      th.style.padding = '8px';
      th.style.backgroundColor = '#f2f2f2';
      th.style.border = '1px solid #ccc';
      headerRow.appendChild(th);
    }
    table.appendChild(headerRow);

    // 테이블 행 채우기
    data.forEach(row => {
      const tr = document.createElement('tr');
      for (const key in row) {
        const td = document.createElement('td');
        td.textContent = row[key];
        td.style.padding = '8px';
        td.style.border = '1px solid #ccc';
        td.style.textAlign = 'center';

        // 🔍 조건: '편차가 허용된 습도요구' 셀은 클릭 가능하게 만들기
        if (row[key] && row[key].trim() === '편차가 허용된 습도요구') {
          td.style.backgroundColor = '#d0f0fd';
          td.style.cursor = 'pointer';
          td.title = '자세한 정보를 보려면 클릭하세요';

          // 클릭하면 새 창 열기
          td.onclick = () => {
            window.open('supply_loss.html', '_blank');
          };
        }

        tr.appendChild(td);
      }
      table.appendChild(tr);
    });

    tableDiv.appendChild(table);
  });
</script>
