from model.base import Base as Model_Base
from utilities.global_logger_manager import get_model_logger

logger = get_model_logger()


class ProcessData(Model_Base):

    def __init__(self, uri):
        Model_Base.__init__(self, uri)
        logger.debug(f"ProcessData.__init__({uri})")
        self.name = self.query_val("procdata_order:name|procdata_inspection:name|procdata_delivery:name")[0]

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return Model_Base.__str__(self)
