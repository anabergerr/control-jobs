document.getElementById('search-input').addEventListener('keyup', filterTable);
document.getElementById('date-input').addEventListener('change', filterTable);
document.getElementById('company-input').addEventListener('change', filterTable);

function filterTable() {
  const filterName = document.getElementById('search-input').value.toUpperCase();
  const filterDateInput = document.getElementById('date-input').value;
  const filterCompany = document.getElementById('company-input').value;

  let filterDate = null;
  if (filterDateInput) {
    const dateParts = filterDateInput.split('-');
    if (dateParts.length === 3) {
      filterDate = `${dateParts[0]}-${dateParts[1].padStart(2, '0')}-${dateParts[2].padStart(2, '0')}`;
    }
  }

  const rows = document.querySelectorAll('#job-table tbody tr');
  rows.forEach(row => {
    const cells = row.querySelectorAll('td');
    let nameMatch = true;
    let dateMatch = true;
    let companyMatch = true;

    if (filterName) {
      const nameCell = cells[0];
      const nameText = nameCell.textContent || nameCell.innerText;
      nameMatch = nameText.toUpperCase().includes(filterName);
    }

    if (filterDate) {
      const dateCell = cells[1];
      const dateText = dateCell.textContent || dateCell.innerText;
      const tableDate = new Date(dateText);
      const formattedDate = `${tableDate.getFullYear()}-${(tableDate.getMonth() + 1).toString().padStart(2, '0')}-${tableDate.getDate().toString().padStart(2, '0')}`;
      dateMatch = formattedDate === filterDate;
    }

    if (filterCompany) {
      const companyCell = cells[3];
      const companyText = companyCell.textContent || companyCell.innerText;
      companyMatch = companyText === filterCompany;
    }

    row.style.display = nameMatch && dateMatch && companyMatch ? '' : 'none';
  });
}


