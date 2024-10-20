# Spearmint @ DO lab

> *"Making measurements cool."*

*This is based on [MeasureIt](https://github.com/nanophys/MeasureIt) which itself is based on the [QCoDeS Standard](https://github.com/microsoft/qcodes).*

The goal of this is to effortlessly & automatically control many instruments simultaneously all in the form of an easy-to-use GUI. Consistent and efficient control is key! The intended use case of this application is to do low temperature measurements (hence the name), but realistically this can be adapted to control all sorts of instruments!

## TODO (Updated 10/20/2024)

All plans and details about the development of the application can be found in Issues. A rough (unordered) outline of the project can be found here, though:

- [ ] Implement Dual Gate measurements to the GUI
    - [x] Migrate the central pane of the main UI to a "tabbed" setup. Each measurement/instrument category is assigned its own tab. Sequential and simultaneous control will be handled with the sweep queue.
    - [x] GUI fields for 2D  sweep (dual gate) measurements.
    - [ ] Implement necessary functions for "controls" pane of 2D sweep
    - [ ] Implement the ability to send the 2D sweep to the sweep queue.
- [ ] Implement Lakeshore 336
    - [x] Driver loads and can connect to instument
    - [ ] Automatically attempt to set up a monitor of the device when it is connected
    - [ ] Continuously plot temperature
    - [ ] Setpoints can be sent to the instrument
- [ ] Implement Cryomagnetics TM620
- [ ] Implement Model 4G Superconducting Magnet  
- [ ] Create a new requirements.txt file for ease of installation.
- [ ] Remove dependency on unmaintained local drivers wherever possible.
- [ ] Implement features for controlling lock in amplifiers and temperature controllers.
- [ ] Log detected devices on application startup.
- [ ] CSV/XML support for data collection.
