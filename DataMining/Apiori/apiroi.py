'''
Created on 2015年7月10日

@author: Administrator
'''

def load_data_set():
    return [[1, 3, 4], [2, 3, 4], [1, 2, 3, 5], [2, 5]]
def create_c1(data_set):
    c1 = []
    for transcation in data_set:
        for item in transcation:
            if [item] not in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)
def scan_d(data_set, ck, min_support):
    D = map(set, data_set)
    ss_cnt = {}
    for tid in D:
        for can in ck:
            if can.issubset(tid):
                if can not in ss_cnt.keys():
                    ss_cnt[can] = 1
                else:
                    ss_cnt[can] += 1
    num_items = float(len(D))
    
    ret_list= []
    support_data = {}
    
    for key in ss_cnt:
        support = ss_cnt[key]/num_items
        if support >=min_support:
            ret_list.insert(0, key)
        support_data[key] = support
    return ret_list, support_data    
    
    
    
    
            
                        
            







