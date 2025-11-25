set -x

python src/topo.py --puml_out=puml_generated/topo_01.puml --data_uri={{cookiecutter.jldg_uri_data_prot}}://{{cookiecutter.jldg_uri_data_host}}:{{cookiecutter.jldg_uri_data_port}}/simulations/2be950b7-144e-45c9-9e9d-f6b856535044 --detail 0
python src/topo.py --puml_out=puml_generated/topo_02.puml --data_uri={{cookiecutter.jldg_uri_data_prot}}://{{cookiecutter.jldg_uri_data_host}}:{{cookiecutter.jldg_uri_data_port}}/simulations/2be950b7-144e-45c9-9e9d-f6b856535044 --detail 2 --gentag=pumpe
python src/topo.py --puml_out=puml_generated/topo_03.puml --data_uri={{cookiecutter.jldg_uri_data_prot}}://{{cookiecutter.jldg_uri_data_host}}:{{cookiecutter.jldg_uri_data_port}}/simulations/2be950b7-144e-45c9-9e9d-f6b856535044 --detail 2 --gentag=hgü

python src/swimlanes.py --puml_out=puml_generated/swim_01.puml --data_uri={{cookiecutter.jldg_uri_data_prot}}://{{cookiecutter.jldg_uri_data_host}}:{{cookiecutter.jldg_uri_data_port}}/simulations/e43b1486-db8e-4c5f-afa2-0ea0c2fb4625
python src/swimlanes.py --puml_out=puml_generated/swim_02.puml --data_uri={{cookiecutter.jldg_uri_data_prot}}://{{cookiecutter.jldg_uri_data_host}}:{{cookiecutter.jldg_uri_data_port}}/simulations/e59758b5-5576-42ef-ab06-c9cf076a461f

docker run -it --rm -v "$(pwd):/docs" docker-sphinx-generator:2025.11 make latexpdf
