"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR, Text  # ForeignKey
from models.db import Model
from models.base_object import BaseObject
import numpy


class MainTask(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id = Column(VARCHAR(length=100))
    study_part = Column(Integer, nullable=False)
    blockNum = Column(VARCHAR(length=100))
    startTime = Column(VARCHAR(length=100))
    sectionStartTime = Column(VARCHAR(length=100))
    blockFinishTime = Column(VARCHAR(length=100))
    all_element_values = Column(Text(length=10000), nullable=False)
    trialTotal = Column(VARCHAR(length=100))

    corr_elements = Column(Text(length=10000), nullable=False)
    trialSgmMu = Column(Text(length=10000), nullable=False)
    times_element1 = Column(Text(length=100000), nullable=False)
    times_element2 = Column(Text(length=100000), nullable=False)
    times_element3 = Column(Text(length=100000), nullable=False)
    element1Col = Column(VARCHAR(length=100), nullable=False)
    element2Col = Column(VARCHAR(length=100), nullable=False)
    element3Col = Column(VARCHAR(length=100), nullable=False)
    startSgm = Column(VARCHAR(length=100))
    startMu = Column(VARCHAR(length=100))
    all_true_pop_size = Column(Text(length=10000), nullable=False)
    indicKey = Column(Text(length=10000), nullable=False)
    outcomeHeight = Column(Text(length=100000), nullable=False)
    trialRT = Column(Text(length=10000), nullable=False)
    blockTotal = Column(VARCHAR(length=1000))
    indicReq = Column(VARCHAR(length=1000))
    trialPerBlock = Column(VARCHAR(length=100))
    bonusPerBlock = Column(Text(length=1000))
    sgmPrompt = Column(Text(length=1000))

    def get_id(self):
        return (self.id)

    def get_user_id(self):
        return str(self.user_id)

    def get_study_part(self):
        return (self.study_part)

    def get_blockNum(self):
        return (self.blockNum)

    def get_startTime(self):
        return (self.startTime)

    def get_sectionStartTime(self):
        return (self.sectionStartTime)

    def get_blockFinishTime(self):
        return (self.blockFinishTime)

    def get_all_element_values(self):
        return (self.all_element_values)

    def get_corr_elements(self):
        return (self.corr_elements)

    def get_trialSgmMu(self):
        return (self.trialSgmMu)

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

    def get_trialRT(self):
        return (self.trialRT)

    def get_trialTotal(self):
        return (self.trialTotal)

    def get_indicKey(self):
        return (self.indicKey)


    def get_blockTotal(self):
        return (self.blockTotal)

    def get_indicReq(self):
        return (self.indicReq)

    def get_trialPerBlock(self):
        return (self.trialPerBlock)

    def get_bonusPerBlock(self):
        return (self.bonusPerBlock)

    def get_sgmPrompt(self):
        return (self.sgmPrompt)

    def errors(self):
        errors = super(MainTask, self).errors()
        return errors
