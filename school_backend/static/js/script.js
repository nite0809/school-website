// script.js
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav ul');
    
    menuToggle.addEventListener('click', () => {
      nav.classList.toggle('show');
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    const dropdownBtn = document.querySelector('.dropdown-btn');
    
    dropdownBtn.addEventListener('click', (event) => {
      event.preventDefault();
      const dropdown = dropdownBtn.nextElementSibling;
      dropdown.classList.toggle('show');
    });
  });
  