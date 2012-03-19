Python client for Redflash
==========================
Matthew Pontefract, matthew at rethought<dash>solutions<dot>com

RedFlash is a tool for managing notifications. It provides a single HTTP API that any application
can call to send a message to a named person or group, or to fire a generic event. Through RedFlash
you can manage recipients (adding and removing from groups and event notifications) and manage
the channels by which any given individual is notified (for example SMS or Twitter)

This client library provides simple access to RedFlash. Examples:

    from rfclient.redflash import RedFlashClient
    rfc = RedFlashClient(rf_url="http://my.redflash.url", api_key="<key obtained from admin>")
    rfc.notify_contact(<contact_slug>, "message to send")
    rfc.notify_group(<group_slug>, "message to send")
    
    # args are a set of keyword arguments that get passed to the message
    # template
    rfc.fire_event(<event_slug>, **kwargs)
