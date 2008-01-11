# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Django adapter module. Sets up basic type mapping and class mappings for the
Django project

@see L{Django Project<http://www.djangoproject.com>}
 
@author: U{Nick Joyce<mailto:nick@boxdesign.co.uk>}
@since: 0.1b
"""

import pyamf
from django.db.models.query import QuerySet

def _write_queryset(qs):
    return list(qs)

pyamf.add_type(QuerySet, _write_queryset)