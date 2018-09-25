'''
r = float(raw_input(">>"))
h = float(raw_input(">>"))
area = r*r*3.14
volume = area*h
print(volume)
'''
'''
yc = float(raw_input(">>"))
mi = yc*0.305
print(mi)
'''
'''
sl=float(raw_input(">>"))
cswd=float(raw_input(">>"))
zzwd=float(raw_input(">>"))
Q=sl*(zzwd-cswd)*4184
print(Q)
'''
'''
ce=float(raw_input(">>"))
nly=float(raw_input(">>"))
lixi=ce*(nly/1200)
print(lixi)
'''
'''
v0=eval(raw_input(">>"))
v1=eval(raw_input(">>"))
t=eval(raw_input(">>"))
a=(v1-v0)/t
print(a)
'''
'''
csq=eval(raw_input(">>"))
yll=1.00417
lbdl1=csq*(1+0.00417)
lbdl2=(lbdl1+csq)*yll
lbdl3=(lbdl2+csq)*yll
lbdl4=(lbdl3+csq)*yll
lbdl5=(lbdl4+csq)*yll
lbdl6=(lbdl5+csq)*yll
print(lbdl6)
'''

x=eval(raw_input("enter a number between 0 and 1000:"))
a=x/100%10+x/10%10+x%10
print(a)

