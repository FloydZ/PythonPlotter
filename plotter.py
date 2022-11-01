import pandas as pd
import matplotlib.pyplot as plt
import copy


# good source:
# https://vincentarelbundock.github.io/Rdatasets/datasets.html


def return_plot(csv_file: str, ignore_col=None, date_col=1):
    """
    :param csv_file path to a file containing data
    """

    data = pd.read_csv(csv_file)
    headers = data.columns

    # remove unwanted columns
    if type(ignore_col) == int:
        data = data.drop(columns=[headers[ignore_col]])

    if type(ignore_col) == list:
        cols = [headers[a] for a in ignore_col]
        data = data.drop(columns=cols)

    # remove dates
    # data = data.drop(columns=[headers[date_col]])

    # dont drop it
    number_of_plots = len(data.columns) - 1

    ranges = list(range(data.shape[0]))
    for i in range(number_of_plots):
        column = data.columns[i+1]
        plt.plot(ranges, data.loc[:, column].tolist())

    plt.show()


def return_plot_star(csv_file: str, ignore_col=None, date_col=1):
    """
    :param csv_file path to a file containing data
    """

    data = pd.read_csv(csv_file)
    headers = data.columns

    # remove unwanted columns
    if type(ignore_col) == int:
        data = data.drop(columns=[headers[ignore_col]])

    if type(ignore_col) == list:
        cols = [headers[a] for a in ignore_col]
        data = data.drop(columns=cols)

    # remove dates
    # data = data.drop(columns=[headers[date_col]])

    # dont drop it
    number_of_plots = len(data.columns) - 1
    for i in range(number_of_plots):
        column = data.columns[i+1]
        Y = data.loc[:, column].tolist()
        X = copy.deepcopy(Y)
        Y = Y[1:]
        X = X[:-1]


        plt.plot(X, Y)

    plt.show()


if __name__ == "__main__":
    # return_plot("data/stocks_18.csv", ignore_col=0, date_col=1)
    return_plot_star("data/stocks_18.csv", ignore_col=0, date_col=1)
