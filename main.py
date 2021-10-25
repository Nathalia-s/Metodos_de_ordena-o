import random
import time
vetor = []
qtd = 0
op = 0

def menu(): 
  print("\n*** Escolha o Metodo de ordenação *****")
  print("\n 3. Buble Sort")
  print("\n 4. Selection Sort")
  #print("\n 5. Insertion Sort")
  #print("\n 6. Quick Sort ")
  print("\n 7. sair\n")
  op = int(input())

  return op

def SelectionSort(limite):
    global vetor
    auxiliar = 0
    lista = list(vetor)
    for i in range(0,limite):
        j=i+1
        for j in range(0,limite):
            if lista[j] > lista[i]:
                auxiliar = lista[j]
                lista[j] = lista[i]
                lista[i] = auxiliar
        j = j+1
    i=i+1
    return lista  

def BubleSort(limite): 
   global vetor
   auxiliar = 0
   lista = list(vetor)
   for i in range(0,limite-1):
      for j in range(0,limite-1-i):
          if lista[j] > lista[j+1]: 
            auxiliar = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = auxiliar
      j = j+1    
   i = i+1
   return lista

def CriarAmostra(tamanho): 
    global vetor
    for i in range(tamanho):
        a = random.randint(0,1000)
        vetor.append(a)   
    i = i+1
    vetor = tuple(vetor)
    return vetor     

while (op != 1 and op != 2):
  print("****** Menu ******")
  print("\n 1. Informar os dados")
  print("\n 2. Gerar os dados \n")
  op = int(input())

print("Quantos valores quer ordenar: ")
qtd = int(input())

#o código que solicita os dados da amostra
if op == 1:
    i = 0
    while i < qtd :
        print("Informe o {0}. valor: ".format(i+1))
        vetor.append(int(input()))
        i = i+1
        
# cria a amostra	
elif op == 2 :
  CriarAmostra(qtd)

# implementar o tempo de execução
while op !=7:
  op = menu()

  #ordenação BubleSort
  if op == 3 :
    print("\n\nOrdenando os dados com Buble Sort... \n")
    
    inicio = time.time()
    print(BubleSort(qtd))
    fim = time.time()
    print("Tempo de execução: %f " %(fim - inicio))

  #ordenação selection sort
  elif op == 4 :
    print("\n\nOrdenando os dados com Selection Sort... \n")

    inicio = time.time()
    print(SelectionSort(qtd))
    fim = time.time()
    print("Tempo de execução: %f "%(fim - inicio))