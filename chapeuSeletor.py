#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import time

import sys

#definindo cores
negrito = '\033[1m'

amarelo = '\033[33m'
cinza = '\033[90m'
preto = '\033[30m'
branco = '\033[37m'

fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'

resetColor = '\033[0;0m'

corGrifinoria = negrito + amarelo + fundo_vermelho
corSonserina = negrito + cinza + fundo_verde
corLufalufa = negrito + preto + fundo_amarelo
corCorvinal = negrito + amarelo + fundo_azul

corBrasao = negrito + branco


def show(brasao, nomesCasas, chapeuSeletor, maxPorCasa):
	#printando brasao
	for l in brasao:
		print(f"{corBrasao}{l:^190}{resetColor}")
	
	#printando nomes das casas
	for i in range(len(nomesCasas["Grifinoria"])):
		print(f"{corGrifinoria}{nomesCasas['Grifinoria'][i]}{resetColor}    {corSonserina}{nomesCasas['Sonserina'][i]}{resetColor}     {corLufalufa}{nomesCasas['Lufa-lufa'][i]}{resetColor}     {corCorvinal}{nomesCasas['Corvinal'][i]}{resetColor}")
	
	#printando alunos distribuídos
	for i in range(maxPorCasa):
		if i < len(chapeuSeletor['Grifinoria']):
			print(f" {chapeuSeletor['Grifinoria'][i]:<50}",end="")
		else:
			print(" "*51,end="")
			
		if i < len(chapeuSeletor['Sonserina']):
			print(f"{chapeuSeletor['Sonserina'][i]:<53}",end="")
		else:
			print(" "*53,end="")
		
		try:
			if i < len(chapeuSeletor['Lufa-lufa']):
				print(f"{chapeuSeletor['Lufa-lufa'][i]:<52}",end="")
			else:
				print(" "*52,end="")
			
			if i < len(chapeuSeletor['Corvinal']):
				print(f"{chapeuSeletor['Corvinal'][i]:<30}")
			else:
				print(" ")
				
		except KeyError:
			print(" ")


def sortChapeuSeletor(chapeuSeletor, casas, alunos, ksize, sobras):
	alunosTmp = alunos.copy()
	
	random.shuffle(alunosTmp)
	
	for i in range(len(casas)):
		sample = random.sample(alunosTmp,ksize)
		alunosTmp = [a for a in alunosTmp if a not in sample]
		chapeuSeletor[casas[i]] = sample
	
	random.shuffle(casas)
	
	for s in range(sobras):
		chapeuSeletor[casas[s]].append(alunosTmp[s])

def usage():
	print("Usage:\n./chapeuSeletor.py <lista_alunos.txt> <num_casas [2..4]>")
	sys.exit(0)

def main():
	
	if len(sys.argv) < 3:
		usage()
	
	random.seed()
	
	#lendo brasao
	with open("casas.txt") as f:
		brasao = f.read().split()
	
	#lendo nomes das casas
	nomesCasas = {}
	with open("grifinoria.txt") as f:
		nomesCasas["Grifinoria"] = f.read().split("\n")[:-1]
	with open("sonserina.txt") as f:
		nomesCasas["Sonserina"] = f.read().split("\n")[:-1]
	with open("lufalufa.txt") as f:
		nomesCasas["Lufa-lufa"] = f.read().split("\n")[:-1]
	with open("corvinal.txt") as f:
		nomesCasas["Corvinal"] = f.read().split("\n")[:-1]
	
	#lendo lista de alunos
	try:
		with open(sys.argv[1]) as f:
			alunos = f.read().split("\n")[:-1]
	except FileNotFoundError:
		print("Error: Lista de alunos não encontrada.")
		sys.exit(1)
	
	try:
		ncasas = int(sys.argv[2])
		if ncasas not in range(2,5):
			print("Error: Número de cassas precisa estar entre 2 e 4.")
			sys.exit(1)
	except ValueError:
		print("Error: Número de cassas precisa ser um inteiro.")
		sys.exit(1)
	
	ksize = len(alunos) // ncasas
	sobras = len(alunos) % ncasas
	maxPorCasa = ksize + (1 if sobras else 0)
	
	casas = ["Grifinoria","Sonserina","Lufa-lufa","Corvinal"]
	casas = casas[:ncasas]
	
	#sorteio pelo chapeu seletor		
	try:
		while True:
			chapeuSeletor = {}
			sortChapeuSeletor(chapeuSeletor, casas, alunos, ksize, sobras)
			show(brasao,nomesCasas,chapeuSeletor,maxPorCasa)
			time.sleep(0.1)
			
	except KeyboardInterrupt:
		pass
	
	return 0

if __name__ == '__main__':
	main()
