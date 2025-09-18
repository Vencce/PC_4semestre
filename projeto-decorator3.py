import os
import sys
from abc import ABC, abstractmethod

# --- Exceção Customizada (Única para todo o projeto) ---
class BebidaNaoPersonalizavelError(Exception):
    """Exceção para tentativas de decorar uma bebida não personalizável."""
    def __init__(self, mensagem="Esta bebida não pode receber adicionais."):
        self.mensagem = mensagem
        super(BebidaNaoPersonalizavelError, self).__init__(self.mensagem)

# --- Estrutura Base (Componente) ---
class Bebida(ABC):
    """Componente Abstrato: A base para todas as bebidas."""
    def __init__(self):
        self._descricao = "Bebida desconhecida"
        self.personalizavel = True 

    @property
    @abstractmethod
    def descricao(self):
        pass

    @property
    @abstractmethod
    def preco(self):
        pass

# --- Componentes Concretos: COQUETÉIS ---
class CaipiraBase(Bebida):
    def __init__(self):
        super(CaipiraBase, self).__init__()
        self._descricao = "Caipira (base)"
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 20.0

class MojitoBase(Bebida):
    def __init__(self):
        super(MojitoBase, self).__init__()
        self._descricao = "Mojito (Rum, Hortelã, Limão, Água com Gás)"
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 22.00

class GinTonicaBase(Bebida):
    def __init__(self):
        super(GinTonicaBase, self).__init__()
        self._descricao = "Gin Tônica (Gin, Tônica, Gelo)"
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 25.0

# --- Componentes Concretos: CAFÉS ---
class Espresso(Bebida):
    def __init__(self):
        super(Espresso, self).__init__()
        self._descricao = "Espresso"
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 6.00

class CafeCoado(Bebida):
    def __init__(self):
        super(CafeCoado, self).__init__()
        self._descricao = "Café Coado"
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 5.00

# --- Componentes Concretos "PRONTOS/ASSINADOS" (Não personalizáveis) ---
class CaipirinhaTradicional(Bebida):
    def __init__(self):
        super(CaipirinhaTradicional, self).__init__()
        self._descricao = "Caipirinha Tradicional (Cachaça, Limão, Gelo e Açúcar)"
        self.personalizavel = False
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 25.0

class MoscowMuleTradicional(Bebida):
    def __init__(self):
        super(MoscowMuleTradicional, self).__init__()
        self._descricao = "Moscow Mule Tradicional (Vodka, Ginger Beer, Limão)"
        self.personalizavel = False
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 28.00

class CafePretinhoTradicional(Bebida):
    def __init__(self):
        super(CafePretinhoTradicional, self).__init__()
        self._descricao = "Café Pretinho Tradicional (puro 'de casa')"
        self.personalizavel = False
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return 4.00

# --- Decorador Abstrato ---
class Adicional(Bebida, ABC):
    def __init__(self, bebida):
        super(Adicional, self).__init__()
        if not bebida.personalizavel:
            raise BebidaNaoPersonalizavelError(
                "A bebida '{}' não aceita adicionais.".format(bebida.descricao)
            )
        self._bebida = bebida
    @property
    def descricao(self):
        return self._bebida.descricao
    @property
    def preco(self):
        return self._bebida.preco

# --- Decoradores Concretos (Todos os adicionais) ---

# Adicionais de Caipira
class Saque(Adicional):
    @property
    def descricao(self):
        return self._bebida.descricao + " + Saquê"
    @property
    def preco(self):
        return self._bebida.preco + 8.0

class Vodka(Adicional):
    @property
    def descricao(self):
        return self._bebida.descricao + " + Vodka"
    @property
    def preco(self):
        return self._bebida.preco + 10.0

class Morango(Adicional):
    @property
    def descricao(self):
        return self._bebida.descricao + " + Morango"
    @property
    def preco(self):
        return self._bebida.preco + 6.0
        
