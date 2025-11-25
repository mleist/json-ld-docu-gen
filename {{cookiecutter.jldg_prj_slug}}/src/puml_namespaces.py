from rdflib import Namespace

all_ns_list = ['functions',
               'locations',
               'organisations',
               'products',
               'loc_amp_geod',
               'func_amp_aos',
               'prod_amp_aos',
               'prod_amp_bestand',
               'prod_amp_budget',
               'prod_amp_netzplanung',
               'processes',
               'procdata_delivery',
               'procdata_inspection',
               'procdata_order',
               'prod_amp_bestand_befund',
               'prod_amp_bestand_ereignis',
               'prod_amp_bestand_handlungsbed',
               'simulations']


def bind_all_ns(graph):
    graph.bind("base", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/base/"))
    graph.bind("function", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/function/"))
    graph.bind("location", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/location/"))
    graph.bind("organisation", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/organisation/"))
    graph.bind("product", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/product/"))
    graph.bind("loc_amp_geod", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/loc_amp_geod/"))
    graph.bind("func_amp_aos", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/func_amp_aos/"))
    graph.bind("prod_amp_aos", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_aos/"))
    graph.bind("prod_amp_bestand", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_bestand/"))
    graph.bind("prod_amp_budget", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_budget/"))
    graph.bind("prod_amp_netzplanung", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_netzplanung/"))
    graph.bind("process", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/process/"))
    graph.bind("procdata_delivery", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/procdata_delivery/"))
    graph.bind("procdata_inspection", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/procdata_inspection/"))
    graph.bind("procdata_order", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/procdata_order/"))
    graph.bind("simulation", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/simulation/"))
    graph.bind("prod_amp_bestand_befund", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_bestand_befund/"))
    graph.bind("prod_amp_bestand_ereignis", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_bestand_ereignis/"))
    graph.bind("prod_amp_bestand_handlungsbed", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/prod_amp_bestand_handlungsbed/"))
