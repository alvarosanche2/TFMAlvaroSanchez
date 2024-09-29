import os
import pandas as pd
import argparse


def group_data(file_path, output_folder):
    print(f'Iniciando conversión del archivo: {file_path}...')

    df = pd.read_parquet(file_path)

    required_columns = ['fecha_inicio', 'fecha_fin', 'distrito', 'barrio', 'tipo_zona']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f'Advertencia: El archivo {file_path} no contiene las siguientes columnas necesarias: {", ".join(missing_columns)}')
        return

    df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
    df['fecha_fin'] = pd.to_datetime(df['fecha_fin'])

    time_range = pd.date_range(start=df['fecha_inicio'].min().floor('H'), end=df['fecha_fin'].max().ceil('H'), freq='H')
    results = []
    for time in time_range:
        mask = (df['fecha_inicio'] <= time) & (df['fecha_fin'] > time)
        grouped = df[mask].groupby(['barrio', 'distrito', 'tipo_zona']).size().reset_index(name='cantidad_tickets')
        grouped['hora'] = time
        results.append(grouped)
    result_df = pd.concat(results, ignore_index=True)

    parquet_filename = os.path.splitext(os.path.basename(file_path))[0] + '.parquet'
    parquet_path = os.path.join(output_folder, parquet_filename)
    result_df.to_parquet(parquet_path, engine='pyarrow', index=False)
    print(f'Archivo procesado correctamente: {parquet_path}')


def process_input_path(input_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f'Carpeta de salida creada: {output_folder}')
    
    if os.path.isfile(input_path):
        print(f'Procesando archivo: {input_path}')
        group_data(input_path, output_folder)
    elif os.path.isdir(input_path):
        print(f'Procesando carpeta: {input_path}')
        for root, _, files in os.walk(input_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                group_data(file_path, output_folder)
    else:
        print(f'Error: La ruta proporcionada {input_path} no es válida.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Agrupa datos de archivos Parquet por barrio, distrito, tipo de zona y hora, indicando la cantidad de tickets activos en cada momento y ubicación. Los archivos deben contener las siguientes columnas: fecha_inicio, fecha_fin, distrito, barrio, tipo_zona.')
    parser.add_argument('input', type=str, help='Ruta del archivo o carpeta que contiene archivos Parquet a agrupar')
    parser.add_argument('-o', '--output_folder', type=str, default='output', help='Carpeta de salida para los archivos Parquet agrupados')

    args = parser.parse_args()
    process_input_path(args.input, args.output_folder)
