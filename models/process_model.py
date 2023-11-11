from app import db
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired


class Process(db.Model):
    __tablename__ = "process"

    id = db.Column(db.Integer, primary_key=True)
    result_rhythms = db.Column(db.String, nullable=False)
    direct_image = db.Column(db.String, nullable=False)
    name_model = db.Column(db.String, nullable=False)
    accracy_model = db.Column(db.String, nullable=False)
    conf_matriz = db.Column(db.String, nullable=False)
    ROC = db.Column(db.String, nullable=False)
    loss_train_val = db.Column(db.String, nullable=False)
    acc_train_val = db.Column(db.String, nullable=False)
    boxplot_models = db.Column(db.String, nullable=False)
    outras_metricas = db.Column(db.String, nullable=False)
    preprocessing_data = db.Column(db.String, nullable=False)
    timestemp = db.Column(db.Timestamp, nullable=False)

    def __init__(self, result_rhythms, direct_image, name_model, accracy_model, conf_matriz, ROC, loss_train_val, acc_train_val, boxplot_models, outras_metricas, preprocessing_data, timestemp):
        self.result_rhythms = result_rhythms
        self.direct_image = direct_image
        self.name_model = name_model
        self.accracy_model = accracy_model
        self.conf_matriz = conf_matriz
        self.ROC = ROC
        self.loss_train_val = loss_train_val
        self.acc_train_val = acc_train_val
        self.boxplot_models = boxplot_models
        self.outras_metricas = outras_metricas
        self.preprocessing_data = preprocessing_data
        self.timestemp = timestemp

    def __repr__(self):
        return f"<Process {self.id}>"



class ProcessForm(FlaskForm):
    file = FileField('file', validators=[DataRequired()])
