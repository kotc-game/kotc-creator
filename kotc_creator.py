#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


__version__ = "10.0a0"


import argparse
import gettext
import os

import sge


if getattr(sys, "frozen", False):
    __file__ = sys.executable

DATA = os.path.join(os.path.dirname(__file__), "data")
CONFIG = os.path.join(
    os.getenv("XDG_CONFIG_HOME", os.path.join(os.path.expanduser("~"),
                                              ".config")), "kotc-creator")

gettext.install("kotc-creator", os.path.abspath(os.path.join(DATA, "locale")))

parser = argparse.ArgumentParser()
parser.add_argument(
    "--version", action="version", version="%(prog)s " + __version__,
    help=_("Output version information and exit."))
parser.add_argument(
    "-l", "--lang",
    help=_("Manually choose a different language to use."))
parser.add_argument(
    "-d", "--datadir",
    help=_('Where to load the game data from (Default: "{}")').format(DATA))
parser.add_argument(
    "-c", "--configdir",
    help=_('Where to store save data in (Default: "{}")').format(CONFIG))
args = parser.parse_args()

if args.datadir:
    DATA = args.datadir
if args.configdir:
    CONFIG = args.configdir

gettext.install("kotc-creator", os.path.abspath(os.path.join(DATA, "locale")))

if args.lang:
    lang = gettext.translation("kotc-creator",
                               os.path.abspath(os.path.join(DATA, "locale")),
                               [args.lang])
    lang.install()


class Game(sge.dsp.Game):

    pass





if __name__ == "__main__":
    pass
