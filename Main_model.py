#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wangsuixue'

# 分别导入线下和线上的包
import Main_processing_offline as MpOff
import Main_processing_online  as MpOn
from ReadCSV import ReadCSV
import numpy as np
import pickle

'''
函数功能: 线下处理主函数
'''
def main_offline():
    print '------------------- start -----------------------------'

    # 线下训练
#     model = MpOff.model_train(True,'model_tmp.pkl')
    
    f = open('model_tmp.pkl','r')
    model = pickle.load(f)
    f.close()
    
    # 线下预测
    proba_positive = MpOff.model_predict(model)
    
    # 线下预测结果排序,并挑选概率大于门限的值提交
    submits = MpOff.model_sortAndsubmit(proba_positive,0.310) # 0.28
    
    # 线下评估
    MpOff.model_evaluation_offline(submits)
    
    print '------------------- over -----------------------------'


'''
函数功能: 线下模型融合处理主函数
'''
def main_offline_ensemble():
    print '------------------- start -----------------------------'

    # -------------------------------- 模型1 --------------------------------------------
    X1_left  = ReadCSV('datasets_csv/feature_0630_1700/X1_offline_0630_1700.csv','float64')
    X1_midle = ReadCSV('datasets_csv/feature_0701_1100/X1_offline_0701_1100.csv','float64')
    X1_right = ReadCSV('datasets_csv/feature_0701_1400/X1_offline_0701_1400.csv','float64')
    Y1 = ReadCSV('datasets_csv/feature_0701_1100/Y1_offline_0701_1100.csv','float64')    
    X1 = np.c_[X1_left,X1_midle,X1_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X1,Y1,Save=False)
    
    # 线下预测
    proba_positive1 = MpOff.model_predict(model)


    # -------------------------------- 模型3 --------------------------------------------
    X3_left  = ReadCSV('datasets_csv/feature_0630_1700/X3_offline_0630_1700.csv','float64')
    X3_midle = ReadCSV('datasets_csv/feature_0701_1100/X3_offline_0701_1100.csv','float64')
    X3_right = ReadCSV('datasets_csv/feature_0701_1400/X3_offline_0701_1400.csv','float64')
    Y3 = ReadCSV('datasets_csv/feature_0701_1100/Y3_offline_0701_1100.csv','float64')
     
    X3 = np.c_[X3_left,X3_midle,X3_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X3,Y3,Save=False)
    
    # 线下预测
    proba_positive3 = MpOff.model_predict(model)

    # -------------------------------- 模型4 --------------------------------------------
    X4_left  = ReadCSV('datasets_csv/feature_0630_1700/X4_offline_0630_1700.csv','float64')
    X4_midle = ReadCSV('datasets_csv/feature_0701_1100/X4_offline_0701_1100.csv','float64')
    X4_right = ReadCSV('datasets_csv/feature_0701_1400/X4_offline_0701_1400.csv','float64')
    Y4 = ReadCSV('datasets_csv/feature_0701_1100/Y4_offline_0701_1100.csv','float64')
     
    X4 = np.c_[X4_left,X4_midle,X4_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X4,Y4,Save=False)
    
    # 线下预测
    proba_positive4 = MpOff.model_predict(model)

    # -------------------------------- 模型5 --------------------------------------------
    X5_left  = ReadCSV('datasets_csv/feature_0630_1700/X5_offline_0630_1700.csv','float64')
    X5_midle = ReadCSV('datasets_csv/feature_0701_1100/X5_offline_0701_1100.csv','float64')
    X5_right = ReadCSV('datasets_csv/feature_0701_1400/X5_offline_0701_1400.csv','float64')
    Y5 = ReadCSV('datasets_csv/feature_0701_1100/Y5_offline_0701_1100.csv','float64')
     
    X5 = np.c_[X5_left,X5_midle,X5_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X5,Y5,Save=False)
    
    # 线下预测
    proba_positive5 = MpOff.model_predict(model)
    
    # -------------------------------- 模型6 --------------------------------------------
    X6_left  = ReadCSV('datasets_csv/feature_0630_1700/X6_offline_0630_1700.csv','float64')
    X6_midle = ReadCSV('datasets_csv/feature_0701_1100/X6_offline_0701_1100.csv','float64')
    X6_right = ReadCSV('datasets_csv/feature_0701_1400/X6_offline_0701_1400.csv','float64')
    Y6 = ReadCSV('datasets_csv/feature_0701_1100/Y6_offline_0701_1100.csv','float64')
     
    X6 = np.c_[X6_left,X6_midle,X6_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X6,Y6,Save=False)
    
    # 线下预测
    proba_positive6 = MpOff.model_predict(model)
    
    # -------------------------------- 模型7 --------------------------------------------
    X7_left  = ReadCSV('datasets_csv/feature_0630_1700/X7_offline_0630_1700.csv','float64')
    X7_midle = ReadCSV('datasets_csv/feature_0701_1100/X7_offline_0701_1100.csv','float64')
    X7_right = ReadCSV('datasets_csv/feature_0701_1400/X7_offline_0701_1400.csv','float64')
    Y7 = ReadCSV('datasets_csv/feature_0701_1100/Y7_offline_0701_1100.csv','float64')
     
    X7 = np.c_[X7_left,X7_midle,X7_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X7,Y7,Save=False)
    
    # 线下预测
    proba_positive7 = MpOff.model_predict(model)

    # -------------------------------- 模型8 --------------------------------------------
    X8_left  = ReadCSV('datasets_csv/feature_0630_1700/X8_offline_0630_1700.csv','float64')
    X8_midle = ReadCSV('datasets_csv/feature_0701_1100/X8_offline_0701_1100.csv','float64')
    X8_right = ReadCSV('datasets_csv/feature_0701_1400/X8_offline_0701_1400.csv','float64')
    Y8 = ReadCSV('datasets_csv/feature_0701_1100/Y8_offline_0701_1100.csv','float64')
     
    X8 = np.c_[X8_left,X8_midle,X8_right]
    
    # 线下训练
    model = MpOff.model_train_ensemble(X8,Y8,Save=False)
    
    # 线下预测
    proba_positive8 = MpOff.model_predict(model)

    # -------------------------------- 模型融合 -------------------------------------
    
    proba_positive = []
    for i in range(len(proba_positive1)):
        avr = 0.2 * proba_positive1[i] + 0.2 * proba_positive3[i] + 0.2 * proba_positive4[i] + \
              0.1 * proba_positive5[i] + 0.1 * proba_positive6[i] + 0.1 * proba_positive7[i] + 0.1 * proba_positive8[i]
        proba_positive.append(avr)
    
    # 线下预测结果排序,并挑选概率大于门限的值提交
    submits = MpOff.model_sortAndsubmit(proba_positive,0.28) # 0.28
    
    # 线下评估
    MpOff.model_evaluation_offline(submits)
    
    print '------------------- over -----------------------------'

    
