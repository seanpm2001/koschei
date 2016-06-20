# Copyright (C) 2016 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>

import koschei.models as m

from .common import DBTest


class ModelTest(DBTest):

    def test_group_cardinality(self):
        group = self.prepare_group('xyzzy', content=['foo', 'bar', 'baz'])
        self.assertEqual(3, group.package_count)

    def test_group_cardinality_multiple_collections(self):
        group = self.prepare_group('xyzzy', content=['foo', 'bar', 'baz'])
        new_collection = m.Collection(name="new", display_name="New", target_tag="tag2",
                                      build_tag="build_tag2", priority_coefficient=2.0)
        self.s.add(new_collection)
        self.s.commit()
        self.s.add(m.Package(name='bar', collection_id=new_collection.id))
        self.s.commit()
        self.assertEqual(3, group.package_count)
