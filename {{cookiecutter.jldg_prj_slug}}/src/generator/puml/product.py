from generator.puml.base import Base as Gen_Base
from utilities.global_logger_manager import get_generator_logger
from utilities.tools import uri2puml_id

logger = get_generator_logger()


class Product(Gen_Base):

    def __init__(self):
        Gen_Base.__init__(self)

    def seq_pre(self, puml_fp):
        logger.debug(f"generator.Product.seq_pre() [{self}]")
        print(f'participant "{self.name}" as {self.puml_uri()} #add8e6', file=puml_fp)

    def seq_post(self, puml_fp):
        logger.debug(f"generator.Product.seq_post() [{self}]")

    def topo_pre(self, puml_fp):
        logger.debug(f"generator.Product.topo_pre() [{self}]")
        if self.detail >= 0:
            print(f'class "{self.name}" as {self.puml_uri()} $COL_PRODUCT', file=puml_fp)
        if self.detail >= 1:
            print(f'"{self.puml_uri()}" : description = "{self.description}"', file=puml_fp)
        if self.detail >= 2:
            manufacturer = self.query_val("product:manufacturer")[0]
            if manufacturer:
                print(f'"{self.puml_uri()}" : manufacturer = "{manufacturer}"', file=puml_fp)
            serial_number = self.query_val("product:serial_number")[0]
            if serial_number:
                print(f'"{self.puml_uri()}" : serial_number = "{serial_number}"', file=puml_fp)

    def topo_post(self, puml_fp):
        logger.debug(f"generator.Product.topo_post() [{self}]")

    def topo_get_links(self, puml_fp, objs_seen, all_links):
        logger.debug(f"generator.Product.topo_get_links() [{self}]")
        # knows_query = """
        # SELECT DISTINCT ?a ?b
        # WHERE
        # {
        #     ?a product:isPartOf ?b .
        # }"""
        # qres = self.sys_landscape.graph.query(knows_query)
        # for row in qres:
        #     source_id = uri2puml_id(row.a)
        #     target_id = uri2puml_id(row.b)
        #     if source_id in objs_seen and target_id in objs_seen:
        #         all_links.add((source_id, target_id, 'isPartOf'))
        knows_query = """
        SELECT DISTINCT ?a ?b
        WHERE
        {
            ?a product:hasPart ?b .
        }"""
        qres = self.sys_landscape.graph.query(knows_query)
        for row in qres:
            source_id = uri2puml_id(row.a)
            target_id = uri2puml_id(row.b)
            if source_id in objs_seen and target_id in objs_seen:
                all_links.add((source_id, target_id, 'hasPart'))
        knows_query = """
        SELECT DISTINCT ?a ?b
        WHERE
        {
            ?a product:providesFunction ?b .
        }"""
        qres = self.sys_landscape.graph.query(knows_query)
        for row in qres:
            source_id = uri2puml_id(row.a)
            target_id = uri2puml_id(row.b)
            if source_id in objs_seen and target_id in objs_seen:
                all_links.add((source_id, target_id, 'providesFunction'))
