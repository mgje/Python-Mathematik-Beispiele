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
# EOL

def apply_mask(self, mask, newshape):
        # Apply a mask to a matrix:
        # In [160]: data
        # Out[160]: 
        # array([[ 8,  3,  7,  2,  5],
        #       [ 1,  4,  9,  4,  4],
        #       [ 4,  5, 10,  6,  1],
        #       [ 2,  8,  6,  1,  5],
        #       [ 4,  6,  2,  6,  5]])
        #
        # In [161]: overlay
        # Out[161]: 
        #        array([[0, 1, 1, 1, 1],
        #               [1, 0, 1, 1, 1],
        #               [1, 1, 0, 1, 1],
        #               [1, 1, 1, 0, 1],
        #               [1, 1, 1, 1, 0]])
        #
        # In [162]: # Remove one row
        #
        # In [163]: data.compress(overlay.flatten()).reshape((data.shape[0] , data.shape[1] - 1))
        # Out[163]: 
        #         array([[3, 7, 2, 5],
        #               [1, 9, 4, 4],
        #               [4, 5, 6, 1],
        #               [2, 8, 6, 5],
        #               [4, 6, 2, 6]])
        return self.compress(mask.flatten()).reshape(newshape)
