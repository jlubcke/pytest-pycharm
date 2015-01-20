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
        thread.additionalInfo.exception = (exctype, value, traceback)
        thread.additionalInfo.pydev_force_stop_at_exception = (frame, frames_by_id)
        thread.additionalInfo.message = "test fail"
        debugger = pydevd.debugger
        if hasattr(debugger, "force_post_mortem_stop"):
            debugger.force_post_mortem_stop += 1

        pydevd_tracing.SetTrace(None)
        debugger.handle_post_mortem_stop(thread.additionalInfo, thread)

    return report
