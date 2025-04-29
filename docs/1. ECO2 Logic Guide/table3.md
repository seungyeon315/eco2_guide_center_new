# 📊 Humidity Data Table (Clickable Cells)

<!-- PapaParse 라이브러리 불러오기 -->
<script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.0/papaparse.min.js"></script>

<!-- 테이블을 표시할 영역 -->
<div id="csv-table"></div>

<script>
// CSV 파일 불러오기
fetch('humidity_data1.csv') // CSV 파일 경로 (예: assets 폴더에 넣었다고 가정)
  .then(response => response.text())
  .then(text => {
    const data = Papa.parse(text, { header: true }).data;
    const tableDiv = document.getElementById('csv-table');

    const table = document.createElement('table');
    table.border = '1';
    table.style.borderCollapse = 'collapse';
    table.style.width = '100%';

    // 테이블 헤더 만들기
    const headerRow = document.createElement('tr');
    for (const key in data[0]) {
      const th = document.createElement('th');
      th.textContent = key;
      th.style.padding = '8px';
      th.style.backgroundColor = '#f2f2f2';
      headerRow.appendChild(th);
    }
    table.appendChild(headerRow);

    // 테이블 데이터 채우기
    data.forEach(row => {
      const tr = document.createElement('tr');
      for (const key in row) {
        const td = document.createElement('td');
        td.textContent = row[key];
        td.style.padding = '8px';
        td.style.textAlign = 'center';

        // 📌 특정 셀 클릭 시 새 창 열기 기능 추가
        if (key === 'Humidity' && parseFloat(row[key]) >= 80) { // 조건: Humidity >= 80
          td.style.backgroundColor = 'lightblue';
          td.style.cursor = 'pointer';
          td.title = 'Click to see details';

          td.onclick = () => {
            // 클릭 시 새 창 열기
            window.open('https://example.com', '_blank'); 
            // 여기서 URL을 row 데이터에 따라 다르게 설정할 수도 있음
          };
        }

        tr.appendChild(td);
      }
      table.appendChild(tr);
    });

    tableDiv.appendChild(table);
  });
</script>
