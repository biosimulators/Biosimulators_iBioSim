# Biosimulators_iBioSim
BioSimulators-compliant command-line interface to the [iBioSim](https://github.com/MyersResearchGroup/iBioSim) simulation program.

## Contents
* [Installation](#installation)
* [Usage](#local-usage)
* [License](#license)
* [Development team](#development-team)
* [Questions and comments](#questions-and-comments)

## Installation
### Install Docker image
```
docker pull ghcr.io/MyersResearchGroup/ibiosim
```

## Local Usage
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

## Usage Through Docker Container
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

## License
This package is released under the [Apache-2.0](License)

## Development Team
This package was developed by the [Genetic Logic Lab](https://myersresearchgroup.github.io/) at the University of Colorado Boulder.

## Questions and comments
Please contact the [Genetic Logic Lab](mailto:chris.myers@colorado.edu) with any questions or comments.