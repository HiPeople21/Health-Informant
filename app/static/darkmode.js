let darkMode = localStorage.getItem('darkMode');
const darkModeToggle = document.querySelector('#darkModeToggle');
const contentContainer = document.querySelector('.content-container');


function toggleMode() {
  if (darkMode === 'enabled') {
    contentContainer.classList.remove('darkmode');
    localStorage.setItem('darkMode', 'null');
  } else {
    contentContainer.classList.add('darkmode');
    localStorage.setItem('darkMode', 'enabled');
  }
}

if (darkMode === 'enabled') {
  contentContainer.classList.add('darkmode');
}

darkModeToggle.addEventListener('click', () => {
  darkMode = localStorage.getItem('darkMode');
  console.log(darkMode);
  toggleMode();
});