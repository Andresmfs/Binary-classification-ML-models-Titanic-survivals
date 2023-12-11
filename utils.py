import matplotlib.pyplot as plt
import re


def print_percentage(data, column_name: str, order, axis=None, x_shift=0, y_shift=0.02):
    '''
   This function is to be used below a count plot. 
   It prints the percentage on the bars of vertical countplots
   '''
    val_counts = data[column_name].value_counts().loc[order]
    total_counts = val_counts.sum()
    max_count = val_counts.sort_values(ascending=False).iloc[0]

    for i, count in enumerate(val_counts):
        pct_string = f'{100*count/total_counts:.1f}%'

        if not axis:
            plt.text(i + x_shift, count + y_shift *
                     max_count, pct_string, va='center', ha='center')
        else:
            axis.text(i + x_shift, count + y_shift *
                      max_count, pct_string, va='center', ha='center')


def general_info(data, title: str):
    print(title)
    print('-----------------------------------------------')
    print('Shape:', data.shape)
    print('Columns:', ', '.join([feature for feature in data.columns]))
    print('Duplicates:', sum(data.duplicated()))
    print('')


def revertir_one_hot(data, one_hot_cols, single_col, eliminate_prefix=False):
    '''This function reverts one-hot encoding'''
    data[single_col] = data[one_hot_cols].idxmax(axis=1)
    data.drop(columns=one_hot_cols, inplace=True)

    if eliminate_prefix:
        data[single_col] = data[single_col].apply(
            lambda x: re.split('_', x)[-1])
