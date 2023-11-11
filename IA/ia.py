# ia.py
from data_loader import load_data
import json

class Ia:
    def run(self):
        try:
            data, random_file, target_class = load_data()
            ia_instance = Ia()
            resp = ia_instance.run_model(data)
            resp = resp['result']

            # Calcule a média das previsões para cada classe
            class_means = resp.mean(axis=0)
            winning_class = np.argmax(class_means)
            porc = class_means[winning_class] / class_means.sum() * 100

            result_rhythms = {f'doença{i+1}': float(class_means[i]) for i in range(len(class_means))}

            response_json = {
                'result_rhythms': result_rhythms,
                'direct_image': ['local_da_img_do_eletrocardiograma_salvo'],
                'name_model': ['model_06_2023_08_13 23_50_08'],
                'accracy_model': {'qtd_iters_boostrap': 50, 'acuracia': 0.958, 'desvio_padrao_do_erro': 0.15},
                'conf_matriz': {'direct_image': 'local_da_imagem'},
                'ROC': {'direct_image': 'static/roc_auc/roc_curve1_2023_08_13 23_50_08.png', 'roc_values': 0.89},
                'loss_train_val': {'direct_image': 'static/train_performance/9_3_metrics1_epochs_2023_08_13 23_50_08.png'},
                'acc_train_val': {'direct_image': 'static/train_performance/9_3_metrics1_epochs_2023_08_13 23_50_08.png'},
                'outras_metricas': {'f1': 0.90, 'recall': 0.98},
                'preprocessing_data': {'old_shape': (5000, 12), 'new_shape': (500, 12), 'subamostras': 10, 'overlap': 0.10, 'batch': 64, 'transform': 'yeo-johnson'},
                'timestemp': '2023-11-11 09:27:53',
            }

            return json.dumps(response_json)  # Retorna o JSON como uma string
        except Exception as e:
            print(f'Ocorreu um erro durante a execução: {str(e)}')
            return None
