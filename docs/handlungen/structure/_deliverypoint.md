
!!! tip "{{ term_deliverypoint }}: {{ def_deliverypoint }}"

    **Lieferstelle der technischen Infrastruktur**  
    {{ def_deliverypoint_tech }}  

    **Lieferstelle der organisatorischen Struktur**  
    {{ def_deliverypoint_org }}  

<!-- Buttons für die 4 Optionen -->
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
  <button onclick="toggleContainer('container-1', 'button1')" class="toggle-button" id="button-1">1. {{ function_call }}</button>
  <button onclick="toggleContainer('container-2', 'button-2')" class="toggle-button" id="button-2">2. {{ data_input }}</button>
  <button onclick="toggleContainer('container-3', 'button-3')" class="toggle-button" id="button-3">3. {{ object_shares_definition }}</button>
  <button onclick="toggleContainer('container-4', 'button-4')" class="toggle-button" id="button-4">{{ optional }}{{ data_edit }}</button>
</div>

<!-- Container für die Inhalte (nur der erste ist sichtbar) -->
<div id="container-1" class="toggle-container" style="display: none;">
    <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/deliverypoint_function_call.png"></div>
    <ol>
      <li>{{ action_openpage }}<strong>{{ men_item_deliverypoints }}</strong></li>
      <li>Wähle den Verbrauchssektor. <br>
      Für elektrische Heizungsanlagen mit eigener Zähleinrichtung wähle die Ressource <strong>{{ waerme }}</strong>. </li>
      <li>{{action_callfunction}}<strong>{{new_deliverypoint}}</strong> | <i>{{result_dialog_appears}}<strong>{{dialog_header_editdata}}</strong></i></li>
    </ol>      
</div>

<div id="container-2" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/deliverypoint_data-input.png"></div>
    <p>Alle gelb hinterlegten Felder sind Pflichtfelder und müssen ausgefüllt werden, die Daten in den anderen Felder kannst du später ergänzen. </p> 
    <p>Bist du mit den Eingaben fertig, klicke auf <strong>[Speichern]</strong>. <br><i>Die neue Lieferstelle erscheint in der Liste auf dieser Seite.</i></p>
    <hr>
    <h3>{{ struct_head_parameters }}</h3>

    <details>
      <summary>{{ deliverypoint_name }}</summary>
      <p>{{ deliverypoint_name_definition }}</p>
    </details>
    <details>
    <summary>{{ deliverypoint_marketlocation }}</summary>
    <p>{{ deliverypoint_marketlocation_definition }}<br>    
    </details>
    <details>
    <summary>{{ deliverypoint_adress }}</summary>
    <p>{{ deliverypoint_adress_definition }}</p>    
    </details>
    <details>
    <summary>{{ deliverypoint_resource }}</summary>
    <p>{{ deliverypoint_resource_definition }}</p>
    </details>
    

  <!-- Buttons für alle Termini
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
  -->

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
</div>


<div id="container-3" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/deliverypoint_assign_object.png"></div>
  <p>Nun teilst du der Lieferstelle mit, welche Objekte sie versorgt und wie hoch der Anteil des jeweiligen Objekts am Verbrauch über diese Lieferstelle ist.  
  Eine Lieferstelle kann mehrere Objekte versorgen. Jede Lieferstelle muss mindestens ein Objekt versorgen (ansonsten wäre die Lieferstelle sinnlos). </p>
  <p>So ordnest du der Lieferstelle ein Objekt zu:</p>
  <ol>
    <li>Im Datensatz der Lieferstelle: Klicke auf: <img src="../../../assets/images/symbol_edit.png"> <strong>neue Zuordnung</strong>. <br><i>{{result_dialog_appears}}<strong>{{dialog_header_editdata}}</strong></i></li>
    <li>Wähle das zu versorgende Objekt: <strong>{{ deliverypoint_assignment_object}}.</strong><br><i>Die Auswahl zeigt alle deine zuvor definierten Objekte. Durch Mausklick ordnest du das gewählte Objekt der Lieferstelle zu.</i></li>
    <li> Definiere den Anteil der Ressource den das Objekt aus der Lieferstelle bezieht. Gib den Wert als Faktor an (0 ... 1). <br><strong>An dieser Stelle berücksichtigst du den Anteil fremdgenutzter (vermieteter Gebäudeteile).</strong></li> 
    <li>Klicke auf <strong>[Speichern]</strong>. <br><i>Das gewählte Objekt ist mit der Lieferstelle verbunden.</i></li>
    <li>Versorgt die Lieferstelle weitere Objekte, wiederhole die Schritte 1 bis 4. Die Summe der Zuordnungsanteile darf nicht größer als 1 sein.</li>
  </ol>     
</div>

<div id="container-4" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/deliverypoint_edit.png"></div>
  <p>Mit diesen Möglichkeiten kannst du die Lieferstelle nachträglich bearbeiten:</p>
  <ol>
    <li>Benennung und Daten der Lieferstelle ändern.</li>
    <li>Die Zuordnung zum Objekt ändern (z. B. Wert des Zuordnungsanteils), ein anderes Objekt zuordnen oder die Zuordnung löschen.</li>
    <li>Der Lieferstelle ein weiteres Objekt zuordnen.
  </ol>
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
 

