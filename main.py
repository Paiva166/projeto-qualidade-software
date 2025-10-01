"""
SISTEMA DE GERENCIAMENTO DE TAREFAS - v2.0
Disciplina: Qualidade de Software
Professor: MSc. Sybelle Nogueira

CARACTERÍSTICAS DE QUALIDADE IMPLEMENTADAS (ISO/IEC 25010):
1. FUNCIONALIDADE: Sistema completo com adicionar, listar, concluir, excluir
2. CONFIABILIDADE: Tratamento de erros e validações robustas  
3. USABILIDADE: Interface intuitiva com feedback visual
4. MANUTENIBILIDADE: Código modular e bem documentado

CONTROLE DE VERSÃO:
- Repositório: https://github.com/Paiva166/projeto-qualidade-software
- Fluxo: Feature branches + Pull Requests
- Commits: Significativos e descritivos
"""

import json
import os

class GerenciadorTarefas:
    def __init__(self):
        self.arquivo = "tarefas.json"
        self.tarefas = self.carregar_tarefas()
    
    def carregar_tarefas(self):
        """Carrega tarefas do arquivo - CONFIABILIDADE"""
        try:
            if os.path.exists(self.arquivo):
                with open(self.arquivo, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Erro ao carregar: {e}")
            return []
    
    def salvar_tarefas(self):
        """Salva tarefas no arquivo - CONFIABILIDADE"""
        try:
            with open(self.arquivo, 'w') as f:
                json.dump(self.tarefas, f, indent=2)
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
    
    def adicionar_tarefa(self, descricao):
        """Adiciona nova tarefa - FUNCIONALIDADE"""
        if not descricao.strip():
            print("Erro: Descrição não pode ser vazia!")
            return False
        
        nova_tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao.strip(),
            "concluida": False
        }
        
        self.tarefas.append(nova_tarefa)
        if self.salvar_tarefas():
            print(f"Tarefa '{descricao}' adicionada com sucesso! (ID: {nova_tarefa['id']})")
            return True
        return False
    
    def listar_tarefas(self):
        """Lista todas as tarefas - USABILIDADE"""
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        
        concluidas = sum(1 for t in self.tarefas if t["concluida"])
        total = len(self.tarefas)
        
        print(f"\nLISTA DE TAREFAS ({concluidas}/{total} concluidas)")
        print("=" * 50)
        for tarefa in self.tarefas:
            status = "[X]" if tarefa["concluida"] else "[ ]"
            print(f"{tarefa['id']}. {status} {tarefa['descricao']}")
        print("=" * 50)
    
    def marcar_concluida(self, id_tarefa):
        """Marca tarefa como concluída - FUNCIONALIDADE"""
        try:
            id_tarefa = int(id_tarefa)
            for tarefa in self.tarefas:
                if tarefa["id"] == id_tarefa:
                    if not tarefa["concluida"]:
                        tarefa["concluida"] = True
                        self.salvar_tarefas()
                        print(f"Tarefa {id_tarefa} marcada como concluida!")
                        return True
                    else:
                        print(f"Tarefa {id_tarefa} ja estava concluida!")
                        return True
            print(f"Tarefa {id_tarefa} nao encontrada!")
            return False
        except ValueError:
            print("Erro: ID deve ser um numero!")
            return False

    def excluir_tarefa(self, id_tarefa):
        """Exclui uma tarefa - nova funcionalidade"""
        try:
            id_tarefa = int(id_tarefa)
            for i, tarefa in enumerate(self.tarefas):
                if tarefa["id"] == id_tarefa:
                    tarefa_excluida = self.tarefas.pop(i)
                    self.salvar_tarefas()
                    print(f"Tarefa '{tarefa_excluida['descricao']}' excluida com sucesso!")
                    return True
            print(f"Tarefa {id_tarefa} nao encontrada!")
            return False
        except ValueError:
            print("Erro: ID deve ser um numero!")
            return False

def main():
    """Função principal do sistema - CONFIABILIDADE"""
    try:
        sistema = GerenciadorTarefas()
        print("Sistema inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar sistema: {e}")
        return
    
    while True:
        print("\n" + "="*50)
        print("           SISTEMA DE TAREFAS v2.0")
        print("="*50)
        print("1. Adicionar tarefa")
        print("2. Listar tarefas") 
        print("3. Marcar tarefa como concluida")
        print("4. Excluir tarefa")
        print("5. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opcao (1-5): ").strip()
        
        if opcao == "1":
            descricao = input("Digite a descricao da tarefa: ")
            sistema.adicionar_tarefa(descricao)
        
        elif opcao == "2":
            sistema.listar_tarefas()
        
        elif opcao == "3":
            sistema.listar_tarefas()
            if sistema.tarefas:
                id_tarefa = input("Digite o ID da tarefa a concluir: ")
                sistema.marcar_concluida(id_tarefa)
        
        elif opcao == "4":
            sistema.listar_tarefas()
            if sistema.tarefas:
                id_tarefa = input("Digite o ID da tarefa a excluir: ")
                sistema.excluir_tarefa(id_tarefa)
        
        elif opcao == "5":
            print("Obrigado por usar o Sistema de Tarefas!")
            print("Dados salvos automaticamente.")
            break
        
        else:
            print("Opcao invalida! Tente 1, 2, 3, 4 ou 5.")

if __name__ == "__main__":
    main()