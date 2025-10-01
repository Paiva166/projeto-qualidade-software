"""
Testes basicos para o Sistema de Tarefas
Qualidade de Software - ISO 25010
"""
import os
import json

def test_criar_sistema():
    """Testa criacao do sistema - CONFIABILIDADE"""
    try:
        from main import GerenciadorTarefas
        print("Teste de importacao: PASSOU")
        return True
    except ImportError as e:
        print(f"Erro na importacao: {e}")
        return False

def test_estrutura_arquivos():
    """Testa se arquivos necessarios existem - FUNCIONALIDADE"""
    arquivos_necessarios = ['main.py', 'README.md', 'requirements.txt']
    
    for arquivo in arquivos_necessarios:
        if os.path.exists(arquivo):
            print(f"Arquivo {arquivo}: ENCONTRADO")
        else:
            print(f"Arquivo {arquivo}: NAO ENCONTRADO")
            return False
    return True

def test_execucao_basica():
    """Testa execucao basica do sistema - USABILIDADE"""
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            codigo = f.read()
        compile(codigo, 'main.py', 'exec')
        print("Teste de sintaxe: PASSOU")
        return True
    except SyntaxError as e:
        print(f"Erro de sintaxe: {e}")
        return False

if __name__ == "__main__":
    print("INICIANDO TESTES DO SISTEMA")
    print("=" * 40)
    
    testes_passados = 0
    testes_totais = 3
    
    if test_criar_sistema():
        testes_passados += 1
    
    if test_estrutura_arquivos():
        testes_passados += 1
        
    if test_execucao_basica():
        testes_passados += 1
    
    print("=" * 40)
    print(f"RESULTADO: {testes_passados}/{testes_totais} testes passaram")
    
    if testes_passados == testes_totais:
        print("TODOS OS TESTES PASSARAM!")
    else:
        print("Alguns testes falharam - verifique o sistema")