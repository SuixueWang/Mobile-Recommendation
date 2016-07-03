#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wangsuixue'

from ReadCSV import ReadCSV
from DowmSample import DowmSample
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import numpy as np

'''
函数功能: 训练模型
'''
def model_train(Save = False, modelname = None):
    
    X1_left  = ReadCSV('datasets_csv/feature_0630_1700/X1_offline_0630_1700.csv','float64')
    X1_midle = ReadCSV('datasets_csv/feature_0701_1100/X1_offline_0701_1100.csv','float64')
    X1_right = ReadCSV('datasets_csv/feature_0701_1400/X1_offline_0701_1400.csv','float64')
    Y1 = ReadCSV('datasets_csv/feature_0701_1100/Y1_offline_0701_1100.csv','float64')    
    X1 = np.c_[X1_left,X1_midle,X1_right]
#     X1 = np.c_[X1_left]
    
    X1 = list(X1)
    Y1 = list(Y1)

    X2_left  = ReadCSV('datasets_csv/feature_0630_1700/X2_offline_0630_1700.csv','float64')
    X2_midle = ReadCSV('datasets_csv/feature_0701_1100/X2_offline_0701_1100.csv','float64')
    X2_right = ReadCSV('datasets_csv/feature_0701_1400/X2_offline_0701_1400.csv','float64')
    Y2 = ReadCSV('datasets_csv/feature_0701_1100/Y2_offline_0701_1100.csv','float64')    
    X2 = np.c_[X2_left,X2_midle,X2_right]
#     X2 = np.c_[X2_left]
    
    X2 = list(X2)
    Y2 = list(Y2)
    X1.extend(X2)
    Y1.extend(Y2)
    del X2,Y2
    
    X3_left  = ReadCSV('datasets_csv/feature_0630_1700/X3_offline_0630_1700.csv','float64')
    X3_midle = ReadCSV('datasets_csv/feature_0701_1100/X3_offline_0701_1100.csv','float64')
    X3_right = ReadCSV('datasets_csv/feature_0701_1400/X3_offline_0701_1400.csv','float64')
    Y3 = ReadCSV('datasets_csv/feature_0701_1100/Y3_offline_0701_1100.csv','float64')
     
    X3 = np.c_[X3_left,X3_midle,X3_right]
#     X3 = np.c_[X3_left]
    
    X3 = list(X3)
    Y3 = list(Y3)
    X1.extend(X3)
    Y1.extend(Y3)
    del X3,Y3
     
    X4_left  = ReadCSV('datasets_csv/feature_0630_1700/X4_offline_0630_1700.csv','float64')
    X4_midle = ReadCSV('datasets_csv/feature_0701_1100/X4_offline_0701_1100.csv','float64')
    X4_right = ReadCSV('datasets_csv/feature_0701_1400/X4_offline_0701_1400.csv','float64')
    Y4 = ReadCSV('datasets_csv/feature_0701_1100/Y4_offline_0701_1100.csv','float64')
       
    X4 = np.c_[X4_left,X4_midle,X4_right]
