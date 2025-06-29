# Copyright 2025 ellipse2v
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
STRIDE Threat Analysis Library with MITRE ATT&CK Integration
"""

__version__ = "1.0.0"
__author__ = "ellipse2v"

from .models_module import ThreatModel
from .mitre_mapping_module import MitreMapping
from .severity_calculator_module import SeverityCalculator
from .report_generator import ReportGenerator
from .diagram_generator import DiagramGenerator
from .model_parser import ModelParser

__all__ = [
    'ThreatModel',
    'MitreMapping',
    'SeverityCalculator',
    'ReportGenerator',
    'DiagramGenerator',
    'ModelParser'
]