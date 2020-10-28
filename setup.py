import re
import setuptools
import subprocess
import sys
try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "show", "pkg_utils"],
        check=True, capture_output=True)
    match = re.search(r'\nVersion: (.*?)\n', result.stdout.decode(), re.DOTALL)
    assert match and tuple(match.group(1).split('.')) >= ('0', '0', '5')
except (subprocess.CalledProcessError, AssertionError):
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-U", "pkg_utils"],
        check=True)
import os
import pkg_utils

name = 'iBioSim'
dirname = os.path.dirname(__file__)

# get package metadata
md = pkg_utils.get_package_metadata(dirname, name)

# install package
setuptools.setup(
    name=name,
    version=md.version,
    description=("BioSimulators-compliant command-line interface to "
                 "the iBioSim simulation program https://async.ece.utah.edu/tools/ibiosim/."),
    long_description=md.long_description,
    url="https://github.com/MyersResearchGroup/iBioSim",
    download_url="https://github.com/MyersResearchGroup/iBioSim",
    author='Myers Research Group',
    author_email="chris.myers@colorado.edu",
    license="Apache-2.0",
    keywords=['kinetic modeling', 'dynamical simulation', 'systems biology',
              'biochemical networks', 'SBML', 'SED-ML', 'COMBINE', 'OMEX',
              'BioSimulators'],
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=md.install_requires,
    extras_require=md.extras_require,
    tests_require=md.tests_require,
    dependency_links=md.dependency_links,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    entry_points={
        'console_scripts': [
            'iBioSim = Biosimulators_iBioSim.__main__:main',
        ],
    },
)
