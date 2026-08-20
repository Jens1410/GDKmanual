## resources

<details>
    <summary>{{ meter_resource }}: {{ strom }}</summary>
    <p>{{ resource_electrical_eco_current }}  </p>    
    <p>{{ resource_electrical_chp_ownconsumption }}  </p>    
    <p>{{ resource_electrical_pv_ownconsumption }}  </p>    
    <p>{{ resource_electrical_current }}  </p>    
    {{ include_file("snippets/resources_strom.md") }}    
</details>

<details>
<summary>{{ meter_resource }}: {{ waerme }}</summary>
    <p>{{ resource_heat_nlg }}  </p>
    <p>{{ resource_heat_nlg_10bio }}  </p>
    <p>{{ resource_heat_nlg_20bio }}  </p>
    <p>{{ resource_heat_distheat }}  </p>
    <p>{{ resource_heat_nlg_lpg }}  </p>
    <p>{{ resource_heat_heatingoil }}  </p>
    <p>{{ resource_heat_woodchips }}  </p>
    <p>{{ resource_heat_woodpellets }}  </p>
    <p>{{ resource_heat_locheat }}  </p>
    <p>{{ resource_heat_locheat_biogas }} </p> 
    <p>{{ resource_heat_electrical_ecocurrent }}  </p>
    <p>{{ resource_heat_electrical_current }}  </p>
    <p>{{ resource_heat_hotwater }} </p>
    {{ include_file("snippets/resources_waerme.md") }} </p>
</details>


<details>
<summary>{{ meter_resource }}: {{ wasser }}</summary>
    {{ resource_water_pwc }}  
    {{ resource_water_pwh }}
    {{ include_file("snippets/resources_wasser.md") }}  
</details>

<details>
<summary>{{ meter_resource }}: {{ regstrom_ertrag }}</summary>
    keine Auswahl   Solarstrom
</details>

<details>
<summary>{{ meter_resource }}: {{ regwaerme_ertrag }}</summary>
    keine Auswahl    Solarwärme
</details>

<details>
<summary>{{ meter_resource }}: {{ verkehr }}</summary>
    {{ resource_traffic_train }}  
    {{ resource_traffic_ebike }}  
    {{ resource_traffic_bike }}  
    {{ resource_traffic_plane_abroad }}  
    {{ resource_traffic_plane_domestic }}  
    {{ resource_traffic_van }}  
    {{ resource_traffic_publictransportation }}  
    {{ resource_traffic_car_general }}  
    {{ resource_traffic_car_benzin_large }}  
    {{ resource_traffic_car_benzin_small }}  
    {{ resource_traffic_car_benzin_medium }}  
    {{ resource_traffic_car_diesel_large }}  
    {{ resource_traffic_car_diesel_samll }}  
    {{ resource_traffic_car_diesel_medium }}  
    {{ resource_traffic_car_electrical }}  
    {{ resource_traffic_car_nlg }}  
    {{ resource_traffic_coach }}
    {{ include_file("snippets/resources_verkehr.md") }}   
</details>

<details>
<summary>{{ meter_resource }}: {{ papier }}</summary>
    {{ resource_paper_fresh }}  
    {{ resource_paper_recycl }}  
    {{ resource_paper_cartonage }}  
    {{ include_file("snippets/resources_papier.md") }} 
</details>

<details>
<summary>{{ meter_resource }}: {{ abfall }}</summary>
    {{ resource_garbage_bio }}  
    {{ resource_garbage_hazard }}  
    {{ resource_garbage_paper }}  
    {{ resource_garbage_generalwaste }}  
    {{ resource_garbage_packagingwaste }}  
    {{ include_file("snippets/resources_abfall.md") }}  
</details>

<details>
<summary>{{ meter_resource }}: {{ klima_komp }}</summary>
    keine Auswahl
</details>

<details>
<summary>{{ meter_resource }}: {{ flaechen }}</summary>
    {{ resource_area_green }}  
    {{ resource_area_natural_awayfromsite }}  
    {{ resource_area_natural_atsite }}  
    {{ resource_area_partiallypermeable }}  
    {{ resource_area_builtup }}  
    {{ resource_area_sealed }}  
    {{ include_file("snippets/resources_flaechen.md") }}  
</details>

<details>    
<summary>{{ meter_resource }}: {{ lebensmittel }}</summary>
    {{ resource_food_beverage_nonalc_conv }}  
    {{ resource_food_beverage_nonalc_eco }}  
    {{ resource_food_beverage_alc_conv }}  
    {{ resource_food_beverage_alc_eco }}  
    {{ resource_food_bread_conv }}  
    {{ resource_food_bread_eco }}  
    {{ resource_food_eggs_conv }}  
    {{ resource_food_eggs_eco }}  
    {{ resource_food_fish_conv }}  
    {{ resource_food_fish_eco }}  
    {{ resource_food_meat_conv }}  
    {{ resource_food_meat_eco }}  
    {{ resource_food_coffee_conv }}  
    {{ resource_food_coffe_eco }}  
    {{ resource_food_milk_conv }}  
    {{ resource_food_milk_eco }}  
    {{ resource_food_fruits_conv }}  
    {{ resource_food_fuits_eco }}  
    {{ resource_food_diverse_conv }}  
    {{ resource_food_diverse_eco }}
    {{ include_file("snippets/resources_lebensmittel.md") }}  
</details>

<details>
<summary>{{ meter_resource }}: {{ buerobedarf }}</summary>
    {{ resource_paper_fresh }}  
    {{ resource_paper_recycl }}    
    {{ include_file("snippets/resources_buerobedarf.md") }}    
</details>

<details>
<summary>{{ meter_resource }}: {{ haushaltsbedarf }}</summary>
    keine Auswahl  
</details>