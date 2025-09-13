import duckdb
import pandas as pd
import os

# Caminhos dos arquivos
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'dados_eda.duckdb')


# Arquivos alvo
files = {
    'dados_painel_consolidado': 'dados_painel_consolidado.csv',
    'ifdm_and_cadunico_long': 'ifdm_and_cadunico_long.csv'
}

def main():
    # Cria o banco se não existir
    # if not os.path.exists(DB_PATH):
    #     open(DB_PATH, 'w').close()
    con = duckdb.connect(DB_PATH)
    for table, filename in files.items():
        file_path = os.path.join(DATA_DIR, filename)
        con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM read_csv_auto('{file_path}')")
    con.close()
    print(f"Dados salvos em {DB_PATH}")

if __name__ == "__main__":
    main()
