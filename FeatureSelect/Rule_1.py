#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'


import MySQLdb

def Rule_1(id_ui,time_start,time_end):
    
    print '----- x_rule_1 -----'

    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()    

    # ------------------------------- UF3 -------------------------------------------------
    sql_UF_B3 = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s' and\
                    behavior_type = '3'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF_B3)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF3_B3_dict = {}
    for key in results:
        UF3_B3_dict[(key[0],key[1])] = key[2]

    print '--- UF3 ---'

    # ------------------------------- UF4 -------------------------------------------------
    sql_UF_B4 = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s' and\
                    behavior_type = '4'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF_B4)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF4_B4_dict = {}
    for key in results:
        UF4_B4_dict[(key[0],key[1])] = key[2]
        print key[0],key[1]

    print 'buy ',len(UF4_B4_dict)    
    print '--- UF4 ---'
    
        
    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()
    
    
    # ------------------------------------------ 整理特征 ----------------------------------
    X_rule = []
    for uid in id_ui:
        if(True == UF3_B3_dict.has_key(uid)):
            if(False == UF4_B4_dict.has_key(uid)):
                X_rule.append((uid[0],uid[1]))   
                
    print 'len of X_rule ia ',len(X_rule)            
                
    supplement = {}
    with open('SubmitsResults/tianchi_mobile_recommendation_predict_0630_0.65.csv','r') as fp:
        for line in fp:
            line = line.strip()
            value = line.split(',')

            supplement[(value[0],value[1])] = 1

    fp.close()
    
    print 'len of original ia ',len(supplement)
    
    X_rule = list(set(X_rule))
    for x in X_rule:
        if(~supplement.has_key(x)):
            supplement[x] = 1
    
    X_rule = []
    for key in supplement:
        X_rule.append((key[0],key[1]))
        
    # --------------------------------------
    k = 0
    for uid in X_rule:
        if(UF4_B4_dict.has_key(uid)):
            k += 1
    print 'k = ',k
    
    # --------------------------------------

    return X_rule



