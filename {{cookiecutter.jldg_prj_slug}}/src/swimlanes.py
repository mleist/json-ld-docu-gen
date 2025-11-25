#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

import simulator
from utilities.global_logger_manager import logger_manager


@click.command()
@click.option('--data_uri',
              help='URI of input data file, e.g. "http://data.amp.net:8880/simulations/e59758b5-5576-42ef-ab06-c9cf076a461f"')
@click.option('--puml_out',
              help='Output filename for PlantUML')
@click.option('--detail', type=click.IntRange(0, 2), default=0,
              help='Detail-Grad (0-2)', show_default=True)
@click.option('--debug', count=True, help='debug, multiple times for more verbosity')
@click.option('--gentag', multiple=True,
              help='Tags for filtering in generation (can be specified multiple times)')
def main(data_uri, puml_out, detail, debug, gentag):
    logger_manager.configure_from_cli(debug=debug)
    gentags = set(gentag) if gentag else None
    sim_sysLandscape = simulator.SysLandscape(data_uri, detail, gentags)
    sim_sysLandscape.get_parts()
    sim_sysLandscape.get_processes()
    puml_fp = open(puml_out, 'w')
    sim_sysLandscape.seq_generate(puml_fp)
    puml_fp.close()

if __name__ == '__main__':
    main()

