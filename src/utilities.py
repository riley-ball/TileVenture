import tkinter as tk


class Stepper:
    """Asynchronous control class to emulate non-blocking loop for
    tkinter GUI application by repeatedly runnning step function
    after a given interval

    Can be stopped/paused
    """

    def __init__(self, master: Union[tk.Widget, tk.Tk], delay: int = 30):
        """Constructor

        Parameters:
            master (tk.Widget|tk.Tk): The tkinter master widget
            delay (int): The number of milliseconds between each _step
                         (does not include time taken to run _step)
        """
        self._master = master
        self._step_number = -1
        self._paused = False
        self._delay = delay
        self._after_id = None

    def is_started(self):
        """(bool) Returns True iff the stepper is started"""
        return self._after_id is not None

    def is_stopped(self):
        """(bool) Returns True iff the stepper is stopped"""
        return self._after_id is None and not self._paused

    def is_paused(self):
        """(bool) Returns True iff the stepper is paused"""
        return self._paused

    def start(self):
        """Start the stepper"""
        if self.is_started():
            return
        self._paused = False
        self._after_id = self._master.after(self._delay, self._step_manager)

    def stop(self):
        """Stop the stepper & reset steps to 0"""
        if self.is_stopped():
            return
        if not self.is_paused():
            self._paused = False
            self._master.after_cancel(self._after_id)
            self._after_id = None
        self._step_number = -1

    def pause(self):
        """Pause the stepper (does not reset steps to 0)"""
        if self.is_paused() or self.is_stopped():
            return
        self._paused = True
        self._master.after_cancel(self._after_id)
        self._after_id = None

    def _step_manager(self):
        """Internal wrapper around step method to keep track of the number of steps and queue next step"""
        self._step_number += 1

        if self._step() and not self.is_stopped():
            self._after_id = self._master.after(
                self._delay, self._step_manager)

    def _step(self):
        """(bool) Performs a step

        Returns True if stepping should continue
        """
        raise NotImplementedError("_step must be implemented by a subclass")
