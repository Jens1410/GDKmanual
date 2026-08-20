

!!! tip "{{ term_submeter }}: {{ def_submeter }}"

    **Unterzähler in der technischen Infrastruktur**  
    {{ def_submeter_tech }}  

    **Unterzähler in der organisatorischen Struktur**  
    {{ def_submeter_org }}  

<!-- Buttons für die 4 Optionen -->
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
  <button onclick="toggleContainer('container-1', 'button-1')" class="toggle-button" id="button-1">1. {{ function_call }}</button>
  <button onclick="toggleContainer('container-2', 'button-2')" class="toggle-button" id="button-2">2. {{ data_input }}</button>
  <button onclick="toggleContainer('container-3', 'button-3')" class="toggle-button" id="button-3">3. {{ object_shares_definition }}</button>
  <button onclick="toggleContainer('container-4', 'button-4')" class="toggle-button" id="button-4">{{ optional }}{{ data_edit }}</button>
</div>

<!-- Container für die Inhalte (nur der erste ist sichtbar) -->
<div id="container-1" class="toggle-container" style="display: none;">
    <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/submeter_function_call.png"></div>
    <ol>
      <li>{{ action_openpage }}<strong>{{ men_item_meters }}</strong></li>
      <li>Wähle den Verbrauchssektor. <br>
      Für elektrische Heizungsanlagen mit eigener Zähleinrichtung wähle die Ressource <strong>{{ waerme }}</strong>. </li>
      <li>{{action_callfunction}}<strong>{{new_submeter}}</strong> | <i>{{result_dialog_appears}}<strong>{{dialog_header_editdata}}</strong></i></li>
    </ol>      
</div>

