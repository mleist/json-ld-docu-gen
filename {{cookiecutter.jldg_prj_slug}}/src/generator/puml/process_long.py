from generator.puml.base import Base as Gen_Base
from utilities.tools import uri2puml_id


class Process(Gen_Base):

    def __init__(self):
        Gen_Base.__init__(self)

    def pre(self, puml_fp):
        self.logger.debug(f"generator.Process.pre() [{self}]")
        # print(f'participant "{self.name}" as {self.puml_uri()} #add8e6', file=puml_fp)

        print(f'{self.puml_source_uri()}'
              ' -> '
              f'{self.puml_target_uri()}',
              f' : {self.name}',
              file=puml_fp)

        print(f"""note left #lightgrey""",
              file=puml_fp)

        # print(f"""
        # | name | Pumpen Bestellung |
        # |<#lightgreen> order_date | 2019-06-30T12:30:00+02:00 |
        # | order_number | 123-456-789 |""", file=puml_fp)

        # dd = self.graph.predicate_objects(self.source_data.uri)
        # for pred, obj in dd:
        #     print(f"""| <color:grey>{pred.split('/')[-2]}:</color>{pred.split('/')[-1]} | {obj} |""", file=puml_fp)



        print("11111111")
        print(self.sorted_values_list(self.source_data))
        print("22222222")
        sorted_values = self.sorted_values_list(self.source_data)

        for lifecycle_val in self.sys_landscape.lifecycle_sum.values():
            lifecycle_val['state'] = 'unchanged'

        for value in sorted_values:
            if value['ns_key'] not in self.sys_landscape.lifecycle_sum:
                value['state'] = 'added'
                self.sys_landscape.lifecycle_sum[value['ns_key']] = value
                # print(f"""| <#lightgreen><color:grey>{value['ns']}:</color>{value['key']} | {value['value']} |""", file=puml_fp)
            else:
                if value['value'] != self.sys_landscape.lifecycle_sum[value['ns_key']]['value']:
                    self.sys_landscape.lifecycle_sum[value['ns_key']]['state'] = 'modified'
                else:
                    self.sys_landscape.lifecycle_sum[value['ns_key']]['state'] = 'unchanged'

        import pprint
        pprint.pprint(self.sys_landscape.lifecycle_sum)
        print("33333333")

        for lifecycle_key, lifecycle_val in sorted(self.sys_landscape.lifecycle_sum.items()):
            if lifecycle_val['state'] == 'added':
                print(f"""| <#lightgreen><color:grey>{lifecycle_val['ns']}:</color>{lifecycle_val['key']} | <#lightgreen>{lifecycle_val['value']} |""", file=puml_fp)
            elif lifecycle_val['state'] == 'modified':
                print(f"""| <#orange><color:grey>{lifecycle_val['ns']}:</color>{lifecycle_val['key']} | <#orange>{lifecycle_val['value']} |""", file=puml_fp)
            elif lifecycle_val['state'] == 'unchanged':
                print(f"""| <#lightgrey><color:grey>{lifecycle_val['ns']}:</color>{lifecycle_val['key']} | <#lightgrey>{lifecycle_val['value']} |""", file=puml_fp)
            else:
                raise ValueError(f"Unknown lifecycle state: {lifecycle_val['state']}")

        print(f"""end note""",
              file=puml_fp)




        # print(f"""note left #lightgrey
        #         | name | Pumpen Bestellung |
        #         |<#lightgreen> order_date | 2019-06-30T12:30:00+02:00 |
        #         | order_number | 123-456-789 |
        #         end note""", file=puml_fp)

        # print(f"""note left\n"""
        #       f"""**{self.source_data.name}**""",
        #       file=puml_fp)
        # print("<code>", file=puml_fp)
        # dd = self.graph.predicate_objects(self.source_data.uri)
        # x = PrettyTable()
        # x.align = "l"
        # for pred, obj in dd:
        #     x.add_row([f"{pred.split('/')[-1]}", f"{obj}"])
        #     # print(f"""<#E8E8E8,#E8E8E8>|{pred.split("/")[-1]}|{obj}|""",
        #     #       file=puml_fp)
        # print(x.get_string(border=False, header=False, left_padding_width=0, preserve_internal_border=True),
        #       file=puml_fp)
        #
        # lcm = PrettyTable()
        # lcm.align = "l"
        # lcm.add_row([1, 2])
        # print(lcm.get_string(border=False, header=False, left_padding_width=0, preserve_internal_border=True),
        #       file=puml_fp)
        #
        #
        #
        # print("</code>", file=puml_fp)
        # print(self.sys_landscape.lifecycle_sum)
        #
        # print(f"""end note""",
        #       file=puml_fp)

    def post(self, puml_fp):
        self.logger.debug(f"generator.Process.post() [{self}]")

    def puml_source_uri(self):
        return uri2puml_id(self.source_uri)

    def puml_target_uri(self):
        return uri2puml_id(self.target_uri)
