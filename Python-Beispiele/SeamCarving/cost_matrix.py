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

from PIL import Image
from numpy import ndarray, inf

class CostMatrix(ndarray):
        def calculate(self, energy_map):
                if not energy_map.shape == self.shape:
                        raise Exception, "Wrong shape"
                (h, w) = self.shape
                self[0] = energy_map[0].copy()
                self[0] = self[0]
                for y in range(1, h):
                        for x in range(0, w):
                                bestcost = inf
                                bestx = x
                                for dx in range(x - 1, x + 2):
                                        if dx >= 0 and dx < w:
                                                if self[y - 1, dx] < bestcost:
                                                        bestcost = self[y - 1, dx]
                                                        bestx = dx
                                self[y, x] = self[y - 1, bestx] + energy_map[y, x]
                self._calculated = True

        def _get_max_index(self, row, startcol = 0):
                maxx = startcol
                maxval = self[row, maxx]
                
                for x in range(0, len(self[row])):
                        if self[row, x] > maxval:
                                maxx = x
                                maxval = self[row, x]

                return maxx

        def find_shortest_path(self):
                (h, w) = self.shape
                
                x = self._get_max_index(-1)
                path = [x]
                for y in range(h - 2, -1, -1):
                        bestcost = inf
                        for dx in range(x - 1, x + 2):
                                if dx >= 0 and dx < w:
                                        if self[y, dx] < bestcost:
                                                bestcost = self[y, dx]
                                                x = dx
                        path.append(x)

                path.reverse()
                return path


        def get_image(self):
                scaling = 0.03
                (h, w) = self.shape
                im = Image.new("L", (w, h))
                im.putdata(self.flatten() * scaling)
                return im
