import asyncio
class run_async_task:
    def __init__(self):
        pass
    def run_async_task(self, coro):
        """Helper để khởi tạo event loop mới cho mỗi luồng task"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(coro)
        finally:
            loop.close()