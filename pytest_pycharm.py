# -*- coding: utf-8 -*-
import threading


def pytest_exception_interact(node, call, report):
    """
    Drop into PyCharm debugger, if available, on uncaught exceptions.
    """
    try:
        import pydevd
        from pydevd import pydevd_tracing
    except ImportError:
        pass
    else:
        exctype, value, traceback = call.excinfo._excinfo
        frames = []
        while traceback:
            frames.append(traceback.tb_frame)
            traceback = traceback.tb_next
        thread = threading.current_thread()
        frames_by_id = dict([(id(frame), frame) for frame in frames])
        frame = frames[-1]
        exception = (exctype, value, traceback)
        thread.additional_info.pydev_message = 'test fail'
        try:
            debugger = pydevd.debugger
        except AttributeError:
            debugger = pydevd.get_global_debugger()
        pydevd_tracing.SetTrace(None)  # no tracing from here
        debugger.handle_post_mortem_stop(thread, frame, frames_by_id, exception)

    return report
