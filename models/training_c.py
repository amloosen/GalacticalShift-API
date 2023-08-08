"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR, ARRAY, Text # ForeignKey
from models.db import Model
from models.base_object import BaseObject
import numpy


class TrainingC(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id = Column(VARCHAR(length=100))
    study_part = Column(Integer, nullable=False)
    startTime = Column(VARCHAR(length=100))
    sectionStartTime = Column(VARCHAR(length=100))

    all_element_values = Column(Text(length=10000))
    traintrialTotal = Column(VARCHAR(length=100))

    corr_elements = Column(Text(length=10000), nullable=False)
    traintrialSgmMu = Column(Text(length=10000), nullable=False)
    times_element1 = Column(Text(length=10000), nullable=False)
    times_element2 = Column(Text(length=10000), nullable=False)
    times_element3 = Column(Text(length=10000), nullable=False)
    element1Col = Column(VARCHAR(length=100), nullable=False)
    element2Col = Column(VARCHAR(length=100), nullable=False)
    element3Col = Column(VARCHAR(length=100), nullable=False)
    startSgm = Column(VARCHAR(length=100))
    startMu = Column(VARCHAR(length=100))
    all_true_pop_size =  Column(Text(length=10000), nullable=False)
    outcomeHeight = Column(Text(length=100000), nullable=False)
    traintrialRT = Column(Text(length=100000), nullable=False)

    def get_id(self):
        return (self.id)

    def get_user_id(self):
        return str(self.user_id)

    def get_study_part(self):
        return (self.study_part)

    def get_startTime(self):
        return (self.startTime)

    def get_sectionStartTime(self):
        return (self.sectionStartTime)

    def get_all_element_values(self):
        return (self.all_element_values)

    def get_corr_elements(self):
        return (self.corr_elements)

    def get_traintrialSgmMu(self):
        return (self.traintrialSgmMu)

    def get_times_element1(self):
        return (self.times_element1)

    def get_times_element2(self):
        return (self.times_element2)

    def get_times_element3(self):
        return (self.times_element3)

    def get_element1Col(self):
        return (self.element1Col)

    def get_element2Col(self):
        return (self.element2Col)

    def get_element3Col(self):
        return (self.element3Col)

    def get_startSgm(self):
        return (self.startSgm)

    def get_startMu(self):
        return (self.startMu)

    def get_all_true_pop_size(self):
        return (self.all_true_pop_size)

    def get_outcomeHeight(self):
        return (self.outcomeHeight)

    def get_traintrialRT(self):
        return (self.traintrialRT)

    def get_traintrialTotal(self):
        return (self.traintrialTotal)

    def errors(self):
        errors = super(TrainingC, self).errors()
        return errors
