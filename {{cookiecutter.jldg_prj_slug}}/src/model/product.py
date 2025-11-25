from model.base import Base as Model_Base
from utilities.global_logger_manager import get_model_logger

logger = get_model_logger()


class Product(Model_Base):

    def __init__(self, uri):
        Model_Base.__init__(self, uri)
        logger.debug(f"Product.__init__({uri})")
        self.name = self.query_val("product:name")[0]
        self.description = self.query_val("product:description")[0]
        self.tags = set(self.query_val("product:tags"))

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return Model_Base.__str__(self)
