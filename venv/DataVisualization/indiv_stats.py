import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')


@click.command()
@click.argument('name', type=str)
@click.argument('cat1', type=str)
@click.argument('cat2', type=str)
def indiv_stats(name, cat1, cat2):
    # Players' stats
    ind = games_details.groupby(['PLAYER_NAME'])
    person = ind.get_group(name)

    plt.figure(figsize=(10, 8))
    plt.xlabel(cat, fontsize=10)
    plt.ylabel('Number of Games', fontsize=10)
    plt.title(f'Career Performance of {name} in {cat}')
    sns.violinplot(person[cat], inner="box", palette="pastel", color="cyan")
    plt.xticks(rotation=0)
    plt.show()


if __name__ == '__main__':
    indiv_stats()
