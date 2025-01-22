from sistemalogistico import SistemaLogistico
from caminhao import Caminhao
from produto import Produto
from funcionario import Funcionario

sistema = SistemaLogistico()

def exibir_menu_principal():
    print("\nMenu Principal")
    print("1. Cadastrar Funcionário")
    print("2. Acessar Funcionário")
    print("3. Listar Permissões")
    print("0. Sair")

def exibir_menu_funcionario():
    print("\nPágina do Funcionário")
    print("1. Acessar Sistema de Rotas")
    print("2. Acessar Controle de Estoque")
    print("0. Voltar")

def exibir_menu_sistema_rotas():
    print("\nSistema de Rotas")
    print("1. Cadastrar Local")
    print("2. Adicionar Conexão entre Locais")
    print("3. Planejar Rota")
    print("4. Planejar Múltiplas Entregas")
    print("5. Visualizar mapa")
    print("6. Remover Local")
    print("7. Remover Conexão entre Locais")
    print("0. Voltar")

def exibir_menu_controle_estoque():
    print("\nControle de Estoque")
    print("1. Adicionar produto ao estoque")
    print("2. Atualizar quantidade de produto")
    print("3. Consultar quantidade de produto")
    print("4. Consultar quantidade em intervalo")
    print("5. Calcular valor total do estoque")
    print("6. Remover produto do estoque")
    print("7. Listar produtos no estoque")
    print("8. Listar quantidade de produtos no estoque")
    print("9. Consultar produtos com quantidade menor ou igual a X")
    print("0. Voltar")

