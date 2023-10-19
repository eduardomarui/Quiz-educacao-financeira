def reset():
    revanche = input('''
    =======================================
    Você deseja tentar novamente? (Sim/Não)
    =======================================
    ''').lower()

    if (revanche == "sim" or revanche == "ss" or revanche == "yes" or revanche == "y"):
        return False
    else:
        return True


def questoes(pergunta, alternativas, resposta_certa, resposta_explicada):
    pontos = 0

    for i in range(0, len(pergunta)):
        print(pergunta[i])
        resposta = input(alternativas[i]).upper()

        if(resposta == resposta_certa[i]):
            pontos += 100

        print(resposta_explicada[i], "\n")

    return pontos


def resultado(pontos):
    if (pontos == 1000):
        print("Parabéns!")
    else:
        if pontos > 700:
            print("Ótimo!")
        else:
            if pontos > 500:
                print("Razoável")
            else:
                print("Tem muito a melhorar")


def quiz():
    fim = False

    while(fim == False):
        pergunta = [
            '''
            1. Receitas e Despesas são termos que compõem parcialmente a base da Educação Financeira. Assinale a 
            alternativa que representa uma Receita e uma Despesa, respectivamente:
            ''',
            '''
            2. Rodinei trabalha há 12 anos, porém vive pedindo dinheiro emprestado pois gasta seu dinheiro
            desenfreadamente. Ao conversar sobre finanças numa roda de amigos, ele se dá conta que podia estar gastando 
            de maneira mais inteligente. Rodinei saiu do encontro decidido a fazer melhor uso do seu dinheiro, para isso
            ele deve:
             ''',
            '''
            3. Erick, um garoto de 12 anos, está interessado em assuntos de educação financeira. Ao ouvir na rádio sobre
            um banco que ofertava crédito aos clientes e perguntou ao seu pai, Eduardo, sobre o que se tratava, e o pai
            de maneira correta disse que:
            ''',
            '''
            4. Rivaldo fez um teste de perfil para investidores visando saber em quais produtos ele devia alocar o
            dinheiro de seu bônus. Segundo resultados do teste, o perfil de Rivaldo é mais avesso a risco, sendo 
            caracterizado como CONSERVADOR. Dessa maneira, qual seria o produto mais adequado ao mais novo investidor?
            ''',
            '''
            5. Supondo que, ao conversar com um consultor financeiro, Rivaldo decidiu investir uma quantia de 
            R$297.000,00 em um produto de renda fixa que dá retorno estimado de 10.5% ao ano, durante 4 anos, qual será
            o saldo estimado aproximado de Rivaldo no fim desses 4 anos?
            ''',
            '''
            6. Henrique quer comprar um presente de aniversário  para seu pai, Eduardo, que será daqui a 5 meses. O
            perfume que Eduardo quer custa R$890,00. Quanto Henrique terá que economizar todo mês, durante 5 meses para
            conseguir o valor do perfume?
            ''',
            '''
            7. Giovanne pretende fazer uma festa de aniversário para isso foi ao mercado e consultou o preço da lata
            de refrigerante e do salgado que custavam respectivamente 3 reais e 1 real. Sabe-se que cada convidado come
            pelo menos 5 salgados e bebe pelo menos 1 lata de refrigerante. Giovanne possui R$300,00 para realização da
            festa, qual o máximo de convidados que ela pode chamar sem comprometer a alimentação dos convidados?
            ''',
            '''
            8. Existem três características de investimentos que devem ser analisadas antes de realizar a aplicação, que
            são risco, liquidez e rentabilidade. Determine as definições como verdadeiras (V)  ou falsas (F):
            ( ) Liquidez é a possibilidade de o investimento ser transformado em dinheiro a qualquer momento, por um
            preço justo.
            ( ) Risco  é a probabilidade de ocorrência de perdas. Normalmente, quanto maior o risco maior a
            probabilidade de o investidor incorrer em perdas.
            ( ) Rentabilidade é o retorno, a remuneração do investimento. Quando fazemos um investimento, temos uma
            expectativa de rentabilidade que pode se concretizar ou não.
            ''',
            '''
            9. Mila pretende abrir o seu próprio negócio de doces, com a intenção de ajudar nas despesas de casa. Ela
            gasta R$30,00 para preparar uma porção de 15 bolinhos de chocolate e vende cada por R$6,00. Quantos bolinhos
            Mila precisa vender para atingir a meta de R$1000,00 de lucro?
            ''',
            '''
            10. Joaquim comprou um lote com 100 ações de uma empresa X no início de março, cada ação estava valendo
            R$24,00. No fim de agosto as ações valorizaram 150%, caso Joaquim decida vender suas ações, quanto ele irá
            lucrar?
            '''
        ]

        alternativas = [
            '''
            a) Financiamento de carro e pagamento da conta de internet.
            b) Recebimento de salário e recebimento de aluguel.
            c) Pagamento de aluguel e recebimento de bônus do trabalho.
            d) Pagamento da conta de internet e recebimento de salário.
            e) Recebimento de bônus do trabalho e financiamento de carro.
            ''',
            '''
            a) Anotar as despesas e receitas em uma planilha, com intuito de planejar as compras futuras e gastar mais
            do que o planejado.
            b) Comprar produtos que viu na televisão sem necessidade porque achou legal.
            c) Fazer compras apenas no cartão de crédito e parcelar as compras sempre que possível.
            d) Anotar as despesas e receitas em uma planilha, com intuito de planejar as compras futuras e guardar uma
            quantia.
            e) Guardar todos os recibos em uma caixa de sapato.
            ''',
            '''
            a) Trata-se de  quanto de dinheiro o banco te dá para abrir uma conta de forma gratuita.
            b) Trata-se de uma oferta de emprego no banco em troca de créditos.
            c) Trata-se de um bônus dado pelo pagamento antecipado da fatura do cartão de crédito.
            d) Trata-se sobre uma oferta que o banco oferece para renegociação de dívidas.
            e) Trata- se de uma oferta de uso de dinheiro por um determinado tempo, que terá que ser devolvido com juros
            no futuro.
            ''',
            '''
            a) Investimento de renda fixa, baixo risco, que rende 12% ao ano.
            b) Investimento em produtos de renda fixa e variável, risco moderado, que pode render de 2% a 20%.
            c) Investimento total em renda variável, de alto risco, que pode ter ganhos inestimáveis, porém podendo
            perder todo o dinheiro.
            d) Investimento em criptomoedas de alto risco e com altas possibilidades de ganhos.
            e) Investimentos alternativos, como artes digitais (NFTs), vinhos e criptomoedas populares - como Bitcoin.
            ''',
            '''
            a) R$537.824,00.
            b) R$697.763,00.
            c) R$493.514,00.
            d) R$442.797,00.
            e) R$612,790,00.
            ''',
            '''
            a) R$250,00.
            b) R$178,00.
            c) R$148,00.
            d) R$188,00.
            e) R$225,00.
            ''',
            '''
            a) 40 convidados.
            b) 38 convidados.
            c) 37 convidados.
            d) 39 convidados.
            e) 41 convidados.
            ''',
            '''
            a) Todas são verdadeiras.
            b) V,F,F.
            c) F,V,V.
            d) F,F,V.
            e) V,V,F.
            ''',
            '''
            a) 180 bolinhos.
            b) 200 bolinhos.
            c) 250 bolinhos.
            d) 264 bolinhos.
            e) 324 bolinhos.
            ''',
            '''
            a) aR$2400,00.
            b) R$3600,00.
            c) R$4800,00.
            d) R$6000,00.
            e) R$7200,00.
            ''',
            ]

        resposta_certa = [
            "E",
            "D",
            "E",
            "A",
            "D",
            "B",
            "C",
            "A",
            "C",
            "B"
        ]

        resposta_explicada = [
            '''
            ============================================================================================================
            A alternativa correta é a E, o recebimento de bônus é uma receita, visto que trata-se de um ganho financeiro
            obtido por meio do trabalho; já o financiamento de um carro representa uma despesa no orçamento de uma
            pessoa.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa correta é a D. Anotar as despesas e receitas é essencial para obter um parâmetro das contas a
            serem pagas, total de gastos mensais, e também saber qual será o saldo do mês para poder realizar o
            pagamentos dessas contas e se haverá a possibilidade de fazer uma reserva financeira para planejar o futuro.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa E é a correta, visto que trata de forma correta a definição de crédito bancário que é o
            dinheiro oferecido pelo banco ao cliente que fica comprometido a devolvê-lo em forma de dívida, devendo ser
            pago em parcelas, sendo que o valor total a ser pago é o dinheiro oferecido, acrescido de juros, conforme
            estipulado em contrato.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            Alternativa A, pois investimentos em renda fixa, possibilita, antes de investir, saber de quanto será o
            ganho e dificilmente haverá perdas, dessa forma, trata-se de um investimento seguro que é ideal ao perfil de
            conservador do Rivaldo.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            Alternativa D. Através da fórmula de juros compostos: M = C x (1 + i) ^ n, em que M representa o montante
            investido (resultado pós investimento), C o capital inicial investido, com o 'i' sendo a taxa de juros
            aplicada e 'n' o tempo do investimento. Assim, para realizar o cálculo de Rivaldo fica
            297.000,00 * (1 + 0,105) ^ 4 resultando em aproximadamente R$442.797,00.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa B é a correta, visto que para conseguir o montante para compra do perfume deve-se fazer um
            planejamento financeiro de quanto Henrique deveria economizar mensalmente, tal resposta é alcançada pelo
            cálculo da divisão do valor pelo tempo, assim ficaria 890/5 que resulta em R$178,00.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa C é a correta, pois cada convidado consumirá pelo menos 5 salgados e pelo menos 1 lata de
            refrigerante totalizando 8 reais, sabendo que Giovanne possui 300 reais, o máximo de convidados que ele
            poderia chamar sem comprometer a alimentação é dada pelo cálculo da divisão do dinheiro total pelo  dinheiro
            que cada convidado consumirá  que resulta em 37,5 ou seja o máximo seria 37.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa A é a correta, pois as definições apresentadas de liquidez, risco e rentabilidade são
            corretas.
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa C é a correta. Pois Mila gasta R$30,00 para produzir 15 bolinhos, logo gera R$2,00 de gasto
            para cada bolinho e, considerando o preço de venda de R$6,00, ela apresenta R$4,00 de lucro para a venda de
            cada unidade, então para atingir a meta de R$1000,00, é necessário vender 250 bolinhos (4 * 250 = 1000).
            ============================================================================================================
            ''',
            '''
            ============================================================================================================
            A alternativa B é a correta. Pois Joaquim investe R$2400,00 considerando a compra do lote de 100 ações com
            valor de R$24,00 cada, com a valorização de 150%, o investimento de R$2400,00 se tornou R$6000,00
            considerando o valor base de R$2400,00 mais 100% (R$2400,00) deste valor e mais 50% (R$1200,00), com o
            desconto do valor gasto (R$2400,00), ele obteve R$3600,00 de lucro.
            ============================================================================================================
            '''
        ]

        print('''
        =========================================
        BEM VINDO AO QUIZ DE EDUCAÇÃO FINANCEIRA!
        =========================================
        ''')

        pontos = questoes(pergunta, alternativas, resposta_certa, resposta_explicada)

        print("Sua pontuação foi {}/1000". format(pontos))

        resultado(pontos)

        fim = reset()


quiz()
