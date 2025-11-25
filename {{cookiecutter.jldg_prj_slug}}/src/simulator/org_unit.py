from generator.puml import OrgUnit as GenPuml_OrgUnit
from model import OrgUnit as Model_OrgUnit
from simulator.base import Base as Simulator_Base

from utilities.global_logger_manager import get_simulator_logger

logger = get_simulator_logger()


class OrgUnit(Model_OrgUnit,
              GenPuml_OrgUnit,
              Simulator_Base):
    def __init__(self, sys_landscape, uri):
        self.sys_landscape = sys_landscape
        Simulator_Base.__init__(self)
        Model_OrgUnit.__init__(self, uri)
        GenPuml_OrgUnit.__init__(self)
        logger.debug(f"{uri}")
