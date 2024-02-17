import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="tabula")
import tabula
import pandas as pd
import numpy as np


def test_compare_multiple_tables_v1():
	gold_standard_file = "17cc3e7c-a227-40e1-b693-6f75503b5cd1.pdf"
	generated_file = "810abb0c-4cbf-467b-b319-57896a28f42c.pdf"
	gold_standard_tables = tabula.read_pdf(gold_standard_file, pages='all', multiple_tables=True)
	generated_tables = tabula.read_pdf(generated_file, pages='all', multiple_tables=True)
	
	for i, (gold_table, generated_table) in enumerate(zip(gold_standard_tables, generated_tables)):
		try:
			pd.testing.assert_frame_equal(gold_table, generated_table, check_dtype=False, check_exact=True)
		except AssertionError as e:
			raise AssertionError(f"Таблицы не совпадают на странице {i + 1}: {e}")


def compare_tables(gold_table, generated_table):
	if not np.array_equal(gold_table.values, generated_table.values):
		raise AssertionError("Таблицы не совпадают:\n"
		                     f"Отличия в данных:\n{gold_table.values}\nvs\n{generated_table.values}")


def test_compare_multiple_tables_v2():
	gold_standard_file = "17cc3e7c-a227-40e1-b693-6f75503b5cd1.pdf"
	generated_file = "810abb0c-4cbf-467b-b319-57896a28f42c.pdf"
	gold_standard_tables = tabula.read_pdf(gold_standard_file, pages='all', multiple_tables=True)
	generated_tables = tabula.read_pdf(generated_file, pages='all', multiple_tables=True)
	
	for i, (gold_table, generated_table) in enumerate(zip(gold_standard_tables, generated_tables)):
		try:
			compare_tables(gold_table, generated_table)
		except AssertionError as e:
			raise AssertionError(f"Таблицы не совпадают на странице {i + 1}:\n{e}")


def test_compare_multiple_tables_v3():
	gold_standard_file = "17cc3e7c-a227-40e1-b693-6f75503b5cd1.pdf"
	generated_file = "810abb0c-4cbf-467b-b319-57896a28f42c.pdf"
	gold_standard_tables = tabula.read_pdf(gold_standard_file, pages='all', multiple_tables=True)
	generated_tables = tabula.read_pdf(generated_file, pages='all', multiple_tables=True)
	
	for i, (gold_table, generated_table) in enumerate(zip(gold_standard_tables, generated_tables)):
		try:
			pd.testing.assert_frame_equal(gold_table, generated_table, check_dtype=False, check_exact=True)
		except AssertionError as e:
			raise AssertionError(f"Таблицы не совпадают на странице {i + 1}:\n{e}")
