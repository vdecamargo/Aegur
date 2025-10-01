#!/usr/bin/env python3
"""
Cálculo de entropia e resistência a força bruta para Aegur
"""
import math
from typing import Tuple
from charsets import (
    ASCII_SAFE_CHARS,
    UNICODE_SAFE_CHARS,
    BANK_SAFE_CHARS
)

def calculate_entropy(password: str, charset_size: int = None) -> float:
    """
    Calcula a entropia de uma senha.
    
    Args:
        password: A senha para calcular entropia
        charset_size: Tamanho do conjunto de caracteres usado
    
    Returns:
        Entropia em bits
    """
    if charset_size is None:
        # Inferir tamanho do charset com base nos caracteres usados
        used_chars = set(password)
        charset_size = len(used_chars)
        
        # Alternativamente, usar o tamanho máximo do charset baseado no modo
        # Isso é mais preciso para senhas geradas
        if all(c in "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz" for c in password):
            charset_size = len("23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz")
        elif all(c in "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            charset_size = len("23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?")
        else:
            # Usar tamanho máximo dos caracteres usados
            charset_size = max(len(set(password)), charset_size)
    
    # Fórmula: log2(charset_size^length) = length * log2(charset_size)
    entropy = len(password) * math.log2(charset_size)
    return entropy

def estimate_brute_force_time(entropy_bits: float, guesses_per_second: int = 10**12) -> str:
    """
    Estima o tempo necessário para quebrar a senha por força bruta.
    
    Args:
        entropy_bits: Entropia da senha em bits
        guesses_per_second: Tentativas por segundo
    
    Returns:
        String com estimativa de tempo
    """
    total_combinations = 2 ** entropy_bits
    seconds = total_combinations / (2 * guesses_per_second)  # Média: metade do tempo
    
    # Converter para unidades legíveis
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.1f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.1f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.1f} days"
    else:
        years = seconds / 31536000
        if years < 1000:
            return f"{years:.1f} years"
        elif years < 1000000:
            return f"{years / 1000:.1f} thousand years"
        else:
            return f"{years / 1000000:.1f} million years"

def format_entropy_info(password: str, mode: str) -> str:
    """
    Formata informações de entropia para exibição.
    
    Args:
        password: A senha gerada
        mode: Modo de geração ('strong', 'ascii', 'bank', 'paranoid')
    
    Returns:
        String formatada com informações de entropia
    """
    # Determinar tamanho do charset baseado no modo
    if mode == 'bank':
        charset_size = len(BANK_SAFE_CHARS)
    elif mode == 'ascii':
        charset_size = len(ASCII_SAFE_CHARS)
    elif mode == 'paranoid':
        charset_size = len(ASCII_SAFE_CHARS)  # Modo paranoico usa ASCII seguro
    else:  # strong
        charset_size = len(ASCII_SAFE_CHARS + UNICODE_SAFE_CHARS)
    
    entropy = calculate_entropy(password, charset_size)
    time_estimate = estimate_brute_force_time(entropy)
    
    info = (
        f"Length: {len(password)}\n"
        f"Character pool: {charset_size}\n"
        f"Estimated entropy: {entropy:.1f} bits\n"
        f"Brute-force resistance (10^12 guesses/s): {time_estimate}"
    )
    
    return info