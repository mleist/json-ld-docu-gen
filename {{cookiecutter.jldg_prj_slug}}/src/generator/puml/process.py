from generator.puml.base import Base as Gen_Base
from utilities.tools import uri2puml_id
from utilities.global_logger_manager import get_generator_logger

logger = get_generator_logger()


class Process(Gen_Base):

    def __init__(self):
        Gen_Base.__init__(self)

    def seq_generate(self, puml_fp):
        self.seq_pre(puml_fp)
        print(f'{self.puml_source_uri()}'
              ' -[$COL_PROCESS]> '
              f'{self.puml_target_uri()}',
              f' : <color:$COL_PROCESS>{self.name}</color>',
              file=puml_fp)

        print(f"""note left #gainsboro""",
              file=puml_fp)

        sorted_values = self.sorted_values_list(self.source_data)
        for lifecycle_val in self.sys_landscape.lifecycle_sum.values():
            lifecycle_val['state'] = 'unchanged'
        for value in sorted_values:
            if value['ns_key'] not in self.sys_landscape.lifecycle_sum:
                value['state'] = 'added'
                self.sys_landscape.lifecycle_sum[value['ns_key']] = value
            else:
                if value['value'] != self.sys_landscape.lifecycle_sum[value['ns_key']]['value']:
                    self.sys_landscape.lifecycle_sum[value['ns_key']]['state'] = 'modified'
                else:
                    self.sys_landscape.lifecycle_sum[value['ns_key']]['state'] = 'unchanged'

        for lifecycle_key, lifecycle_val in sorted(self.sys_landscape.lifecycle_sum.items()):
            if lifecycle_val['state'] == 'added':
                print(f"""| <$COL_STATE_ADDED><color:grey>{lifecycle_val['ns']}:</color>{lifecycle_val['key']} """
                      f"""| <$COL_STATE_ADDED>{lifecycle_val['value']} |""",
                      file=puml_fp)
            elif lifecycle_val['state'] == 'modified':
                print(f"""| <$COL_STATE_MODIFIED><color:grey>{lifecycle_val['ns']}:</color>{lifecycle_val['key']} """
                      f"""| <$COL_STATE_MODIFIED>{lifecycle_val['value']} |""",
                      file=puml_fp)
            elif lifecycle_val['state'] == 'unchanged':
                print(f"""| <$COL_STATE_UNCHANGED><color:grey>{lifecycle_val['ns']}:</color>{lifecycle_val['key']} """
                      f"""| <$COL_STATE_UNCHANGED>{lifecycle_val['value']} |""",
                      file=puml_fp)
            else:
                raise ValueError(f"Unknown lifecycle state: {lifecycle_val['state']}")

        print(f"""end note""",
              file=puml_fp)
        self.seq_post(puml_fp)

    def seq_pre(self, puml_fp):
        logger.debug(f"generator.Process.pre() [{self}]")

    def seq_post(self, puml_fp):
        logger.debug(f"generator.Process.post() [{self}]")

    def puml_source_uri(self):
        return uri2puml_id(self.source_uri)

    def puml_target_uri(self):
        return uri2puml_id(self.target_uri)
