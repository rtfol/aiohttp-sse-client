#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import pytest

from aiohttp_sse_client import client as sse_client

from .const import WPT_SERVER

async def test_rquest_accept():
    """Test EventSource: Accept header.
    
    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/request-accept.htm
    """
    source = sse_client.EventSource(
        WPT_SERVER + 'resources/accept.event_stream?pipe=sub')
    await source.connect()
    async for e in source:
        assert e.data == "text/event-stream"
        break
    await source.close()


async def test_rquest_cache_control():
    """Test EventSource: Cache-Control.
    
    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/request-cache-control.htm
    """
    source = sse_client.EventSource(
        WPT_SERVER + 'resources/cache-control.event_stream?pipe=sub')
    await source.connect()
    async for e in source:
        assert e.data == "no-cache"
        break
    await source.close()


async def test_rquest_redirect():
    """Test EventSource: redirect.
    
    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/request-redirect.htm
    """
    async def test(status):
        def on_error():
            assert False
        
        def on_open():
            assert source.ready_state == sse_client.READY_STATE_OPEN

        source = sse_client.EventSource(
            WPT_SERVER.replace('eventsource', 'common/redirect.py?'
            'location=/eventsource/resources/message.py&status='
            + str(status)),
            on_open=on_open,
            on_error=on_error)
        await source.connect()
        await source.close()

    await test(301)
    await test(302)
    await test(303)
    await test(307)


async def test_rquest_status_error():
    """Test EventSource: redirect.
    
    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/request-status-error.htm
    """
    async def test(status):
        def on_error():
            assert source.ready_state == sse_client.READY_STATE_CLOSED

        def on_message():
            assert source.ready_state == sse_client.READY_STATE_OPEN

        source = sse_client.EventSource(
            WPT_SERVER + 'resources/status-error.py?status=' + str(status),
            on_message=on_message,
            on_error=on_error)
        with pytest.raises(ConnectionError):
            await source.connect()

    await test(204)
    await test(205)
    await test(210)
    await test(299)
    await test(404)
    await test(410)
    await test(503)
