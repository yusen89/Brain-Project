#!/usr/bin/python
# -*- coding: UTF-8 -*-
class neuron:
    '神经元'

    def __int__(self, ran, tra, rva):
        self.tra = tra
        self.ran = ran
        self.rva = rva
        self.val = 1

    def res(self):
        if ran == 1:
            return random.randint(0, 1)
        if tra == -1:
            return not(self.val)
        elif tra ==0:
            return self.val or self.rva
        else:
            return self.val and self.rva
            
