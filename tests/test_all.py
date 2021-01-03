""" Tests of the command-line interface

:Author: Myers Research Group <chris.myers@colorado.edu>
:Date: 2020-10-29
:Copyright: 2020
:License: Apache-2.0
"""

from biosimulators_ibiosim import __main__
from biosimulators_ibiosim.core import get_ibiosim_version, exec_sedml_docs_in_combine_archive
from biosimulators_utils.simulator.exec import exec_sedml_docs_in_archive_with_containerized_simulator
from unittest import mock
import os
import shutil
import tempfile
import unittest


class CliTestCase(unittest.TestCase):
    EXAMPLE_ARCHIVE_FILENAME = os.path.join(os.path.dirname(__file__), 'fixtures', 'BIOMD0000000297.omex')
    DOCKER_IMAGE = 'ghcr.io/myersresearchgroup/biosimulators_ibiosim/ibiosim:latest'

    def setUp(self):
        self.dirname = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.dirname)

    def test_get_ibiosim_version(self):
        self.assertEqual(get_ibiosim_version(), None)

    @unittest.skip('Method not yet implemented')
    def test_exec_sedml_docs_in_combine_archive(self):
        # execute COMBINE archive
        exec_sedml_docs_in_combine_archive(self.EXAMPLE_ARCHIVE_FILENAME, self.dirname)

        # assert outputs created correctly

    def test_app_help(self):
        with self.assertRaises(SystemExit):
            with __main__.App(argv=['--help']) as app:
                app.run()

    def test_main_help(self):
        with mock.patch('sys.argv', ['', '--help']):
            with self.assertRaises(SystemExit) as context:
                __main__.main()
                self.assertRegex(context.Exception, 'usage: ')

    @unittest.skip('Docker image not yet built')
    def test_exec_sedml_docs_in_combine_archive_with_docker_image(self):
        archive_filename = self.EXAMPLE_ARCHIVE_FILENAME

        # environment variables to pass to container
        env = {}

        # execute COMBINE archive
        exec_sedml_docs_in_archive_with_containerized_simulator(
            archive_filename, self.dirname, self.DOCKER_IMAGE, environment=env, pull_docker_image=False)

        # assert outputs created correctly
