import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')

@click.command()
@click.argument('name', type=str)
@click.argument('cat', type=str)
def indiv_stats(name, cat):
    # Players' stats
    ind = games_details.groupby(['PLAYER_NAME'])
    person = ind.get_group(name)
    plt.figure(figsize=(10, 8))
    plt.xlabel(cat, fontsize=10)
    plt.ylabel('Number of Games', fontsize=10)
    plt.title('Career Benchmarks of %s' ' in %s' % (name, cat))
    sns.violinplot(person[cat])
    plt.xticks(rotation=90)
    plt.show()

if __name__ == '__main__':
    indiv_stats()