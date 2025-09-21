#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2025-09-21 18:45:37 krylon>
#
# /data/code/python/politeia/engine.py
# created on 21. 09. 2025
# (c) 2025 Benjamin Walkenhorst
#
# This file is part of the PyKuang network scanner. It is distributed under the
# terms of the GNU General Public License 3. See the file LICENSE for details
# or find a copy online at https://www.gnu.org/licenses/gpl-3.0

"""
politeia.engine

(c) 2025 Benjamin Walkenhorst
"""


from politeia.model import Polis


class Engine:
    """Engine wraps the game logic."""

    __slots__ = [
        'polis',
        'player',
        'round',
    ]

    polis: Polis
    player: str
    round: int

# Local Variables: #
# python-indent: 4 #
# End: #
