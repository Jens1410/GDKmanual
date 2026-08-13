<!-- JavaScript-Funktion zum Toggle -->
<script>
function toggleContainer(containerId, buttonId) {
  // Alle Container ausblenden
  document.querySelectorAll('.toggle-container').forEach(container => {
    container.style.display = 'none';
  });

  // Alle Buttons auf Standard-Stil zurücksetzen
  document.querySelectorAll('.toggle-button').forEach(button => {
    button.classList.remove('active-button');
  });

  // Den gewählten Container einblenden
  const selectedContainer = document.getElementById(containerId);
  if (selectedContainer) {
    selectedContainer.style.display = 'block';
  }

  // Den gewählten Button als aktiv markieren
  const selectedButton = document.getElementById(buttonId);
  if (selectedButton) {
    selectedButton.classList.add('active-button');
  }
}
</script>

