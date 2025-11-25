from generator.puml import ProcessData as GenPuml_ProcessData
from model import ProcessData as Model_ProcessData
from simulator.base import Base as Simulator_Base

from utilities.global_logger_manager import get_simulator_logger

logger = get_simulator_logger()


class ProcessData(Model_ProcessData,
                  GenPuml_ProcessData,
                  Simulator_Base):
    def __init__(self, sys_landscape, uri):
        self.sys_landscape = sys_landscape
        Model_ProcessData.__init__(self, uri)
        GenPuml_ProcessData.__init__(self)
        Simulator_Base.__init__(self)
