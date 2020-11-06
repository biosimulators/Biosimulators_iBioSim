![Latest version](https://img.shields.io/github/v/tag/biosimulators/Biosimulators_iBioSim)
[![PyPI](https://img.shields.io/pypi/v/biosimulators_ibiosim)](https://pypi.org/project/biosimulators_ibiosim/)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/biosimulators/Biosimulators_iBioSim/workflow-id)](https://github.com/biosimulators/Biosimulators_iBioSim/actions?query=workflow%3Aworkflow-id)
[![Documentation](https://img.shields.io/github/license/biosimulators/Biosimulators_iBioSim?badges-awesome-green.svg)](https://biosimulators.github.io/Biosimulators_iBioSim/)
[![Issues](https://img.shields.io/github/issues/biosimulators/Biosimulators_iBioSim)](https://github.com/biosimulators/Biosimulators_iBioSim/issues)
[![License](https://img.shields.io/github/license/biosimulators/Biosimulators_iBioSim?badges-awesome-green.svg)](https://github.com/biosimulators/Biosimulators_iBioSim/blob/dev/LICENSE)

# BioSimulators-iBioSim
BioSimulators-compliant command-line interface to the [iBioSim](https://github.com/MyersResearchGroup/iBioSim) simulation program.

This command-line interface and Docker image enable users to use iBioSim to execute [COMBINE/OMEX archives](https://combinearchive.org/) that describe one or more simulation experiments (in [SED-ML format](https://sed-ml.org)) of one or more models (in [SBML format](http://sbml.org])).

A list of the algorithms and algorithm parameters supported by iBioSim is available at [BioSimulators](https://biosimulators.org/simulators/ibiosim).

A simple web application and web service for using iBioSim to execute COMBINE/OMEX archives is also available at [runBioSimulations](https://run.biosimulations.org).

## Contents
* [Installation](#installation)
* [Usage](#local-usage)
* [Documentation](#documentation)
* [License](#license)
* [Development team](#development-team)
* [Questions and comments](#questions-and-comments)

## Installation
### Install Docker image
```
docker pull ghcr.io/MyersResearchGroup/ibiosim
```

## Usage

### Local Usage
```
usage: ibiosim [-h] [-d] [-q] -i ARCHIVE [-o OUT_DIR] [-v]

BioSimulators-compliant command-line interface to the [iBioSim](https://github.com/MyersResearchGroup/iBioSim) simulation program.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           full application debug mode
  -q, --quiet           suppress all console output
  -i ARCHIVE, --archive ARCHIVE
                        Path to OMEX file which contains one or more SED-ML-
                        encoded simulation experiments
  -o OUT_DIR, --out-dir OUT_DIR
                        Directory to save outputs
  -v, --version         show program's version number and exit
```

### Usage Through Docker Container
```
docker run \
  --tty \
  --rm \
  --mount type=bind,source="$(pwd)"/tests/fixtures,target=/root/in,readonly \
  --mount type=bind,source="$(pwd)"/tests/results,target=/root/out \
  ghcr.io/MyersResearchGroup/ibiosim:latest \
    -i /root/in/<Need to Update to Cleaned Archive> \
    -o /root/out
```

## Documentation
Documentation is available at https://biosimulators.github.io/Biosimulators_iBioSim/.

## License
This package is released under the [Apache-2.0](License)

## Development Team
This package was developed by the [Genetic Logic Lab](https://myersresearchgroup.github.io/) at the University of Colorado Boulder.

## Questions and comments
Please contact the [Genetic Logic Lab](mailto:chris.myers@colorado.edu) with any questions or comments.