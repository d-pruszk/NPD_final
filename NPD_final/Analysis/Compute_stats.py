def calculate_basic_stats(df, column):
    """Calculate basic statistics for a given column"""
    return {
        'min': df[column].min(),
        'max': df[column].max(),
        'mean': df[column].mean(),
        'std_dev': df[column].std(),
        'q1': df[column].quantile(0.25),
        'q3': df[column].quantile(0.75),
    }