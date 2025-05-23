# Design Changes

## Prototype Version Comparison

The following table provides an overview of design differences between the nPOC-BB Alpha and Beta/Gamma prototypes developed at GHL.

!!! note
    The GHL Beta and Gamma prototypes have the same mechanical design but different main printed circuit boards (PCBs), which are denoted RevB and RevC, respectively, by GHL. The RevC PCB redesign primarily address flaws in the main board that can cause units to fail randomly. Changes to the main PCB are described further below.

<table>
  <tbody>
    <tr>
      <th>Component</th>
      <th>Alpha prototype</th>
      <th>Beta/Gamma prototype</th>
    </tr>
    <tr>
      <td>Design Elements</td>
      <td>
        <ul>
            <li>Single tube operation/cycle</li>
            <li>Hinged lid with view window</li>
            <li>Daughter heater board with aluminum heat block</li>
            <li>Scotch-yoke carriage system with brushless motor</li>
            <li>Battery operated (rechargeable Li-ion battery)</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Upgraded Scotch-yoke carriage with better wear characteristics and insulation</li>
            <li>Upgraded motor and bearing</li>
            <li>Clip-in tube retainer</li>
            <li>Taller heat block</li>
            <li>Upgraded flex cable</li>
            <li>Upgraded power management on main PCBA</li>
            <li>More and larger Li-ion batteries</li>
            <li>Physical battery disconnect (kill) switch</li>
            <li>Battery door</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Size</td>
      <td>
        <ul>
            <li>5" × 2.9" × 4.2"</li>
            <li>1.2 kg</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>7.6" × 3.6" × 4.4"</li>
            <li>2.5 kg</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Throughput</td>
      <td>
        <ul>
            <li>1 tube/cycle</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>1 tube/cycle</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Tube Compatibility</td>
      <td>
        <ul>
            <li>NAATOS PE dropper tube</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>NAATOS PE dropper tube</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Mechanical Actuation</td>
      <td>
        <ul>
            <li>Brushless motor and scotch yoke</li>
            <li>Motor: 3625BL-24 (24 V, 3.2 W, 4400 rpm motor)</li>
            <li>Bearing: 57155K346 (60/20 lb dynamic/static)</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Brushless motor and scotch yoke</li>
            <li>Motor: Higher power DIX36B (24 V, 7 W, 5200 rpm)</li>
            <li>Bearing: Higher radial load capacity 57155k374 (290/100 lb dynamic/static)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Carriage & Rails</td>
      <td>
        <ul>
            <li>Carriage housing with small air gap</li>
            <li>No tube retainer feature (added strike plate on lid window)</li>
            <li>Smaller debris shield</li>
            <li>Nickel plated stainless steel rails</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Enlarged carriage housing with air gap for better insulation</li>
            <li>Clip-in tube retainer feature to maintain tube-heat block contact</li>
            <li>Debris shield </li>
            <li>Delrin or stainless steel (17-4 Ph) rails</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Amplitude & Frequency</td>
      <td>
        <ul>
            <li>7 mm</li>
            <li>65 Hz</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>7 mm</li>
            <li>65 Hz</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Heat Block</td>
      <td>
        <ul>
            <li>Aluminum</li>
            <li>Shorter heat block (19.37 mm)</li>
            <li>Bottom is opened to force convection</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Aluminum</li>
            <li>Taller heat block (30.67 mm) for better sample coverage</li>
            <li>Bottom enclosed by heater to reduce heat loss</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Heater</td>
      <td>
        <ul>
            <li>Single PCB heater with integral traces with attached aluminum heat block</li>
            <li>Trace resistance = 2.1 Ω through electromagnetic modeling</li>
            <li>Temperature sensor: TE Connectivity G-NICO-018 integrated on the opposite side of heater</li>
            <li>Opened center cutout</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Single PCB heater with attached aluminum heat block</li>
            <li>Trace resistance = 2.7 Ω measured on the board</li>
            <li>PWM’d with a 6V supply</li>
            <li>Temperature sensor: TE Connectivity G-NICO-018 integrated on the opposite side of heater</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Heater Connector</td>
      <td>
        <ul>
           <li>20-pin FFC connector</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>40-pin FFC connector (for decreased series power loss)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Battery / Power</td>
      <td>
        <ul>
            <li>4× 18650 Li-ion batteries in parallel</li>
            <li>Off-the-shelf battery holder with wire leads, modified for batteries to operate in parallel</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>6× 21700 Li-ion batteries in 2s3p configuration</li>
            <li>Custom battery holder with thick gauge wires (10 ga) to reduce voltage drop</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Firmware</td>
      <td>
        <ul>
            <li>Code version: V1.6 (branch: ```power-module-V1.6```)</li>
            <li></li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Code version: V3.1 (tag: ```V3.1_and_odic_splitpoint```)</li>
            <li>Refactored (compare to alpha firmware) to be used for both PM and SPM</li>
            <li>User customizable process cycle (temperature and motor speed control)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Power Management</td>
      <td>
        <ul>
            <li>Heaters ran from unregulated battery voltage with series-inductor losses, due to design problems with the 5V boost converter (which was kept switched off)</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Heater boost power supply and motor power supply working well. However, there is a design flaw which exposed MCU pins connected to the motor to higher than Nordic absolute maximums when the motor power supply was shutdown. A hardware and software rework was put into place as a mitigation.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>File System</td>
      <td>
        <ul>
            <li>SD card</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>On-board solid state memory</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Developer Features</td>
      <td>
        <ul>
            <li>Data logging</li>
            <li>Mass storage mode for file access</li>
            <li>Status and battery indications</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Physical battery disconnect (kill) switch</li>
            <li>File system reset on device</li>
            <li>Serial communication, including data streaming</li>
            <li>Automatic run modes</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Main PCB Changes

