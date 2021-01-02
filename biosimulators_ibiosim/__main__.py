""" BioSimulators-compliant command-line interface to the `iBioSim <https://github.com/MyersResearchGroup/iBioSim>`_ simulation program.

:Author: Myers Research Group <chris.myers@colorado.edu>
:Date: 2020-06-12
:Copyright: 2020
:License: Apache-2.0
"""

from ._version import __version__
from .core import get_ibiosim_version, exec_sedml_docs_in_combine_archive
from biosimulators_utils.simulator.cli import build_cli

App = build_cli('ibiosim', __version__,
                'iBioSim', get_ibiosim_version(), 'https://github.com/MyersResearchGroup/iBioSim',
                exec_sedml_docs_in_combine_archive)


def main():
    with App() as app:
        app.run()
