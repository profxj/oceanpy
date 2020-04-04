# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This package defines the oceanography-specific units.  They are also
available in the `unyt` namespace.
"""

import numpy as _numpy
import unyt

# Sverdrup
unyt.define_unit('Sverdrup', 1e6*unyt.m**3/unyt.s)
