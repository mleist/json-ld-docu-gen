from generator.puml import Process as GenPuml_Process
from model import Process as Model_Process
from simulator.base import Base as Simulator_Base

from utilities.global_logger_manager import get_simulator_logger

logger = get_simulator_logger()


class Process(Model_Process,
              GenPuml_Process,
              Simulator_Base):
    def __init__(self, sys_landscape, uri):
        self.sys_landscape = sys_landscape
        Model_Process.__init__(self, uri)
        GenPuml_Process.__init__(self)
        Simulator_Base.__init__(self)
        self.source = sys_landscape.get_PyObj(self.source_uri)
        self.target = sys_landscape.get_PyObj(self.target_uri)
        self.source_data = sys_landscape.get_PyObj(self.source_data_uri)
