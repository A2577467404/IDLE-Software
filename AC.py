'''
IDLE Studios 与 HackGate 制作
制作人员名单：
[HackGate]HG_Backdoor
[IDLE]CondaIDLE

FailsafeCore版本：0.12.8
当前版本FailsafeAC最后更新日期：2021.5.2
FailsafeAC版本：0.1.2

目前Failsafe核心反作弊可检测：
Cheat Engine 7+
'''

CE_process = ['Cheat Engine.exe','cheatengine-i386.exe','cheatengine-x86_64.exe','windowsrepair.exe'] #CheatEngine可能的进程列表

import os
import sys
import psutil

#定义检测进程函数
def ac_normal(name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == name:
                output = True #检测到进程
        else:
            output = False
        pass
    pass

for i in range(len(CE_process)): #依次检测进程
    ac_normal(CE_process[i])
    pass


with open('output','w')as o:
    o.write(output) #输出检测结果
    pass
