from data_loader import load_data
import json

class Ia:
    """
    Classe que representa um componente de inteligência artificial para execução de modelos
    e geração de resultados relacionados à análise de dados médicos.

    Methods:
    - run(): Executa o modelo e retorna um JSON contendo resultados da análise.
    """
    def run(self):
        """
        Executa o modelo e retorna um JSON contendo resultados da análise.

        Returns:
        - result_json: Um JSON contendo informações detalhadas sobre a execução do modelo.

        Note:
        O JSON de resultado contém informações como previsões do modelo, métricas de desempenho,
        gráficos de treino/validação, informações de pré-processamento, entre outros.
        """
        try:
            data, random_file, target_class = load_data()
            ia_instance = Ia()
            resp = ia_instance.run_model(data)
            resp = resp['result']

            # Calcule a média das previsões para cada classe
            class_means = resp.mean(axis=0)
            winning_class = np.argmax(class_means)
            porc = class_means[winning_class] / class_means.sum() * 100

            result_rhythms = {f'doença{i+1}': float(class_means[i]) for i in range(len(class_means))} # Resultados das previsões para cada classe

            response_json = {
                'result_rhythms': result_rhythms, # Previsões médias para cada classe
                'name_model': ['model_06_2023_08_13 23_50_08'], # Nome do modelo utilizado
                'accracy_model': {'qtd_iters_boostrap': 50, 'acuracia': 0.958, 'desvio_padrao_do_erro': 0.15}, # Métricas de desempenho do modelo
                'ROC': {'direct_image': 'static/roc_auc/roc_curve1_2023_08_13 23_50_08.png', 'roc_values': 0.89}, # Informações sobre a curva ROC
                'loss_train_val': {'direct_image': 'static/train_performance/9_3_metrics1_epochs_2023_08_13 23_50_08.png'}, # Gráfico de perda no treino/validação
                'acc_train_val': {'direct_image': 'static/train_performance/9_3_metrics1_epochs_2023_08_13 23_50_08.png'}, # Gráfico de acurácia no treino/validação
                'outras_metricas': {'f1': 0.90, 'recall': 0.98}, # Outras métricas de desempenho
                'preprocessing_data': {'old_shape': (5000, 12), 'new_shape': (500, 12), 'subamostras': 10, 'overlap': 0.10, 'batch': 64, 'transform': 'yeo-johnson'}, # Informações de pré-processamento dos dados
            }

            return json.dumps(response_json)  # Retorna o JSON como uma string
        except Exception as e:
            print(f'Ocorreu um erro durante a execução: {str(e)}')
            return None
