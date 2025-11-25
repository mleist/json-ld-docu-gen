import logging
import sys
from utilities.tools import ContextFilter

class GlobalLoggerManager:
    """Singleton Logger Manager für modulübergreifendes Logging"""
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.handler_stdout = logging.StreamHandler(sys.stdout)
            self.formatter = logging.Formatter(
                "[%(simtime)7.1f] %(levelname)07s - %(message)-145s " +
                "{%(name)s:%(filename)s:%(lineno)d}")
            self.handler_stdout.setFormatter(self.formatter)
            self._loggers = {}
            self._env = None
            GlobalLoggerManager._initialized = True
    
    def set_env(self, env):
        """Setze SimPy Environment für alle Logger"""
        self._env = env
        # Update alle bestehenden Logger
        for logger in self._loggers.values():
            for handler in logger.handlers:
                for filter_obj in handler.filters:
                    if hasattr(filter_obj, 'env'):
                        filter_obj.env = env
    
    def configure_from_cli(self, debug=0):
        """Konfiguriere Logger basierend auf CLI-Argumenten"""
        self._setup_logger('model', debug)
        self._setup_logger('simulator', debug)
        self._setup_logger('generator', debug)
    
    def _get_dbg_level(self, level):
        """Konvertiere Level-Count zu Logging-Level"""
        if level == 1:
            return logging.WARNING
        elif level == 2:
            return logging.INFO
        elif level > 2:
            return logging.DEBUG
        else:
            return logging.ERROR
    
    def _setup_logger(self, name: str, level_count: int):
        """Erstelle oder aktualisiere Logger für gegebenes Modul"""
        if name in self._loggers:
            # Logger bereits vorhanden, nur Level ändern
            log_level = self._get_dbg_level(level_count)
            self._loggers[name].setLevel(log_level)
        else:
            # Neuen Logger erstellen
            logger = logging.getLogger(name)
            logger.handlers.clear()  # Bestehende Handler entfernen
            
            # Context Filter hinzufügen
            cFilter = ContextFilter()
            if self._env:
                cFilter.env = self._env
            logger.addFilter(cFilter)
            
            # Level setzen
            log_level = self._get_dbg_level(level_count)
            logger.setLevel(log_level)
            
            # Handler hinzufügen
            logger.addHandler(self.handler_stdout)
            
            self._loggers[name] = logger
    
    def get_logger(self, name: str) -> logging.Logger:
        """Gib Logger für gegebenes Modul zurück"""
        if name not in self._loggers:
            self._setup_logger(name, 0)  # Default ERROR level
        return self._loggers[name]

# Globale Instanz
logger_manager = GlobalLoggerManager()

# Convenience Functions für die Module
def get_model_logger() -> logging.Logger:
    return logger_manager.get_logger('model')

def get_simulator_logger() -> logging.Logger:
    return logger_manager.get_logger('simulator')

def get_generator_logger() -> logging.Logger:
    return logger_manager.get_logger('generator')
