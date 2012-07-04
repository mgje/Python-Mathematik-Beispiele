# scarve.py - Seam Craving based image resizing algorithm
#
# This implementation is highly inefficient, can only resize width
# and most likely contains several bugs and algorithmic nonsense.
# Feel free to submit patches :-)
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
#
# run with:
# python scarve.py -v -n 10 test.jpg
#
# EOL

from PIL import Image, ImageFilter, ImageChops, ImageOps
import sys
import getopt
import random
import numpy
from cost_matrix import CostMatrix
from utils import clip

class SeamCarve:
        def __init__(self, image):
                self._original = image

        def get_energy_image(self):
                return self._energy.get_energy_image()

        def get_costs_image(self):
                return self._costs.get_image()

        def resize_width(self, pixels, energy_calculator):
                (w, h) = self._original.size
                image = self._original.copy()
                for i in range(0, pixels):
                        print "Removing seam #%d" % i
                        energy = energy_calculator(image)
                        self._energy = energy
                        energy.calculate()
                        costs = CostMatrix(energy.get_energy_matrix_shape())
                        costs.calculate(energy.get_energy_matrix())
                        self._costs = costs
                        path = costs.find_shortest_path()
                        image = self._carve_vertical(image, path)
                        # debug zeige das neue bildchen
                        #image.show();
                        tmpname="seam_%0*d.jpg" % (3,i)
                        image.save(tmpname)
                return image

        def _carve_vertical(self, image, path):
                (w, h) = image.size

                nw = w - 1
                nh = h

                ret = Image.new(image.mode, (nw, nh))

                op = image.load()
                rp = ret.load()

                for y in range(0, h):
                        for x in range(0, w - 1):
                                if x < path[y]:
                                        rp[x, y] = op[x, y]
                                if x > path[y]:
                                        rp[x, y] = op[x + 1, y]
                                if x == path[y]:
                                        cl = op[x, y]
                                        cr = op[x + 1, y]
                                        cn = ((cl[0] + cr[0]) / 2, (cl[1] + cr[1]) / 2, (cl[2] + cr[2]) / 2)
                                        rp[x, y] = cn

                return ret

                self._resized = ret

        def get_resized(self):
                return self._resized

def usage():
        print "Options:"
        print "\t-v: verbose (optional)"
        print "\t-p: run using profiler (optional)"
        print "\t-d: h or w, height or width scaling"
        print "\t-n: number of pixels to scale (integer)"
        print "\tlast argument: filename of input image"

def main():
        from sobel_energy_calculator import SobelEnergyCalculator
        opts = "pvn:"
        args = sys.argv
        if args[0] == "python":
                args = args[1:]
        args = args[1:]
        optlist, args = getopt.getopt(args, opts)

        verbose = False
        try:
                i = optlist.index(("-v", ""))
                verbose = True
        except:
                pass

        pixels = None
        filename = args[-1]
        for i in optlist:
                if i[0] == "-n":
                        pixels = int(i[1])

        if pixels == None:
                usage()
                raise Exception, "No pixels given"

        if filename == None:
                usage()
                raise Exception, "No filename given"

        image = Image.open(filename)

        c = SeamCarve(image)
        carved = c.resize_width(pixels, SobelEnergyCalculator)

        carved.show()
        carved.save("carved.jpg")
        if verbose:
                c.get_energy_image().show()
                c.get_costs_image().show()
                image.show()

if __name__ == "__main__":
        try:
                import psyco
                psyco.full()
        except ImportError:
                pass

        try:
                i = sys.argv.index("-p")
        except ValueError:
                main()
                sys.exit()

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
