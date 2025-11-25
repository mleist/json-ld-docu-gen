from generator.puml.base import Base as Gen_Base
from utilities.global_logger_manager import get_generator_logger

logger = get_generator_logger()


class OrgUnit(Gen_Base):

    def __init__(self):
        Gen_Base.__init__(self)

    def seq_pre(self, puml_fp):
        logger.debug(f"generator.OrgUnit.pre() [{self}]")
        print(f'participant "{self.name}" as {self.puml_uri()} #A0A020', file=puml_fp)

    def seq_post(self, puml_fp):
        logger.debug(f"generator.OrgUnit.post() [{self}]")
