import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import PowerTransformer

SHAPE_DEFAULT = (500, 12)
OVERLAP_DEFAULT = 0.1

class TransformData:
    def __init__(self):
        self.overlap = OVERLAP_DEFAULT
        self.shape = SHAPE_DEFAULT
        self.transformer = PowerTransformer(method='yeo-johnson', standardize=True)

    def overlapping_windows(self, matrix):
        """Segmenta uma matriz de dados em janelas sobrepostas.

        Essa função divide uma matriz de dados em várias janelas de tamanho especificado em `new_shape`,
        com uma sobreposição controlada pelo atributo `overlap`.

        Args:
            matrix (np.ndarray): A matriz de dados a ser dividida em janelas.

        Returns:
            np.ndarray: Um array numpy contendo as janelas sobrepostas resultantes.
        """
        try:
            overlap_size = int(self.shape[0] * self.overlap)  # Tamanho da sobreposição
            step_size = self.shape[0] - overlap_size  # Tamanho do passo

            # Ajusta o tamanho do passo para 1 se for menor que 1
            if step_size < 1:
                step_size = 1

            windows = []  # Lista para armazenar as janelas
            matrix = pd.DataFrame(matrix)
            # Itera sobre a matriz de dados com base no tamanho da janela e tamanho do passo
            for i in range(0, matrix.shape[0] - self.shape[0] + 1, step_size):
                window = matrix.iloc[i:i+self.shape[0], :]  # Seleciona a janela da matriz
                windows.append(window)  # Adiciona a janela à lista de janelas

            return np.array(windows)  # Retorna as janelas como um array numpy

        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            return None

    def yeo_johnson_transform(self, data):
        shape_backup = data.shape
        data = data.reshape(-1, 1)
        data = self.transformer.fit_transform(data)
        data = data.reshape(shape_backup)
        return data

    def transformation_and_tensor(self, data):
        display(type(data))
        data_windows = self.overlapping_windows(data)
        transformed_windows = []

        for window in data_windows:
            transformed_window = self.yeo_johnson_transform(window)
            transformed_windows.append(transformed_window)

        del data_windows
        data_tensor = tf.convert_to_tensor(transformed_windows, dtype=tf.float32)
        return data_tensor