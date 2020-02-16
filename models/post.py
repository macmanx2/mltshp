from __future__ import absolute_import
from lib.flyingcow import Model, Property

from datetime import datetime
from tornado.options import options


class Post(Model):
    user_id = Property()
    sourcefile_id = Property()
    sharedfile_id = Property()
    shake_id    = Property(default=0)
    seen = Property(default=0)
    deleted = Property(default=0)
    created_at  = Property()

    def save(self, *args, **kwargs):
        if options.readonly:
            self.add_error('_', 'Site is read-only.')
            return False

        self._set_dates()
        return super(Post, self).save(*args, **kwargs)

    def _set_dates(self):
        """
        Sets the created_at and updated_at fields. This should be something
        a subclass of Property that takes care of this during the save cycle.
        """
        if self.id is None or self.created_at is None:
            self.created_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
