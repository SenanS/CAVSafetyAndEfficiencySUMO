# CAV Safety And Efficiency SUMO

The code used to generate and evaluate SUMO scenarios for measuring the safety and efficiency of low penetration rates of connected autonomous vehicles.


## Running Single Simulation 
A single simulation can be run by navigating to `DublinSimulation/DublinCity/run.bat` or `NorthDublinSimulation/NorthDublinSection/run.bat`.
This will launch the larger or smaller simulation environment, given the [SUMO Simulator](https://sumo.dlr.de/docs/index.html) is installed.

The simulations consist of sections of Dublin city built from OpenStreetMaps data, useful resources to accomplish this are [Using OSMWebWizard](https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html) and [Data Cleaning with JOSM](https://toolbox.hotosm.org/pages/data-cleaning-upload-and-quality-assurance/5.1-data-cleaning-with-josm/).

The two simulation environments can be seen below:

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

## Results Visualisation
Using the `plot_tripinfo_distributions.py` script, or any others available in the SUMO visualisation documentation, a user can plot the TripInfo results as compaitive distribution between simulation scenarios, instructions can be found in the [SUMO visualisation documentation](https://sumo.dlr.de/docs/Tools/Visualization.html#plot_tripinfo_distributionspy).

![tripinfo_distribution_wait](https://user-images.githubusercontent.com/30498489/118028937-8f269b80-b35b-11eb-98f7-4768ee83e2ea.png)

The command used to generate the Figure above is as follows.
`python plot_tripinfo_distributions.py -i tripinfo0.xml,tripinfo1.xml,tripinfo2.xml,tripinfo3.xml,tripinfo4.xml,tripinfo5.xml,tripinfo6.xml,tripinfo7.xml,tripinfo8.xml,tripinfo9.xml,tripinfo10.xml,tripinfo11.xml,tripinfo12.xml,tripinfo13.xml,tripinfo14.xml,tripinfo15.xml -o tripinfo_distribution_wait.png -l CAV2-0.0%__CAV4-0.0%__HDV-100%,CAV2-0.5%__CAV4-0.5%__HDV-99%,CAV2-1.0%__CAV4-1.0%__HDV-98%,CAV2-1.5%__CAV4-1.5%__HDV-97%,CAV2-2.0%__CAV4-2.0%__HDV-96%,CAV2-2.5%__CAV4-2.5%__HDV-95%,CAV2-3.0%__CAV4-3.0%__HDV-94%,CAV2-3.5%__CAV4-3.5%__HDV-93%,CAV2-4.0%__CAV4-4.0%__HDV-92%,CAV2-4.5%__CAV4-4.5%__HDV-91%,CAV2-5.0%__CAV4-5.0%__HDV-90%,CAV2-5.5%__CAV4-5.5%__HDV-89%,CAV2-6.0%__CAV4-6.0%__HDV-88%,CAV2-6.5%__CAV4-6.5%__HDV-87%,CAV2-7.0%__CAV4-7.0%__HDV-86%,CAV2-7.5%__CAV4-7.5%__HDV-85% -v -m waitingTime --minV 0 --maxV 1000 --bins 10 --xticks 0,1000,100,16 --xlabel "Wait Time [s]" --ylabel "Number of Commuters[#]"  --title "Time Spent Waiting in Traffic"  --yticks 16 --xlabelsize 16 --ylabelsize 16 --titlesize 30 
![image](https://user-images.githubusercontent.com/30498489/118029222-de6ccc00-b35b-11eb-8a79-9b8e90767bef.png)
`

Broken into constituent parts it makes more sense.
An important aspect is that there is no unintentional whitespace in the command.

* The python visualisation tool call 
  * `python plot_tripinfo_distributions.py`
* The input files to read
  * `-i tripinfo0.xml,tripinfo1.xml,tripinfo2.xml,tripinfo3.xml,tripinfo4.xml,tripinfo5.xml,tripinfo6.xml,tripinfo7.xml,tripinfo8.xml,tripinfo9.xml,tripinfo10.xml,tripinfo11.xml,tripinfo12.xml,tripinfo13.xml,tripinfo14.xml,tripinfo15.xml`
* The output file location
  * `-o tripinfo_distribution_wait.png`
* The graph legend
  * `-l CAV2-0.0%__CAV4-0.0%__HDV-100%,CAV2-0.5%__CAV4-0.5%__HDV-99%,CAV2-1.0%__CAV4-1.0%__HDV-98%,CAV2-1.5%__CAV4-1.5%__HDV-97%,CAV2-2.0%__CAV4-2.0%__HDV-96%,CAV2-2.5%__CAV4-2.5%__HDV-95%,CAV2-3.0%__CAV4-3.0%__HDV-94%,CAV2-3.5%__CAV4-3.5%__HDV-93%,CAV2-4.0%__CAV4-4.0%__HDV-92%,CAV2-4.5%__CAV4-4.5%__HDV-91%,CAV2-5.0%__CAV4-5.0%__HDV-90%,CAV2-5.5%__CAV4-5.5%__HDV-89%,CAV2-6.0%__CAV4-6.0%__HDV-88%,CAV2-6.5%__CAV4-6.5%__HDV-87%,CAV2-7.0%__CAV4-7.0%__HDV-86%,CAV2-7.5%__CAV4-7.5%__HDV-85%`
* Verbose console output
  * `-v`
* The measurement to consider, the # of histogram bins and the x axis setup
  * `-m waitingTime --minV 0 --maxV 1000 --bins 10 --xticks 0,1000,100,16`
* The y axis setup and the labels
  * `--xlabel "Wait Time [s]" --ylabel "Number of Commuters[#]"  --title "Time Spent Waiting in Traffic"  --yticks 16 --xlabelsize 16 --ylabelsize 16 --titlesize 30`

When combined it creates a histogram as pictured above.



