=====
Usage
=====

To use SSE Client in a project:

.. code-block:: python

    from aiohttp_sse_client import client as sse_client
    
    async with sse_client.EventSource(
        'https://stream.wikimedia.org/v2/stream/recentchange'
    ) as event_source:
        try:
            async for event in event_source:
                print(event)
        except ConnectionError:
            pass
