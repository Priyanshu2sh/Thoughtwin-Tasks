import asyncio
async def funnc():
    print("Hello")
    await asyncio.sleep(2)
    print("asassa")

asyncio.run(funnc())