# tasks = []
# recuperation_tasks = []
#
#
# def print_tasks(tasks_list: list) -> None:
#     print("\nTAREFAS:")
#     [print(task) for task in tasks_list]
#     print("\n")
#
# def add_task(tasks_list: list, item: str) -> list:
#     tasks_list.append(item)
#     return tasks_list
#
# def operation_lists(original_list: list, recovery_list: list) -> list:
#     return original_list.append(recovery_list.pop())
#
#
# while True:
#
#     comands = ("listar", "desfazer", "refazer")
#
#     print("Comandos: listar, desfazer, refazer")
#
#     option = input("Digite uma tarefa ou comando: ").lower()
#
#     try:
#
#         if option not in comands:
#             add_task(tasks, option)
#
#         # if option == comands[0]:
#         #     print_tasks(tasks)
#
#         if option == comands[1]:
#             operation_lists(recuperation_tasks, tasks)
#
#         if option == comands[2]:
#             operation_lists(tasks, recuperation_tasks)
#
#     except IndexError:
#         print("\nNada há o que" + (f"{comands[1]}" if option == comands[1] else f"{comands[2]}"))
#
#     print_tasks(tasks)



# CODIGO DO PROFESSOR

import json


def listar(tarefas):
    print()
    if not tarefas:
        print("Nenhuma tarefa para listar")
        return

    print("Tarefas:")
    for tarefa in tarefas:
        print(f"\t{tarefa}")


def desfazer(tarefas, tarefa_refazer):
    print()
    if not tarefas:
        print("Nenhuma tarefa para desfazer")
        return

    tarefa = tarefas.pop()
    print(f"Tarefa {tarefa=} removida na lista de tarefas")
    tarefa_refazer.append(tarefa)
    listar(tarefas)


def refazer(tarefas, tarefa_refazer):
    print()
    if not tarefa_refazer:
        print("Nenhuma tarefa para refazer")
        return

    tarefa = tarefa_refazer.pop()
    print(f"Tarefa {tarefa=} adicionada na lista de tarefas")
    tarefas.append(tarefa)
    listar(tarefas)

def add(tarefa, tarefas):
    print()
    if not tarefa.strip():
        print("Voce nao digitou nenhuma tarefa")
        return

    tarefas.append(tarefa)

    listar(tarefas)


def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, "r", encoding="utf8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print("Arquivo não existe")
        salvar(tarefas, caminho)
    return dados


def salvar(tarefas, caminho):
    dados = tarefas
    with open(caminho, "w", encoding="utf8") as f:
        dados = json.dump(tarefas, f, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = "tarefas.json"
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []


while True:
    print("Comandos: listar, desfazer e refazer")
    tarefa = input("Digite uma tarefa ou comando: ")

    comandos = {
        "listar": lambda: listar(tarefas),
        "desfazer": lambda: desfazer(tarefas, tarefas_refazer),
        "refazer": lambda: refazer(tarefas, tarefas_refazer),
        "adicionar": lambda: add(tarefa, tarefas),
    }
    # a função é executada a partir da chave (tarefa) inserida no método get
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos["adicionar"]
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
    # if tarefa == "listar":
    #     listar(tarefas)
    # elif tarefa == "desfazer":
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    # elif tarefa == "refazer":
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    # else:
    #     add(tarefa, tarefas)
    #     listar(tarefas)
    # print("\n")



























































