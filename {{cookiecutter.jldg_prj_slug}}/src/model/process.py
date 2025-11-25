from model.base import Base as Model_Base
from utilities.global_logger_manager import get_model_logger

logger = get_model_logger()


class Process(Model_Base):

    def __init__(self, uri):
        Model_Base.__init__(self, uri)
        logger.debug(f"Process.__init__({uri})")
        self.name = self.query_val("process:name")[0]
        self.source_uri = self.query_val("process:source")[0]
        self.target_uri = self.query_val("process:target")[0]
        self.source_data_uri = self.query_val("process:source_data")[0]

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return Model_Base.__str__(self)
