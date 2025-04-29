# 📊 Humidity Data Table from CSV

<!-- PapaParse 라이브러리 (CSV 파싱용) 불러오기 -->
<script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.0/papaparse.min.js"></script>

<!-- 테이블을 삽입할 div -->
<div id="csv-table"></div>

<!-- 특정 셀 결과를 보여줄 div -->
<p><strong>❄️ Extracted Winter Humidity:</strong> <span id="winter-humidity" style="color:blue;"></span></p>

<script>
// CSV 파일 불러오기
fetch('humidity_data1.csv')  // 파일 경로는 GitHub Pages에 업로드된 경로로 수정해야 함 
  .then(response => response.text())
  .then(text => {
    const data = Papa.parse(text, { header: true }).data;
    const tableDiv = document.getElementById('csv-table');

    // 테이블 생성
    const table = document.createElement('table');
    table.border = '1';
    const headerRow = document.createElement('tr');

    // 첫 번째 행 (헤더)
    for (const key in data[0]) {
      const th = document.createElement('th');
      th.textContent = key;
      headerRow.appendChild(th);
    }
    table.appendChild(headerRow);

    // 데이터 행
    data.forEach(row => {
      const tr = document.createElement('tr');
      for (const key in row) {
        const td = document.createElement('td');
        td.textContent = row[key];
        tr.appendChild(td);
      }
      table.appendChild(tr);
    });

    tableDiv.appendChild(table);

    // ❄️ 특정 조건에 맞는 셀 값 추출
    const winterRow = data.find(d => d.Season && d.Season.trim() === 'Winter');
    if (winterRow) {
      document.getElementById('winter-humidity').textContent = winterRow.Humidity || '(no data)';
    } else {
      document.getElementById('winter-humidity').textContent = '(Winter not found)';
    }
  });
</script>