# Adicionais de Mixologia
class HortelaExtra(Adicional):
    @property
    def descricao(self):
        return "{}, Hortelã Extra".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco + 3.00

class RodelasPepino(Adicional):
    @property
    def descricao(self):
        return "{}, Rodelas de Pepino".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco + 2.50

# Adicionais de Cafeteria
class Leite(Adicional):
    @property
    def descricao(self):
        return "{}, com Leite".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco + 2.00

class Chocolate(Adicional):
    @property
    def descricao(self):
        return "{}, com Chocolate".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco + 2.50

class Chantilly(Adicional):
    @property
    def descricao(self):
        return "{}, com Chantilly".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco + 3.00
        
# Adicionais Gerais
class Acucar(Adicional):
    @property
    def descricao(self):
        return self._bebida.descricao + " + Açúcar"
    @property
    def preco(self):
        return self._bebida.preco + 0.50

class Adoçante(Adicional):
    @property
    def descricao(self):
        return "{}, com Adoçante".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco + 0.00
        
# Decoradores Multiplicativos
class CopoGrande(Adicional):
    FATOR_PRECO = 1.20 # +20%
    @property
    def descricao(self):
        return "{} (Copo Grande)".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco * self.FATOR_PRECO
        
class TamanhoGrande(Adicional):
    FATOR_PRECO = 1.30 # +30%
    @property
    def descricao(self):
        return "{} (Tamanho Grande)".format(self._bebida.descricao)
    @property
    def preco(self):
        return self._bebida.preco * self.FATOR_PRECO

# --- MENUS UNIFICADOS ---
BEBIDAS_BASE_MENU = {
    # Coquetéis
    '1': {'nome': 'Montar sua Caipira', 'classe': CaipiraBase},
    '2': {'nome': 'Mojito (personalizável)', 'classe': MojitoBase},
    '3': {'nome': 'Gin Tônica (personalizável)', 'classe': GinTonicaBase},
    '4': {'nome': 'Caipirinha Tradicional (pronta)', 'classe': CaipirinhaTradicional},
    '5': {'nome': 'Moscow Mule (pronto)', 'classe': MoscowMuleTradicional},
    # Cafeteria
    '6': {'nome': 'Espresso', 'classe': Espresso},
    '7': {'nome': 'Café Coado', 'classe': CafeCoado},
    '8': {'nome': 'Café Pretinho Tradicional (pronto)', 'classe': CafePretinhoTradicional},
}

ACRESCIMOS_MENU = {
    '1': {
        'nome_categoria': 'Adicionais de Café',
        'itens': {
            '1': {'nome': 'Leite', 'classe': Leite, 'preco': 2.00},
            '2': {'nome': 'Chocolate', 'classe': Chocolate, 'preco': 2.50},
            '3': {'nome': 'Chantilly', 'classe': Chantilly, 'preco': 3.00},
        }
    },
    '2': {
        'nome_categoria': 'Bases Alcoólicas (p/ Caipira)',
        'itens': {
            '1': {'nome': 'Saquê', 'classe': Saque, 'preco': 8.0},
            '2': {'nome': 'Vodka', 'classe': Vodka, 'preco': 10.0},
        }
    },
    '3': {
        'nome_categoria': 'Frutas e Mixologia',
        'itens': {
            '1': {'nome': 'Morango (p/ Caipira)', 'classe': Morango, 'preco': 6.0},
            '2': {'nome': 'Hortelã Extra (p/ Mojito)', 'classe': HortelaExtra, 'preco': 3.00},
            '3': {'nome': 'Rodelas de Pepino (p/ Gin)', 'classe': RodelasPepino, 'preco': 2.50},
        }
    },
    '4': {
        'nome_categoria': 'Extras e Tamanhos',
        'itens': {
            '1': {'nome': 'Açúcar', 'classe': Acucar, 'preco': 0.50},
            '2': {'nome': 'Adoçante', 'classe': Adoçante, 'preco': 0.00},
            '3': {'nome': 'Copo Grande (p/ Coquetéis, +20%)', 'classe': CopoGrande, 'preco': 0.0},
            '4': {'nome': 'Tamanho Grande (p/ Cafés, +30%)', 'classe': TamanhoGrande, 'preco': 0.0},
        }
    }
}

