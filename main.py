# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
from styleframe import StyleFrame, Styler
respon = requests.get('https://tw.sports.yahoo.com/nba/teams/%E6%8B%93%E8%8D%92%E8%80%85/stats/')
res = BeautifulSoup(respon.content, 'lxml')
nams = res.find_all('tr',{'class':"Bgc(table-hover):h"})
df01 = pd.DataFrame(columns=['名字',"比賽",'命中','罰球命中',"三分命中","得分","進攻籃版",'防守籃版','籃版','助攻',"抄截","阻攻","失誤","犯規"])
for td in nams:
    '''
    名字
    '''
    nam = td.find_all("td")[0].get_text()
    '''
    比賽
    '''
    gam = td.find_all("td")[1].get_text()
    '''
    命中
    '''
    shoot = td.find_all("td")[5].get_text()
    '''
    罰球命中
    '''
    rules = td.find_all("td")[8].get_text()
    '''
    三分命中
    '''
    thres = td.find_all("td")[11].get_text()
    '''
    得分
    '''
    point = td.find_all("td")[12].get_text()
    '''
    進攻籃版
    '''
    fen = td.find_all("td")[13].get_text()
    '''
    防守籃版
    '''
    dfen = td.find_all("td")[14].get_text()
    '''
    籃版
    '''
    rebound = td.find_all("td")[15].get_text()
    '''
    助攻
    '''
    ad = td.find_all("td")[16].get_text()
    '''
    抄截
    '''
    steal = td.find_all("td")[17].get_text()
    '''
    阻攻
    '''
    block = td.find_all("td")[18].get_text()
    '''
    失誤
    '''
    mistak = td.find_all("td")[19].get_text()
    '''
    犯規
    '''
    misrul = td.find_all("td")[20].get_text()
    surie = pd.Series([nam,gam,shoot,rules,thres,point,fen,dfen,rebound,ad,steal,block,mistak,misrul],
                      index=['名字',"比賽",'命中','罰球命中',"三分命中","得分","進攻籃版",'防守籃版','籃版','助攻',"抄截","阻攻","失誤","犯規"])
    df01 = df01.append(surie, ignore_index=True)
    df01.index = df01.index+1
    print(nam +" "+gam+" "+shoot+" "+rules+" "+thres+" "+point+" "+fen+" "+dfen+" "+rebound+" "+ad+" "+steal+" "+block+" "+mistak+" "+misrul)
print(df01)
sf = StyleFrame(df01)
sf.set_column_width_dict(col_width_dict={("罰球命中"): 22,("三分命中"): 22,("進攻籃版"):22,("防守籃版"):22,("名字"):39})
sname = 'nba.xlsx'
output = sf.to_excel(sname).save()
