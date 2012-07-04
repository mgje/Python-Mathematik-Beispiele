# sobel_energy_calculator - Implementation of EnergyCalculator using
#                           the Sobel matrix
#
# This file is part of "scarving", a Python implementation of the
# seam carving image resize algorithm
#
# Copyright (C) 2007  Nicolas Trangez <eikke@eikke.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License (and no other).
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# EOL

from energy_calculator import EnergyCalculator
from scipy.ndimage.filters import generic_gradient_magnitude, sobel
import sys
from PIL import Image

class SobelEnergyCalculator(EnergyCalculator):
        def __init__(self, image):
                EnergyCalculator.__init__(self, image)

        def calculate_per_pixel(self):
                return False

        def _calculate_full_energy(self):
                return generic_gradient_magnitude(self.get_image_matrix(), derivative = sobel)

def usage(pname):
        print "Usage: %s filename.jpg" % pname

def main():
        image = None
        try:
                image = Image.open(sys.argv[-1])
        except:
                usage(sys.argv[0])
                return

        ec = SobelEnergyCalculator(image)
        energy = ec.get_energy_image()
        energy.show()

if __name__ == "__main__":
        try:
                try:
                        import cProfile as profile
                except ImportError:
                        import profile
        except ImportError:
                print "Not profiling"
                main()
                sys.exit()
        print "Profiling using %s" % profile.__name__
        profile.run("main()")
