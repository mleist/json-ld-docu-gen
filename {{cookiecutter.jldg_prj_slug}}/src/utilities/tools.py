import logging


class ContextFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(self, 'env'):
            record.simtime = -999.0
        else:
            record.simtime = self.env.now
        return True


def uri2puml_id(uri):
    return uri.replace(':', '_').replace('/', '_').replace('-', '_')
