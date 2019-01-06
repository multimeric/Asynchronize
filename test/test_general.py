import threading
import time
import asynchronize
import pytest


class MultiThreadedLibrary:
    """
    Simulates some function that calls callbacks to report progress, on a different thread
    """

    def __init__(self, step_callback, end_callback, iterator):
        # If iterator is true, the step callback will be called multiple times
        if iterator:
            self.thread = threading.Thread(target=self.thread_run_iter)
        else:
            self.thread = threading.Thread(target=self.thread_run)

        self.step_callback = step_callback
        self.end_callback = end_callback

    def start(self):
        self.thread.start()

    def thread_run_iter(self):
        for i in range(10):
            # Simulate some processing
            time.sleep(0.1)

            self.step_callback(i)

        self.end_callback(i + 1)

    def thread_run(self):
        time.sleep(0.1)
        self.end_callback(True)


@pytest.mark.asyncio
async def test_multithreaded_iterator():
    """
    Test for the async iterator use-case
    """
    # Start the multithreaded simulation
    callback = asynchronize.AsyncCallback()
    lib = MultiThreadedLibrary(
        step_callback=callback.step_callback,
        end_callback=callback.finished_callback,
        iterator=True
    )
    lib.start()

    # Check all the return values
    i = 0
    async for val in callback:
        assert val.args[0] == i
        i += 1


@pytest.mark.asyncio
async def test_multithreaded_callback():
    """
    Test for the awaitable use-case
    """
    # Start the multithreaded simulation
    callback = asynchronize.AsyncCallback()
    lib = MultiThreadedLibrary(
        step_callback=callback.step_callback,
        end_callback=callback.finished_callback,
        iterator=False
    )
    lib.start()

    # Check the single return value
    val = await callback
    assert val.args[0] is True
