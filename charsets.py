#!/usr/bin/env python3
"""
Definições de conjuntos de caracteres seguros para Aegur
"""

# Caracteres visualmente ambíguos que devem ser excluídos
AMBIGUOUS_CHARS = set([
    '0', 'O', 'o',  # Zero, letra O maiúscula, letra o minúscula
    '1', 'l', 'I', 'i'  # Um, letra l minúscula, letra I maiúscula, letra i minúscula
])

# Caracteres ASCII seguros (sem ambiguidades)
ASCII_SAFE_CHARS = (
    "23456789"  # Dígitos (excluindo 0 e 1)
    "ABCDEFGHJKLMNPQRSTUVWXYZ"  # Letras maiúsculas (excluindo I, O)
    "abcdefghijkmnpqrstuvwxyz"  # Letras minúsculas (excluindo l, o)
    "!@#$%^&*()_+-=[]{}|;:,.<>?"
)

# Caracteres Unicode seguros (símbolos visualmente distintos)
UNICODE_SAFE_CHARS = (
    "ΔΘΛΞΠΣΦΨΩ≠≤≥±∫∏√€₹₽₺←→↑↓↔️↵¶§"
    "αβγδεζηθικλμνξοπρστυφχψω"
    "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    "абвгдежзийклмнопрстуфхцчшщъыьэюя"
)

# Caracteres seguros para modo bancário (apenas alfanumérico)
BANK_SAFE_CHARS = (
    "23456789"  # Dígitos (excluindo 0 e 1)
    "ABCDEFGHJKLMNPQRSTUVWXYZ"  # Letras maiúsculas (excluindo I, O)
    "abcdefghijkmnpqrstuvwxyz"  # Letras minúsculas (excluindo l, o)
)

def validate_charsets():
    """Valida que os conjuntos de caracteres não contêm ambiguidades."""
    for char in AMBIGUOUS_CHARS:
        # Verificar ASCII_SAFE_CHARS
        if char in ASCII_SAFE_CHARS:
            print(f"Aviso: Caractere ambíguo '{char}' encontrado em ASCII_SAFE_CHARS")
            # Remover o caractere ambíguo
            globals()['ASCII_SAFE_CHARS'] = ASCII_SAFE_CHARS.replace(char, '')
        
        # Verificar UNICODE_SAFE_CHARS
        if char in UNICODE_SAFE_CHARS:
            print(f"Aviso: Caractere ambíguo '{char}' encontrado em UNICODE_SAFE_CHARS")
            globals()['UNICODE_SAFE_CHARS'] = UNICODE_SAFE_CHARS.replace(char, '')
        
        # Verificar BANK_SAFE_CHARS
        if char in BANK_SAFE_CHARS:
            print(f"Aviso: Caractere ambíguo '{char}' encontrado em BANK_SAFE_CHARS")
            globals()['BANK_SAFE_CHARS'] = BANK_SAFE_CHARS.replace(char, '')

# Executar validação (comentado para evitar problemas)
# validate_charsets()

# Ou executar validação e corrigir automaticamente
validate_charsets()