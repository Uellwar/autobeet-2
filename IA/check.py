import pandas as pd
import numpy as np

SHAPE_DEFAULT = (500, 12)

class Check:
    def __init__(self):
        self.returns_check = {'is_csv': True, 'length': None, 'is_numeric': None}

    def check_file(self, file):
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
