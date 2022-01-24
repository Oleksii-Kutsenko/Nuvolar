#! /usr/bin/env python

import json
import os
import signal
import subprocess

import click

APPLICATION_CONFIG_PATH = "config"
DOCKER_PATH = "docker"


def setenv(variable, default):
    os.environ[variable] = os.getenv(variable, default)


def app_config_file(config):
    return os.path.join(APPLICATION_CONFIG_PATH, f"{config}.json")


def docker_compose_file(config):
    return os.path.join(DOCKER_PATH, f"{config}.yml")


def read_json_configuration(config):
    # Read configuration from the relative JSON file
    with open(app_config_file(config)) as f:
        config_data = json.load(f)
    # Convert the config into a usable Python dictionary
    config_data = dict((i['name'], i['value']) for i in config_data)

    return config_data


def configure_app(config):
    configuration = read_json_configuration(config)

    for key, value in configuration.items():
        setenv(key, value)


def docker_compose_cmdline(commands_string):
    config = os.getenv('FASTAPI_ENV')
    configure_app(config)

    compose_file = docker_compose_file(config)

    if not os.path.isfile(compose_file):
        raise ValueError(f'The file {compose_file} does not exist')

    command_line = [
        'docker-compose',
        '-p',
        config,
        '-f',
        compose_file
    ]

    if commands_string:
        command_line.extend(commands_string.split(' '))

    return command_line


@click.group()
def cli():
    pass


@cli.command(context_settings={'ignore_unknown_options': True})
@click.argument('subcommand', nargs=-1, type=click.Path())
def compose(subcommand):
    configure_app(os.getenv("FASTAPI_ENV"))
    cmdline = docker_compose_cmdline('') + list(subcommand)

    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


if __name__ == '__main__':
    cli()