'''
函数功能: 线上处理主函数
'''
def main_online_ensemble():
    
    print '------------------- start -----------------------------'

    # -------------------------------- 模型1 --------------------------------------------
    X1_left  = ReadCSV('datasets_csv/feature_0630_1700/X1_offline_0630_1700.csv','float64')
    X1_midle = ReadCSV('datasets_csv/feature_0701_1100/X1_offline_0701_1100.csv','float64')
    X1_right = ReadCSV('datasets_csv/feature_0701_1400/X1_offline_0701_1400.csv','float64')
    Y1 = ReadCSV('datasets_csv/feature_0701_1100/Y1_offline_0701_1100.csv','float64')    
    X1 = np.c_[X1_left,X1_midle,X1_right]
    
    # 线上训练
    model = MpOff.model_train_ensemble(X1,Y1,Save=False)
    
    # 线上预测
    proba_positive1 = MpOff.model_predict(model)


    # -------------------------------- 模型2 --------------------------------------------
    X2_left  = ReadCSV('datasets_csv/feature_0630_1700/X2_offline_0630_1700.csv','float64')
    X2_midle = ReadCSV('datasets_csv/feature_0701_1100/X2_offline_0701_1100.csv','float64')
    X2_right = ReadCSV('datasets_csv/feature_0701_1400/X2_offline_0701_1400.csv','float64')
    Y2 = ReadCSV('datasets_csv/feature_0701_1100/Y2_offline_0701_1100.csv','float64')    
    X2 = np.c_[X2_left,X2_midle,X2_right]
    
    # 线上训练
    model = MpOff.model_train_ensemble(X2,Y2,Save=False)
    
    # 线上预测
    proba_positive2 = MpOff.model_predict(model)

    # -------------------------------- 模型3 --------------------------------------------
    X3_left  = ReadCSV('datasets_csv/feature_0630_1700/X3_offline_0630_1700.csv','float64')
    X3_midle = ReadCSV('datasets_csv/feature_0701_1100/X3_offline_0701_1100.csv','float64')
    X3_right = ReadCSV('datasets_csv/feature_0701_1400/X3_offline_0701_1400.csv','float64')
    Y3 = ReadCSV('datasets_csv/feature_0701_1100/Y3_offline_0701_1100.csv','float64')
     
    X3 = np.c_[X3_left,X3_midle,X3_right]
    
    # 线上训练
    model = MpOff.model_train_ensemble(X3,Y3,Save=False)
    
    # 线上预测
    proba_positive3 = MpOff.model_predict(model)

    # -------------------------------- 模型4 --------------------------------------------
    X4_left  = ReadCSV('datasets_csv/feature_0630_1700/X4_offline_0630_1700.csv','float64')
    X4_midle = ReadCSV('datasets_csv/feature_0701_1100/X4_offline_0701_1100.csv','float64')
    X4_right = ReadCSV('datasets_csv/feature_0701_1400/X4_offline_0701_1400.csv','float64')
    Y4 = ReadCSV('datasets_csv/feature_0701_1100/Y4_offline_0701_1100.csv','float64')
     
    X4 = np.c_[X4_left,X4_midle,X4_right]
    
    # 线上训练
    model = MpOff.model_train_ensemble(X4,Y4,Save=False)
    
    # 线上预测
    proba_positive4 = MpOff.model_predict(model)
    
    # -------------------------------- 模型融合 -------------------------------------
    
    proba_positive = []
    for i in range(len(proba_positive1)):
        
        avr = 0.3 * proba_positive1[i] + 0.3 * proba_positive2[i] + 0.2 * proba_positive3[i] + 0.2 * proba_positive4[i]

        proba_positive.append(avr)
    
    # 线上预测结果排序,并挑选概率大于门限的值提交
    submits = MpOff.model_sortAndsubmit(proba_positive,0.65  ) # 0.28
    
    # 保存线上预测结果到csv文件
    MpOn.model_save(submits, 'SubmitsResults/tianchi_mobile_recommendation_predict_0703_ensemble_826.csv')
    
    
    print '------------------- over -----------------------------'        


'''
函数功能: 线上处理主函数
'''
def main_online():
    
    print '------------------- start -----------------------------'

    # 线上训练
#     model = MpOn.model_train(True,'model_online_0701_1700.pkl')
    
    f = open('model_online_0701_1700.pkl','r')
    model = pickle.load(f)
    f.close()
    
    # 线上预测
    proba_positive = MpOn.model_predict(model)
    
    # 线上预测结果排序,并挑选概率大于门限的值提交
    submits = MpOn.model_sortAndsubmit(proba_positive,0.645)
    
    # 保存线上预测结果到csv文件
    MpOn.model_save(submits, 'SubmitsResults/tianchi_mobile_recommendation_predict_0701_557.csv')
    
    
    print '------------------- over -----------------------------'        
    


if __name__ == '__main__':
    
    # 处理线下数据
#     main_offline()

    # 处理线上数据
#     main_online()

#     main_offline_ensemble()
    
    main_online_ensemble()
    
    # 实际线上经过推算,共有517个购买量

