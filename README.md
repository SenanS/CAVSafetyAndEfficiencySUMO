# CAV Safety And Efficiency SUMO

The code used to generate and evaluate SUMO scenarios for measuring the safety and efficiency of low penetration rates of connected autonomous vehicles.


## Running Single Simulation 
A single simulation can be run by navigating to `DublinSimulation/DublinCity/run.bat` or `NorthDublinSimulation/NorthDublinSection/run.bat`.
This will launch the larger or smaller simulation environment, given the [SUMO Simulator](https://sumo.dlr.de/docs/index.html) is installed.

The simulations consist of sections of Dublin city built from OpenStreetMaps data.
The simulation environments can be seen below:

### NorthDublinSection
![bigViewNorth](https://user-images.githubusercontent.com/30498489/118026956-52f23b80-b359-11eb-84fd-e4089f5fbd45.png)

### DublinCity
![DUBLIN](https://user-images.githubusercontent.com/30498489/118026948-51c10e80-b359-11eb-87d9-41d81fd64f34.PNG)


## Running Multiple Simulations
Using the code found in the `runSimulations.bat` file, a user can configure a suite of simulations to run.
Specifically a user can choose the amount of simulation instances and the penetration rates of Connected Autonomous Vehicles (CAVs).
Though, this code could be altered to vary any factor within the SUMO environment, with the augmentation of the `change_simulation_config.py` Python script.

In the `change_simulation_config.py` python script, a user can configure changes to the SUMO simulation environment, which can be run before each new simulation. 
This allows for automation in running many different simulations, each saved to their own output directory.
