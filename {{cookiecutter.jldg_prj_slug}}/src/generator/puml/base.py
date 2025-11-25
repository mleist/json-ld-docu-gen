from utilities.tools import uri2puml_id
from utilities.global_logger_manager import get_generator_logger

logger = get_generator_logger()


class Base:
    LEGEND_DICT = {
        '00_function': '|<$COL_FUNCTION> Function | <#gainsboro> <color:grey>Aspect</color> |',
        '00_location': '|<$COL_LOCATION> Location | <#gainsboro> <color:grey>Aspect</color> |',
        '00_organisation': '|<$COL_ORGANISATION> Organisation | <#gainsboro> <color:grey>Aspect</color> |',
        '00_product': '|<$COL_PRODUCT> Product | <#gainsboro> <color:grey>Aspect</color> |',
        '01_process': '|<$COL_PROCESS> Process | <#gainsboro> <color:grey>Aspect</color> |',
        '10_domain': '|<$COL_DOMAIN> Domain | <#gainsboro> <color:grey>Meta Model</color> |',
        '11_subdomain': '|<$COL_SUBDOMAIN> Subdomain | <#gainsboro> <color:grey>Meta Model</color> |',
        '12_business_term': '|<$COL_BUSINESS_TERM> Buisiness Term | <#gainsboro> <color:grey>Meta Model</color> |',
        '20_system': '|<$COL_SYSTEM> System | <#gainsboro> <color:grey>Meta Model</color> |',
        '21_sub_system': '|<$COL_SUB_SYSTEM> Sub System | <#gainsboro> <color:grey>Meta Model</color> |'
    }

    def __init__(self):
        if ('sys_landscape' in self.__dict__) and (hasattr(self.sys_landscape, 'detail')):
            self.detail = self.sys_landscape.detail

    def seq_generate(self, puml_fp):
        logger.debug(f"generator.Base.seq_generate() [{self}]")
        self.seq_pre(puml_fp)
        self.seq_post(puml_fp)

    def seq_pre(self, puml_fp):
        logger.debug(f"generator.Base.seq_pre()")

    def seq_post(self, puml_fp):
        logger.debug(f"generator.Base.seq_post()")

    def topo_generate(self, puml_fp):
        logger.debug(f"generator.Base.topo_generate() [{self}]")
        self.topo_pre(puml_fp)
        self.topo_post(puml_fp)

    def topo_pre(self, puml_fp):
        logger.debug(f"generator.Base.topo_pre()")

    def topo_post(self, puml_fp):
        logger.debug(f"generator.Base.topo_post()")

    def puml_uri(self):
        return uri2puml_id(self.uri)

    def append_legend(self, entry):
        self.legend[entry] = self.LEGEND_DICT[entry]

    def complete_legend(self):
        for entry in ['00_function', '00_location', '00_organisation', '00_product',
                      '01_process',
                      '10_domain', '11_subdomain',
                      '12_business_term',
                      '20_system', '21_sub_system']:
            self.append_legend(entry)
