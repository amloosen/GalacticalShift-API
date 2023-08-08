"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR, Text  # ForeignKey
from models.db import Model
from models.base_object import BaseObject
import numpy


class TaskParams(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id = Column(VARCHAR(length=100))
    study_part = Column(Integer, nullable=False)

    w0 = Column(Text(length=10000), nullable=False)
    relevant_w = Column(Text(length=10000), nullable=False)
    val_corr_elem = Column(Text(length=10000), nullable=False)
    epsilon = Column(Text(length=10000), nullable=False)
    precededShift = Column(Text(length=10000), nullable=False)
    true_pop_size = Column(Text(length=10000), nullable=False)
    corPos_sq = Column(Text(length=10000))

    def get_id(self):
        return (self.id)

    def get_user_id(self):
        return str(self.user_id)

    def get_study_part(self):
        return (self.study_part)

    def get_corPos_sq(self):
        return (self.corPos_sq)

    def get_w0(self):
        return (self.w0)

    def get_w0(self):
        return (self.w0)

    def get_relevant_w(self):
        return (self.relevant_w)

    def get_val_corr_elem(self):
        return (self.val_corr_elem)

    def get_epsilon(self):
        return (self.epsilon)

    def get_precededShift(self):
        return (self.precededShift)

    def get_true_pop_size(self):
        return (self.true_pop_size)

    def errors(self):
        errors = super(TaskParams, self).errors()
        return errors
