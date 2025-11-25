from generator.puml import Function as GenPuml_Function
from model import Function as Model_Function
from simulator.base import Base as Simulator_Base
from utilities.global_logger_manager import get_simulator_logger

logger = get_simulator_logger()


class Function(Model_Function,
              GenPuml_Function,
              Simulator_Base):
    def __init__(self, sys_landscape, uri):
        self.sys_landscape = sys_landscape
        Model_Function.__init__(self, uri)
        GenPuml_Function.__init__(self)
        Simulator_Base.__init__(self)
