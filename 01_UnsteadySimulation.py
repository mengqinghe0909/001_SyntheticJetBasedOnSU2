
'''
This is to imply synthetic jets on SU2
'''
import numpy as np
import os
import math

# period_steps stands for the steps included in one cycle
period_steps = 100
cfg_file_name = '3D.cfg'



m_file_names = os.listdir()
vtk_names = []
for item in m_file_names:
    if item.find('.vtk') != -1:
        vtk_names.append(item)

def main():
    os.system('multicore.bat')
    while True:
        file_names = os.listdir()
        for file_name in file_names:
            if file_name.find('.vtk') != -1:
                if file_name in vtk_names:
                    pass
                else:
                    vtk_names.append(file_name)
                    count = len(vtk_names)
                    step = count % period_steps
                    changecfg(step, count)
                    os.system('multicore.bat')


# this function changes the inlet boundary contion and the restart iteration in the cfg file
# the direction of the inlet BCs is perpendicular to the wall
def changecfg(step, count):
    flow_velocity = np.sin(2*math.pi*step/period_steps)*1.8
    changestr('MARKER_INLET', 'MARKER_INLET= ( JETHOLEUPPER, 300, ' + str(flow_velocity) + ', -0.052336, 0.99863, 0.0, JETHOLELOWER, 300, ' + str(flow_velocity) + ', -0.052336, -0.99863, 0.0) \t\n')
    str_iter = 'RESTART_ITER= ' + str(count) + ' \t\n'
    changestr('RESTART_ITER', str_iter)

# this function is to change cfg file with new parameters
def changestr(old_str, new_str):
    with open(cfg_file_name, 'r') as cfg:
        cfg_text = cfg.readlines()
    with open(cfg_file_name, 'w') as cfg:
        for line in cfg_text:
            if line.find(old_str) != -1:
                cfg.write(new_str)
            else:
                cfg.write(line)

if __name__ == "__main__":
    main()
