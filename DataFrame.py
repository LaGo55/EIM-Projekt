import pandas as pd


def DataFrame(x_value, data1, data2, i):

        df = pd.DataFrame(columns=['Time', 'Frequency', 'Temperature'])
        df_new_row = pd.DataFrame({'Time': [x_value], 'Frequency': [data1], 'Temperature': [data2]})
        df = pd.concat([df, df_new_row])
        df = df.reset_index(drop=True)

        if i > 20:
            df = df.iloc[1:]

        i += 1
        return df, i