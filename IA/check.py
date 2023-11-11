import pandas as pd
import numpy as np

SHAPE_DEFAULT = (500, 12)

class Check:
    def __init__(self):
        """
        Classe para verificar propriedades de um arquivo representado como DataFrame.

        Attributes:
        - returns_check (dict): Dicionário contendo resultados da verificação, com as chaves:
            - 'is_csv' (bool): Indica se o arquivo é um CSV válido.
            - 'length' (bool): Indica se o arquivo possui o comprimento mínimo esperado.
            - 'is_numeric' (bool): Indica se todas as colunas do arquivo são numéricas.

        Methods:
        - check_file(file): Realiza a verificação do arquivo representado como DataFrame.

        Exemplo de Uso:
        ```python
        checker = Check()
        result = checker.check_file(my_data_frame)
        print(result)
        ```

        """
        self.returns_check = {'is_csv': True, 'length': None, 'is_numeric': None}

    def check_file(self, file):
        """
        Realiza a verificação do arquivo representado como DataFrame.

        Parameters:
        - file (DataFrame): O arquivo a ser verificado.

        Returns:
        - dict: Dicionário contendo resultados da verificação.
        """
        try:
            data = pd.DataFrame(file).astype(np.float32)
            # Removendo a primeira linha caso nao seja numérica
            if data.shape[0] >= SHAPE_DEFAULT[0] and not pd.api.types.is_numeric_dtype(data.iloc[0, 0]):
                data = data.iloc[1:]
            if data.shape[0] >= SHAPE_DEFAULT[0]:
                self.returns_check['length'] = True
            else:
                self.returns_check['length'] = False

            numeric_columns = data.select_dtypes(include=[np.number]).columns
            if len(numeric_columns) == data.shape[1]:
                self.returns_check['is_numeric'] = True
            else:
                self.returns_check['is_numeric'] = False

        except Exception as e:
            self.returns_check['is_csv'] = False

        return self.returns_check
