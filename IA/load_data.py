import os
import csv
import random

def load_data(num_samples=1, target_class='ST', 
              data_dir='/content/drive/MyDrive/Projeto_TCC_ECG/dados_ecg/ECGDataDenoised/ECGDataDenoised/', 
              labels_csv='/content/drive/MyDrive/Projeto_TCC_ECG/dados_ecg/Diagnostics.CSV'):
    """
    Carrega dados de eletrocardiograma (ECG) para análise.

    Parameters:
    - num_samples (int): Número de amostras a serem carregadas. Padrão é 1.
    - target_class (str): Classe alvo dos dados. Padrão é 'ST'.
    - data_dir (str): Diretório onde os arquivos de dados estão localizados. Padrão é o diretório fornecido.
    - labels_csv (str): Caminho para o arquivo CSV que contém os rótulos das classes. Padrão é o arquivo fornecido.

    Returns:
    - data (list): Lista de listas contendo os dados do ECG.
    - random_file (str): Nome aleatório do arquivo de dados carregado.
    - target_class (str): Classe alvo dos dados carregados.
    """    
    
    col_data = 'FileName'
    col_label = 'Rhythm'

    labels = []
    with open(labels_csv, 'r') as labels_file:
        csv_reader = csv.DictReader(labels_file, delimiter=';')
        for row in csv_reader:
            labels.append(row)

    filtered_files = [row[col_data] for row in labels if row[col_label] == target_class]

    sample_files = random.sample(filtered_files, min(num_samples, len(filtered_files)))
    random_file = random.choice(sample_files)

    data_file_path = os.path.join(data_dir, random_file + '.csv')

    with open(data_file_path, 'r') as data_file:
        csv_reader = csv.reader(data_file, delimiter=',')
        data = []
        for row in csv_reader:
            data.append(row)

    return data, random_file, target_class