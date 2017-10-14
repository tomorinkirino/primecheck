#Python 2.7.6
#coding: utf8

import random

def prime_check(q,k=52):
    q = abs(q)
    #簡単なものを判定
    if q == 2: return True  #2と等しいならTrue
    if q < 2 or q&1 == 0: return False  #2より小さい or 0と等しいならFalse
    
    #ミラー・ラビン素数判定法(確率的判定法) 参考： https://ja.wikipedia.org/wiki/ミラー–ラビン素数判定法
    #n-1を2^s*dの形にしてdを求める（aは整数、dは奇数)
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    #判定をk回繰り返す(間違える確率は4^-k)
    for i in xrange(k): #k回繰り返す
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲のすべてをチェック
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True
