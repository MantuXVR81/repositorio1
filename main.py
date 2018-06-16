import math
S=["Sexagesimal","sexagesimal","S"]
C=["Centesimal","centesimal","C"]
R=["Radianes","radianes","R"]
def conversor7(n,m):
  n=input("Ingrese valor numérico: ")
  m=input("Ingrese medida del ángulo: ")
  if m in S:
    k=10*n/9
    s= print(k,"C")
    return s
def conversor8(n,m):
  n=input("Ingrese valor numérico: ")
  m=input("Ingrese medida del ángulo: ")
  if m in C:
    k=9*n/10
    s= print(k,"S")
    return s
def conversor9(n,m):
  n=input("Ingrese valor numérico: ")
  m=input("Ingrese medida del ángulo: ")
  if m in R:
    k=180*n/math.pi
    s= print(k,"S")
    return s
def conversor10(n,m):
  n=input("Ingrese valor numérico: ")
  m=input("Ingrese medida del ángulo: ")
  if m in R:
    k=200*n/math.pi
    s= print(k,"C")
    return s
def conversor11(n,m):
  n=input("Ingrese valor numérico: ")
  m=input("Ingrese medida del ángulo: ")
  if m in S:
    k=math.pi*n/180
    s= print(k,"R")
    return s
def conversor7(n,m):
  n=input("Ingrese valor numérico: ")
  m=input("Ingrese medida del ángulo: ")
  if m in C:
    k=math.pi*n/200
    s= print(k,"R")
    return s
