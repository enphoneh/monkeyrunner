#!/usr/bin/python  
#encoding:utf-8
#encoding=gbk


'''
Created on 2014年11月11日

@author: huangyinfeng
'''


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnection(8,'4d00833a528c8057')


#keyboards  480x854，需要根据机器分辨率和使用的输入法调节
dict_arr = {'qx':62, 'wx':159, 'ex':277,'rx':377,'tx':477,'yx':577,'ux':677,'ix':777,'ox':877,'px':977,
            'qy':1347,'wy':1347,'ey':1347,'ry':1347,'ty':1347,'yy':1347,'uy':1347,'iy':1347,'oy':1347,'py':1347,
            'ax':112, 'sx':202, 'dx':307,'fx':402,'gx':502,'hx':602,'jx':702,'kx':812,'lx':930,
            'ay':1512,'sy':1512,'dy':1512,'fy':1512,'gy':1512,'hy':1512,'jy':1512,'ky':1512,'ly':1512,
            'zx':217, 'xx':317,'cx':417,'vx':517,'bx':617,'nx':800,'mx':910,
            'zy':1667,'xy':1667,'cy':1667,'vy':1667,'by':1667,'ny':1667,'my':1667,
            '空格x':570,
            '空格y':1840,
            '回车x':978,
            '回车y':1840}

            
#inputwords
words = ('concentraition',
        'understansing',
        'infrastrucyure',
        'underdevelpmennt',
        'endorrsemnt',
        'conveertibility',
        'depreciaetion',
        'Avataars',
        'Hashags',
        'Scunthhorpe',
        'Trollong',
        'Spaam',
        'Cupertimo',
        'Geedks',
        'Advancce',
        'Bugdet',
        'Bost',
        'Conply',
        'Collbaorate',
        'Deisgn',
        'Efficient',
        'Enhane',
        'Forcast',
        'Genenrate',
        'Hodt',
        'Impllement',
        'Invsetigate',
        'Juistify',
        'Lidt',
        'Mainain',
        'Negoitate',
        'Obsirve',
        'Prograam',
        'Proect',
        'Qialify',
        'Recomend',
        'Susntain',
        'Schdule',
        'Trijmph',
        'Transate',
        'Uodate',
        'Upgrsd',
        'Valiaate',
        'Worlwide',
        'calishtenics',
        'pesumptuous',
        'treacheerous',
        'revererate',
        'superabiundant',
        'unentcumbered',
        'Homogneously',
        'MITt',
        'Luree',
        'substittion',
        'peramnent',
        'conventtion',
        'magistreate',
        'manuafcture',
        'renissance',
        'CAIz',
        'acrophovia',
        'ASArP',
        'orcheestra',
        'opiuim',
        'oriendtation',
        'accopmmodation',
        'loby',
        'bils',
        'maximm',
        'decroation',
        'passaport',
        'acceount',
        'depolsit',
        'stateent',
        'PINe',
        'compeetition',
        'Voilunteer',
        'festiveal',
        'opea',
        'thrller',
        'gyn',
        'annufal',
        'receeption',
        'gollf',
        'squeash',
        'matrsh',
        'vallrey',
        'cliffa',
        'areeas',
        'boooklet',
        'anatonmy',
        'Ctb',
        'denetist',
        'inventozry',
        'margixn',
        'reveonue',
        'exrtanet',
        'firewaull',
        'virwus')

Times=0
for j in range(0,10000):
    for i in range(0,len(words)):
        word=words[i].lower()
        for key in list(word):
            device.touch(dict_arr.get(key+'x'),dict_arr.get(key+'y'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.1)
        Times=Times+1
        path = "./pic/"+str(Times)+".png"
        print ("total times:"+str(Times)+",now input:=====>"+word)
        MonkeyRunner.sleep(0.1)
        # 截屏
        #result = device.takeSnapshot()
        #print ("takeshot")
        MonkeyRunner.sleep(0.1)
        device.touch(dict_arr.get('空格x'),dict_arr.get('空格y'),MonkeyDevice.DOWN_AND_UP)
        #MonkeyRunner.sleep(0.1)
        #device.touch(dict_arr.get('回车x'),dict_arr.get('回车y'),MonkeyDevice.DOWN_AND_UP)
        # 保存截屏
        #result.writeToFile(path,'png')
        MonkeyRunner.sleep(0.2)
    if j%2==0:
        device.touch(806,1200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
        device.touch(80,1336,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
        device.touch(250,1336,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
        device.touch(80,1185,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
    else:
        device.touch(280,1200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
        device.touch(140,1350,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
        device.touch(930,1350,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)
        device.touch(280,1200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.1)