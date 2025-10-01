#!/usr/bin/env python3
"""
Aegur — Gerador de Senhas Offline em Python (Seu Escudo Digital)
🛡️ Your Digital Shield
"""
import argparse
import sys
import secrets
import hashlib
import math

def generate_password(length: int, mode: str = 'strong') -> str:
    """Gera uma senha com base no modo especificado."""
    
    # Caracteres ASCII seguros (sem ambiguidades)
    ASCII_SAFE_CHARS = (
        "23456789"  # Dígitos (excluindo 0 e 1)
        "ABCDEFGHJKLMNPQRSTUVWXYZ"  # Letras maiúsculas (excluindo I, O)
        "abcdefghijkmnpqrstuvwxyz"  # Letras minúsculas (excluindo l, o)
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    )
    
    # Caracteres Unicode seguros
    UNICODE_SAFE_CHARS = (
        "ΔΘΛΞΠΣΦΨΩ≠≤≥±∫∏√€₹₽₺←→↑↓↔↵¶§"
        "αβγδεζηθικλμνξοπρστυφχψω"
        "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    )
    
    # Caracteres seguros para modo bancário
    BANK_SAFE_CHARS = (
        "23456789"  # Dígitos (excluindo 0 e 1)
        "ABCDEFGHJKLMNPQRSTUVWXYZ"  # Letras maiúsculas (excluindo I, O)
        "abcdefghijkmnpqrstuvwxyz"  # Letras minúsculas (excluindo l, o)
    )
    
    if mode == 'bank':
        chars = BANK_SAFE_CHARS
    elif mode == 'ascii':
        chars = ASCII_SAFE_CHARS
    elif mode == 'paranoid':
        chars = ASCII_SAFE_CHARS  # Modo paranoico usa ASCII seguro
    else:  # strong (padrão)
        chars = ASCII_SAFE_CHARS + UNICODE_SAFE_CHARS
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def calculate_entropy(password: str, mode: str) -> float:
    """Calcula a entropia de uma senha."""
    
    # Determinar tamanho do charset baseado no modo
    ASCII_SAFE_CHARS = (
        "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?"
    )
    UNICODE_SAFE_CHARS = "ΔΘΛΞΠΣΦΨΩ≠≤≥±∫∏√€₹₽₺←→↑↓↔↵¶§αβγδεζηθικλμνξοπρστυφχψωАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"
    BANK_SAFE_CHARS = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz"
    
    if mode == 'bank':
        charset_size = len(BANK_SAFE_CHARS)
    elif mode == 'ascii':
        charset_size = len(ASCII_SAFE_CHARS)
    elif mode == 'paranoid':
        charset_size = len(ASCII_SAFE_CHARS)
    else:  # strong
        charset_size = len(ASCII_SAFE_CHARS + UNICODE_SAFE_CHARS)
    
    entropy = len(password) * math.log2(charset_size)
    return entropy

def estimate_brute_force_time(entropy_bits: float, guesses_per_second: int = 10**12) -> str:
    """Estima o tempo necessário para quebrar a senha por força bruta."""
    total_combinations = 2 ** entropy_bits
    seconds = total_combinations / (2 * guesses_per_second)
    
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
        else:
            return f"{years / 1000:.1f} thousand years"

def format_entropy_info(password: str, mode: str) -> str:
    """Formata informações de entropia para exibição."""
    entropy = calculate_entropy(password, mode)
    time_estimate = estimate_brute_force_time(entropy)
    
    info = (
        f"Length: {len(password)}\n"
        f"Estimated entropy: {entropy:.1f} bits\n"
        f"Brute-force resistance (10^12 guesses/s): {time_estimate}"
    )
    return info

def secure_overwrite(obj: str) -> None:
    """Sobrescreve seguramente uma string."""
    if isinstance(obj, str):
        temp_list = list(obj)
        for i in range(len(temp_list)):
            temp_list[i] = secrets.choice('abcdefghijklmnopqrstuvwxyz')
        ''.join(temp_list)

def main():
    parser = argparse.ArgumentParser(
        description="Aegur — Gerador de Senhas Offline (Seu Escudo Digital)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python3 Aegur.py                           # Modo forte (padrão)
  python3 Aegur.py --bank-mode --length 12
  python3 Aegur.py --ascii-only --length 20 --verbose
  python3 Aegur.py --paranoid-mode --length 16 --show-password
        """
    )
    
    parser.add_argument(
        '--ascii-only',
        action='store_true',
        help='Apenas caracteres ASCII seguros (sem ambiguidades)'
    )
    
    parser.add_argument(
        '--bank-mode',
        action='store_true',
        help='Modo ultra-conservador: apenas alfanumérico ASCII'
    )
    
    parser.add_argument(
        '--strong-mode',
        action='store_true',
        help='Modo forte: ASCII + símbolos Unicode seguros (padrão)'
    )
    
    parser.add_argument(
        '--paranoid-mode',
        action='store_true',
        help='Modo paranoico: sobrescrita segura e hash SHA3'
    )
    
    parser.add_argument(
        '--length',
        type=int,
        default=16,
        help='Comprimento da senha (padrão: 16)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Mostrar estatísticas de entropia'
    )
    
    parser.add_argument(
        '--show-password',
        action='store_true',
        help='Mostrar senha no modo paranoico (requer flag explícita)'
    )
    
    args = parser.parse_args()
    
    # Determinar o modo de geração
    if args.bank_mode:
        mode = 'bank'
    elif args.ascii_only:
        mode = 'ascii'
    elif args.paranoid_mode:
        mode = 'paranoid'
    else:
        mode = 'strong'  # padrão
    
    # Gerar senha
    password = generate_password(length=args.length, mode=mode)
    
    if args.paranoid_mode and not args.show_password:
        print("Modo paranoico ativado. Use --show-password para exibir a senha.")
        if args.verbose:
            sha3_hash = hashlib.sha3_256(password.encode()).hexdigest()
            print(f"SHA3-256 Hash: {sha3_hash}")
        secure_overwrite(password)
        return
    
    # Exibir senha
    print(password, end='')
    print()  # Nova linha após a senha
    
    # Estatísticas de entropia se solicitado
    if args.verbose:
        entropy_info = format_entropy_info(password, mode)
        print(entropy_info)
    
    # No modo paranoico, sobrescrever senha após exibição
    if args.paranoid_mode:
        secure_overwrite(password)

if __name__ == "__main__":
    main()