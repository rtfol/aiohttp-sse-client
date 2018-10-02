#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `aiohttp_sse_client` package."""
import json

from aiohttp_sse_client import client as sse_client


async def test_basic_usage():
    """Test basic usage."""
    messages = []
    async with sse_client.EventSource(
        'https://stream.wikimedia.org/v2/stream/recentchange'
    ) as event_source:
        async for message in event_source:
            if len(messages) > 1:
                break
            messages.append(message)

    print(messages)
    assert messages[0].type == 'message'
    assert messages[0].origin == 'https://stream.wikimedia.org'
    assert messages[1].type == 'message'
    assert messages[1].origin == 'https://stream.wikimedia.org'
    data_0 = json.loads(messages[0].data)
    data_1 = json.loads(messages[1].data)
    assert data_0['id'] != data_1['id']
