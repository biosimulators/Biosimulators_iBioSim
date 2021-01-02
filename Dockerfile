# Base OS
FROM ubuntu:18.04

# Version
ARG VERSION=0.0.1
ARG SIMULATOR_VERSION=3.1.0

# Open Containers Initiative and BioContainers metadata
LABEL \
    org.opencontainers.image.title="iBioSim" \
    org.opencontainers.image.version="${SIMULATOR_VERSION}" \
    org.opencontainers.image.description="CAD tool aimed for the modeling, analysis, and design of genetic circuits" \
    org.opencontainers.image.url="https://github.com/MyersResearchGroup/iBioSim" \
    org.opencontainers.image.documentation="https://github.com/MyersResearchGroup/iBioSim" \
    org.opencontainers.image.source="https://github.com/biosimulators/Biosimulators_iBioSim" \
    org.opencontainers.image.authors="Chris Myers <chris.myers@colorado.edu>" \
    org.opencontainers.image.vendor="Chris Myers" \
    org.opencontainers.image.licenses="Apache-2.0" \
    \
    base_image="ubuntu:18.04" \
    version="${VERSION}" \
    software="iBioSim" \
    software.version="${SIMULATOR_VERSION}" \
    about.summary="CAD tool aimed for the modeling, analysis, and design of genetic circuits" \
    about.home="https://github.com/MyersResearchGroup/iBioSim" \
    about.documentation="https://github.com/MyersResearchGroup/iBioSim" \
    about.license_file="https://github.com/MyersResearchGroup/iBioSim/blob/master/LICENSE.txt" \
    about.license="SPDX:Apache-2.0" \
    about.tags="kinetic modeling,dynamical simulation,systems biology,biochemical networks,SBML,SED-ML,COMBINE,OMEX,BioSimulators" \
    maintainer="Chris Myers <chris.myers@colorado.edu>"

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
RUN git clone https://github.com/MyersResearchGroup/iBioSim.git --branch ${SIMULATOR_VERSION} --depth 1 \
    && cd iBioSim \
    && mvn package -Dmaven.javadoc.skip=true

# Install reb2sac and GeneNet
# TODO: compile reb2sac outside of image and copy it in

# Copy code for command-line interface into image and install it
COPY . /root/Biosimulators_iBioSim
RUN python3.7 -m pip install /root/Biosimulators_iBioSim \
    && rm -rf /root/Biosimulators_iBioSim
ENV MPLBACKEND=PDF

# Entrypoint
ENTRYPOINT ["iBioSim"]
CMD []
