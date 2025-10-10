const toggleBtn = document.getElementById('themeToggle');
const currentTheme = localStorage.getItem('theme');

// Apply saved theme on load
if(currentTheme === 'light'){
    document.body.classList.add('light');
    toggleBtn.textContent = '🌞 Light Mode';
}

// Toggle theme on button click 
toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('light');
    const theme = document.body.classList.contains('light') ? 'light' : 'dark';
    localStorage.setItem('theme', theme);
      toggleBtn.textContent = theme === 'light' ? '🌞 Light Mode' : '🌙 Dark Mode';
});

