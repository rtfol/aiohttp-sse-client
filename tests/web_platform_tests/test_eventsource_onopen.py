#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from aiohttp_sse_client import client as sse_client

from .const import WPT_SERVER


async def test_eventsource_onopen():
    """Test EventSource: open (announcing the connection).
    
    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/eventsource-onopen.htm
    """
    def on_open():
        """Callback for open event."""
        assert source.ready_state == sse_client.READY_STATE_OPEN
    
    source = sse_client.EventSource(WPT_SERVER + 'resources/message.py',
                                    on_open=on_open)
    assert source.ready_state == sse_client.READY_STATE_CONNECTING
    await source.connect()
    assert source.ready_state == sse_client.READY_STATE_OPEN
    await source.close()
