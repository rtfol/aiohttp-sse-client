#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from aiohttp_sse_client import client as sse_client

from .const import WPT_SERVER


async def test_eventsource_reconnect():
    """Test EventSource: reconnection.

    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/eventsource-reconnect.htm
    """
    source = sse_client.EventSource(
        WPT_SERVER + 'resources/status-reconnect.py?status=200')
    await source.connect()
    async for e in source:
        assert e.data == 'data'
        break
    await source.close()


async def test_eventsource_reconnect_event():
    """Test EventSource: reconnection event.

    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/eventsource-reconnect.htm
    """
    opened  = False
    reconnected = False

    def on_error():
        nonlocal reconnected
        assert source.ready_state == sse_client.READY_STATE_CONNECTING
        assert opened is True
        reconnected = True

    async with sse_client.EventSource(
        WPT_SERVER + 'resources/status-reconnect.py?status=200&ok_first&id=2',
        reconnection_time=timedelta(milliseconds=2),
        on_error=on_error
    ) as source:
        async for e in source:
            if not opened:
                opened = True
                assert reconnected is False
                assert e.data == "ok"
            else:
                assert reconnected is True
                assert e.data == "data"
                break
