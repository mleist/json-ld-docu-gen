import rdflib

from generator.puml import SysLandscape as GenPuml_SysLandscape
from model import SysLandscape as Model_SysLandscape
from simulator.base import Base as Simulator_Base
import simulator
from utilities.global_logger_manager import get_simulator_logger

logger = get_simulator_logger()


class SysLandscape(Model_SysLandscape,
                   GenPuml_SysLandscape,
                   Simulator_Base):
    def __init__(self, uri, detail, gentags):
        Model_SysLandscape.__init__(self, uri)
        GenPuml_SysLandscape.__init__(self, detail, gentags)
        Simulator_Base.__init__(self)
        self.lifecycle_sum = {}

    def get_parts(self):
        hasPartsIt = self.graph.objects(predicate=rdflib.term.URIRef('http://type.amp.net:8880/simulation/hasPart'))
        for hasPart in hasPartsIt:
            (o_type, o_uuid) = hasPart.split('/')[-2:]
            match o_type:
                case 'organisations':
                    org = simulator.OrgUnit(self,
                                            hasPart)
                    self.add_Org(org)
                case 'products':
                    product = simulator.Product(self,
                                                hasPart)
                    self.add_Product(product)
                case 'functions':
                    function = simulator.Function(self,
                                                hasPart)
                    self.add_Function(function)

    def get_processes(self):
        processesIt = self.graph.objects(predicate=rdflib.term.URIRef('http://type.amp.net:8880/simulation/processes'))
        for process in processesIt:
            (o_type, o_uuid) = process.split('/')[-2:]
            match o_type:
                case 'processes':
                    process = simulator.Process(self,
                                                process)
                    self.add_Process(process)
                case 'procdata_delivery' | 'procdata_inspection' | 'procdata_order':
                    procdata = simulator.ProcessData(self,
                                                     process)
                    self.add_ProcessData(procdata)
