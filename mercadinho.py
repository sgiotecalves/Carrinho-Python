class Supermercado:
    def __init__(self):
        self.catalogo = {'Arroz': 10.0, 'Feijão': 8.5, 'Macarrão': 5.0, 'Carne': 25.0}
        self.carrinho = {}
        self.total = 0.0

    def comprar(self):
        while True:
            print('Catálogo de produtos:')
            for produto, preco in self.catalogo.items():
                print(f'{produto.capitalize()} - R${preco:.2f}')
                
            escolha = input('Digite o nome do produto que deseja comprar (ou "sair" para encerrar): ')
            if escolha.lower() == 'sair':
                break
            if escolha in self.catalogo:
                quantidade = int(input('Digite a quantidade desejada: '))
                if escolha in self.carrinho:
                    self.carrinho[escolha] += quantidade
                else:
                    self.carrinho[escolha] = quantidade
                print(f'{quantidade} unidade(s) de {escolha.capitalize()} adicionadas ao carrinho.')
            else:
                print('Produto não encontrado no catálogo. Tente novamente.')
                           
            remover = input('Deseja remover algum item do carrinho? (Sim/não): ')
            if remover.lower() == 'sim':
                produto_remover = input('Digite o nome do produto que deseja remover: ')
                quantidade_remover = float(input('Digite a quantidade que deseja remover: '))
                
                if produto_remover in self.carrinho:
                    if self.carrinho[produto_remover] >= quantidade_remover:
                        self.carrinho[produto_remover] -= quantidade_remover
                        if self.carrinho[produto_remover] == 0:
                            del self.carrinho[produto_remover]
                        print(f'{quantidade_remover} do produto {produto_remover.capitalize()} removido do carrinho.')
                    else:
                        print('Quantidade a remover é maior do que a disponível no carrinho.')

        print('\nResumo da compra')
        for produto, quantidade in self.carrinho.items():
            preco_unitario = self.catalogo[produto]
            preco_total = preco_unitario * quantidade
            print(f'{quantidade} unidade(s) de {produto.capitalize()} - R${preco_total:.2f}')
            self.total += preco_total
        
        print(f'Total da compra: R${self.total:.2f}')
        self.pagar()

    def pagar(self):
        pagamento = input('Digite o valor recebido pelo cliente (ou "Cancelar" para cancelar a compra): ')
        if pagamento.lower() == 'cancelar':
            print('Compra cancelada.')
            return
        
        valor_pago = float(pagamento)
        troco = valor_pago - self.total
        
        if valor_pago < self.total:
            print(f'Valor insuficiente. Falta R$ {self.total - valor_pago:.2f}.')
            self.pagar()
        elif troco > 0:
            print(f'Troco: R${troco:.2f}')
        
        cpf_nota = input('Deseja informar o CPF na nota fiscal? (Sim/não): ')
        if cpf_nota.lower() == 'sim':
            cpf = input('Digite o CPF: ')
            print(f'Nota fiscal: Total da compra - R${self.total:.2f} | CPF - {cpf}')
        else:
            print(f'Nota fiscal: Total da compra - R${self.total:.2f}')
            
            self.gerar_nota_fiscal()

            # Resetando os valores após a compra
            self.catalogo = {'Arroz': 10.0, 'Feijão': 8.5, 'Macarrão': 5.0, 'Carne': 25.0}
            self.carrinho = {}
            self.total = 0.0

    def gerar_nota_fiscal(self):
        total = 0
        with open("nota_fiscal.txt", "w") as nota_fiscal:
            nota_fiscal.write("====================================NOTA FISCAL==============================================\n")
            nota_fiscal.write("===========================\n")
            for produto, quantidade in self.carrinho.items():
                preco_unitario = self.catalogo[produto]
                subtotal = preco_unitario * quantidade
                total += subtotal
                nota_fiscal.write(f"{produto.capitalize()} - {quantidade} x R${preco_unitario:.2f} = R${subtotal:.2f}\n")
            nota_fiscal.write("===========================\n")
            nota_fiscal.write(f"Total: R${total:.2f}\n")
        print("\nCompra finalizada! Nota fiscal gerada em 'nota_fiscal.txt'.")
        
        
        # Resetando os valores após a compra
        self.catalogo = {'Arroz': 10.0, 'Feijão': 8.5, 'Macarrão': 5.0, 'Carne': 25.0}
        self.carrinho = {}
        self.total = 0.0

mercado = Supermercado()
mercado.comprar()
