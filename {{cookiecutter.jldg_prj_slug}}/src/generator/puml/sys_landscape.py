from generator.puml.base import Base as Gen_Base
from utilities.global_logger_manager import get_generator_logger

logger = get_generator_logger()


class SysLandscape(Gen_Base):

    def __init__(self, detail, gentags):
        Gen_Base.__init__(self)
        self.detail = detail
        self.gentags = gentags
        self.puml_start = "startuml"
        self.puml_end = "enduml"
        self.legend = {}

    def seq_generate(self, puml_fp):
        self.seq_pre(puml_fp)
        for org in self.organisations:
            self.append_legend('00_organisation')
            org.seq_generate(puml_fp)
        for product in self.products:
            self.append_legend('00_product')
            product.seq_generate(puml_fp)
        for process in self.processes:
            self.append_legend('01_process')
            process.seq_generate(puml_fp)
        self.seq_post(puml_fp)

    def seq_pre(self, puml_fp):
        logger.debug(f"generator.SysLandscape.seq_pre()")
        print(f"@{self.puml_start}", file=puml_fp)
        print(f"!include ../puml/include_auto.puml", file=puml_fp)
        print(f"autonumber", file=puml_fp)
        print(f"!pragma teoz true", file=puml_fp)

    def seq_post(self, puml_fp):
        Gen_Base.seq_post(self, puml_fp)
        logger.debug(f"generator.SysLandscape.seq_post()")
        # self.complete_legend()
        print(f"legend right", file=puml_fp)
        for key, value in sorted(self.legend.items()):
            print(value, file=puml_fp)
        print(f"endlegend", file=puml_fp)
        print(f"@{self.puml_end}", file=puml_fp)

    def topo_generate(self, puml_fp):
        self.topo_pre(puml_fp)
        objs_seen = {}
        for org in self.organisations:
            self.append_legend('00_organisation')
            # org.topo_generate(puml_fp)
        for function in self.functions:
            if self.gentags:
                if self.gentags & function.tags:
                    self.append_legend('00_function')
                    function.topo_generate(puml_fp)
                    objs_seen[function.puml_uri()] = function
            else:
                self.append_legend('00_function')
                function.topo_generate(puml_fp)
                objs_seen[function.puml_uri()] = function
        for product in self.products:
            if self.gentags:
                if self.gentags & product.tags:
                    self.append_legend('00_product')
                    product.topo_generate(puml_fp)
                    objs_seen[product.puml_uri()] = product
            else:
                self.append_legend('00_product')
                product.topo_generate(puml_fp)
                objs_seen[product.puml_uri()] = product
        for process in self.processes:
            self.append_legend('01_process')
            # process.topo_generate(puml_fp)

        all_links = set()
        for function in self.functions:
            function.topo_get_links(puml_fp, objs_seen, all_links)
        for product in self.products:
            product.topo_get_links(puml_fp, objs_seen, all_links)
        for link in all_links:
            print(f'"{link[0]}" --> "{link[1]}" : {link[2]}', file=puml_fp)
        self.topo_post(puml_fp)

    def topo_pre(self, puml_fp):
        logger.debug(f"generator.SysLandscape.topo_pre()")
        print(f"@{self.puml_start}", file=puml_fp)
        print(f"!include ../puml/include_auto.puml", file=puml_fp)
        # print(f"autonumber", file=puml_fp)
        # print(f"!pragma teoz true", file=puml_fp)

    def topo_post(self, puml_fp):
        Gen_Base.topo_post(self, puml_fp)
        logger.debug(f"generator.SysLandscape.topo_post()")
        # self.complete_legend()
        print(f"legend right", file=puml_fp)
        print(f"", file=puml_fp)
        for key, value in sorted(self.legend.items()):
            print(value, file=puml_fp)
        print(f"endlegend", file=puml_fp)
        print(f"@{self.puml_end}", file=puml_fp)
