import pandas as pd
import tabula
import pytest

def remove_unnamed_columns(table):
    return table.loc[:, ~table.columns.str.contains('^Unnamed')]

@pytest.fixture
def discrepancies():
    discrepancies_list = []
    yield discrepancies_list
    if discrepancies_list:
        print("\nDiscrepancies found:")
        for discrepancy in discrepancies_list:
            print(discrepancy)
        pytest.fail("Test failed due to discrepancies.")

def test_compare_multiple_tables_v3(discrepancies):
    gold_standard_file = "копия.pdf"
    generated_file = "копия.pdf"
    gold_standard_tables = tabula.read_pdf(
        gold_standard_file,
        pages='all',
        multiple_tables=True,
    )
    generated_tables = tabula.read_pdf(generated_file, pages='all', multiple_tables=True)

    for gold_table, generated_table in zip(gold_standard_tables, generated_tables):
        gold_table_cleaned = remove_unnamed_columns(gold_table)
        generated_table_cleaned = remove_unnamed_columns(generated_table)

        try:
            pd.testing.assert_frame_equal(
                gold_table_cleaned,
                generated_table_cleaned,
                check_dtype=False,
                check_exact=True,
            )
        except AssertionError as e:
            discrepancies.append(f"Discrepancy in tables: {e}")
