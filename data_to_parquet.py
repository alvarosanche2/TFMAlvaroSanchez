import os
import pandas as pd
import argparse
import ast


def convert_file(file_path, output_folder, delimiter, column_types):
    print(f'Iniciando conversión del archivo: {file_path}...')
    
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, sep=delimiter, dtype=str, engine='pyarrow')
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path, dtype=str, engine='openpyxl')
        else:
            print(f'Error: Formato de archivo no compatible: {file_path}')
            return
    except Exception as e:
        print(f'Error al cargar el archivo {file_path}: {e}')
        return

    if column_types:
        types_dict = ast.literal_eval(column_types)
        for col, dtype in types_dict.items():
            if col in df.columns:
                try:
                    if dtype == 'int':
                        df[col] = pd.to_numeric(df[col], errors='coerce', downcast='integer')
                    elif dtype == 'float':
                        df[col] = df[col].str.replace(',', '.')
                        df[col] = pd.to_numeric(df[col], errors='coerce', downcast='float')
                    elif dtype == 'str':
                        df[col] = df[col].astype(str)
                    elif dtype == 'datetime':
                        df[col] = pd.to_datetime(df[col], errors='coerce')
                    else:
                        print(f'Advertencia: Tipo de datos {dtype} no es compatible. La columna {col} se mantendrá como string.')
                except Exception as e:
                    print(f'Error al convertir la columna {col} a {dtype}: {e}')

    parquet_filename = os.path.splitext(os.path.basename(file_path))[0] + '.parquet'
    parquet_path = os.path.join(output_folder, parquet_filename)
    
    try:
        df.to_parquet(parquet_path, engine='pyarrow')
        print(f'Archivo convertido exitosamente: {parquet_path}')
    except Exception as e:
        print(f'Error al guardar el archivo Parquet {parquet_path}: {e}')


def process_input_path(input_path, output_folder, delimiter, column_types):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f'Carpeta de salida creada: {output_folder}')
    
    if os.path.isfile(input_path):
        print(f'Procesando archivo: {input_path}')
        convert_file(input_path, output_folder, delimiter, column_types)
    elif os.path.isdir(input_path):
        print(f'Procesando carpeta: {input_path}')
        for root, _, files in os.walk(input_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                convert_file(file_path, output_folder, delimiter, column_types)
    else:
        print(f'Error: La ruta proporcionada {input_path} no es válida.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convierte archivos CSV o Excel a formato Parquet.')
    parser.add_argument('input', type=str, help='Archivo o carpeta que contiene archivos CSV o Excel para convertir')
    parser.add_argument('-o', '--output_folder', type=str, default='output', help='Carpeta de salida para los archivos convertidos a Parquet')
    parser.add_argument('-d', '--delimiter', type=str, default=',', help='Delimitador de campos en los archivos CSV')
    parser.add_argument('-t', '--column_types', type=str, help='Tipos de datos de las columnas en formato diccionario. Ej: "{\'col1\': \'int\', \'col2\': \'float\', \'col3\': \'datetime\'}"')

    args = parser.parse_args()
    process_input_path(args.input, args.output_folder, args.delimiter, args.column_types)
