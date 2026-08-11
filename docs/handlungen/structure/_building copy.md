# Strukturen erfassen

## Gebäude als Objekt

<object type="image/svg+xml" data="/assets/images/_building.svg" width="100%"></object>

<!-- Buttons für alle Termini -->
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
  <button onclick="toggleContainer('strom-container', 'strom-button')" class="toggle-button" id="strom-button">{{ strom }}</button>
  <button onclick="toggleContainer('waerme-container', 'waerme-button')" class="toggle-button" id="waerme-button">{{ waerme }}</button>
  <button onclick="toggleContainer('wasser-container', 'wasser-button')" class="toggle-button" id="wasser-button">{{ wasser }}</button>
  <button onclick="toggleContainer('regstrom_ertrag-container', 'regstrom_ertrag-button')" class="toggle-button" id="regstrom_ertrag-button">{{ regstrom_ertrag }}</button>
  <button onclick="toggleContainer('regwaerme_ertrag-container', 'regwaerme_ertrag-button')" class="toggle-button" id="regwaerme_ertrag-button">{{ regwaerme_ertrag }}</button>
  <button onclick="toggleContainer('verkehr-container', 'verkehr-button')" class="toggle-button" id="verkehr-button">{{ verkehr }}</button>
  <button onclick="toggleContainer('papier-container', 'papier-button')" class="toggle-button" id="papier-button">{{ papier }}</button>
  <button onclick="toggleContainer('abfall-container', 'abfall-button')" class="toggle-button" id="abfall-button">{{ abfall }}</button>
  <button onclick="toggleContainer('klima_komp-container', 'klima_komp-button')" class="toggle-button" id="klima_komp-button">{{ klima_komp }}</button>
  <button onclick="toggleContainer('flaechen-container', 'flaechen-button')" class="toggle-button" id="flaechen-button">{{ flaechen }}</button>
  <button onclick="toggleContainer('lebensmittel-container', 'lebensmittel-button')" class="toggle-button" id="lebensmittel-button">{{ lebensmittel }}</button>
  <button onclick="toggleContainer('buerobedarf-container', 'buerobedarf-button')" class="toggle-button" id="buerobedarf-button">{{ buerobedarf }}</button>
  <button onclick="toggleContainer('haushaltsbedarf-container', 'haushaltsbedarf-button')" class="toggle-button" id="haushaltsbedarf-button">{{ haushaltsbedarf }}</button>
</div>

<!-- Container für alle Termini (standardmäßig ausgeblendet) -->
<div id="strom-container" class="toggle-container" style="display: none;">
  <h3>{{ strom }}</h3>
  <p>Hier steht der Inhalt für Strom-Verbrauch.</p>
</div>

<div id="waerme-container" class="toggle-container" style="display: none;">
  <h3>{{ waerme }}</h3>
  <p>Hier steht der Inhalt für Wärmeenergie-Verbrauch.</p>
</div>

<div id="wasser-container" class="toggle-container" style="display: none;">
  <h3>{{ wasser }}</h3>
  <p>Hier steht der Inhalt für Wasser-Verbrauch.</p>
</div>

<div id="regstrom_ertrag-container" class="toggle-container" style="display: none;">
  <h3>{{ regstrom_ertrag }}</h3>
  <p>Hier steht der Inhalt für Regenerativstrom-Ertrag.</p>
</div>

<div id="regwaerme_ertrag-container" class="toggle-container" style="display: none;">
  <h3>{{ regwaerme_ertrag }}</h3>
  <p>Hier steht der Inhalt für Regenerativwärme-Ertrag.</p>
</div>

<div id="verkehr-container" class="toggle-container" style="display: none;">
  <h3>{{ verkehr }}</h3>
  <p>Hier steht der Inhalt für Verkehrsmenge.</p>
</div>

<div id="papier-container" class="toggle-container" style="display: none;">
  <h3>{{ papier }}</h3>
  <p>Hier steht der Inhalt für Papierverbrauch.</p>
</div>

<div id="abfall-container" class="toggle-container" style="display: none;">
  <h3>{{ abfall }}</h3>
  <p>Hier steht der Inhalt für Abfall-Entsorgung.</p>
</div>

<div id="klima_komp-container" class="toggle-container" style="display: none;">
  <h3>{{ klima_komp }}</h3>
  <p>Hier steht der Inhalt für Klima-Kompensation.</p>
</div>

<div id="flaechen-container" class="toggle-container" style="display: none;">
  <h3>{{ flaechen }}</h3>
  <p>Hier steht der Inhalt für Flächen.</p>
</div>

<div id="lebensmittel-container" class="toggle-container" style="display: none;">
  <h3>{{ lebensmittel }}</h3>
  <p>Hier steht der Inhalt für Lebensmittel.</p>
</div>

<div id="buerobedarf-container" class="toggle-container" style="display: none;">
  <h3>{{ buerobedarf }}</h3>
  <p>Hier steht der Inhalt für Bürobedarf.</p>
</div>

<div id="haushaltsbedarf-container" class="toggle-container" style="display: none;">
  <h3>{{ haushaltsbedarf }}</h3>
  <p>Hier steht der Inhalt für Haushaltsbedarf.</p>
</div>

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

<!-- CSS für die Buttons und Container (Dark Mode-kompatibel) -->
<style>
.toggle-button {
  padding: 8px 16px;
  background: var(--md-primary-fg-color);
  color: white; /* Weiße Textfarbe für inaktive Buttons */
  border: 1px solid var(--md-primary-fg-color);
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s, color 0.2s;
}

.toggle-button:hover {
  background: var(--md-primary-fg-color-dark);
}

.toggle-button.active-button {
  background: transparent !important; /* Transparenter Hintergrund für den aktiven Button */
  color: var(--md-primary-fg-color) !important; /* Primärfarbe für den Text des aktiven Buttons */
  border: 1px solid var(--md-primary-fg-color);
}

.toggle-container {
  margin-top: 16px;
  padding: 12px;
  background: var(--md-default-fg-color--lighter);
  border-radius: 4px;
  color: var(--md-default-fg-color-on);
  border: 1px solid var(--md-default-fg-color--lighter);
}
</style>


