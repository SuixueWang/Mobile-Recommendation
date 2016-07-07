#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'

import sys
sys.path.append('/home/learning_resource/machine_learning/source/MobileRecommedation/src/FeatureSelect')
sys.path.append('/home/learning_resource/machine_learning/source/MobileRecommedation/src/UI_Label')

from GetUI import GetUI_offline,GetUI_online
from GetLabel import GetLabel 
from UnionFeature import UnionFeature
from UserFeature import UserFeature
from ItemFeature import ItemFeature
from Rule_1 import Rule_1
import time
import pandas as pd
import numpy as np

'''
函数功能: 提取线下用户数据集
'''
def GetDataSets_offline(time_start_ui,time_start,time_end,time_end_lable):
    
    id_ui   = GetUI_offline(time_start_ui,time_end,time_end_lable)
    
    X_user = UserFeature(id_ui,time_start,time_end)
      
    X_item = ItemFeature(id_ui,time_start_ui,time_start,time_end)
    
    X_union = UnionFeature(id_ui,time_start,time_end)
    
    X = np.c_[X_user,X_item,X_union]
#     X = X_union
    X = list(X)
    
    Y,id_ui_buy = GetLabel(id_ui,time_end,time_end_lable)
    
    return X, Y, id_ui, id_ui_buy

'''
函数功能: 提取线上用户数据集
'''
def GetDataSets_online(time_start_ui,time_start,time_end):
    
    id_ui   = GetUI_online(time_start_ui,time_end)
    
#     X_user = UserFeature(id_ui,time_start,time_end)
#     
#     X_item = ItemFeature(id_ui,time_start_ui,time_start,time_end)
    
    X_union = UnionFeature(id_ui,time_start,time_end)
    
#     X = np.c_[X_user,X_item,X_union]
    X = X_union
    X = list(X)
    
    return X,id_ui


def GetRuleOnline(time_start,time_end):
    
    id_ui   = GetUI_online(time_start,time_end)
    
    X_rule = Rule_1(id_ui,time_start,time_end)
    
    X = list(X_rule)
    
    return X,id_ui

'''
主函数
'''
if __name__ == '__main__':
    print 'start'
    
    # ------------------------------- 规则1 -----------------------------------------------
    
    time_start     = '2014-12-18 20'
    time_end       = '2014-12-18 23'
    X,id_ui = GetRuleOnline(time_start,time_end)
    
    # 保存线上预测结果到csv文件
    import Main_processing_online  as MpOn
    MpOn.model_save(X, 'SubmitsResults/tianchi_mobile_recommendation_predict_0.65_rule3.csv')
    
    time1 = time.time()

    # ------------------------------- 数据1 -----------------------------------------------
    print '--------------- datasets 1 ---------------'    
    time_start_ui  = '2014-12-05 23'
    time_start     = '2014-12-05 23'
    time_end       = '2014-12-06 23'
    time_end_lable = '2014-12-07 23'
    
#     X,Y,id_ui,id_ui_buy = GetDataSets_offline(time_start_ui,time_start,time_end,time_end_lable)
#     
#     print 'The number of X is ',len(X)
#     print 'The number of Y is ',len(X)
#     print 'The number of id_ui is ',len(id_ui)
#     
#     df = pd.DataFrame(X)
#     df.to_csv('datasets_csv/X5_offline_0630_1700.csv',encoding='utf-8')
#     del X
#      
#     df = pd.DataFrame(Y)
#     df.to_csv('datasets_csv/Y5_offline_0630_1700.csv',encoding='utf-8')
#     del Y
#     del id_ui,id_ui_buy
    
    # ------------------------------- 数据2 -----------------------------------------------   
    print '--------------- datasets 2 ---------------'
    time_start_ui  = '2014-12-06 23'  
    time_start     = '2014-12-06 23'
    time_end       = '2014-12-07 23'
    time_end_lable = '2014-12-08 23'
    
#     X,Y,id_ui,id_ui_buy = GetDataSets_offline(time_start_ui,time_start,time_end,time_end_lable)
#      
#     print 'The number of X is ',len(X)
#     print 'The number of Y is ',len(X)
#     print 'The number of id_ui is ',len(id_ui)
#      
#     df = pd.DataFrame(X)
#     df.to_csv('datasets_csv/X6_offline_0630_1700.csv',encoding='utf-8')
#     del X
#      
#     df = pd.DataFrame(Y)
#     df.to_csv('datasets_csv/Y6_offline_0630_1700.csv',encoding='utf-8')
#     del Y
    
#     df = pd.DataFrame(id_ui)
#     df.to_csv('datasets_csv/id_ui_offline_0630_1700.csv',encoding='utf-8',float_format='string')
#     del id_ui
# 
#     df = pd.DataFrame(id_ui_buy)
#     df.to_csv('datasets_csv/id_ui_buy_offline_0630_1700.csv',encoding='utf-8',float_format='string')
#     del id_ui_buy

    # ------------------------------- 数据3 -----------------------------------------------    
    print '--------------- datasets 3 ---------------' 
    time_start_ui  = '2014-12-17 23'
    time_start     = '2014-12-18 17'
    time_end       = '2014-12-18 23'
#     X_online,id_ui = GetDataSets_online(time_start_ui,time_start,time_end)
#    
#     print 'The number of X_online is ',len(X_online)
#     print 'The number of id_ui is ',len(id_ui)
#        
#     df = pd.DataFrame(X_online)
#     df.to_csv('datasets_csv/X_online_0701_1400.csv',encoding='utf-8')
#     del X_online
#     
#     df = pd.DataFrame(id_ui)
#     df.to_csv('datasets_csv/id_ui_online_0701_1100.csv',encoding='utf-8',float_format='string')
#     del id_ui

    # --------------------------------------------------------------------------------------------   
    print 'Total time is ',time.time() - time1
    print 'over'