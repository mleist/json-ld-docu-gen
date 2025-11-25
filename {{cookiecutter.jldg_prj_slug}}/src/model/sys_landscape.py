from model.base import Base as Model_Base
from utilities.global_logger_manager import get_model_logger

logger = get_model_logger()


class SysLandscape(Model_Base):

    def __init__(self, uri):
        self.functions = []
        self.locations = []
        self.organisations = []
        self.products = []
        self.processes = []
        self.procdata = []
        Model_Base.__init__(self, uri)
        self.name = self.query_val("simulation:name")[0]

    def add_Org(self, org):
        logger.info(f"model.SysLandscape.add_Org({org})")
        self.organisations.append(org)

    def add_Product(self, product):
        logger.info(f"model.SysLandscape.add_Product({product})")
        self.products.append(product)

    def add_Function(self, function):
        logger.info(f"model.SysLandscape.add_Function({function})")
        self.functions.append(function)

    def add_Process(self, process):
        logger.info(f"model.SysLandscape.add_Process({process})"
                    f"   '{process.source.description}' -{process.name}-> '{process.target.description}'")
        self.processes.append(process)

    def add_ProcessData(self, procdata):
        logger.info(f"model.SysLandscape.add_ProcessData({procdata})")
        self.procdata.append(procdata)

    def get_PyObj(self, uri):
        logger.debug(f"model.SysLandscape.get_PyObj({uri})")
        objs = [obj for obj in self.all_items if str(obj.uri) == uri]
        try:
            return objs[0]
        except IndexError:
            return None

    @property
    def all_items(self):
        return (self.functions + self.locations + self.organisations +
                self.products + self.processes + self.procdata)
