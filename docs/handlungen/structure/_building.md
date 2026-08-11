# Objekt anlegen

!!! tip "{{ term_object }}: {{ def_object }}"

    **Objekt der technischen Infrastruktur**  
    {{ def_object_tech }}  

    **Objekt der organisatorischen Struktur**  
    {{ def_object_org }}  

<!-- Buttons für die 4 Optionen -->
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
  <button onclick="toggleContainer('strukturen-container', 'strukturen-button')" class="toggle-button" id="strukturen-button">1. {{ function_call }}</button>
  <button onclick="toggleContainer('objekt-container', 'objekt-button')" class="toggle-button" id="objekt-button">2. {{ data_input }}</button>
  <button onclick="toggleContainer('daten-container', 'daten-button')" class="toggle-button" id="daten-button">{{ optional }}{{ data_edit }}</button>
  <button onclick="toggleContainer('bild-container', 'bild-button')" class="toggle-button" id="bild-button">{{ optional }}{{ image_add }}</button>
</div>

<!-- Container für die Inhalte (nur der erste ist sichtbar) -->
<div id="strukturen-container" class="toggle-container" style="display: none;">
    <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/object_function_call.png"></div>
    <ol>
      <li>{{ action_openpage }}<strong>{{ men_item_structure }}</strong></li>
      <li>{{action_callfunction}}<strong>{{new_object}}</strong> | <i>{{result_dialog_appears}}<strong>{{dialog_header_editdata}}</strong></i></li>
    </ol>      
</div>

<div id="objekt-container" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/object_data-input.png"></div>
  <p>Alle gelb hinterlegten Felder sind Pflichtfelder und müssen ausgefüllt werden. Alle anderen Felder sind optional. Sie können für die weitere Arbeit zunächst leer bleiben, nachträglich eingetragen oder geändert werden.</p> 
  <p>Bist du mit den Eingaben fertig, klicke auf <strong>[Speichern]</strong>. <br><i>Das Objekt erscheint in der Liste auf dieser Seite.</i></p>
  <hr>
  <h3>{{ struct_head_parameters }}</h3>
 
</details>
  <details>
    <summary>{{ object_name }}</summary>
    <p>{{ object_name_definition }}</p>
  </details>
  <details>
    <summary>{{ object_code }}</summary>
    <p>{{ object_code_definition }}<br>
    <strong>{{ object_code_key }}</strong></p>
    <p><strong>Codeziffer für den Gebäudetyp</strong ><br>01 Kirche; 02 Gemeindehaus; 03 Kindergarten; 04 Verwaltung; 05 Gemeindezentrum; 06 Wohnhaus; 07 Gästehaus; 08 Schule; 09 Werkstatt; 10 Tagesstätte/-einrichtung; 11 Stationäre Einrichtung; 12 Krankenhaus; 13 Außenanlage; 14 sonstiges; 15 Kapelle; 16 Pfarrhaus; 36 Gewerbe; 37 KiTa (Betriebsträgerschaft); 38 Friedhof; 39 Friedhof (Betriebsträgerschaft)</p>
  </details>
  <details>
    <summary>{{ object_type }}</summary>
    <p>{{ object_type_definition }}</p>
    <p><strong>Für ein Objekt der organisatorischen Struktur: "sonstiges" </strong></p>
  </details>
  <details>
    <summary>{{ object_plz }} / {{ object_city }} / {{ object_street}}</summary>
    <p>{{ object_plz_definition }}</p>
  </details>
  <details>
    <summary>{{ object_coordinates }}</summary>
    <p>{{ object_coordinates_definition }}</p>
  </details>
  <details>
    <summary>{{ object_built }}</summary>
    <p>{{ object_built_definition }}</p>
  </details>
  <details>
    <summary>{{ object_area }}</summary>
    <p>{{ object_area_definition }}</p>
  </details>
  <details>
    <summary>{{ object_historic }}</summary>
    <p>{{ object_historic_definition }}</p>
  </details>
  <details>
    <summary>{{ object_annotation }}</summary>
    <p>{{ object_annotation_definition }}</p>
  </details>
</div>

<div id="daten-container" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/object_data-edit.png"></div>
  <p>Um die Daten für ein Objekt nachträglich zu ändern, klickst du auf das Symbol <img src="../../../assets/images/symbol_edit.png">. <br><i>{{result_dialog_appears}}<strong>{{dialog_header_editdata}}</strong></i></p>
  <hr>
  <h3>{{ struct_head_parameters }}</h3>
</div>

<div id="bild-container" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/object_add_image.png"></div>
  <p>Um dem dem Objekt ein Foto zuzuordnen, klickst du auf das Symbol <img src="../../../assets/images/symbol_add_image.png">.</p>
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

<!-- CSS für die Buttons und Container
<style>
.toggle-button {
  padding: 8px 16px;
  background: var(--md-primary-fg-color);
  color: white;
  border: 1px solid var(--md-primary-fg-color);
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s, color 0.2s;
}

.toggle-button:hover {
  background: transparent !important;
  color: var(--md-primary-fg-color) !important;
  border: 1px solid var(--md-primary-fg-color);
}

.toggle-button.active-button {
  background: transparent !important;
  color: var(--md-primary-fg-color) !important;
  border: 1px solid var(--md-primary-fg-color);
}

.toggle-container {
  margin-top: 16px;
  padding: 0;
  background: transparent;
  border: none;
  color: var(--md-default-fg-color-on);
}
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;
  padding:10px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-u9tq{border-color:#009485;text-align:left;vertical-align:top}
.tg .tg-b2xu{background-color:#009485;border-color:#009485;color:#ffffff;font-weight:bold;text-align:left;vertical-align:top}
</style>
-->
