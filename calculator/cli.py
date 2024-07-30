import click

from calculator.model import Calculator

@click.group()
@click.pass_context
def calc(ctx : click.context):
    """a simple calculator"""

    ctx.obj = {"calculator_object", Calculator()}