# Gamma version (2025Q1)

## Bill of Materials

### Consumables / Reagents

The consumables / reagents BOM table ([.csv](../tables/nPOC-BB_gamma_consumables-reagents.csv)) lists the components and assemblies used as part of the sample preparation workflow for the nPOC-BB.

{{ read_csv("docs/tables/nPOC-BB_gamma_consumables-reagents.csv", na_filter = False) }}

### Mechanicals

The mechanicals BOM table ([.csv](../tables/nPOC-BB_gamma_mechanicals.csv)) lists the components and assemblies used in the construction of the nPOC-BB.

{{ read_csv("docs/tables/nPOC-BB_gamma_mechanicals.csv", na_filter = False) }}

### Electronics

The main PCBA BOM table ([.csv](../tables/nPOC-BB_gamma_main_PCBA_BOM.csv)) lists the components used to populate the main PCBA of the nPOC-BB.

{{ read_csv("docs/tables/nPOC-BB_gamma_main_PCBA_BOM.csv", na_filter = False) }}

The heater PCBA BOM table ([.csv](../tables/nPOC-BB_gamma_heater_PCBA_BOM.csv)) lists the components used to populate the heater PCBA of the nPOC-BB.

{{ read_csv("docs/tables/nPOC-BB_gamma_heater_PCBA_BOM.csv", na_filter = False) }}

## Formulations

### Sample Prep Buffer

#### Formulation

20mM Tris-HCl, 0.1% (v/v) ProClin, pH 8.8

Batch Size: 1 L

{{ read_csv("docs/tables/nPOC-BB_gamma_formulation.csv", na_filter = False) }}

#### Method

1. Add 900 mL of water to a clean formulation flask with a magnetic stir bar
2. Add 10 mL of 2 M Tris-HCl, pH 8.8
3. Add 1 mL ProClin 300
4. Stir solution for 2 min to ensure proper mixing
5. Check pH with a pH meter. The acceptable pH range is: 8.8 +/- 0.1 (8.70 – 8.90)
6. If the pH is outside the acceptable range adjust with 1 M NaOH or 1 M HCl as needed.
7. Once pH of solution is within the acceptable range, QS to 1 L with water and sterile filter with a 0.2 µm filter unit.
8. Store in sterile filter unit bottle, refrigerated until use.

*Stability for this reagent has not been established.*

## Hardware

### CAD

- SolidWorks Parts, Assemblies, and Drawings
    - [/hw/gamma/CAD/solidworks/](https://github.com/Global-Health-Labs/nPOC-BB/tree/main/hw/gamma/CAD/solidworks){:target="_blank"}
- Top-Level Assembly
    - [/hw/gamma/CAD/solidworks/GHL-1-22000.SLDASM](https://github.com/Global-Health-Labs/nPOC-BB/blob/main/hw/gamma/CAD/solidworks/GHL-1-22000.SLDASM){:target="_blank"}
    - [/hw/gamma/CAD/derived/GHL-1-22000.x_t](https://github.com/Global-Health-Labs/nPOC-BB/blob/main/hw/gamma/CAD/derived/GHL-1-22000.x_t){:target="_blank"} (Parasolid)
- Drawings
    - [/hw/gamma/CAD/derived/drawings/](https://github.com/Global-Health-Labs/nPOC-BB/tree/main/hw/gamma/CAD/derived/drawings){:target="_blank"}

### eCAD

- Main PCBA
    - [/hw/gamma/ECAD/main-board/](https://github.com/Global-Health-Labs/nPOC-BB/tree/main/hw/gamma/ECAD/main-board){:target="_blank"}
- Heater PCBA
    - [/hw/gamma/ECAD/heater-board/](https://github.com/Global-Health-Labs/nPOC-BB/tree/main/hw/gamma/ECAD/heater-board){:target="_blank"}

## Firmware

- Version 1.0–3.5
    - [NAATOS-V1-Modules-FW](https://github.com/Global-Health-Labs/NAATOS-V1-Modules-FW){:target="_blank"}
