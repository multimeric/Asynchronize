# Asynchronize
## Introduction
Asynchronize is designed for situations where you are using a library that provides a callback interface, but you want
to work with the convenience of `await` or `async for`.

## Installation
To install Asynchronize, run:
```bash
pip install asynchronize
```

## Examples
### Async Generator
First, let's say you're working with a library that's designed to call `step_callback` each time it receives a new chunk of data, and then `end_callback` once it's finished.
[`sounddevice.InputStream`](https://github.com/spatialaudio/python-sounddevice) works like this:
```python
library = MultiThreadedLibrary(
    step_callback=step_callback,
    end_callback=end_callback
)
```

With [`sounddevice.InputStream`](https://github.com/spatialaudio/python-sounddevice), this looks like:
```python
import sounddevice as sd

sd.InputStream(
    channels=2,
    callback=step_callback,
    finished_callback=finished_callback
)
```

To convert this library into an [async generator](https://www.python.org/dev/peps/pep-0525/) you can iterate with `async for`, all you need to do is instantiate `asynchronize.AsyncCallback`, and pass its methods into whatever is expecting the callbacks:
```python
import asynchronize

callback = asynchronize.AsyncCallback()
lib = MultiThreadedLibrary(
    step_callback=callback.step_callback,
    end_callback=callback.finished_callback,
)
lib.start()

async for val in callback:
    # Do something with val
    pass
```

### Awaitable Function
This time, let's assume that the library is designed to call a single callback once it's processed something, and after that it's done.
For example:
```python
lib = MultiThreadedLibrary(
    callback=callback,
)
```

To convert this library into an awaitable, instantiate `asynchronize.AsyncCallback` as before, but this time you only need to pass in the `finished_callback`:
```python
import asynchronize

callback = asynchronize.AsyncCallback()
lib = MultiThreadedLibrary(
    end_callback=callback.finished_callback
)
lib.start()

val = await callback
```

### More Examples
A more complicated, real-world example is available in [`example.py`](https://github.com/TMiguelT/Asynchronize/blob/master/example.py).

In addition, the unit tests can be a useful example on how to use the library, from end to end: [`test_general.py`](https://github.com/TMiguelT/Asynchronize/blob/master/test/test_general.py).

## API
Asynchronize is actually very simple.
The only public class is `asynchronize.AsyncCallback`, and its constructor has no arguments.
The only way to use the class is by passing `step_callback` or `finished_callback` to something that expects a callback.
That's all!
