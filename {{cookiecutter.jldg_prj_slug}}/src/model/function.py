from model.base import Base as Model_Base
from utilities.global_logger_manager import get_model_logger

logger = get_model_logger()


class Function(Model_Base):

    def __init__(self, uri):
        Model_Base.__init__(self, uri)
        logger.debug(f"Function.__init__({uri})")
        self.name = self.query_val("function:name")[0]
        self.description = self.query_val("function:description")[0]
        self.tags = set(self.query_val("function:tags"))


    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return Model_Base.__str__(self)
