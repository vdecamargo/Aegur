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

# Verificação de integridade
def validate_charsets():
    """Valida que os conjuntos de caracteres não contêm ambiguidades."""
    for char in AMBIGUOUS_CHARS:
        assert char not in ASCII_SAFE_CHARS, f"Caractere ambíguo '{char}' encontrado em ASCII_SAFE_CHARS"
        assert char not in UNICODE_SAFE_CHARS, f"Caractere ambíguo '{char}' encontrado em UNICODE_SAFE_CHARS"
        assert char not in BANK_SAFE_CHARS, f"Caractere ambíguo '{char}' encontrado em BANK_SAFE_CHARS"

# Executar validação
validate_charsets()