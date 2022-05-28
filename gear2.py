
from math import sqrt, atan, cos, ceil

from numpy import cbrt

def closest(l, zv):
	min = 10000000000
	for i in range(len(l)):
		m = abs(l[i] - zv)
		if m < min:
			min = m
			pos = i

	return l[pos]	

pi = 3.14

power = float(input("Power in watts :"))

# gear_ratio = float(input("Gear ratio :"))

# input_speed = float(input("Input Speed :"))

print("\n\nMaterial\tBending stress\tCompressive stress")
ch = int(input("1. 15Ni2Cr1Mo15\t\t320\t\t950\n2. C45\t\t\t140\t\t500\n3. 40Ni2Cr1Mo28\t\t400\t\t1100\nEnter choice : "))

ch1 = int(input("Please specify the datas you would like to enter :\n1. N, i\n2. n, i\n3. N, n\nEnter choice : "))

if ch1 == 1:
	input_speed = float(input("Input Speed :"))
	gear_ratio = float(input("Gear ratio :"))

elif ch1 == 2:
	out_speed = float(input("Output Speed : "))
	gear_ratio = float(input("Gear ratio :"))
	input_speed = gear_ratio * out_speed

elif ch1 == 3:
	input_speed = float(input("Input Speed :"))
	out_speed = float(input("Output Speed : "))
	gear_ratio = input_speed/out_speed



if ch == 1:
	comp_stress = 950		
	b_stress = 320
	material = "15Ni2Cr1Mo15"

elif ch == 2:
	comp_stress = 500		
	b_stress = 140	
	material = "C45"

elif ch == 3:
	comp_stress = 1100		
	b_stress = 400	
	material = "40Ni2Cr1Mo28"

mt = round(((power*60) * 1000)/(2*pi*input_speed), 3)

# print(mt)

bmt = int(mt * 1.5) 

# print(bmt)

E = 2.15 * (10**5)

if (gear_ratio>=1 and gear_ratio<=3):
	phiy = 3

elif (gear_ratio == 4 or gear_ratio == 5):
	phiy = 	4

elif (gear_ratio==6):
	phiy = 5

a = round(sqrt(pow(gear_ratio,2) + 1), 3)

#print(phiy)

# print("Test")
# print(a)

b = (0.72/((phiy-0.5)*comp_stress))

b = pow(b,2)

# print(b)

c = round((E*bmt)/gear_ratio, 3)

# print(c)

d = round((b * c), 4)

# print(d)

e = round(cbrt(d), 3)

# print(e)

f = round(a * e, 3)

# print(f)

# print(phiy)

r1 = round(f * phiy, 3)

# print(r1)

z1 = 20

phi = float(input("Shaft angle :"))

d2 = round(atan(gear_ratio), 3)

# print(d2)

phi = (phi*pi)/180

d1 = round(phi - d2, 3)

# print("d1 :",d1)

zv = z1/round(cos(d1), 3)

zv = round(zv, 2)

# print("Zv :",zv)

l = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 35, 40, 45, 50, 60, 80, 100, 150, 300]

cl = closest(l, zv)

cl_value = [0.308, 0.330, 0.355, 0.377, 0.389, 0.402, 0.414, 0.427, 0.434, 0.440, 0.452, 0.465, 0.471, 0.477, 0.490, 0.499, 0.505, 0.515, 0.521]

ind = l.index(cl)

yv = cl_value[ind]

# print("yv :",yv)

phim = 10

x = yv*b_stress*phim*z1

m_av = round(1.26 * round(pow((bmt/x), 1/3), 3), 2)

# print("mav :",m_av)

m_trans = round(m_av * (phiy/(phiy-0.5)), 2)

# print("mtrans :",m_trans)

l2 = [1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20]

cl_value2 = closest(l2, m_trans)
#m_trans = cl_value2
# print("Closest val :",cl_value2)

z1 = r1/(0.5 * m_trans * sqrt((gear_ratio**2)+1))

std_z1 = ceil(z1)

print("Z1 :",std_z1)

z2 = gear_ratio * std_z1

# print("Z2 :",z2)

cl_value3 = closest(l,std_z1)

# print("Cl value :",cl_value3)
# print("Mt:",mt)

r = round(0.5 * m_trans * cl_value3 * sqrt(pow(gear_ratio,2) + 1), 3)

# print("R :",r)

f_width = round(r/phiy, 3)

# print("Fw :",f_width)

pi_dia = round(m_trans*z1, 3)

g_dia = round(m_trans * z2, 3)

pcdpi = pi_dia

pcdg = g_dia

# print("D1 :",d1)
# print("Angle :",cos(d1))

tcdpi = round(m_trans * (cl_value3+(2*cos(d1))), 3)

tcdg = round(m_trans * (z2+(2*cos(d2))), 3)

f_two = 0.5*f_width

f_three = r - f_two

first = (0.72/f_three)

#print("first term =", first)

second = (pow(gear_ratio,2)+1)

third = (pow(second,(3/2)))

#print("third term=",third)

fourth = gear_ratio * f_width

#print("fourth term =",fourth)

fifth = (third * E * bmt)

sixth = fifth/fourth

seventh = sqrt(sixth) 

ind_comp_stress = first * seventh

alpha = round(20 * (3.14/180), 2) 
#print(round(m_trans_n,3))
b1 = 1/round(cos(alpha), 3)
b1 = round(b1,2)
#print (b_1)

b2 = 0.5 * f_width
b2=round(b2,2)
#print(b_2)
b3 = r - b2
b3=round(b3,2)
#print(b_3)
b4 = pow(b3,2)
b4=round(b4,2)
#print(b_4)
b5 = b4 * f_width * m_trans * yv
b5=round(b5,2)
#print(b_5)
b6 = sqrt((gear_ratio**2)+1)

b6=round(b6,2)
#print(b_6)
b7 = b6 * r * bmt
b7=round(b7,2)
#print(b_7)
b8 = b7/b5
#print(b8)
ind_bending_stress = round(b8, 2) 

print("Input Power in watts =", power,"\n")
print("Speed ratio =", gear_ratio,"\n")
print("Input speed =", input_speed,"\n")
print("Material used =", material,"\n")
print("Minimum Cone Distance(mm) =", r1,"\n")
print("Actual Cone Distance(mm) =", r,"\n")
print("Torque transmitted by pinion(Nmm) =", mt)
print("Twisting moment(Nmm) :", bmt)
print("Average module(mm) =", m_av,"\n")
print("Form factor :", yv)
print("Virtual teeth =", zv)
print("No. of teeth assumed on pinion =", 20)
print("Actual no. of teeth on pinion =", cl_value3,"\n")
print("Transverse module(mm) =", cl_value2,"\n") 
print("No. of teeth on gear =", z2,"\n")
print("Face width(mm) =", round(f_width,3),"\n")
print("Diameter of pinion(mm) =", round(pi_dia,3),"\n")
print("Diameter of gear(mm) =", round(g_dia,3),"\n")
print("Pitch circle dia of pinion(mm) =", round(pcdpi,3),"\n")
print("Pitch circle dia of gear(mm) =", round(pcdg,3),"\n")
print("Tip circle dia of pinion(mm) =", round(tcdpi,3),"\n")
print("Tip circle dia of gear(mm) =", round(tcdg,3),"\n")
print("Induced bending stress(N/mm2)=", round(b8,3),"\n")
print("Induced compressive stress(N/mm2) =", round(ind_comp_stress,3))


