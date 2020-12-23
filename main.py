from collections import namedtuple

ponto = namedtuple('ponto','x y') #representação dos pontos 

def inv_mod_p(x,p):
    
    if x % p == 0:
        raise ZeroDivisionError("inverso impossivel")
    return pow(x, p-2, p)

def pertence_a_curva(P,Q,a,b,p): 

	aux1 = aux2 = False
	if P == None:
		aux1=True
		print("P pertence a curva? ",aux1)
	else:
		aux1 = (bool((P[1]**2 - (P[0]**3 + a*P[0] + b)) % p == 0 and 0 <= P[1] < p and 0 <= P[1] < p))
		print("P pertence a curva? ",aux1)
	if Q == None:
		aux2 =True
		print("Q pertence a curva? ",aux2)
	else:
		aux2 = (bool((Q[1]**2 - (Q[0]**3 + a*Q[0] + b)) % p == 0 and 0 <= Q[1] < p and 0 <= Q[1] < p))
		print("Q pertence a curva? ",aux2)
	print("‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒")
	return aux1, aux2
	

def soma_de_pontos(P,Q,a,b,p):

	#verifica se os pontos pertencem a curva
	aux1, aux2 = pertence_a_curva(P,Q,a,b,p)
	if aux1==False or aux2==False:
		if aux1 == False: 
			return print("O ponto P({},{}) nao pertence a curva.".format(P[0],P[1]))
		else: 
			return print("O ponto Q({},{}) nao pertence a curva.".format(Q[0],Q[1]))

	# primeiro trata os casos especiais
	if (P == None and Q == None):
		return print("P+Q = ∞")
	if (P == None):
		return print ("P+Q = ({},{})".format(Q[0],Q[1]), "O proprio ponto Q")
	if (Q == None):
		return print ("P+Q = ({},{})".format(P[0],P[1]), "O proprio ponto P")
	if (P[0] == Q[0]) and (P[1] != Q[1] or P[1] == 0): 
		return print("P+Q = ∞")
	if ((P[0] == Q[0]) and P[1] == (-Q[1])%p):
		return print("P+Q = ∞")

	if P[0] != Q[0]:
		m = (Q[1]-P[1])*inv_mod_p(Q[0]-P[0],p)
		print("Coef. angular m =",m)
		x3=(m**2-Q[0]-P[0]) % p
		y3=((m*(Q[0]-x3)-Q[1])) % p
		R = ponto(x3,y3)
		return print ("P+Q = ({},{})".format(R[0],R[1]))

	if (P[0] == Q[0]) and (P[1] == Q[1]):
		m = (3*(P[0]**2)+a)*inv_mod_p(2 * P[1],p)
		print("Coef. angular m =",m)
		x3 = ((m*m)-P[0]-Q[0])%p
		y3 =(-P[1]-(m*(x3-P[0])))%p
		R = ponto(x3,y3)
		return print ("P+Q = ({},{})".format(R[0],R[1]))
		

if __name__ == '__main__':

	print("\n	  Atividade 4")
	A,B= input("\n- Digite os coeficientes A e B: ").split()
	p = input("- Digite o modulo: ")
	op = input("- P eh o ponto no infinito? (s/n): ")
	if op == 's':
		P = None
	else: 
		Px,Py =input("- Digite as coordenadas do ponto P: ").split()
		P = ponto(int(Px),int(Py))
	op2 = input("- Q eh o ponto no infinito? (s/n): ")
	if op2 == 's':
		Q = None
	else:
		Qx,Qy =input("- Digite as coordenadas do ponto Q: ").split()
		Q = ponto(int(Qx),int(Qy))
	print("‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒")
	print("Curva: y^2 = x^3 + {}x + {}".format(A,B))
	print("Primo p = ",p)
	auxP = P
	auxQ = Q
	if P == None:
		auxP = '∞'
	if Q == None:
		auxQ = '∞'
	print("P = {}\nQ = {}".format(auxP,auxQ))
	print("‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒")
	soma_de_pontos(P,Q,int(A),int(B),int(p)) 

	

