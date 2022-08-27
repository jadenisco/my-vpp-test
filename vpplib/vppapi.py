#
# Copyright (c) 2022 John DeNisco
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
import os
import fnmatch
from vpp_papi import VPPApiClient

# Constants
LD_LIBRARY_PATH = '/usr/lib/x86_64-linux-gnu/'
JSON_DIR = '/usr/share/vpp/api/core/'

class VPPApi():

    def __init__(self, clientname='vpp'):
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.NullHandler())
        self.logger.debug("{} __init__({})".format(__name__.strip('_'), locals()))

        self.clientname = clientname
        self.ld_library_path = LD_LIBRARY_PATH
        self.json_dir  = JSON_DIR

        try:
            self.prev_ld_library_path = os.environ["LD_LIBRARY_PATH"]
        except:
            self.prev_ld_library_path = None

        os.environ["LD_LIBRARY_PATH"] = self.ld_library_path
        self.logger.debug("  LD_LIBRARY_PATH: {}".format(os.environ["LD_LIBRARY_PATH"]))  

        self.logger.debug("  json_dir: {}".format(self.json_dir))
        self.json_files = []
        for root, dirnames, filenames in os.walk(self.json_dir):
            for filename in fnmatch.filter(filenames, '*.api.json'):
                self.json_files.append(os.path.join(self.json_dir, filename))
        if not self.json_files:
            logging.critical("There are no json files.")
            self.client = None
        else:
            self.client = VPPApiClient(apifiles=self.json_files)

    def __del__(self):
        self.logger.debug("{} __del__({})".format(__name__.strip('_'), locals()))

        if self.prev_ld_library_path:
            os.environ["LD_LIBRARY_PATH"] = self.ld_library_path
