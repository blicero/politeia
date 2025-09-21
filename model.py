#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2025-09-20 18:43:57 krylon>
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
from typing import Final


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
    population: int = 0
    food: int = 0
    work: map[Work, int] = field(default_factory=dict)

    @property
    def free(self) -> int:
        """Return the number of unused population."""
        return self.population - sum(self.work.values())

    def assign(self, task: Work, cnt: int) -> None:
        """Assign the given number of workers to the given task."""
        free: Final[int] = self.free
        if free < cnt:
            raise ValueError(f"Invalid count {cnt} ({free} available workers)")
        elif cnt <= 0:
            raise ValueError(f"Invalid count {cnt} (must be > 0)")

        if task not in self.work:
            self.work[task] = 0

        self.work[task] += cnt


# Local Variables: #
# python-indent: 4 #
# End: #
