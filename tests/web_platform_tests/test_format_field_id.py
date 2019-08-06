#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from pytest import fail

from aiohttp_sse_client import client as sse_client

from .const import WPT_SERVER


async def test_format_field_id():
    """Test EventSource: Last-Event-ID.

    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/format-field-id.htm
    """
    seen_hello = False

    async with sse_client.EventSource(
        WPT_SERVER + 'resources/last-event-id.py',
    ) as source:
        async for e in source:
            if not seen_hello:
                assert e.data == "hello"
                seen_hello = True
                # default last event id is Unicode U+2026
                assert e.last_event_id == "…"
                last_id = e.last_event_id
            else:
                assert e.data == last_id
                assert e.last_event_id == last_id
                break


async def test_format_field_id_2():
    """Test EventSource: Last-Event-ID (2).

    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/format-field-id-2.htm
    """
    counter = 0

    async with sse_client.EventSource(
        WPT_SERVER + 'resources/last-event-id.py',
    ) as source:
        async for e in source:
            if counter == 0:
                counter += 1
                assert e.data == "hello"
                # default last event id is Unicode U+2026
                assert e.last_event_id == "…"
                last_id = e.last_event_id
            elif counter in (1, 2):
                counter += 1
                assert e.data == last_id
                assert e.last_event_id == last_id
                break
            else:
                fail("Unexpected counter {}".format(counter))


async def test_format_field_id_null():
    """Test EventSource: U+0000 in id field.

    ..seealso: https://github.com/web-platform-tests/wpt/blob/master/
    eventsource/format-field-id-null.htm
    """
    seen_hello = False

    async with sse_client.EventSource(
        WPT_SERVER + 'resources/last-event-id.py?idvalue=%00%00',
    ) as source:
        async for e in source:
            if not seen_hello:
                assert e.data == "hello"
                seen_hello = True
                # Unicode U+0000 will be ignored as Event ID
                assert e.last_event_id == ""
            else:
                assert e.data == "hello"
                assert e.last_event_id == ""
                break
