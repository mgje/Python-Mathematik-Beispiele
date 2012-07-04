# energy_calculator - Base class for all energy calculation implementations
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

from PIL import Image, ImageOps
from numpy import ndarray, reshape
import utils

class EnergyCalculator:
        def __init__(self, image):
                self._energy = None
                
                if isinstance(image, ndarray):
                        self._image = image
                        return

                # Assume this is a PIL Image
                # TODO: How to recognize this?
                (w, h) = image.size
                self._image = reshape(ImageOps.grayscale(image).getdata(), (h, w))

        def calculate_per_pixel(self):
                raise NotImplemented

        def _calculate_pixel_energy(self, x, y):
                if self.calculate_per_pixel() == False:
                        raise Exception, "This function should not be called when calculate_per_pixel is False"
                raise NotImplemented

        def _calculate_full_energy(self):
                if self.calculate_per_pixel() == True:
                        raise Exception, "This function should not be called when calculate_per_pixel is True"
                raise NotImplemented

        def calculate(self):
                if self.calculate_per_pixel() == False:
                        e = self._calculate_full_energy()
                        if not isinstance(e, ndarray):
                                raise Exception, "Return value of _calculate_full_energy should be of type numpy.ndarray"
                        e.clip(utils.MIN_PIXEL_VALUE, utils.MAX_PIXEL_VALUE)
                        self._energy = e
                else:
                        h = len(self._image)
                        if h < 1:
                                raise Exception, "Invalid image size"
                        w = len(self._image[0])
                        for y in range(0, h):
                                for x in range(0, w):
                                        e = self._calculate_pixel_energy(x, y)
                                        if not isinstance(e, int):
                                                raise Exception, "Return value of _calculate_pixel_energy should be of type int"
                                        e = utils.clip(e)
                                        self._energy[y, x] = e

        def get_image_matrix(self):
                return self._image.copy()

        def get_image_pixel(self, x, y):
                return self._image[y, x]

        def get_energy_matrix(self):
                if self._energy == None:
                        self.calculate()
                return self._energy.copy()

        def get_energy_matrix_shape(self):
                if self._energy == None:
                        self.calculate()
                return self._energy.shape

        def get_energy(self, x, y):
                if self._energy == None:
                        self.calculate()
                return self._energy[y, x]

        def get_energy_image(self):
                if self._energy == None:
                        self.calculate()
                (h, w) = self._energy.shape
                im = Image.new("L", (w, h))
                im.putdata(self._energy.flatten())
                return im
