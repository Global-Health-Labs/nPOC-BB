# Requirements - Traceability Matrix (RTM)

## Overview

The Requirements Traceability Matrix (**RTM**) for the [**nPOC-BB**](../index.md) (also, **sample preparation module**, or **SPM**) is excerpted from the RTM of a system designed to diagnose *Mycobacterium tuberculosis* (**MTb**) from a sample comprised of a human specimen collected from the dorsal area of the tongue by a swab (**sample collection consumable**, or **SCC**). The swab-collected specimen is transferred into a small (<2 mL) dropper tube (**sample prep tube**, or **STC**) filled with buffer and micro-scale glass beads. The nPOC-BB-prepared sample is then tested for the presence of MTb by a nucleic acid amplification test within a separate consumable on a separate instrument. Therefore, the nPOC-BB exists as a subcomponent of that diagnostic system, NAATOS, which was developed to the stage of an advanced prototype. As such, some of the User Needs and/or Product Requirements listed in this RTM:

1. Contain references to the "Product," which denotes the NAATOS diagnostic system, from within which the nPOC-BB was developed from a subcomponent into a standalone device.
2. Do not apply to the nPOC-BB subcomponent of the "Product" and therefore state "N/A" in an adjacent cell.
3. Need definition relative to the manufacture and regulatory approval of a medical device and therefore state "**TBD**" in the cell.

A tabular version of this RTM in the ```*.csv``` format can be downloaded from **REPLACE**.

## Requirements Traceability Matrix (RTM)

