import logging
from redflash import RedFlashClient

class RedFlashHandler(logging.Handler):
    """ Logging handler for redflash. Arguments to supply either
via dictConfig or directly are:

    * host
    * apikey
    * notify_groups: list of group names to notify (if any)
    * notify_contacts: list of contact names to notify (if any)
    * fail_silently: default True, swallow errors e.g. if invalid or disabled recipient

Group and contact names are the slugs as defined in the Redflash records.
    """
    def __init__(self, host, apikey, 
                    notify_groups=[], 
                    notify_contacts=[],
                    fail_silently=True):

        logging.Handler.__init__(self)
        self.rfc = RedFlashClient(host, apikey)
        self.notify_groups = notify_groups
        self.notify_contacts = notify_contacts
        self.fail_silently = fail_silently

    def emit(self, record):
        for g in self.notify_groups:
            try:
                self.rfc.notify_group(g, record.message)
            except Exception:
                if not self.fail_silently:
                    raise
        for u in self.notify_contacts:
            try:
                self.rfc.notify_contact(u, record.message)
            except Exception:
                if not self.fail_silently:
                    raise
