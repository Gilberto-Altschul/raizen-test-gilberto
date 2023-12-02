import pandas as pd
import os
import xlrd
import openpyxl
from datetime import datetime

print("Diretório de Trabalho:", os.getcwd())
# Define the path to the Excel file
input_file = os.path.join(os.getcwd(), 'vendas-combustiveis-m3.xlsx')
total_volume_input = 0.0000000000

# Read data from the first tab (Planilha1)
df_planilha1 = pd.read_excel(input_file, sheet_name="Planilha1")

# Read data from the second tab (Planilha2)
df_planilha2 = pd.read_excel(input_file, sheet_name="Planilha2")

# Define a mapping from Portuguese month names to corresponding numerical values
month_mapping = {
    'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': 5, 'Jun': 6,
    'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12
}

# Define a function to convert month names to numerical values
def month_to_number(month_name):
    return month_mapping.get(month_name, 0)

# Function to transform the input DataFrame to the desired output schema
def transform_data(input_df):
    output_data = []
    
    for index, row in input_df.iterrows():
        global total_volume_input
        total_volume_input=total_volume_input + row['TOTAL'] 
        
        for month_col in input_df.columns[5:17]:
            year_month = f"{row['ANO']}-{month_to_number(month_col):02d}"
            uf = row['ESTADO']
            product = row['COMBUSTÍVEL']
            unit = row['UNIDADE']
            volume = round(row[month_col],10)
            created_at = datetime.now()

            output_data.append([year_month, uf, product, unit, volume, created_at])

    output_df = pd.DataFrame(output_data, columns=['year_month', 'uf', 'product', 'unit', 'volume', 'created_at'])

    return output_df

# Transform data from both tabs

df_output_planilha1 = transform_data(df_planilha1)
df_output_planilha2 = transform_data(df_planilha2)

# Concatenate the results
final_output_df = pd.concat([df_output_planilha1, df_output_planilha2], ignore_index=True)
total_volume_output = final_output_df['volume'].sum()


# Print the total volume

print(f'total_volume_input= ', total_volume_input) 
print(f'total_volume_output= ', total_volume_output) 

# Verifique se os totais são iguais com 5 casas decimais
if round(total_volume_input, 7) == round(total_volume_output, 7):
    print("Os totais são iguais.")

    # Salve o DataFrame em uma planilha Excel
  
    output_file = os.path.join(os.getcwd(),'output_data.xlsx')

    final_output_df.to_excel(output_file, index=False)
   
  

    # Imprima a mensagem de conclusão
    print(f"DataFrame salvo com sucesso em {output_file}")
else:
    print("Os totais não são iguais.")