| User Needs | Product Requirements | Subsystem Requirements |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **01 Enable health care workers in primary health care to confirm the presence of pulmonary M. tuberculosis at the peripheral level during the same clinical encounter for effective linkage to patient care.** | **01 Time to result**. The Product must produce a result within 60 min (including sample prep time). | **001 [SPM] Time to result**. The SPM shall measure time continuously.|
| || **002 [SPM] Time to result**. When "system-run-heat" sub-state begins, the SPM shall ramp heating zone temperature up to a configurable temperature setpoint (default 95 °C) in under 2 min.|
| || **003 [SPM] Time to result**. While "system-run-hold" sub-state is active, the SPM shall maintain heating zone temperature for a configurable heating duration (default 4 mins).|
| || **004 [SPM] Time to result**. While "system-run-shake" sub-state is active, the SPM shall maintain tube holder shaking speed for a configurable shaking duration (default 2 mins).|
| **02 Availability** | **02 Component availability**. The Product must use components and raw materials that can be procured from more than one supplier. | **005 [SCC] Component availability**. The SCC shall use components and raw materials that can be procured from more than one supplier.|
| || **006 [SPM] Component availability**. The SPM shall use components and raw materials that can be procured from more than one supplier.|
| || **007 [STC] Component availability**. The STC shall use components and raw materials that can be procured from more than one supplier.|
| | **03 Demand**. The Product must package kit components in quantities sufficient to fulfill the demand of testing services in target settings.| **008 [SCC] Demand**. The SCC shall be provided one per test kit. |
| || **009 [STC] Demand**. The STC shall be provided one per test kit. |
| || **010 [SPM] Demand**. **TBD** |
| | **04 Manufacturability**. The Product must be manufactured at scale of 10 million tests per year.| **011 [SCC] Manufacturability**. The SCC shall be able to be manufactured at minimal volume of 10 million units per year. |
| || **012 [SPM] Manufacturability**. The SPM shall be able to be manufactured at minimal volume of 2000 units per year. |
| || **013 [STC] Manufacturability**. The STC shall be able to be manufactured at minimal volume of 10 million units per year. |
| | **05 Multi-disease platform**. The Product must be capable of supporting tests for other disease targets.|  **[SPM] Multi-disease platform**. **TBD**|
| **03 Compliance with local rules and regulations**| **06 Data system standard**. The Product must comply with ISO IEC 62304 Medical Device Data Systems standard on manufacturing of the assay and system. |  **[SPM] Data system standard**. **TBD**|
| | **07 Electrical safety**. The Product must comply with IEC 61010 and 61326 or higher standards or regulations on electrical equipment for laboratory use.| **014 [SPM] Electrical safety - electrical disconnect**. When the "power" switch is switched to off, the SPM shall electrically disconnect the battery. |
| || **015 [SPM] Electrical safety - IEC 61010-1**. The SPM shall comply with IEC 61010-1. |
| || **016 [SPM] Electrical safety - IEC 61010-2-101**. The SPM shall comply with IEC 61010-2-101. |
| || **017 [SPM] Electrical safety - IEC 61326-1**. The SPM shall comply with IEC 61326-1. |
| || **018 [SPM] Electrical safety - IEC 61326-2-6**. The SPM shall comply with IEC 61326-2-6. |
| | **08 Manufacturing facility certification**. The Product must be manufactured in a facility certified and authorized under ISO 13485 or certified under MDSAP. |  **[SPM] Manufacturing facility certification**. **TBD**|
| | **09 Regulatory**. The Product must comply with ISO EN 13485 or higher standards or regulations on manufacturing of assay and system.|  **[SPM] Regulatory**. **TBD**|
| **04 Affordability**| **10 Cost per test**. The Product must not exceed cost per test of $5 USD. (Price of individual test is cost of consumables only and amortized capital costs of any instrumentation; after scale-up; ex works [manufacturing costs only, excluding shipping].) | **019 [SCC] Cost per test**. The SCC shall cost less than $0.80 EXW at required scale.|
| || **020 [SPM] Cost per test**. The SPM shall cost less than $200 EXW at required scale. |
| || **021 [STC] Cost per test**. The STC shall cost less than $1.00 EXW at required scale.|
| **05 Durability under transport and storage** | **11 Storage stability**. The Product must not exceed required non-actionable rate after storage at 0 °C to 40 °C and at 15% to 90% RH for required shelf life in final packaging. | **022 [STC] Storage stability**. While in transport and storage, the STC shall be sealed with an air tight seal to inhibit leakage and evaporation. |
| | **12 Transport**. The Product must not exceed required non-actionable rate after transportation at 50 °C and 90% RH for 72 hours | **023 [SPM] Transport**. The SPM shall not be damaged during transport conditions of 50 °C and 90% RH for 72 hours. |
| || **024 [SPM] Transport**. The SPM shall comply with transportation regulations related to electronic devices containing batteries<br>or<br>The SPM shall be tested in accordance with the UN Manual of Tests and Criteria Part III, Subsection 38.3. |
| **06 Compatibility with health infrastructure** | **13 Mains power time**. The Product must require no more than 8 hours of mains power per day. | **025 [SPM] Mains power time**. The SPM shall take no longer than 6 hours to charge.|
| | **14 Power requirements**. The Product must not rely on mains power during test operation. | **026 [SPM] Power requirements**. The SPM shall detect USB plugged-in/unplugged state.|
| || **027 [SPM] Power requirements**. The SPM shall compensate for battery temperature during charge/discharge cycle. |
| || **028 [SPM] Power requirements**. The SPM shall measure battery state of charge (SoC).|
| || **029 [SPM] Power requirements**. While "stand-by" state is active, if battery SoC is below a configurable threshold, then the SPM shall transition to "battery-low" state. |
| || **030 [SPM] Power requirements**. The SPM shall have a battery. |
| || **031 [SPM] Power requirements**. The SPM shall detect USB charging on/off state. |
| | **15 Product workspace dimensions**. The Product must fit on a table within a space ≤ 60 cm deep, 90 cm wide, and 45 cm high.| **032 [SCC] Product workspace dimensions**. The SCC shall be no larger than 30 cm deep, 30 cm wide, and 45 cm high. |
| || **033 [SPM] Product workspace dimensions**. The SPM shall be no larger than 30 cm deep, 45 cm wide, and 45 cm high. |
| || **034 [STC] Product workspace dimensions**. The STC shall be no larger than 30 cm deep, 30 cm wide, and 45 cm high. |
| **07 Conformity with clinical workflows** | **16 Data display**. The Product must have a visual read out of the test result. |  N/A |
| | **17 Imaging-compatible read out**. The Product must present results compatible with imaging-based reader(s) [model(s) TBD] for electronic data recording. |  N/A |
| | **18 Patient identification**. The Product must include designated space to accurately record and display patient identifiers. | **035 [STC] Patient identification**. The STC include designated space to accurately record and display patient identifiers that is writeable with gel pen, ballpoint pen, or volatile solvent markers and proof or resistant to moisture and wiping. |
| || **036 [STC] Test identification**. The STC shall contain a label that minimally identifies the product name, part name, part number, and STC expiration date. |
| | **19 Post-opening stability**. The Product must have open package stability of at least 60 minutes in maximum required operating environment temperature and humidity. | **037 [SCC] Post-opening stability**. The SCC shall have open package stability of at least 60 minutes in maximum required operating environment temperature and humidity.|
| || **038 [STC] Post-opening stability**. The STC shall have open package stability of at least 60 minutes in maximum required operating environment temperature and humidity.|
| | **20 Random access**. The Product must offer random access capability to run parallel analyses of tests. |  **[SPM] Random access**. **TBD** |
| | **21 User interactions**. The Product must not require more than 3 user interactions after collecting the specimen and before recording the result.| **039 [SPM] User interactions**. The SPM shall have a "run" button. |
| || **040 [SPM] User interactions**. While "stand-by" state is active and the lid is closed and the board temperature is < 60 °C and sufficient battery power is available, when the "run" button is pressed, the SPM shall transition to "system-run" state. |
| || **041 [SPM] User interactions**. The SPM shall allow configuration of sensor threshold for lid open/close detection.|
| || **042 [SPM] User interactions**. The SPM shall detect lid open/close state. |
| || **043 [SPM] User interactions**. When "system-run-complete" sub-state begins, the SPM shall transition to "stand-by" state. |
| || **044 [SPM] User interactions**. While "system-run-shake" sub-state is active, when a configurable shaking duration elapses, the SPM shall transition to "run-complete" sub-state.|
| || **045 [SPM] User interactions**. While "system-run-shake" sub-state is active, the SPM shall maintain tube holder shake speed using a configurable motor speed (default 3925 RPM / 60 s/min = 65 Hz shake speed). |
| || **046 [SPM] User interactions**. While "system-run-shake" sub-state is active, the SPM shall shake tube holder with a minimum throw of 7 ± TBD mm.|
| || **047 [SPM] User interactions**. While "system-run-shake" sub-state is active, the SPM shall control the heating zone temperature to a configurable setpoint (default = 95 ºC). |
| || **048 [SPM] User interactions**. While "system-run-hold" sub-state is active, when the heating duration elapses, the SPM shall transition to "system-run-shake" sub-state.|
| || **049 [SPM] User interactions**. While "system-run-heat" sub-state is active, when the temperature setpoint - TBD °C is reached, the SPM shall transition to the "system-run-hold" sub-state. |
| || **050 [SPM] User interactions**. When "system-run" state begins, the SPM shall start in "system-run-heat" sub-state.|
| || **051 [SPM] User interactions - "power-off" state**. When the "power" switch is switched to off, the SPM shall transition to the "power-off" state. |
| || **052 [SPM] User interactions - power switch**. The SPM shall have a "power" switch.|
| | **22 Visual read out**. The Product must present results for visual read out and manual data recording.|  N/A |
| | **23 Waste disposal - infectious**. The Product must render infectious samples biosafe such that they can be disposed of as non-infectious waste when appropriate per local rules and regulations. | **053 [SCC] Waste disposal - infectious**. The SCC shall be single use. |
| || **054 [SPM] Waste disposal - infectious**. While "system-run-shake" sub-state is active, the SPM shall maintain sample temperature above 75 °C. |
| || **055 [STC] Waste disposal - infectious**. When processed in the SPM, the STC shall render infectious samples biosafe such that they can be disposed of as non-infectious waste when appropriate per local rules and regulations. |
| || **056 [SPM] Waste disposal - infectious**. While "system-run" state is active, if the lid is opened, then the SPM shall transition to "system-run-abort" sub-state. |
| || **057 [SPM] Waste disposal - infectious**. While "system-run" state is active and "system-run-heat" or "system-run-hold" or "system-run-shake" sub-state is active, when the "run" button is pressed, the SPM shall transition to "system-run-abort" sub-state. |
| || **058 [SPM] Waste disposal - infectious**. While "system-run" state is active, if heating zone exceeds a configurable max temperature, then the SPM shall transition to "system-run-abort" state. |
| **08 Scalability to support patient throughput**| **24 Daily throughput**. The Product must be able to support a daily throughput of 10-25 tests per 6-hour day. | **059 [SPM] Daily throughput**. While using battery power at room temperature, when "battery-full" state is indicated, the SPM shall run 24 tests before "battery-low" indication.|
| **09 Usability**| **25 Automate assay transfer**. The Product must automate assay transfer from amplification to detection.|  N/A |
| | **26 Indications**. The Product must visually communicate progress and completion of system processes. | **060 [SPM] Indications**. The SPM shall prevent access to configuration or logs while the device is in "system-run" state..|
| || **061 [SPM] Indications**. While "system-run" state is active, the SPM shall log events with UTC timestamps, including battery state, board temperature, heating zone temperature, and motor speed. |
| || **062 [SPM] Indications**. The SPM shall allow configurable notifications (defined in Table X) of states and sub-states via indicators. |
| || **063 [SPM] Indications**. While "power-off" state is not active, the SPM shall ad-hoc log events with UTC timestamps, including state start, state end, change in battery sufficient/insufficient charge state, and errors/alerts. |
| || **064 [SPM] Indications**. The SPM shall store a log file on non-volatile storage.. |
| || **065 [SPM] Indications**. The SPM shall allow configuration of event logging rate. |
| | **27 Language support**. The Product kit must include Instructions for Use (IFU) with in-country context and language and any language mandated by local regulatory or trade compliance requirements.| **066 [SCC] Language support**. The SCC shall be included in the Instructions for Use (IFU) with in-country context and language and any language mandated by local regulatory or trade compliance requirements.|
| || **067 [SPM] Language support**. The SPM shall be included in the Instructions for Use (IFU) with in-country context and language and any language mandated by local regulatory or trade compliance requirements.|
| || **068 [STC] Language support**. The STC shall be included in the Instructions for Use (IFU) with in-country context and language and any language mandated by local regulatory or trade compliance requirements.|
| | **28 Manual preparation of samples**. The Product must not require precise measuring of volume or time required for any step and should instead require number of drops or visual markers. | **069 [STC] Manual preparation of samples - filter cap**. The STC shall contain a filter of sufficient pore size to remove inert microbeads from solution when dispensing sample into TC. |
| || **070 [STC] Manual preparation of samples - squeezable tube**. The STC shall be made of squeezable material.|
| | **29 Packaging**. The Product must be packaged to ensure protection and maintain product integrity.| **071 [SCC] Packaging**. The SCC shall be individually packaged.|
| || **072 [SPM] Packaging**. While the SPM is being shipped, the battery shall be electrically disconnected.|
| | **30 Portability**. The Product must be a hand transportable product that weighs less than < 1 kg. | **073 [SPM] Portability**. The SPM shall weigh ≤ 0.6 kg.|
| | **31 Ready to use**. The Product must be ready to use without the need for additional components or accessories. | **074 [SCC] Ready to use - SCC non-inhibition**. The SCC shall not inhibit reactions in the STC or TC.|
| || **075 [SCC] Ready to use - SCC with STC**. The SCC shall have an integrated designated breakpoint within a distance from the end of the swab head that is less than the interior height of the STC. |
| || **076 [STC] Ready to use**. The STC shall contain a resealable, leak-proof dropper cap that is compatible with direct sample transfer from STC to TC without any ancillary tools, consumables, aides, or additional user steps. |
| || **077 [STC] Ready to use - free-standing**. The STC tube shall be free-standing on a flat surface and not require any type of rack or ancillary aid for proper function.|
| || **078 [STC] Ready to use - STC integrity**. When heated to an internal liquid temperature of 95 +/- 2 °C, the STC shall not melt, deform, or leach reaction inhibitors. |
| || **079 [STC] Ready to use - STC with TC**. The STC shall load sample into the TC at a mutually defined interface.|
| | **32 Reagent integration**. The Product must store all chemical and biological reagents required for completing all diagnostic steps of the assay must be integrated into single-use disposable(s), including reagents for amplification, lysis, detection, and internal controls. | **080 [STC] Reagent integration - bead-beating**. The STC shall contain inert microbeads to support bead-beating. |
| || **081 [STC] Reagent integration - buffer flow rate**. The STC shall contain an aqueous buffer that is capable of transport in porous materials at a flow rate within 50% of Tris buffer, pH 8.|
| || **082 [STC] Reagent integration - buffer lysis compatibility**. The STC shall contain an aqueous buffer that is compatible with bacterial cell lysis. |
| || **083 [STC] Reagent integration - buffer reaction compatibility**. The STC shall contain an aqueous buffer that does not inhibit reactions in the STC or TC.|
| || **084 [STC] Reagent integration - buffer rehydration compatibility**. The STC shall contain an aqueous buffer that is capable of rehydrating dried amplification reagents.|
| || **085 [STC] Reagent integration - buffer single use**. The STC shall contain a buffer fill volume sufficient for a single use only. |
| || **086 [STC] Reagent integration - buffer temperature compatibility**. The STC shall contain an aqueous buffer that is compatible with TC materials at temperatures ≤ 100 °C.|
| || **087 [STC] Reagent integration - buffer valve compatibility**. The STC shall contain an aqueous buffer that is compatible with any valves or valving materials contained within the test consumable at temperatures up to and including the max System temp..|
| | **33 Sample type**. The Product must support testing with a noninvasive tongue swab. | **088 [SCC] Sample type - access**. The SCC shall have a shaft at least 5 cm long.|
| || **089 [SCC] Sample type - bacteria**. The SCC shall be compatible with bacterial testing. |
| || **090 [SCC] Sample type - collection**. The SCC shall contain a regular, nylon-flocked head.|
| || **091 [SCC] Sample type - swab integrity**. While in the STC during processing by the SPM, the SCC shall retain structural integrity. |
| || **092 [SCC] Sample type - validation**. The SCC shall be validated as a diagnostic specimen wherein it collects a sample from the dorsal area of the human tongue.|
| || **093 [STC] Sample type**. The STC shall be of sufficient height to completely enclose the swab head when sealed. |
| | **34 Training and education**. The Product must be able to be operated by a user after reading IFU.| **094 [SPM] Training and education**. The SPM shall have graphics that indicate a method for opening the lid. |
| || **095 [SPM] Training and education**. The SPM shall have graphics that indicate the correct placement of the tube in the tube holder. |
| **10 Reliability**| **35 Calibration**. The Product must operate without the need for calibration during its intended lifespan.| **096 [SPM] Calibration**. The SPM shall measure motor speed. |
| || **097 [SPM] Calibration**. The SPM shall measure heating zone temperature.|
| || **098 [SPM] Calibration**. The SPM shall operate without the need for calibration during its required lifespan. |
| | **36 Maintenance**. The Product must operate without the need for maintenance during its intended lifespan.| **099 [SPM] Maintenance**. The SPM shall operate without the need for maintenance during its required lifespan. |
| **11 Confidence in test performance (tongue swab)** | **37 Amplification contamination**. The Product must prevent the escape of amplifiable material into the testing area. | **100 [STC] Sample pre safety**. While in use within the SPM, the STC shall remain sealed.|
| | **38 Analytical specificity (tongue swabs)**. The Product must achieve an analytical specificity ≥ 98%.|  N/A |
| | **39 Clinical sensitivity (tongue swabs)**. The Product must achieve a clinical sensitivity ≥ 80%. |  N/A |
| | **40 Clinical specificity (tongue swabs)**. The Product must achieve a clinical specificity ≥ 98%. |  N/A |
| **12 Confidence in test quality** | **41 Controls**. The Product must use controls to account for any processing errors (from sample to result)| **101 [STC] Controls - sample prep**. The STC shall use a control reagent to account for processing errors in sample preparation. |
| || **102 [STC] Controls - SPC**. The STC shall contain a sample processing control (SPC) that can report failure of sample processing, amplification, or detection steps.|
| | **42 Non-actionable indication**. The Product must indicate to users when a test result is non-actionable (indeterminant or invalid).| **103 [SPM] Non-actionable indication**. While "system-run-abort" sub-state is active, when a configurable abort duration elapses, the SPM shall transition to "system-standby" state.|
| || **104 [SPM] Non-actionable indication - max temp abort**. While "system-run" state is active, if the board temperature exceeds 60 °C, then the SPM shall transition to "system-run-abort" sub-state.|
| || **105 [SPM] Non-actionable indications - motor control abort**. While "system-run-shake" sub-state is active, if motor speed is not within TBD RPM of motor speed setpoint, then the SPM shall transition to "system-run-abort" sub-state.|
| || **106 [SPM] Non-actionable indications - temp control abort**. While "system-run-hold" sub-state is active, if heating zone is not within TBD °C of temperature setpoint, then the SPM shall transition to the "system-run-abort" sub-state.|
| | **43 Non-actionable rate**. The Product non-actionable (indeterminate + invalid) rate must not exceed 5%.|  N/A |
| | **44 Result validity window**. The Product must have a result validity window of 2 hours after test completion in which test signals allow one interpretation. |  N/A |
| | **45 Shock and vibration resistance**. The Product must withstand resistance to shocks and vibrations from drops by users of 90 cm TBR height without performance failures.| **107 [SPM] Shock and vibration resistance**. While "system-run-shake" state is active, and the SPM is suspended perpendicularly to the carriage direction, the SPM shall experience accelerations less than TBD m/s^2. |
| **13 Confidence in test safety**| **46 Burn safety**. The Product must not cause skin temperature above 60 °C after five seconds of contact to any surface.| **108 [SPM] Burn safety**. The SPM shall not have any areas accessible by a user's finger (defined as sphere of 1 cm diameter) with temperatures above 60 °C. |
| | **47 Sample prep safety**. The Product must reduce the risk of transmission of infectious agent of TB from potentially infectious sample to operator.| **109 [SCC] Sample prep safety**. The SCC shall be sterile packaged.|
| || **110 [SPM] Sample prep safety**. The SPM shall not melt the tube.|
| || **111 [SPM] Sample prep safety - STC interface**. The SPM shall fit a specified Tube (SPC) in a tube holder.|
| || **112 [SPM] Sample prep safety - STC shaking**. While "system-run-shake" sub-state is active, the SPM shall not allow the tube to lose its fit in the tube holder.|
| **14 Robustness to environmental conditions** | **48 Contaminate and dust protection**. The Product must be designed to effectively protect against dust and contaminants, ensuring its functionality and integrity. | **113 [SPM] Contaminate and dust protection**. The SPM shall comply with IEC 60529 at IP64 rating.|
| | **49 Operating humidity level**. The Product must operate within the humidity range of 70% to 90% non-condensing humidity without exceeding the required non-actionable rate.| **114 [SPM] Operating humidity level**. The SPM shall operate within the humidity range of 70% to 90% non-condensing humidity without exceeding the required non-actionable rate. |
| | **50 Operating temperature**. The Product must operate within a temperature range of +5 °C to +45 °C without exceeding the required non-actionable rate. | **115 [SPM] Operating temperature**. The SPM shall operate within a temperature range of +5 °C to +45 °C without exceeding the required non-actionable rate.|
| **15 Longevity**| **51 Cycle life**. The Product must have a cycle life of 12,000 tests. | **116 [SPM] Cycle life**. The SPM shall have a use life of 12,000 cycles. |
| | **52 Single-use consumable lifespan**. The Product must have a lifespan ≥18 months for any single-use consumables. | **117 [SCC] Single-use consumable lifespan**. The SCC shall have a packaged shelf life of at least 18 months from date of manufacture.|
| || **118 [STC] Single-use consumable lifespan**. The STC shall have a packaged stability of no less than 2 years when stored at the maximum environment temperature and humidity storage conditions. |
| **16 Environmental responsibility** | **53 Instrumentation lifespan**. The Product must have a lifespan ≥24 months for any instrumentation (no calibration or servicing).| **119 [SPM] Instrumentation lifespan**. The SPM shall have a shelf life of 2 y. |
| **17 Minimal instrumentation**|  N/A |  N/A |
