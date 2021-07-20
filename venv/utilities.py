# Our main reusable functions for the DataVisualization part

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# import seaborn as sns

def read_df(dframe):
    dframe = pd.read_csv('../Data/%s' %(dframe))

def rename_df(df, col_dict):
    cols = df.columns
    new_cols = [(col_dict[c] if c in col_dict else c) for c in cols]
    df.columns = new_cols
    return df


def print_missing_values(df):
    # Missing values with plot
    df_null = pd.DataFrame(len(df) - df.notnull().sum(), columns=['Count'])
    df_null = df_null[df_null['Count'] > 0].sort_values(by='Count', ascending=False)
    df_null = df_null / len(df) * 100

    x = df_null.index.values
    height = [e[0] for e in df_null.values]
    gold, silver, bronze, other = ('#FFA400', '#bdc3c7', '#cd7f32', '#3498db')
    colors = [gold if i == 0 else silver if i == 1 else bronze if i == 2 else other for i in range(0, len(height))]
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.set_facecolor("green")
    ax.bar(x, height, width=0.8, color=colors)
    plt.xticks(x, x, rotation=60)
    plt.xlabel('Columns')
    plt.ylabel('Percentage')
    plt.title('Percentage of missing values in columns')
    plt.show()


def dataset_overview(df):
    # A general overview
    print_missing_values(df)


def blind_plot(df, column, label_col=None, max_plot=5):
    # Function for plotting
    top_df = df.sort_values(column, ascending=False).head(max_plot)
    height = top_df[column]
    if label_col is None:
        x = top_df.index
    else:
        x = top_df[label_col]
    gold, silver, bronze, other = ('#FFA400', '#bdc3c7', '#cd7f32', '#3498db')
    colors = [gold if i == 0 else silver if i == 1 else bronze if i == 2 else other for i in range(0, len(top_df))]
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.bar(x, height, color=colors)
    plt.xticks(x, x, rotation=60)
    plt.xlabel(label_col)
    plt.ylabel(column)
    plt.title(f'Top {max_plot} of {column}')
    plt.show()


def column_distribution(df, nShown, nPerRow):
    # Distribution graphs of column data
    nunique = df.nunique()
    # For displaying purposes, pick columns that
    # have between 1 and 100 unique values
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 100]]
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nPerRow - 1) / nPerRow
    plt.figure(num=None, figsize=(6 * nPerRow, 8 * nGraphRow), dpi=80, facecolor='w', edgecolor='k')
    for i in range(min(nCol, nShown)):
        plt.subplot(nGraphRow, nPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if not np.issubdtype(type(columnDf.iloc[0]), np.number):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel("Total Numbers")
        plt.xticks(rotation=90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=10.0)
    plt.show()


def correlation_matrix(df, graphWidth):
    # Correlation matrix
    filename = df
    # drop columns with NaN
    df = df.dropna('columns')
    # keep columns where there are more than 1 unique values
    df = df[[col for col in df if df[col].nunique() > 1]]
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()


def scatter_matrix(df, plotSize, textSize):
    # Scatter and density plots
    # keep only numerical columns
    df = df.select_dtypes(include=[np.number])
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]]
    columnNames = list(df)
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=1.0, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()


def convert_min(x):
    # Players with the most minutes played
    # Firstly, convert minutes to seconds to easier our work
    if pd.isna(x):
        return 0
    x = str(x).split(':')
    if len(x) < 2:
        return int(x[0])
    else:
        return int(x[0])*60+int(x[1])


def radar_plot(ax, df, max_val=1):
    # Radar plot tests
    # number of variable
    categories = list(df)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=12)

    # Draw ylabels
    ax.set_rlabel_position(0)
    yticks = [max_val * i / 4 for i in range(1, 4)]
    plt.yticks(yticks, [str(e) for e in yticks], color="grey", size=10)
    plt.ylim(0, max_val)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    colors = ['b', 'r', 'g']
    for i in range(len(df)):
        values = df.values[i].flatten().tolist()
        values += values[:1]
        color = colors[i]

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid', color=color, label=df.index[i])

        # Fill area
        ax.fill(angles, values, color, alpha=0.1)

    # Add legend
    plt.legend(loc=0, bbox_to_anchor=(0.008, 0.008), prop={'size': 10})


def pearson_r(x, y):
    # Pearson correlation function
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)
    return corr_mat[0, 1]