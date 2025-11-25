from generator.puml import Product as GenPuml_Product
from model import Product as Model_Product
from simulator.base import Base as Simulator_Base
from utilities.global_logger_manager import get_simulator_logger

logger = get_simulator_logger()


class Product(Model_Product,
              GenPuml_Product,
              Simulator_Base):
    def __init__(self, sys_landscape, uri):
        self.sys_landscape = sys_landscape
        Model_Product.__init__(self, uri)
        GenPuml_Product.__init__(self)
        Simulator_Base.__init__(self)
