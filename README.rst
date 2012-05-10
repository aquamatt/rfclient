Python client for Redflash
==========================
Matthew Pontefract, matthew at rethought<dash>solutions<dot>com

RedFlash is a tool for managing notifications. It provides a single HTTP API that any application
can call to send a message to a named person or group, or to fire a generic event. Through RedFlash
you can manage recipients (adding and removing from groups and event notifications) and manage
the channels by which any given individual is notified (for example SMS or Twitter)

This client library provides simple access to RedFlash. Examples::

    from rfclient.redflash import RedFlashClient
    rfc = RedFlashClient(rf_url="http://my.redflash.url", api_key="<key obtained from admin>")
    rfc.notify_contact(<contact_slug>, "message to send")
    rfc.notify_group(<group_slug>, "message to send")
    
    # args are a set of keyword arguments that get passed to the message
    # template
    rfc.fire_event(<event_slug>, **kwargs)

Logging
-------

A simple RedFlash logging handler is also provided. Use as any other
log handler. The class is ``rfclient.rflogger.RedFlashHandler`` and takes the following arguments:

* host: the RedFlash server
* apikey
* notify_groups: list of group names to notify (if any)
* notify_contacts: list of contact names to notify (if any)
* fail_silently: default True, swallow errors e.g. if invalid or disabled recipient
* max_len: If None or 0 messages are sent 'as-is', otherwise the message is truncated to the stated length prior to sending. Prevent accidentally sending a large message as a multi-part SMS! Default 160.
* prefix: If set, this is prefixed to all messages going through this logger.

The expectation is that this be used to raise SMS alerts rather than email
hence the default position of truncating messages. To disable truncation,
set max_len to zero or None.

An exmaple of a Python ``dictConfig`` handler clause::

    'handlers': {
        'redflash': {
            'level': 'INFO',
            'class': 'rfclient.rflogger.RedFlashHandler',
            'host' : '<REDFLASH HOST>',
            'apikey': '<YOUR API KEY>',
            'notify_groups': [<GROUPS LIST>],
            'notify_contacts': [<CONTACTS LIST>],
            'max_len': 140,
            'prefix': "SYS01:",
        }   
    },
