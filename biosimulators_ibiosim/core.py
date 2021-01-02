""" Methods for executing SED tasks in COMBINE archives and saving their outputs

:Author: Myers Research Group <chris.myers@colorado.edu>
:Date: 2020-06-12
:Copyright: 2020
:License: Apache-2.0
"""

import os
import shutil
import subprocess
#import zipfile

__all__ = ['get_ibiosim_version', 'exec_sedml_docs_in_combine_archive']


IBIOSIM_PATH = os.getenv('IBIOSIM_PATH', '/iBioSim/analysis/target/iBioSim-analysis-3.1.0-SNAPSHOT-jar-with-dependencies.jar')


def get_ibiosim_version():
    """ Get the version of iBioSim

    Returns:
        :obj:`str`: version
    """
    # TODO: implement
    return None


def exec_sedml_docs_in_combine_archive(archive_file, out_dir):
    """ Execute the SED tasks defined in a COMBINE archive and save the outputs

    Args:
        archive_file (:obj:`str`): path to COMBINE archive
        out_dir (:obj:`str`): directory to store the outputs of the tasks
    """
    if not os.path.isfile(archive_file):
        raise FileNotFoundError("File does not exist: {}".format(archive_file))

    '''if not zipfile.is_zipfile(archive_file):
        raise IOError("File is not an OMEX Combine Archive in zip format: {}".format(archive_file))'''

    subprocess.check_call(['java', '-jar', IBIOSIM_PATH, '-sim', 'hode', archive_file])
    # shutil.move(archive_file.rsplit('.', 1)[0], out_dir)
