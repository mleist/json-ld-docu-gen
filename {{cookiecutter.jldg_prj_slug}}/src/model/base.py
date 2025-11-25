from pprint import pprint
import json

from rdflib import ConjunctiveGraph, Graph
import requests
from pyld import jsonld

from puml_namespaces import bind_all_ns
from utilities.global_logger_manager import get_model_logger

logger = get_model_logger()


class Base:
    def __init__(self, uri):
        self.uri = uri
        self.model_data = {}
        # on big graph for all
        if hasattr(self, 'sys_landscape'):
            self.graph = self.sys_landscape.graph
        else:
            self.graph = ConjunctiveGraph()
            bind_all_ns(self.graph)
        self.get_from_json_ld()

    def parse_data(self, url):
        self.graph.parse(url)

    def get_from_json_ld(self):
        if not self.uri:
            logger.error("model.Base.get_from_json_ld(): no uri")
            raise ValueError("No URI provided")

        try:
            # JSON-LD laden
            response = requests.get(self.uri)
            response.raise_for_status()
            document = response.json()

            # PyLD kompaktiert und validiert automatisch
            compacted = jsonld.compact(document, document.get('@context'))

            # RDF-Graph direkt mit JSON-LD String befüllen
            if not hasattr(self, 'graph'):
                self.graph = Graph()

            # JSON-LD als String für rdflib
            jsonld_string = json.dumps(compacted)
            self.graph.parse(data=jsonld_string, format='json-ld')

        except jsonld.JsonLdError as e:
            logger.error(f"JSON-LD validation failed: {e}")
            raise
        except requests.RequestException as e:
            logger.error(f"Failed to load JSON-LD from {self.uri}: {e}")
            raise

    def old_get_from_json_ld(self):
        if not self.uri:
            print("model.Base.get_from_json_ld(): no uri")
            exit(1)
        self.parse_data(self.uri)

    def model_print(self):
        pprint(self.model_data)

    def graph_print(self):
        print(self.graph.serialize(format="json-ld",
                                   # context=context,
                                   auto_compact=True))

    def query_val_old(self, val):
        knows_query = f"""
        SELECT ?id ?val WHERE
        {{
            ?id {val} ?val .
        }}"""
        qres = self.graph.query(knows_query)
        return str(qres.bindings[0]['id']), str(qres.bindings[0]['val'])

    def query_val_old2(self, praed):
        knows_query = f"""
        SELECT ?val WHERE
        {{
            <{self.uri}> {praed} ?val .
        }}"""
        qres = self.graph.query(knows_query)
        if len(qres.bindings) != 1:
            pass
            # print(f"model.Base.query_val(): {knows_query}")
        try:
            ret_val = qres.bindings[0]['val']
            return str(ret_val)
        except IndexError:
            pass
        return None

    def query_val(self, praed):
        knows_query = f"""
        SELECT ?val WHERE
        {{
            <{self.uri}> {praed} ?val .
        }}"""
        qres = self.graph.query(knows_query)
        values = []
        for binding in qres.bindings:
            try:
                val = str(binding['val'])
                values.append(val)
            except (KeyError, IndexError):
                pass
        return values if values else []

    def sorted_values_list(self, subject):
        values = []
        dd = self.graph.predicate_objects(subject.uri)
        for pred, obj in dd:
            value = {
                "ns": pred.split('/')[-2],
                "key": pred.split('/')[-1],
                "ns_key": f"{pred.split('/')[-2]}:{pred.split('/')[-1]}",
                "value": str(obj)
            }
            values.append(value)
        return sorted(values, key=lambda x: x['ns'] + x['key'])
