#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2022 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This file is part of Wonderlands ModCabinet Sorter.
#
# Wonderlands ModCabinet Sorter is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# Wonderlands ModCabinet Sorter is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Wonderlands ModCabinet Sorter.  If not, see
# <https://www.gnu.org/licenses/>.

import io
import unittest
from wlcabinetsorter.app import ModFile, NotAModFile

class ModFileTextHotfixesTests(unittest.TestCase):
    """
    Testing importing a text-hotfixes-format file.
    """

    valid_categories = {
            'qol': 'Quality of Life',
            'scaling': 'Scaling',
            'char-gunner': 'Gunner',
            }

    def setUp(self):
        """
        Initialize some vars we'll need on every test.
        """
        self.errors = []
        self.modfile = ModFile(0, error_list=self.errors, valid_categories=self.valid_categories)
        self.modfile.full_filename = 'modname.wlhotfix'
        self.df = io.StringIO()

    def set_df_contents(self, lines, do_contents=True, newline_after=True):
        """
        Sets the contents of the "file" that we're gonna read in.
        """
        for line in lines:
            print(line, file=self.df)
        if do_contents:
            if newline_after:
                print('', file=self.df)
            print('SparkServiceWhatever', file=self.df)
        self.df.seek(0)

    def test_load_empty(self):
        self.set_df_contents([], do_contents=False)
        with self.assertRaises(NotAModFile) as cm:
            self.modfile.load_text_hotfixes(self.df)
        self.assertIn('No mod title', str(cm.exception))

    def test_load_only_comments(self):
        self.set_df_contents([
            '# Testing',
            ], do_contents=False)
        with self.assertRaises(NotAModFile) as cm:
            self.modfile.load_text_hotfixes(self.df)
        self.assertIn('No mod title', str(cm.exception))

    def test_load_commentless(self):
        self.set_df_contents([])
        with self.assertRaises(NotAModFile) as cm:
            self.modfile.load_text_hotfixes(self.df)
        self.assertIn('No mod title', str(cm.exception))

    def test_load_only_name_old(self):
        self.set_df_contents([
            '# Name: Mod Name',
            ])
        with self.assertRaises(NotAModFile) as cm:
            self.modfile.load_text_hotfixes(self.df)
        self.assertIn('No mod title', str(cm.exception))

    def test_load_only_categories_old(self):
        self.set_df_contents([
            '# Categories: qol',
            ])
        with self.assertRaises(NotAModFile) as cm:
            self.modfile.load_text_hotfixes(self.df)
        self.assertIn('No mod title', str(cm.exception))

    def test_load_minimum_headers_old(self):
        self.set_df_contents([
            '# Name: Mod Name',
            '# Categories: qol',
            ])
        with self.assertRaises(NotAModFile) as cm:
            self.modfile.load_text_hotfixes(self.df)
        self.assertIn('No mod title', str(cm.exception))

