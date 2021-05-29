#!/usr/bin/env python 
import subprocess

#Atenção!!
#este codigo servirá apenas para Linux, Windows ou mac não se aplica aqui !

def mudar_mac(): 
    print("Mudando Mac Address")
    interface =  input("Digite a interface: ")
    novo_mac = input("Digite o novo mac: ")

    #processo de camuflagem de mac addres.... 
    # há duas formas de fazer a mudaça; uma com lista e a outra com o metodo shell.

    subprocess.call(["ifconfig", interface,"down"]) 
    subprocess.call(["ifconfig", interface,"hw", "ether", novo_mac])
    subprocess.call(["ifconfig", interface,"up"])

# se eu tentasse ejetar meu codigo com ls
# ele nao rodará o comando como comando do
# SO(no caso linux), diferentemete do método Shell=true
# que seria facilmente ejetado, e consequentemente, não seria seguro.

mudar_mac()

def mudar_ip(): 
    print("Mudando Ip")
    interface =  input("Digite a interface: ")
    novo_ip = input("Digite o novo ip: ")

    #processo de camuflagem de mac addres.... 
    # há duas formas de fazer a mudaça; uma com lista e a outra com o metodo shell.

    subprocess.call(["ipconfig", interface,"down"]) 
    subprocess.call(["ipconfig", interface, novo_ip, "netmask", "255.255.255.0"])
    subprocess.call(["ipconfig", interface,"up"])

# A mesma lógica do código anterior, no entanto
# para camuflagem de IP.

mudar_ip()



