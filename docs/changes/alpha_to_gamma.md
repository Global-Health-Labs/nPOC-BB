# Alpha to Gamma Design Updates

## Prototype Version Comparison

The following table provides an overview of design differences between the nPOC-BB (Alpha) and (Gamma) prototypes developed at GHL.

!!! note
    The nPOC-BB (Beta) prototype has a nearly identical mechanical design to the nPOC-BB (Gamma) prototype, but the nPOC-BB (Beta) prototype has serious flaws in its electrical design, which are addressed by the nPOC-BB (Gamma) prototype and the v3.5 firmware. Therefore, the table below addresses the overall changes that exist between the nPOC-BB (Alpha) prototype and the nPOC-BB (Gamma) prototype, skipping over the nPOC-BB (Beta) prototype.

{{ read_csv("docs/tables/nPOC-BB_version-compare.csv") }}

## Main PCB Changes

### Beta RevB PCB → Gamma RevC PCB

### Alpha RevA PCB → Beta RevB PCB

A complete list of main PCB schematic changes made when moving from nPOC-BB (Alpha) prototype RevA PCB to nPOC-BB (Beta) prototype RevB PCB:

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
