# import click
#
# @click.command()
# @click.option("--count", default=1, help="Number of greetings.", required=True)
# @click.option("--name", prompt="Your name", help="The person to greet.")
# @click.option('--password',prompt=True, confirmation_prompt=True, hide_input=True)
# def hello(count, name, password):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for _ in range(count):
#         click.echo(f"Hello, {name}!")
#         click.echo(f'Moje super tajne hasło: {password}')
#
# if __name__ == '__main__':
#     hello()

import os
import click

#opakuj ponizsza funkcje przy uzyciu bibloteki click
def znajdz_pliki_i_katalogi(katalog_startowy, fraza):
    """
    Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
    Parameters
    ----------
    katalog_startowy
    fraza

    Returns
    -------

    """
    znalezione_elementy = []

    fraza = fraza.lower()

    for root, dirs, files in os.walk(katalog_startowy):
        for element in dirs + files:
            if fraza in element.lower():
                znalezione_elementy.append(os.path.join(root, element))


if __name__ == '__main__':
    znajdz_pliki_i_katalogi()