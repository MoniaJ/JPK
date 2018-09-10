from openpyxl.styles import Color, Fill, Font, Alignment

def format_ft1(lista):
    ft1 = Font(name='Calibri',size=9, italic=True)
    for komorka in lista:
        komorka.font = ft1
