from Modules import my_format as mf
from Modules_Ex import Ex115 as Ex
from termcolor2 import c

print(c(mf.tit('Sistema de Registo de Utilizadores')).white)
while True:
    opc = Ex.menu()
    print('\n')
    if opc == '1':
        Ex.registar_user()
        print('\n\n')
    elif opc == '2':
        Ex.ver_users()
        print('\n\n')
    elif opc == '3':
        Ex.delete_user()
        print('\n\n')
    elif opc == '4':
        break
