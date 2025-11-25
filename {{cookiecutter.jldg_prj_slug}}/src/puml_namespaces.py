from rdflib import Namespace

all_ns_list = ['functions',
               'locations',
               'organisations',
               'products',
               'processes',
               'procdata_delivery',
               'procdata_inspection',
               'procdata_order',
               'simulations']


def bind_all_ns(graph):
    graph.bind("base", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/base/"))
    graph.bind("function", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/function/"))
    graph.bind("location", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/location/"))
    graph.bind("organisation", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/organisation/"))
    graph.bind("product", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/product/"))
    graph.bind("process", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/process/"))
    graph.bind("procdata_delivery", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/procdata_delivery/"))
    graph.bind("procdata_inspection", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/procdata_inspection/"))
    graph.bind("procdata_order", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/procdata_order/"))
    graph.bind("simulation", Namespace("{{cookiecutter.jldg_uri_type_prot}}://{{cookiecutter.jldg_uri_type_host}}:{{cookiecutter.jldg_uri_type_port}}/simulation/"))
