"""
Assert that two datasets are equal.
Should there be any differences. Then return a summary, and examples.
Parameters:
    - new_df: DataFrame = New dataset to be evaluated.
    - orig_df: DataFrame = Original dataset to be compared against.
    - subset: [str] = Optional. Set of columns common to both datasets.
        If not provided, then will fail if datasets do not contain the
        same list of columns.
    - use_matched_columns: bool = Optional: If true, then the columns
        subset will be automatically derived by the columns found in
        both datasets. Ignoring unmatched columns.
Returns: NamedTuple:
- A text summary of counts of total rows; and for each discrepancy
    type: matched, not matched, and only in one of the datasets.
- DataFrame. Containing the compared columns, and a single row with a
    count of differences for that column.
- DataFrame. Containing the compared columns, with a sample of 10 rows
    for each discrepancy type: matched, not matched, and only in one of the datasets.
"""
