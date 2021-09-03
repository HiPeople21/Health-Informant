let darkMode = localStorage.getItem('darkMode');
const darkModeToggle = document.querySelector('#darkModeToggle');

function toggleMode() {
  if (darkMode === 'enabled') {
    document.body.classList.remove('darkmode');
    localStorage.setItem('darkMode', 'null');
  } else {
    document.body.classList.add('darkmode');
    localStorage.setItem('darkMode', 'enabled');
  }
}

if (darkMode === 'enabled') {
  document.body.classList.add('darkmode');
}

darkModeToggle.addEventListener('click', () => {
  darkMode = localStorage.getItem('darkMode');
  toggleMode();
});