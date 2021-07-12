let rows = 0;
let columns;
let gameBoard = [rows, columns];

while (rows <= 7) {
  document.getElementById("gameBoard").append(rows);
  let columns = 0;
  while (columns <= 5) {
    let rows;
    rows.appendChild(columns);
    columns++;
  }
  document.write("</br>")
  rows++;
}