def executar_menu():
    funcionarios_cadastrados = {}
    
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                nome = input("Nome do funcionário: ")
                email = input("Email do funcionário: ")
                cpf = input("CPF do funcionário: ")
                cargo = input("Cargo do funcionário: ")
                
                funcionario = Funcionario(nome, email, cpf, cargo)
                funcionarios_cadastrados[cpf] = funcionario
                sistema.cadastrar_usuario(funcionario)
                
                print("Funcionário '{}' cadastrado com sucesso!".format(nome))
            except Exception as e:
                print("Erro ao cadastrar funcionário: {}".format(e))

        elif opcao == "2":
            cpf = input("Digite o CPF do funcionário: ")
            
            if cpf in funcionarios_cadastrados:
                funcionario = funcionarios_cadastrados[cpf]
                print("Bem-vindo, {}!".format(funcionario.nome))

                while True:
                    exibir_menu_funcionario()
                    opcao_funcionario = input("Escolha uma opção: ")

                    if opcao_funcionario == "1":
                        while True:
                            exibir_menu_sistema_rotas()
                            opcao_rotas = input("Escolha uma opção: ")
                            
                            if opcao_rotas == "1":
                                try:
                                    nome_local = input("Nome do local: ")
                                    sistema.cadastrar_local(nome_local)
                                    print("Local '{}' cadastrado com sucesso!".format(nome_local))
                                except Exception as e:
                                    print("Erro ao cadastrar local: {}".format(e))
                            

                            elif opcao_rotas == "2":
                                try:
                                    local1 = input("Local 1: ")
                                    local2 = input("Local 2: ")
                                    distancia = float(input("Distância entre os locais: "))
                                    sistema.adicionar_conexao(local1, local2, distancia)
                                    print("Conexão entre '{}' e '{}' adicionada com sucesso!".format(local1, local2))
                                except ValueError:
                                    print("Erro: A distância deve ser um número válido.")
                                except Exception as e:
                                    print("Erro ao adicionar conexão: {}".format(e))
                            

                            elif opcao_rotas == "3":
                                try:
                                    origem = input("Origem: ")
                                    destino = input("Destino: ")
                                    rota_info = sistema.planejar_rota(origem, destino)
                                    print("Rota planejada: {}".format(" -> ".join(rota_info['rota'])))
                                    print("Distância total: {} km".format(rota_info['distancia']))
                                except ValueError as e:
                                    print(e)
                                except Exception as e:
                                    print("Erro ao planejar rota: {}".format(e))
                            

                            elif opcao_rotas == "4":
                                try:
                                    placa = input("Placa do caminhão: ")
                                    caminhao = Caminhao(placa)
                                    while True:
                                        destino = input("Destino (ou 'fim' para parar): ")
                                        if destino.lower() == "fim":
                                            break
                                        caminhao.adicionar_destino(destino)
                                    sistema.planejar_multiplas_entregas(caminhao, input("Origem: "))
                                    print(caminhao.visualizar_rotas())
                                except ValueError as e:
                                    print(e)
                                except Exception as e:
                                    print("Erro ao planejar múltiplas entregas: {}".format(e))

                            elif opcao_rotas == "5":
                                try:
                                    sistema.map()
                                except Exception as e:
                                    print("Erro ao visualizar mapa: {}".format(e))

                            elif opcao_rotas == "6":
                                try:
                                    nome_local = input("Nome do local a ser removido: ")
                                    print(funcionario.remover_local(sistema, nome_local))
                                except Exception as e:
                                    print("Erro ao remover local: {}".format(e))

                            elif opcao_rotas == "7":
                                try:
                                    local1 = input("Local 1: ")
                                    local2 = input("Local 2: ")
                                    print(funcionario.remover_conexao(sistema, local1, local2))
                                except Exception as e:
                                    print("Erro ao remover conexão: {}".format(e))
                                
                            elif opcao_rotas == "0":
                                break
                            

                            else:
                                print("Opção inválida. Tente novamente.")
                    
                    elif opcao_funcionario == "2":
                        while True:
                            exibir_menu_controle_estoque()
                            opcao_estoque = input("Escolha uma opção: ")

                            if opcao_estoque == "1":
                                try:
                                    codigo = int(input("Digite o código do produto: "))
                                    nome = input("Digite o nome do produto: ")
                                    preco = float(input("Digite o preço do produto: "))
                                    quantidade = int(input("Digite a quantidade do produto: "))
                                    sistema.estoque.adicionar_produto(Produto(codigo, nome, preco, quantidade))
                                except ValueError:
                                    print("Erro: A entrada fornecida não é válida.")
                                except Exception as e:
                                    print("Erro ao adicionar produto: {}".format(e))

                            elif opcao_estoque == "2":
                                try:
                                    codigo = int(input("Digite o código do produto: "))
                                    quantidade = int(input("Digite a quantidade a ser adicionada: "))
                                    sistema.estoque.atualizar_quantidade(codigo, quantidade)
                                except ValueError:
                                    print("Erro: A quantidade deve ser um número válido.")
                                except Exception as e:
                                    print("Erro ao atualizar quantidade: {}".format(e))

                            elif opcao_estoque == "3":
                                try:
                                    codigo = int(input("Digite o código do produto: "))
                                    print(sistema.estoque.consultar_quantidade_produto(codigo))
                                except Exception as e:
                                    print("Erro ao consultar produto: {}".format(e))

                            elif opcao_estoque == "4":
                                try:
                                    codigo_inicio = int(input("Digite o código inicial: "))
                                    codigo_fim = int(input("Digite o código final: "))
                                    print(sistema.estoque.consultar_quantidade_intervalo(codigo_inicio, codigo_fim))
                                except Exception as e:
                                    print("Erro ao consultar intervalo: {}".format(e))

                            elif opcao_estoque == "5":
                                try:
                                    print(sistema.estoque.valor_total_estoque())
                                except Exception as e:
                                    print("Erro ao calcular valor total: {}".format(e))

                            elif opcao_estoque == "6":
                                try:
                                    codigo = int(input("Digite o código do produto a ser removido: "))
                                    sistema.estoque.remover_produto(codigo)
                                except Exception as e:
                                    print("Erro ao remover produto: {}".format(e))

                            elif opcao_estoque == "7":
                                try:
                                    sistema.estoque.listar_produtos()
                                except Exception as e:
                                    print("Erro ao listar produtos: {}".format(e))

                            elif opcao_estoque == "8":
                                try:
                                    print(sistema.estoque.quantidade_presente_estoque())
                                except Exception as e:
                                    print("Erro ao consultar quantidade no estoque: {}".format(e))

                            elif opcao_estoque == "9":
                                try:
                                    quantidade_minima = int(input("Digite a quantidade mínima: "))
                                    sistema.estoque.consultar_produto_com_quantidade_minima(quantidade_minima)
                                except ValueError:
                                    print("Erro: A quantidade mínima deve ser um número válido.")
                                except Exception as e:
                                    print("Erro ao consultar produtos: {}".format(e))

                            elif opcao_estoque == "0":
                                break

                            else:
                                print("Opção inválida. Tente novamente.")

                    elif opcao_funcionario == "0":
                        break

                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("CPF não encontrado. Acesso negado.")

        elif opcao == "3":
            sistema.listar_funcionarios()  

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_menu()
