# encoding: utf-8

#   Copyright 2012 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from PersistentImage import PersistentImage
from props import prop

class TargetImage(PersistentImage):
    """ TODO: Docstring for TargetImage  """

    base_image = prop("_base_image")
    target = prop("_target")
    parameters = prop("_parameters")

    def __init__(self, image, target, parameters):
        """ TODO: Fill me in
        
        @param template TODO
        @param target TODO
        @param parameters TODO
        """
        super(TargetImage, self).__init__()
        self.base_image = image
        self.target = target
        self.parameters = parameters