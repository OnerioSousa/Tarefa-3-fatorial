#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fatorial.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():

	n=0; cont=1; entrada=0;
	
	n = int(input()) #primeira entrada
	
	while n >= 0:

		fatorial = 1 #inicializa o valor fatorial
		num_recebido = n #armazena temporario

		while cont <= n: 	
		
			fatorial = fatorial*n
			n = n-1
			
		print('Fatorial(',num_recebido,') = ',fatorial)

		n = int(input()) #nova entrada

	return 0

if __name__ == '__main__':
	main()
