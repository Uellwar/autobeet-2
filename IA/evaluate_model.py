class EvaluateModel:
    """
    Classe para avaliação de modelos de machine learning.

    Parameters:
    - model: Um modelo treinado que implementa o método predict para fazer previsões.
    - data: Os dados de entrada a serem utilizados para a avaliação do modelo.

    Attributes:
    - model: Armazena o modelo a ser avaliado.
    - data: Armazena os dados de entrada para avaliação.

    Methods:
    - evaluate(): Realiza a avaliação do modelo utilizando os dados fornecidos.
                  Retorna as previsões do modelo.

    Raises:
    - Exception: Se ocorrer um erro durante a avaliação do modelo, uma exceção é levantada
                 contendo uma mensagem detalhando o problema.
    """
    def __init__(self, model, data):
            self.model = model
            self.data = data

    def evaluate(self):
        """
        Avalia o modelo utilizando os dados fornecidos.

        Returns:
        - predictions: As previsões geradas pelo modelo para os dados de entrada.

        Raises:
        - Exception: Se ocorrer um erro durante a avaliação, uma exceção é levantada
                     com uma mensagem detalhada sobre o problema.
        """
        try:
            predictions = self.model.predict(self.data)
            return predictions
        except Exception as e:
            raise Exception(f'Erro ao avaliar o modelo: {str(e)}')