### Beta RevB PCB → Gamma RevC PCB

### Alpha RevA PCB → Beta RevB PCB

A complete list of main PCB schematic changes made when moving from Alpha prototype RevA PCB to Beta prototype RevB PCB:

<table>
  <tbody>
    <tr>
      <th>Component</th>
      <th>Changes</th>
    </tr>
    <tr>
      <td>Heater</td>
      <td>
        <ul>
          <li>Redesigned heater supply: changed from a boost supply to a buck supply (U1. 2V5, 6 A output).</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Storage</td>
      <td>
        <ul>
          <li>Added 1 Gb NOR flash interfaced to the MCU over QSPI. Retained the microSD card holder and interface.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Battery + Charger</td>
      <td>
        <ul>
            <li>Removed caps on the VSYS rail of the battery charger (an unused output). Still meet the nominal 6 µF of cap on the rail specified by TI.</li>
            <li>Connections that were previously to GND on the fuel gauge are now to GND_SNS_N, which more closely follows the manufacturer’s recommended wiring.</li>
            <li>Switched the fuel gauge from I2C0 to I2C1.</li>
            <li>Replaced J3 and J6 (battery) with new Molex MicroFit connector.</li>
            <li>Added low-side switch that will cut off connection to battery pack when pushbutton is pressed (SW2).</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>MCU</td>
      <td>
        <ul>
            <li>Added 10 µF and 10 µF bypass caps to the MCU supply rail to augment single 4.7 µF cap inside module.</li>
            <li>Added a 0 Ω resistor inline with the nRF module’s VCC pin to enable current consumption measurements. 0603 package. Rated for 1 A.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Motor</td>
      <td>
        <ul>
            <li>Named all nets on the motor supply IC.</li>
            <li>Changed motor supply output to 19.75 V, down from 24 V.</li>
            <li>Changed J1 (motor) to a ×6 JST connector. Added a line for the brake. Pulled this line high to disable brake mode.</li>
            <li>Added 3× 68 µF tantalum caps to the MOTOR_VCC line.</li>
            <li>Added Q4 to sever the motor’s GND connection. This eliminates quiescent current into the motor when not in use.</li>
            <li>Added pulldown on MOTOR_POWER_EN.</li>
            <li>Changed pinout on J1 (motor connector) to be the reverse of the pinout on the motor itself. This allows wires connecting the two to run directly from the board to the motor without crossing or twisting around each other</li>
            <li>Changed motor speed output to an open drain signal by pulling to 3.3V. Removed resistor divider used previously.</li>        </ul>
      </td>
    </tr>
    <tr>
      <td>USB</td>
      <td>
        <ul>
            <li>Added USB detect line to MCU. Removed USB comparator circuit.</li>
            <li>Added load switch to switch power to the USB PD controller. Pulled enable high and wired to MCU.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Peripherals</td>
      <td>
        <ul>
            <li>Put the LED driver on the 3V3_SW net. Added a pulldown to the LED driver enable line.</li>
            <li>Switched the RTC from I2C0 to I2C1.</li>
            <li>Changed component used for Hall effect sensor: changed from a digital output to an analog output. Wired this output through an RC filter to an ADC capable pin on the nRF.</li>
            <li>Changed U3 (RTC) supply to be 3V3, removed D1 and R11 which previously connected it to VBAT.</li>
            <li>Added a stuffing resistor on U3 (RTC) 32kHz output and output enable pins.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Test Points</td>
      <td>
        <ul>
            <li>Added test point for SCL and SDA on I2C0 and I2C1 busses.</li>
            <li>Added test point for Hall sensor output.</li>
            <li>Added test point for motor speed output.</li>
            <li>Added test point for motor supply voltage.</li>
            <li>Added test point for heater PWM control.</li>
            <li>Added test point for heater supply voltage.</li>
            <li>Added test point for motor PWM speed control.</li>
            <li>Added test point for VBAT.</li>
            <li>Added test point for 3V3.</li>
            <li>Added test point for 3V3_SW.</li>
            <li>Added test point for 3V3_PD.</li>
            <li>Added test point for 5V.</li>
            <li>Added test point for 5V_SW.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