#     X4 = np.c_[X4_left]
     
    X4 = list(X4)
    Y4 = list(Y4)
    X1.extend(X4)
    Y1.extend(Y4)
    del X4,Y4
    
    X5_left  = ReadCSV('datasets_csv/feature_0630_1700/X5_offline_0630_1700.csv','float64')
    X5_midle = ReadCSV('datasets_csv/feature_0701_1100/X5_offline_0701_1100.csv','float64')
    X5_right = ReadCSV('datasets_csv/feature_0701_1400/X5_offline_0701_1400.csv','float64')
    Y5 = ReadCSV('datasets_csv/feature_0701_1100/Y5_offline_0701_1100.csv','float64')
      
    X5 = np.c_[X5_left,X5_midle,X5_right]
    X5 = list(X5)
    Y5 = list(Y5)
    X1.extend(X5)
    Y1.extend(Y5)
    del X5,Y5
     
    X6_left  = ReadCSV('datasets_csv/feature_0630_1700/X6_offline_0630_1700.csv','float64')
    X6_midle = ReadCSV('datasets_csv/feature_0701_1100/X6_offline_0701_1100.csv','float64')
    X6_right = ReadCSV('datasets_csv/feature_0701_1400/X6_offline_0701_1400.csv','float64')
    Y6 = ReadCSV('datasets_csv/feature_0701_1100/Y6_offline_0701_1100.csv','float64')
      
    X6 = np.c_[X6_left,X6_midle,X6_right]
    X6 = list(X6)
    Y6 = list(Y6)
    X1.extend(X6)
    Y1.extend(Y6)
    del X6,Y6
     
    X7_left  = ReadCSV('datasets_csv/feature_0630_1700/X7_offline_0630_1700.csv','float64')
    X7_midle = ReadCSV('datasets_csv/feature_0701_1100/X7_offline_0701_1100.csv','float64')
    X7_right = ReadCSV('datasets_csv/feature_0701_1400/X7_offline_0701_1400.csv','float64')
    Y7 = ReadCSV('datasets_csv/feature_0701_1100/Y7_offline_0701_1100.csv','float64')
      
    X7 = np.c_[X7_left,X7_midle,X7_right]
    X7 = list(X7)
    Y7 = list(Y7)
    X1.extend(X7)
    Y1.extend(Y7)
    del X7,Y7
     
    X8_left  = ReadCSV('datasets_csv/feature_0630_1700/X8_offline_0630_1700.csv','float64')
    X8_midle = ReadCSV('datasets_csv/feature_0701_1100/X8_offline_0701_1100.csv','float64')
    X8_right = ReadCSV('datasets_csv/feature_0701_1400/X8_offline_0701_1400.csv','float64')
    Y8 = ReadCSV('datasets_csv/feature_0701_1100/Y8_offline_0701_1100.csv','float64')
      
    X8 = np.c_[X8_left,X8_midle,X8_right]
    X8 = list(X8)
    Y8 = list(Y8)
    X1.extend(X8)
    Y1.extend(Y8)    
    del X8,Y8 
     
     
     
    X1 = np.array(X1)
    Y1 = np.array(Y1)
    
    X1,Y1 = DowmSample(X1,Y1,8)
    
    model = GradientBoostingClassifier(n_estimators=100,max_leaf_nodes=5, learning_rate=0.1, subsample=0.8, random_state=1)
    model.fit(X1, Y1.ravel())
    
    # 保存模型
    if Save == True:
        f = open(modelname,'w')
        pickle.dump(model, f)
        f.close()
    
    print '\n ------------- Training is over ----------------------'    
    return model
        
'''
函数功能: 预测模型
'''
def model_predict(model):
    
    X_online_l = ReadCSV('datasets_csv/X_online_0630_1700.csv','float64')  
    X_online_m = ReadCSV('datasets_csv/X_online_0701_1100.csv','float64')  
    X_online_r = ReadCSV('datasets_csv/X_online_0701_1400.csv','float64')  
    
    X_online = np.c_[X_online_l,X_online_m,X_online_r]
    
    Y_preds = model.predict_proba(X_online)  
    
    
    proba_positive = []
    for y in Y_preds:
        proba_positive.append(y[1])
    
    del Y_preds
    
    print '\n -------------- Predicting is over ---------------------'
    return proba_positive

'''
函数功能: 按所属类别的置信度排序,并选择排在前面的结果作为提交结果
'''
def model_sortAndsubmit(proba_positive,thr):
    
    id_ui = ReadCSV('datasets_csv/id_ui_online_0630_1700.csv', object)
    
    samples = zip(id_ui,proba_positive)
    preds_samples = sorted(samples,key=lambda x:x[1], reverse = True)
    
    print 'The number of predicting samples are ',len(proba_positive) 
    submits = []
    for i in range(len(proba_positive)):
        sample = preds_samples[i]
        if(sample[1] > thr):
            submits.append((sample[0][0],sample[0][1]))  
 
    print '\n -------------- Sorting is over-------------------'
    return submits

'''
函数功能: 保存待提交的结果
'''
def model_save(submits,filename):
    
    submitResult = list(set(submits))
    print '\n The number of SubmitResults are ',len(submitResult)
    
    wf = open(filename,'w')
    wf.write('user_id,item_id\n')
    for i in range(len(submitResult)):
        wf.write('%s,%s\n'%(submitResult[i][0],submitResult[i][1]))
     
    wf.close()


    

    