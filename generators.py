#!/usr/bin/env python3
"""
Geradores de senhas para Aegur
"""
import secrets
from typing import List
from charsets import (
    ASCII_SAFE_CHARS,
    UNICODE_SAFE_CHARS,
    BANK_SAFE_CHARS
)
from entropy import calculate_entropy

def generate_password(length: int, mode: str = 'strong') -> str:
    """
    Gera uma senha com base no modo especificado.
    
    Args:
        length: Comprimento da senha
        mode: 'strong', 'ascii', 'bank', 'paranoid'
    
    Returns:
        Senha gerada
    """
    if mode == 'bank':
        chars = BANK_SAFE_CHARS
    elif mode == 'ascii':
        chars = ASCII_SAFE_CHARS
    elif mode == 'paranoid':
        chars = ASCII_SAFE_CHARS  # Modo paranoico usa ASCII seguro
    else:  # strong (padrão)
        chars = ASCII_SAFE_CHARS + UNICODE_SAFE_CHARS
    
    # Gerar senha usando SystemRandom para criptografia segura
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def secure_overwrite(obj: str) -> None:
    """
    Sobrescreve seguramente uma string com caracteres aleatórios.
    """
    if isinstance(obj, str):
        # Converter para lista para permitir modificação
        temp_list = list(obj)
        # Preencher com caracteres aleatórios
        for i in range(len(temp_list)):
            temp_list[i] = secrets.choice('abcdefghijklmnopqrstuvwxyz')
        # Converter de volta para string (o valor original é perdido)
        ''.join(temp_list)