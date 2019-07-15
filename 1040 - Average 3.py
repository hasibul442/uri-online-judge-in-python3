N1,N2,N3,N4 = input().split(" ")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

avg = float(((N1*2)+(N2*3)+(N3*4)+(N4*1))/(2+3+4+1))

print("Media: %.1f"%avg)

if(avg>=7.0):
    print("Aluno aprovado.")
elif avg<5.0:
    print("Aluno reprovado.")
elif avg>=5.0 and avg<7.0:
    print("Aluno em exame.")
    N5 = float(input())
    print("Nota do exame: %.1f"%N5)
    avg1 = (avg+N5)/2

    if(avg1>= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print("Media final: %.1f"%avg1)
