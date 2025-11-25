import logging
import sys

from utilities.tools import ContextFilter


class Logger:
    def __init__(self):
        self.handler_stdout = logging.StreamHandler(sys.stdout)
        self.formatter = logging.Formatter(
            "[%(simtime)7.1f] %(levelname)07s - %(message)-145s " +
            "{%(name)s:%(filename)s:%(lineno)d}")
        self.handler_stdout.setFormatter(self.formatter)
        self.LOG = {}

    def _get_dbg_level(self, level):
        if level == 1:
            return logging.WARNING
        elif level == 2:
            return logging.INFO
        elif level > 2:
            return logging.DEBUG
        else:
            return None

    def _addLogger(self, arg_name, arg_level, arg_handlers=[]):
        self.LOG[arg_name] = logging.getLogger(arg_name)
        cFilter = ContextFilter()
        if hasattr(self, 'env'):
            cFilter.env = self.env
        self.LOG[arg_name].addFilter(cFilter)
        self.LOG[arg_name].setLevel(arg_level)
        for handler in arg_handlers:
            self.LOG[arg_name].addHandler(handler)

    def set_loglevel(self, debug_name, dbg_level):
        level_model = self._get_dbg_level(dbg_level)
        if level_model is None:
            level_model = logging.ERROR
        self._addLogger(debug_name, level_model,
                        [self.handler_stdout])

    @property
    def LOG_model(self):
        return self.LOG["model"]

    @property
    def LOG_generator(self):
        return self.LOG["generator"]

    @property
    def LOG_events(self):
        return self.LOG["event"]

    @property
    def LOG_simulate(self):
        return self.LOG["simulate"]
