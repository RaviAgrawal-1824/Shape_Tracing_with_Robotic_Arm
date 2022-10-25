from sympy import *
from sympy import cos, sin

a,theta,alpha,d = symbols('a theta alpha d')
x0,y0,z0,theta1,theta2,theta3,l1,l2,l3= symbols('x0,y0,z0,theta1,theta2,theta3,l1,l2,l3')

# T=Matrix([[cos(theta), -sin(theta), 0, a], 
#             [sin(theta)*cos(alpha), cos(alpha)*cos(theta), -sin(alpha), -d*sin(alpha)], 
#             [sin(alpha)*sin(theta), sin(alpha)*cos(theta), cos(alpha), d*cos(alpha)], 
#             [0, 0, 0, 1]])
T=Matrix([[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), a*cos(theta)], 
            [sin(theta), cos(alpha)*cos(theta), -sin(alpha)*cos(theta), a*sin(theta)], 
            [0, sin(alpha), cos(alpha), d], 
            [0, 0, 0, 1]])

# for i in range(1,n+1):
#     # inp_d.append(int(input("Enter the d (link offset) for link "+ str(i) +":  ")))
#     g=input("Enter the theta (joint angle) for link "+str(i)+" in degrees:  ")
#     inp_theta.append(g)

def CalcTransformation():
    TransMatrix=eye(4)
    for i in range(n):
        Mat=T.subs([(a,inp_a[i]), (alpha, inp_alpha[i]), (d, inp_d[i]), (theta, inp_theta[i])])
        HomoMat.append(Mat)
        # pretty_print(Mat)
        # TransMatrix = Mat*TransMatrix
        TransMatrix = TransMatrix*Mat
        # TransMatrix = TransMatrix*(Mat.inv(method="LU"))
    return TransMatrix
    
def GenerateEquations(pos_x=0,pos_y=0,pos_z=0):
    e=Matrix(4,1,["pos_x","pos_y","pos_z","1"])
    f=TransformationMat[:]
    # print(e)
    # print(f)
    x1=''
    x=[]
    for i in range(12):
        x1=x1+str(f[i])+" * "+str(e[int(i%4)])+" + "
        if(i%4==3):
            x.append(x1[0:-2])
            x1=''
    return x

if __name__ == "__main__":
    
    inp_theta=[theta1,theta2,theta3]
    inp_a=[l1,l2,l3]
    inp_alpha=[0,0,0]
    inp_d=[0,0,0]
    HomoMat=[]

    n=int(input("Enter the number of links:\n"))
    print("\n Generalised Transformation matrix is \n")
    pretty_print(T)
    # pretty_print(HomoMat[0])
    # pretty_print(HomoMat[1])
    # pretty_print(HomoMat[2])
    TransformationMat=CalcTransformation()
    # pretty_print(TransformationMat)
    TransformationMat=trigsimp(TransformationMat)
    print("\n\n Transformation matrix for frame 3 with respect to frame 0 is \n\n")
    pretty_print(TransformationMat)
    print("\n")
    j=GenerateEquations()
    print("\n Generalised Equations are\n")
    print("x_equation = ",j[0])
    print("y_equation = ",j[1])
    print("z_equation = ",j[2])
    # pretty_print(j[0])
    # print("\n")