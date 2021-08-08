import numpy as np

T1=90
T2=0
T3=0
A1=1
A2=2
A3=1
R1=0
R2=0
R3=0
D1=0
D2=0
D3=1
T1=(T1/180)*np.pi
T2=(T2/180)*np.pi
T3=(T3/180)*np.pi
A1=(A1/180)*np.pi
A2=(A2/180)*np.pi
A3=(A3/180)*np.pi

pt=[[T1,A1,R1,D1],[T2,A2,R2,D2],[T3,A3,R3,D3]]
i=0
H0_1 = [[np.cos(pt[i][0]),-np.sin(pt[i][0])*np.cos(pt[i][1]),np.sin(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.cos(pt[i][0])],
        [np.sin(pt[i][0]),np.cos(pt[i][0])*np.cos(pt[i][1]),-np.cos(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.sin(pt[i][0])],
        [0,np.sin(pt[i][1]),np.cos(pt[i][1]),pt[i][3]],
        [0,0,0,1]]
i=1
H1_2 = [[np.cos(pt[i][0]),-np.sin(pt[i][0])*np.cos(pt[i][1]),np.sin(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.cos(pt[i][0])],
        [np.sin(pt[i][0]),np.cos(pt[i][0])*np.cos(pt[i][1]),-np.cos(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.sin(pt[i][0])],
        [0,np.sin(pt[i][1]),np.cos(pt[i][1]),pt[i][3]],
        [0,0,0,1]]
i=2
H2_3 = [[np.cos(pt[i][0]),-np.sin(pt[i][0])*np.cos(pt[i][1]),np.sin(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.cos(pt[i][0])],
        [np.sin(pt[i][0]),np.cos(pt[i][0])*np.cos(pt[i][1]),-np.cos(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.sin(pt[i][0])],
        [0,np.sin(pt[i][1]),np.cos(pt[i][1]),pt[i][3]],
        [0,0,0,1]]


#H0_3 = np.dot(H0_1,H1_2,H2_3)
print(np.matrix(H0_1))
print(np.matrix(H1_2))
print(np.matrix(H2_3))
H0_3 = np.dot(np.matrix(H0_1),np.matrix(H1_2),np.matrix(H2_3))
print(H0_3)

