# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-


from ...asdftypes import AsdfType


class AsdfObject(dict, AsdfType):
    name = 'core/asdf'


class Software(dict, AsdfType):
    name = 'core/software'


class HistoryEntry(dict, AsdfType):
    name = 'core/history_entry'


from .constant import ConstantType
from .ndarray import NDArrayType
from .complex import ComplexType
