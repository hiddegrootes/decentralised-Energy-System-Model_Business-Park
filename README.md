# Decentralised-Energy-System-Model_Business-Park

This repository contains the energy system model for the **Uitgeest Noord** project, developed using the [Calliope](https://calliope.readthedocs.io/en/stable/) modeling framework. The model simulates energy production, storage, and consumption in a specified region, with a focus on different technology configurations, scenarios, and optimization strategies.

## Project Overview

The Uitgeest Noord model is designed as part of a MSc thesis project to explore various energy scenarios, considering factors such as energy demand, renewable energy sources, storage capacities, and grid interactions. The model aims to support decision-making for sustainable energy planning.

## Repository Structure

- **model.yaml**: Main configuration file for the Calliope model. It includes references to other configuration files, time series data, and solver settings.
- **techs.yaml**: Defines the technologies used in the model, including supply, demand, storage, and transmission technologies.
- **locations.yaml**: Specifies the geographic nodes, including their available area, latitude, longitude, and associated technologies.
- **scenarios.yaml**: Contains various scenarios and their corresponding overrides, allowing the exploration of different energy futures.
- **PythonModel.py**: Script for running the model, handling data processing, and managing outputs.
- **UitgeestNoord_results.nc**: NetCDF file containing the results of a model run, including time series data for various variables.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Calliope 0.7.0+**
- **Gurobi Solver** (optional but recommended for large-scale optimization)

### Installation
See documentation on https://calliope.readthedocs.io/en/latest/installation/

### Building the model 
See documentation on https://calliope.readthedocs.io/en/latest/creating/

### Running the Model
See documentation on https://calliope.readthedocs.io/en/latest/running/

### Customizing the Model

- **Technologies**: Modify `techs.yaml` to change technology parameters like costs, capacities, and efficiency.
- **Locations**: Adjust `locations.yaml` to add or modify nodes and their technologies.
- **Scenarios**: Update `scenarios.yaml` to define new scenarios or adjust existing ones. Scenarios allow you to simulate different energy demand and supply conditions.

### Viewing Results
Results are stored in NetCDF format (`*.nc` files). You can explore these results using tools like [Panoply](https://www.giss.nasa.gov/tools/panoply/) or Python libraries such as `xarray` and `netCDF4`.

## Contributing
Contributions to this project are welcome. Please follow the standard GitHub fork-and-pull request workflow:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a new Pull Request

## License
This project is licensed under the TU Delft.

