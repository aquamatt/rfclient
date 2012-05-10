import logging
from redflash import RedFlashClient

class RedFlashHandler(logging.Handler):
    """ Logging handler for redflash primarily intended for making it easy to send SMS alerts via RedFlash. Arguments to supply either
via dictConfig or directly are:

    * host
    * apikey
    * notify_groups: list of group names to notify (if any)
    * notify_contacts: list of contact names to notify (if any)
    * fail_silently: default True, swallow errors e.g. if invalid or disabled recipient
    * max_len: If None or 0 messages are sent 'as-is', otherwise the message is truncated to the stated length prior to sending. Prevent accidentally sending a large message as a multi-part SMS! Default 160.
    * prefix: If set, this is prefixed to all messages going through this logger.

Group and contact names are the slugs as defined in the Redflash records.
    """
    def __init__(self, host, apikey, 
                    notify_groups=[], 
                    notify_contacts=[],
                    fail_silently=True,
                    max_len=160,
                    prefix=None):

        logging.Handler.__init__(self)
        self.rfc = RedFlashClient(host, apikey)
        self.notify_groups = notify_groups
        self.notify_contacts = notify_contacts
        self.fail_silently = fail_silently
        self.max_len = max_len
        self.prefix = prefix

    def emit(self, record):
        msg = record.message
        if self.prefix:
            msg = "%s%s" % (self.prefix, msg)

        if self.max_len:
            msg = msg[:self.max_len]

        for g in self.notify_groups:
            try:
                self.rfc.notify_group(g, msg)
            except Exception:
                if not self.fail_silently:
                    raise
        for u in self.notify_contacts:
            try:
                self.rfc.notify_contact(u, msg)
            except Exception:
                if not self.fail_silently:
                    raise
