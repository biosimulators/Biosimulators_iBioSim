""" Methods for executing SED tasks in COMBINE archives and saving their outputs

:Author: Myers Research Group <chris.myers@colorado.edu>
:Date: 2020-06-12
:Copyright: 2020
:License: Apache-2.0
"""

from biosimulators_utils.plot.data_model import PlotFormat  # noqa: F401
from biosimulators_utils.report.data_model import ReportFormat, VariableResults  # noqa: F401
from biosimulators_utils.sedml.data_model import (Task, ModelLanguage, UniformTimeCourseSimulation,  # noqa: F401
                                                  Variable, Symbol)
import os
import subprocess
# import zipfile

__all__ = ['get_ibiosim_version', 'exec_sedml_docs_in_combine_archive']


IBIOSIM_PATH = os.getenv('IBIOSIM_PATH', '/iBioSim/analysis/target/iBioSim-analysis-3.1.0-SNAPSHOT-jar-with-dependencies.jar')


def get_ibiosim_version():
    """ Get the version of iBioSim

    Returns:
        :obj:`str`: version
    """
    # TODO: implement
    return None


def exec_sedml_docs_in_combine_archive(archive_filename, out_dir,
                                       report_formats=None, plot_formats=None,
                                       bundle_outputs=None, keep_individual_outputs=None):
    """ Execute the SED tasks defined in a COMBINE/OMEX archive and save the outputs

    Args:
        archive_filename (:obj:`str`): path to COMBINE/OMEX archive
        out_dir (:obj:`str`): path to store the outputs of the archive

            * CSV: directory in which to save outputs to files
              ``{ out_dir }/{ relative-path-to-SED-ML-file-within-archive }/{ report.id }.csv``
            * HDF5: directory in which to save a single HDF5 file (``{ out_dir }/reports.h5``),
              with reports at keys ``{ relative-path-to-SED-ML-file-within-archive }/{ report.id }`` within the HDF5 file

        report_formats (:obj:`list` of :obj:`ReportFormat`, optional): report format (e.g., csv or h5)
        plot_formats (:obj:`list` of :obj:`PlotFormat`, optional): report format (e.g., pdf)
        bundle_outputs (:obj:`bool`, optional): if :obj:`True`, bundle outputs into archives for reports and plots
        keep_individual_outputs (:obj:`bool`, optional): if :obj:`True`, keep individual output files
    """
    if not os.path.isfile(archive_filename):
        raise FileNotFoundError("File does not exist: {}".format(archive_filename))

    '''if not zipfile.is_zipfile(archive_filename):
        raise IOError("File is not an OMEX Combine Archive in zip format: {}".format(archive_filename))'''

    subprocess.check_call(['java', '-jar', IBIOSIM_PATH, '-sim', 'hode', archive_filename])
    # shutil.move(archive_filename.rsplit('.', 1)[0], out_dir)
