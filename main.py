# Sistema de Gerenciamento de Tarefas
# Qualidade de Software - ISO 25010

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
            print("❌ Erro: Descrição não pode ser vazia!")
            return False
        
        nova_tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao.strip(),
            "concluida": False
        }
        
        self.tarefas.append(nova_tarefa)
        if self.salvar_tarefas():
            print(f"✅ Tarefa '{descricao}' adicionada! (ID: {nova_tarefa['id']})")
            return True
        return False
    
    def listar_tarefas(self):
        """Lista todas as tarefas - USABILIDADE"""
        if not self.tarefas:
            print("📝 Nenhuma tarefa cadastrada.")
            return
        
        print(f"\n📋 LISTA DE TAREFAS ({len(self.tarefas)} tarefas)")
        print("=" * 40)
        for tarefa in self.tarefas:
            status = "✅" if tarefa["concluida"] else "⏳"
            print(f"{tarefa['id']}. [{status}] {tarefa['descricao']}")
        print("=" * 40)
    
    def marcar_concluida(self, id_tarefa):
        """Marca tarefa como concluída - FUNCIONALIDADE"""
        try:
            id_tarefa = int(id_tarefa)
            for tarefa in self.tarefas:
                if tarefa["id"] == id_tarefa:
                    if not tarefa["concluida"]:
                        tarefa["concluida"] = True
                        self.salvar_tarefas()
                        print(f"🎉 Tarefa {id_tarefa} concluída!")
                        return True
                    else:
                        print(f"ℹ️  Tarefa {id_tarefa} já estava concluída!")
                        return True
            print(f"❌ Tarefa {id_tarefa} não encontrada!")
            return False
        except ValueError:
            print("❌ Erro: ID deve ser um número!")
            return False

def main():
    sistema = GerenciadorTarefas()
    
    while True:
        print("\n" + "="*50)
        print("           🚀 SISTEMA DE TAREFAS v2.0")
        print("="*50)
        print("1. ➕ Adicionar tarefa")
        print("2. 📋 Listar tarefas") 
        print("3. ✅ Marcar tarefa como concluída")
        print("4. ❌ Sair")
        print("="*50)
        
        opcao = input("👉 Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            descricao = input("📝 Digite a descrição da tarefa: ")
            sistema.adicionar_tarefa(descricao)
        
        elif opcao == "2":
            sistema.listar_tarefas()
        
        elif opcao == "3":
            sistema.listar_tarefas()
            if sistema.tarefas:
                id_tarefa = input("\n🔢 Digite o ID da tarefa a concluir: ")
                sistema.marcar_concluida(id_tarefa)
        
        elif opcao == "4":
            print("\n👋 Obrigado por usar o Sistema de Tarefas!")
            print("💾 Dados salvos automaticamente.")
            break
        
        else:
            print("❌ Opção inválida! Tente 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()