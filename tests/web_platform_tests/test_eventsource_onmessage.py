#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from aiohttp_sse_client import client as sse_client

from .const import WPT_SERVER


async def test_eventsource_onmessage():
    """Test EventSource: onmessage.
    
    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/eventsource-onmessage.htm
    """
    def on_message(event):
        """Callback for message event."""
        assert event.data == "data"
    
    source = sse_client.EventSource(WPT_SERVER + 'resources/message.py',
                                    on_message=on_message)
    await source.connect()
    async for e in source:
        assert e.data == "data"
        break
    await source.close()
