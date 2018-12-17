# encoding: utf-8

import logging
from django.conf import settings

_logger = logging.getLogger('django')


class DatabaseRouter(object):
    """
    Database router to control the  models for different db.
    """

    DEFAULT_DB = 'default'

    def _db(self, model, **hints):
        if not (hasattr(model, 'Meta') and hasattr(model.Meta, '_database')):
            return self.DEFAULT_DB
        else:
            db = getattr(model.Meta, '_database', None)

        if db in settings.DATABASES.keys():
            return db
        else:
            _logger.warn('%s not exist' % db)
            return self.DEFAULT_DB

    def db_for_read(self, model, **hints):
        return self._db(model, **hints)

    def db_for_write(self, model, **hints):
        return self._db(model, **hints)

