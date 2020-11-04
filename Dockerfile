# Base OS
FROM ubuntu:18.04

# Version
ENV VERSION=3.1.0

# BioContainers metadata
LABEL base_image="ubuntu:18.04"
LABEL version="0.0.1"
LABEL software="iBioSim"
LABEL software.version="${VERSION}"
LABEL about.summary="CAD tool aimed for the modeling, analysis, and design of genetic circuits"
LABEL about.home="https://github.com/MyersResearchGroup/iBioSim"
LABEL about.documentation="https://github.com/MyersResearchGroup/iBioSim"
LABEL about.license_file="https://github.com/MyersResearchGroup/iBioSim/blob/master/LICENSE.txt"
LABEL about.license="Apache-2.0"
LABEL about.tags="kinetic modeling,dynamical simulation,systems biology,biochemical networks,SBML,SED-ML,COMBINE,OMEX,BioSimulators"
LABEL maintainer="Chris Myers <chris.myers@colorado.edu>"

# Install requirements
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        git \
        openjdk-8-jdk \
        maven \
        python3.7 \
        python3-pip \
    && python3.7 -m pip install -U setuptools \
    && python3.7 -m pip install -U pip \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Install iBioSim
RUN git clone https://github.com/MyersResearchGroup/iBioSim.git --branch ${VERSION} --depth 1 \
    && cd iBioSim \
    && mvn package -Dmaven.javadoc.skip=true

# Install reb2sac and GeneNet
# TODO: compile reb2sac outside of image and copy it in

# Copy code for command-line interface into image and install it
COPY . /root/Biosimulators_iBioSim
RUN python3.7 -m pip install /root/Biosimulators_iBioSim

# Entrypoint
ENTRYPOINT ["iBioSim"]
CMD []
