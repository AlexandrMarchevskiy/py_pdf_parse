import tabula
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="tabula")

pdf_file = "копия_19.pdf"
tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
selected_table = tables[0]
df_cleaned = selected_table.loc[:, ~selected_table.columns.str.contains('^Unnamed')]
table_dict = df_cleaned.to_dict(orient='records')
print(table_dict)



