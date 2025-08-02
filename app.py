import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import sqlite3

bancoDados = sqlite3.connect("db_tarefas.db")  


tarefas = []

#______________________________________cantinho das function_____________________________________________

def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa.strip() != "":
        tarefas.append({"texto":tarefa,"status":False})
        atualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa válida.")

def remover_tarefa():
    selecionado = lista.curselection()
    if selecionado:
        index = selecionado[0]
        tarefas.pop(index)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

def marcar_tarefa():
    selecionado = lista.curselection() #retorna tupla
    if selecionado: 
        i = selecionado[0]
        tarefas[i]['status'] = True
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Tarefa realizada")
        salvar_tarefas()

def atualizar_lista():
    lista.delete(0, tk.END) 

    for tarefa in tarefas:
        if tarefa['status']:
            lista.insert(tk.END, ' ✅'+tarefa['texto'])
            
            lista.itemconfig(tk.END, {'fg':'green'})
        else:
            lista.insert(tk.END,'     ' + tarefa['texto'])

def salvar_tarefas():
    json_tarefas = {
            "tarefa_salva":tarefas,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")

        }
    print(json_tarefas)
#__________________________________________________________________________________________________________________


#
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("400x500")
janela.configure(bg="#e8e8ee")
titulo = tk.Label(janela, text=" Lista de Tarefas", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)
entrada = tk.Entry(janela, width=30, font=("Arial", 12))
entrada.pack(pady=5)



botao_adicionar = tk.Button(janela, text="Adicionar", width=15, command=adicionar_tarefa)
botao_adicionar.pack(pady=5)



#list das tarefas
lista = tk.Listbox(janela, width=40, height=10, font=("Arial", 12))
lista.pack(pady=10)

container_botao = tk.Frame(janela)
container_botao.pack(pady=10)


botao_marcar = tk.Button(container_botao,text="Marcar como feita",width=20, command=marcar_tarefa)
botao_marcar.configure(bg="#90ffb1")
botao_marcar.pack(padx=5,pady=5,side='left')
botao_remover = tk.Button(container_botao, text="Remover", width=15, command=remover_tarefa)
botao_remover.configure(bg="#ff9b9b")
botao_remover.pack(pady=5,padx=5,side='right')


janela.mainloop()
