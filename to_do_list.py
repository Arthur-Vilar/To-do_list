from time import sleep
print('\033[34mLISTA DE TAREFAS\033[m')
print('-'*17)
user= str(input('Digite seu \033[34mnome\033[m: ')).strip().title()
print('-'*17)
print(f'Seja bem vindo(a), \033[32m{user}\033[m! Nosso aplicativo é uma \033[34mlista de tarefas\033[m. Fique a vontade para utilizar nossos serviços, nós o agradecemos. \033[04;32mBom uso\033[m!')
flag= 0
tarefas= []
while flag!=3:
    print('''[1] - \033[33mAdicionar tarefa\033[m
[2] - \033[01;32mRiscar tarefa\033[m
[3] - \033[04;31mSair\033[m''')
    choice= int(input('Digite o número referente a \033[36mação\033[m desejada: '))
    if choice == 1:
        tarefa=str(input('Digite o nome da tarefa que quer \033[33madicionar\033[m a lista: ')).strip().capitalize()
        tarefas.append(tarefa)
        print('\n\033[34mLista de tarefas\033[m:')
        for c,i in enumerate(tarefas):
            print(f'{c+1} - {i}')
    if choice == 2:
        if not tarefas:
            print('\033[04;31mNenhuma tarefa encontrada\033[m. Você tem que \033[01;33madicionar tarefas\033[m primeiro para poder conclui-lás.')
        else: 
            print('')
            for c,i in enumerate(tarefas):
                print(f'{c+1} - {i}')
            print('-'*17)
            riscar= int(input('Digite o \033[04;31mnúmero\033[m da tarefa que deseja \033[04;32mriscar\033[m: '))
            del tarefas[riscar-1]
            print('-'*17)
            for c,i in enumerate(tarefas):
                print(f'{c+1} - {i}')
    sleep(1.5)
    print('-'*17)        
    if choice==3:
        print('\033[01;31mEncerrando programa...\033[m')
        break
sleep(1)
print('\033[32mObrigado por usar nossos serviços\033[m.')
print(f'Sua lista final foi:')
for c,i in enumerate(tarefas):
    print(f'{c+1      } - {i}')
