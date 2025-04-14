import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)



def get_column_names(df):
    
    """Extract and format column names from a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame whose column names are to be retrieved.
    
    Returns:
        tuple: A tuple containing:
            - pandas.DataFrame: A DataFrame with column names under the 'Columns' header.
            - pandas.Series: A Series containing the column names.
    """
    
    print("|| Retrieve column names from DataFrame")
    column_names = pd.Series(df.columns.values)
    columns = pd.DataFrame(column_names)
    columns.columns = ['Columns']
    
    return columns, column_names


def get_dimensions(df):
    
    """Retrieve the dimensions (number of rows and columns) of a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame to analyze.
    
    Returns:
        pandas.DataFrame: A transposed DataFrame with 'Columns' and 'Rows' as indices and their counts under 'Dimensions'.
    """
    
    print("|| Get dimensions (rows and columns) of DataFrame")
    dimensions_1 = pd.Series(df.shape[1])
    dimensions_2 = pd.Series(df.shape[0])
    dimensions = pd.concat([dimensions_1, dimensions_2], axis=1)
    dimensions.columns = ['Columns', 'Rows']
    dimensions = dimensions.T
    dimensions.columns = ['Dimensions']
    
    return dimensions


def get_dataset_types(df):
    
    """Identify and list the data types of each column in a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame to inspect.
    
    Returns:
        pandas.DataFrame: A DataFrame with columns as indices and their data types under 'Data_Type'.
    """
    
    print("|| Identify data types of DataFrame columns")
    df_types = pd.DataFrame(df.dtypes)
    df_types.reset_index(drop=True, inplace=True)
    df_types.columns = ["Data_Type"]
    df_types["Column"] = pd.Series(df.columns).values
    df_types.set_index("Column", inplace=True)
    
    return df_types


def get_missing_values(df):
    
    """Count the number of missing values for each column in a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame to check for missing values.
    
    Returns:
        pandas.DataFrame: A DataFrame with columns as indices and the count of missing values under 'Missing_Values', sorted descending.
    """
    
    print("|| Count missing values per column")
    missing_values = pd.DataFrame(df.isna().sum())
    missing_values.reset_index(drop=True, inplace=True)
    missing_values.columns = ["Missing_Values"]
    missing_values["Column"] = pd.Series(df.columns).values
    missing_values.set_index("Column", inplace=True)
    missing_values.sort_values(by="Missing_Values", ascending=False, inplace=True)
    
    return missing_values


def get_broadview_miss_val(df):
    
    """Provide a comprehensive view of missing values with percentages and counts.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame to analyze for missing data.
    
    Returns:
        tuple: A tuple containing:
            - pandas.DataFrame: A DataFrame with columns as indices and metrics like 'Absolute Missing (%)', 'Column Missing (%)', etc.
            - list: A list of column names with any missing values.
    """
    
    print("|| Broadview of missing values with percentages")
    
    # Absolute missing: nulls relative to total rows
    absolute_missing = df.isna().sum() / df.shape[0]
    missing_values = pd.DataFrame(absolute_missing, columns=["Absolute Missing (%)"])
    
    column_missing = []
    column_total = []
    column_miss = []
    
    for column in df.columns:
        col_miss = df[column].isnull().sum()
        total_expected = df.shape[0]
        column_miss.append(col_miss)
        column_total.append(total_expected - col_miss)
        column_missing.append(col_miss / total_expected if total_expected > 0 else 0)
    
    missing_values["Column Missing (%)"] = column_missing
    missing_values["Column Remaining (%)"] = [1 - val for val in column_missing]
    missing_values["Column Total"] = column_total
    missing_values["Column Missing"] = column_miss
    
    missing_values.index.name = "Column"
    missing_values.sort_values(by="Absolute Missing (%)", ascending=False, inplace=True)
    
    missing_columns = list(missing_values.query("`Absolute Missing (%)` > 0").index)
    pd.options.display.float_format = '{:.2%}'.format
    
    return missing_values, missing_columns



def get_num_statistics_metrics(df):
    
    """Calculate descriptive statistics for numerical columns in a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame with numerical columns to analyze.
    
    Returns:
        pandas.DataFrame: A DataFrame with columns as indices and statistics like 'Min', 'Max', 'Mean', 'Skew', etc.
    """
    
    print("|| Calculate descriptive statistics for numerical columns")
    ct1 = pd.DataFrame(df.apply(np.mean)).T
    ct2 = pd.DataFrame(df.apply(np.median)).T
    d1 = pd.DataFrame(df.apply(np.std)).T
    d2 = pd.DataFrame(df.apply(min)).T
    d3 = pd.DataFrame(df.apply(max)).T
    d4 = pd.DataFrame(df.apply(lambda x: x.max() - x.min())).T
    d5 = pd.DataFrame(df.apply(lambda x: x.skew())).T
    d6 = pd.DataFrame(df.apply(lambda x: x.kurtosis())).T
    metrics = pd.concat([d2, d3, d4, ct1, ct2, d1, d5, d6]).T.reset_index()
    metrics.columns = ['Attributes', 'Min', 'Max', 'Range', 'Mean', 'Median', 'Standart Deviation', 'Skew', 'Kurtosis']
    metrics.set_index('Attributes', inplace=True)
    
    return metrics


def get_unique_cat_values(df):
    
    """Count and list unique values for each categorical column in a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): Input DataFrame to inspect for unique values.
    
    Returns:
        pandas.DataFrame: A DataFrame with columns as indices, 'Unique Values Count', and a list of unique values under 'Unique Values'.
    """
    
    print("|| Count unique values in categorical columns")
    unique_values = pd.DataFrame(df.apply(lambda x: x.unique().shape[0]))
    unique_values.reset_index(drop=True, inplace=True)
    unique_values.columns = ["Unique Values Count"]
    unique_values["Unique Values"] = df.apply(lambda x: x.unique()).values
    unique_values["Attributes"] = pd.Series(df.columns).values
    unique_values.set_index("Attributes", inplace=True)
    
    return unique_values


def get_analysis_conclusions(matrix, columns = None, columns_included = None):
    
    if columns:
        
        columns = columns
        
    else:
        
        columns = ['Hipóteses', 'Conclusão', 'Relevância', 'Insigth']
        
    def highlight_relevance(value):
        
        positive = ['Alta', 'Verdadeira', 'Sim']
        negative = ['Baixa', 'Falsa', 'Não']
        mid = ['Média', 'Possível']
        if value in positive:
            color = 'green'
            return f'color:{color}'
        elif value in negative:
            color = 'red'
            return f'color:{color}'
        elif value in mid:
            color = 'orange'
            return f'color:{color}'
        
    analysis = pd.DataFrame(matrix,columns=columns)
    
    analysis.reset_index(drop=True, inplace=True)
    analysis.set_index('Hipóteses', inplace = True)
    
    return analysis.style.applymap(highlight_relevance)