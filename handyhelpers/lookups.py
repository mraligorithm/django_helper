"""
This file contains custom filter lookups as per: https://docs.djangoproject.com/en/2.2/howto/custom-lookups/
"""

from django.db.models import Lookup


class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params
