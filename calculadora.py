from decimal import Decimal

import flet as ft
from flet import colors # cores do flet

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    
]
def main(page: ft.Page):
    page.bgcolor = '#000' # cor
    page.window_resizable = False
    page.window_width = 290
    page.window_height = 450
    page.window_always_on_top = True # sempre vísivel

    resultado = ft.Text(value = '0', color = colors.WHITE, size = 30) # cria a linha onde aparece os resultados

    def calcular(operador, valor_atual):
        try: # Tente calcular
            value = eval(valor_atual) # verefica a operação e a executa como operação aritimetrica

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except: # Caso não consiga
            return 'Error'

        digitos = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digitos}f')

    def selecionado(e):
        # if resultado.value == '0':
        #     value_atual = resultado.value
        # else:
        #     value_atual = ''

        value_atual = resultado.value if resultado.value not in ('0', 'Error') else ''

        valor = e.control.content.value

        if valor.isdigit():
            valor = value_atual + valor
        elif valor == 'AC':
            valor = '0'
        else:
            if value_atual and value_atual[-1] in ('/', '*', '-', '+', '.'):
                value_atual = value_atual[:-1]

            valor = value_atual + valor

            if valor[-1] in ('=', '%', '±'):
                valor = calcular(operador=valor[-1], valor_atual=value_atual)

        resultado.value = valor
        resultado.update()

    display = ft.Row(
        width=250,
        height=60,
        controls=[resultado],
        alignment='end',
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte'], size=20),
        width=55,
        height=55,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=selecionado,
    ) for btn in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard) # adiciona a tela

ft.app(target=main) # abre o app a partir da função
