#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `aiohttp_sse_client` package."""
from aiohttp_sse_client import aiohttp_sse_client as sse_client


async def test_content():
    """Sample pytest test function with the pytest fixture as an argument."""
    messages = []
    async with sse_client.EventSource(
        'https://stream.wikimedia.org/v2/stream/recentchange'
    ) as es:
        async for message in es.process():
            if len(messages) > 0:
                break
            messages.append(message)

    assert messages[0].type == 'message'
    assert messages[0].origin == 'https://stream.wikimedia.org'
