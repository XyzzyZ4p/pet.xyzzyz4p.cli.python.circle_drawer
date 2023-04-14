#!/usr/bin/env python3
import click

if __package__:
    from .src import Circle
else:
    from src import Circle


@click.command()
@click.option(
    '-d',
    '--diameter',
    required=True,
    type=int,
    help='Circle diameter.'
)
@click.option(
    '-t',
    '--type',
    default='full',
    show_default=True,
    type=click.Choice(['full', 'hollow', 'thick', 'thin']),
    help='Circle type.'
)
@click.option(
    '-c',
    '--character',
    default='.',
    show_default=True,
    type=str,
    help='Fill character.'
)
@click.option(
    '-b',
    '--blank',
    default=' ',
    show_default=True,
    type=str,
    help='Blank character.'
)
def app(diameter, type, character, blank):
    """Draw a circle of a certain diameter"""
    circle = Circle(diameter, character, blank)
    match type:
        case 'full':
            print(circle.full())
        case 'hollow':
            print(circle.hollow())
        case 'thick':
            print(circle.thick())
        case 'thin':
            print(circle.thin())


if __name__ == '__main__':
    app()
