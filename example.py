"""
Demonstrates the use of Asynchronize with python-sounddevice
"""

import asyncio
import asynchronize
import sounddevice as sd


async def sound_stats(callback):
    async for stats in callback:
        if len(stats.args) > 0:
            print(f"Mean: {stats.args[0].mean()}")
        else:
            print("Finishing stats")


async def record(time, callback):
    with sd.InputStream(channels=2, callback=callback.step_callback, finished_callback=callback.finished_callback):
        await asyncio.sleep(time)
        print("Finishing sleep")


async def main():
    callback = asynchronize.AsyncCallback()
    await asyncio.gather(
        record(1, callback),
        sound_stats(callback)
    )

asyncio.run(main())