<div id="container-2" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/submeter_data-input.png"></div>
    <p>Alle gelb hinterlegten Felder sind Pflichtfelder und müssen ausgefüllt werden, die Daten in den anderen Felder kannst du später ergänzen. </p> 
    <p>Bist du mit den Eingaben fertig, klicke auf <strong>[Speichern]</strong>. <br><i>Der neue Zähler erscheint in der Liste auf dieser Seite.</i></p>
    <hr>
    <h3>{{ struct_head_parameters }}</h3>
    <p>{{ dialog_according_to_sector }}</p>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
      <button onclick="toggleContainer('strom-container', 'strom-button')" class="toggle-button active-button" id="strom-button">{{ strom }}</button>
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
<div id="strom-container" class="toggle-container" style="display: block;">
  <!-- <h3>{{ strom }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
    <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>  
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}            
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>
    {{ include_file("snippets/resources_strom.md") }}        
  </details>
   <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>      
    {{ include_file("snippets/units_strom.md") }}        
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="waerme-container" class="toggle-container" style="display: none;">
  <!--  <h3>{{ waerme }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>
    {{ include_file("snippets/resources_waerme.md") }}         
  </details>
   <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>  
    {{ include_file("snippets/units_waerme.md") }}             
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="wasser-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ wasser }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>
    {{ include_file("snippets/resources_wasser.md") }}          
  </details>
  <!-- <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>      
  </details> -->
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="regstrom_ertrag-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ regstrom_ertrag }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <!-- <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>      
  </details> -->
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>
    {{ include_file("snippets/units_regstrom-ertrag.md") }}               
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details> 
</div>

<div id="regwaerme_ertrag-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ regwaerme_ertrag }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>  
    {{ include_file("snippets/units_regwaerme-ertrag.md") }}    
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="verkehr-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ verkehr }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>
    {{ include_file("snippets/resources_wasser.md") }}       
  </details>
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>
    {{ include_file("snippets/units_verkehr.md") }}      
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="papier-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ papier }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p> 
    {{ include_file("snippets/resources_wasser.md") }}     
  </details>
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>
    {{ include_file("snippets/units_papier.md") }}      
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="abfall-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ abfall }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p> 
    {{ include_file("snippets/resources_abfall.md") }}      
  </details>
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>
    {{ include_file("snippets/units_papier.md") }}      
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>    
</div>

<div id="klima_komp-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ klima_komp }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <!-- <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>      
  </details> -->
  <details>
    <summary>{{ meter_emission }}</summary>
    <p>{{ meter_emission_definition }}</p>      
  </details>
  <!-- <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>      
  </details> -->
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>     
</div>

<div id="flaechen-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ flaechen }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p> 
    {{ include_file("snippets/resources_flaechen.md") }}           
  </details>
  <!--<details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>      
  </details> -->
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="lebensmittel-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ lebensmittel }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>
    {{ include_file("snippets/resources_lebensmittel.md") }}         
  </details>
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>
    {{ include_file("snippets/units_lebensmittel.md") }}      
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>
</div>

<div id="buerobedarf-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ buerobedarf }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p> 
    {{ include_file("snippets/resources_lebensmittel.md") }}   
  </details>
  <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>
    {{ include_file("snippets/units_lebensmittel.md") }}      
  </details>
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details> 
</div>

<div id="haushaltsbedarf-container" class="toggle-container" style="display: none;">
  <!-- <h3>{{ haushaltsbedarf }}</h3> -->
  <hr>
  <details>
    <summary>{{ meter_datasource }}</summary>
    <p>{{ meter_datasource_definition }}</p>      
  </details>
  <details>      
    <summary>{{ meter_activitystatus }}</summary>
    <p>{{ meter_activitystatus_definition }}</p>
    <p>{{ meter_activitystatus_usage }}</p>
  </details>
  <details>
    <summary>{{ submeter_meter_assignment }}</summary>
    <p>{{ submeter_meter_assignment_definition }}</p>      
  </details>
  <details>
    <summary>{{ meter_recordingmethod }}</summary>
    <p>{{ meter_recordingmethod_definition }}</p>          
    {{ include_file("snippets/meter_recordingmethod_types_table.md") }}
  </details>
  <details>
    <summary>{{ meter_resource }}</summary>
    <p>{{ meter_resource_definition }}</p>      
  </details>
  <!-- <details>
    <summary>{{ meter_unit }}</summary>
    <p>{{ meter_unit_definition }}</p>      
  </details> -->
  <details>
    <summary>{{ meter_position }}</summary>
    <p>{{ meter_position_definition }}</p>      
  </details>   
</div>
</div>


<div id="container-3" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/submeter_assign_object.png"></div>
  <p>Nun teilst du dem Unterzähler mit, für welche Objekte der Verbrauch erfasst wird und wie hoch der Anteil des jeweiligen Objekts am gemessenen Verbrauch.  
  Der Unterzähler kann für mehrere Objekte zuständig sein. Jedem Unterzähler muss mindestens ein Objekt zugeordnet sein (ansonsten wäre der Unterzähler sinnlos). </p>
  <p>So ordnest du dem Unterzähler ein Objekt zu:</p>
  <ol>
    <li>Im Datensatz des Unterzählers: Klicke auf: <img src="../../../assets/images/symbol_edit.png"> <strong>neue Zuordnung</strong>. <br><i>{{result_dialog_appears}}<strong>{{dialog_header_editdata}}</strong></i></li>
    <li>Wähle das zu versorgende Objekt: <strong>{{ deliverypoint_assignment_object}}.</strong><br><i>Die Auswahl zeigt alle deine zuvor definierten Objekte. Durch Mausklick ordnest du das gewählte Objekt dem Unterzähler zu.</i></li>
    <li> Definiere den Anteil der Ressource den das Objekt über den Unterzähler bezieht. Gib den Wert als Faktor an (0 ... 1). <br><strong>An dieser Stelle berücksichtigst du den Anteil fremdgenutzter (vermieteter Gebäudeteile).</strong></li> 
    <li>Klicke auf <strong>[Speichern]</strong>. <br><i>Das gewählte Objekt ist dem Unterzähler zugeordnet.</i></li>
    <li>Misst der Unterzähler den Verbrauch für weitere Objekte, wiederhole die Schritte 1 bis 4. Die Summe der Zuordnungsanteile darf nicht größer als 1 sein.</li>
  </ol>     
</div>

<div id="container-4" class="toggle-container" style="display: none;">
  <div style="margin: 16px 0; text-align: center;"><img src="../../../assets/images/submeter_data-edit.png"></div>
  <p>Mit diesen Möglichkeiten kannst du den gesamten Komplex aus Lieferstelle/Zähler/Unterzähler nachträglich bearbeiten:</p>
  <ol>
    <li>Benennung und Daten der Lieferstelle ändern.</li>
    <li>Die Objektzuordnung der Lieferstelle ändern (z. B. Wert des Zuordnungsanteils), ein anderes Objekt zuordnen oder die Zuordnung löschen.</li>
    <li>Der Lieferstelle ein weiteres Objekt zuordnen.</li>
    <li>Benennung und Daten des übergeordneten Zählers ändern.</li>
    <li>Benennung und Daten des Unterzählers ändern.</li>
    <li>Die des Objektzuordnung des Unterzählers ändern (z. B. Wert des Zuordnungsanteils), ein anderes Objekt zuordnen oder die Zuordnung löschen.</li>
    <li>Dem Unterzähler ein weiteres Objekt zuordnen.</li>
  </ol>     
</div>










<script>
  function toggleContainer(containerId, buttonId) {
    // Prüfe, ob es sich um einen der ersten vier Container handelt
    const isFirstGroup = ['container-1', 'container-2', 'container-3', 'container-4'].includes(containerId);

    if (isFirstGroup) {
      // Alle Container der ersten Gruppe ausblenden
      document.querySelectorAll('.toggle-container').forEach(container => {
        if (container.id.startsWith('container-')) {
          container.style.display = 'none';
        }
      });

      // Alle Buttons der ersten Gruppe zurücksetzen
      document.querySelectorAll('.toggle-button').forEach(button => {
        if (button.id.startsWith('button-')) {
          button.classList.remove('active-button');
        }
      });
    } else {
      // Für die zweite Gruppe: Alle Container der zweiten Gruppe ausblenden
      const secondGroupContainers = [
        'strom-container', 'waerme-container', 'wasser-container',
        'regstrom_ertrag-container', 'regwaerme_ertrag-container',
        'verkehr-container', 'papier-container', 'abfall-container',
        'klima_komp-container', 'flaechen-container', 'lebensmittel-container',
        'buerobedarf-container', 'haushaltsbedarf-container'
      ];

      secondGroupContainers.forEach(id => {
        const container = document.getElementById(id);
        if (container) {
          container.style.display = 'none';
        }
      });

      // Alle Buttons der zweiten Gruppe zurücksetzen
      const secondGroupButtons = [
        'strom-button', 'waerme-button', 'wasser-button',
        'regstrom_ertrag-button', 'regwaerme_ertrag-button',
        'verkehr-button', 'papier-button', 'abfall-button',
        'klima_komp-button', 'flaechen-button', 'lebensmittel-button',
        'buerobedarf-button', 'haushaltsbedarf-button'
      ];

      secondGroupButtons.forEach(id => {
        const button = document.getElementById(id);
        if (button) {
          button.classList.remove('active-button');
        }
      });
    }

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





