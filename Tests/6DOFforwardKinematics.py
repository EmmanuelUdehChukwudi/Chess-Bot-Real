import numpy as np
from numpy import sin, cos
T1 = np.deg2rad(0)
T2 = np.deg2rad(0)
T3 = np.deg2rad(0)
T4 = np.deg2rad(0)
T5 = np.deg2rad(0)
T6 = np.deg2rad(0)

a1 = 0.138
a2 = 0.106
a3 = 0.115
a4 = 0.19

DH_table = np.array([[T1, np.pi/2, 0, a1],
                     [T2, np.pi,  a2, 0],
                     [T3, np.pi/2, 0, 0],
                     [T4+np.pi/2, np.pi/2, 0, a3],
                     [T5+np.pi/2, np.pi/2, 0, 0],
                     [T6, 0, 0, a4]])

def forward_kinematics(DH_table):
    H0_1 = np.array([[cos(DH_table[0][0]), -sin(DH_table[0][0])*cos(DH_table[0][1]),sin(DH_table[0][0])*sin(DH_table[0][1]),DH_table[0][2]*cos(DH_table[0][0])],
                     [sin(DH_table[0][0]), cos(DH_table[0][0])*cos(DH_table[0][1]),-cos(DH_table[0][0])*sin(DH_table[0][1]),DH_table[0][2]*sin(DH_table[0][0])],
                     [0, sin(DH_table[0][1]), cos(DH_table[0][1]),DH_table[0][3]],
                     [0,0,0,1]])
    H1_2 = np.array([[cos(DH_table[1][0]), -sin(DH_table[1][0])*cos(DH_table[1][1]),sin(DH_table[1][0])*sin(DH_table[1][1]),DH_table[1][2]*cos(DH_table[1][0])],
                     [sin(DH_table[1][0]), cos(DH_table[1][0])*cos(DH_table[1][1]),-cos(DH_table[1][0])*sin(DH_table[1][1]),DH_table[1][2]*sin(DH_table[1][0])],
                     [0, sin(DH_table[1][1]), cos(DH_table[1][1]),DH_table[1][3]],
                     [0,0,0,1]])
    
    H2_3 = np.array([[cos(DH_table[2][0]), -sin(DH_table[2][0])*cos(DH_table[2][1]),sin(DH_table[2][0])*sin(DH_table[2][1]),DH_table[2][2]*cos(DH_table[2][0])],
                     [sin(DH_table[2][0]), cos(DH_table[2][0])*cos(DH_table[2][1]),-cos(DH_table[2][0])*sin(DH_table[2][1]),DH_table[2][2]*sin(DH_table[2][0])],
                     [0, sin(DH_table[2][1]), cos(DH_table[2][1]),DH_table[2][3]],
                     [0,0,0,1]])
    H3_4 = np.array([[cos(DH_table[3][0]), -sin(DH_table[3][0])*cos(DH_table[3][1]),sin(DH_table[3][0])*sin(DH_table[3][1]),DH_table[3][2]*cos(DH_table[3][0])],
                     [sin(DH_table[3][0]), cos(DH_table[3][0])*cos(DH_table[3][1]),-cos(DH_table[3][0])*sin(DH_table[3][1]),DH_table[3][2]*sin(DH_table[3][0])],
                     [0, sin(DH_table[3][1]), cos(DH_table[3][1]),DH_table[3][3]],
                     [0,0,0,1]])
    H4_5 = np.array([[cos(DH_table[4][0]), -sin(DH_table[4][0])*cos(DH_table[4][1]),sin(DH_table[4][0])*sin(DH_table[4][1]),DH_table[4][2]*cos(DH_table[4][0])],
                     [sin(DH_table[4][0]), cos(DH_table[4][0])*cos(DH_table[4][1]),-cos(DH_table[4][0])*sin(DH_table[4][1]),DH_table[4][2]*sin(DH_table[4][0])],
                     [0, sin(DH_table[4][1]), cos(DH_table[4][1]),DH_table[4][3]],
                     [0,0,0,1]])
    H5_6 = np.array([[cos(DH_table[5][0]), -sin(DH_table[5][0])*cos(DH_table[5][1]),sin(DH_table[5][0])*sin(DH_table[5][1]),DH_table[5][2]*cos(DH_table[5][0])],
                     [sin(DH_table[5][0]), cos(DH_table[5][0])*cos(DH_table[5][1]),-cos(DH_table[5][0])*sin(DH_table[5][1]),DH_table[5][2]*sin(DH_table[5][0])],
                     [0, sin(DH_table[5][1]), cos(DH_table[5][1]),DH_table[5][3]],
                     [0,0,0,1]])
    
    H0_6 = np.dot(np.dot(np.dot(np.dot(np.dot(H0_1, H1_2), H2_3), H3_4), H4_5), H5_6)
    
    x = np.round(H0_6[0][3],3)
    y = np.round(H0_6[1][3],3)
    z = np.round(H0_6[2][3],3)
    
    return x, y, z

x,y,z= forward_kinematics(DH_table)
print(x,y,z)