# --- Lógica da Interface (CLI) ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_pedido_atual(bebida):
    print("\n--- SEU PEDIDO ATUAL ---")
    print("Itens: {}".format(bebida.descricao))
    print("Preço: R$ {:.2f}".format(bebida.preco))
    print("------------------------\n")

def executar_bar_e_cafeteria():
    # Usando raw_input para Python 2 e input para Python 3 para compatibilidade
    prompt_input = raw_input if sys.version_info.major < 3 else input

    while True:
        limpar_tela()
        print("========== BEM-VINDO AO RESSACA'S BAR & CAFETERIA ==========")
        print("Escolha sua bebida base:")
        
        # Imprime cabeçalhos para organizar o menu
        print("\n--- COQUETÉIS ---")
        for key in ['1', '2', '3', '4', '5']:
            value = BEBIDAS_BASE_MENU[key]
            preco_base = value['classe']().preco
            print("{} - {} (R$ {:.2f})".format(key, value['nome'], preco_base))
            
        print("\n--- CAFETERIA ---")
        for key in ['6', '7', '8']:
            value = BEBIDAS_BASE_MENU[key]
            preco_base = value['classe']().preco
            print("{} - {} (R$ {:.2f})".format(key, value['nome'], preco_base))

        print("\n0 - Sair do programa")
        
        escolha_base = prompt_input(">> Digite sua escolha: ")

        if escolha_base.lower() in ['0', 'sair']:
            print("Obrigado pela visita!")
            break

        if escolha_base not in BEBIDAS_BASE_MENU:
            prompt_input("Opção inválida. Pressione Enter para tentar novamente...")
            continue

        item_escolhido = BEBIDAS_BASE_MENU[escolha_base]
        bebida_atual = item_escolhido['classe']()

        while bebida_atual.personalizavel:
            limpar_tela()
            mostrar_pedido_atual(bebida_atual)
            print("Escolha uma categoria de acréscimo:")
            
            for key, value in sorted(ACRESCIMOS_MENU.items()):
                print("{} - {}".format(key, value['nome_categoria']))
            
            print("\n0 - Finalizar pedido")
            escolha_cat = prompt_input(">> Digite a categoria: ")

            if escolha_cat == '0':
                break
            
            categoria_selecionada = ACRESCIMOS_MENU.get(escolha_cat)
            if not categoria_selecionada:
                prompt_input("Categoria inválida. Pressione Enter...")
                continue
            
            limpar_tela()
            print("--- Itens em {} ---".format(categoria_selecionada['nome_categoria']))
            
            for key_item, item in sorted(categoria_selecionada['itens'].items()):
                # Lógica para não mostrar preço de itens multiplicativos
                if item['classe'] in [CopoGrande, TamanhoGrande]:
                    print("{} - {}".format(key_item, item['nome']))
                else:
                    print("{} - {} (+ R$ {:.2f})".format(key_item, item['nome'], item['preco']))
            print("\n0 - Voltar para as categorias")
            
            escolha_item = prompt_input(">> Escolha o item para adicionar: ")

            if escolha_item == '0':
                continue

            item_info = categoria_selecionada['itens'].get(escolha_item)
            if item_info:
                bebida_atual = item_info['classe'](bebida_atual)
            else:
                prompt_input("Item inválido. Pressione Enter...")

        limpar_tela()
        print("\n========== PEDIDO FINALIZADO ==========")
        print("Descrição: {}".format(bebida_atual.descricao))
        print("Preço Total: R${:.2f}".format(bebida_atual.preco))
        print("=======================================")
        prompt_input("\nPressione Enter para fazer um novo pedido...")

if __name__ == "__main__":
    executar_bar_e_cafeteria()