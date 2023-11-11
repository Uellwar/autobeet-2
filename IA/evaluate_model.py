# evaluate_model.py

class EvaluateModel:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def evaluate(self):
        try:
            predictions = self.model.predict(self.data)
            return predictions
        except Exception as e:
            raise Exception(f'Erro ao avaliar o modelo: {str(e)}')