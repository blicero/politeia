#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2025-09-18 22:13:03 krylon>
#
# /data/code/python/politeia/model.py
# created on 18. 09. 2025
# (c) 2025 Benjamin Walkenhorst
#
# This file is part of the PyKuang network scanner. It is distributed under the
# terms of the GNU General Public License 3. See the file LICENSE for details
# or find a copy online at https://www.gnu.org/licenses/gpl-3.0

"""
politeia.model

(c) 2025 Benjamin Walkenhorst
"""


from dataclasses import dataclass, field
from enum import Enum, auto


class Work(Enum):
    """Work specifies the area a group of people are working in."""

    Farming = auto()
    Fishing = auto()
    Construction = auto()
    Science = auto()
    Handiwork = auto()


@dataclass(slots=True, kw_only=True)
class Polis:
    """The central element in our game, a city state set in a world modeled on ancient Greece/Ionia."""

    name: str
    population: int
    food: int
    work: map[Work, int] = field(default_factory=dict)

# Local Variables: #
# python-indent: 4 #
# End: #
