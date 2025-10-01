#!/usr/bin/env python3
"""
Aegur — Gerador de Senhas Offline em Python (Seu Escudo Digital)
🛡️ Your Digital Shield
"""
import argparse
import sys
import secrets
import hashlib
from typing import List, Tuple
from generators import generate_password, secure_overwrite
from charsets import (
    ASCII_SAFE_CHARS,
    UNICODE_SAFE_CHARS,
    BANK_SAFE_CHARS,
    AMBIGUOUS_CHARS
)
from entropy import calculate_entropy, format_entropy_info

def main():
    parser = argparse.ArgumentParser(
        description="Aegur — Gerador de Senhas Offline (Seu Escudo Digital)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python aegur.py                           # Modo forte (padrão)
  python aegur.py --bank-mode --length 12
  python aegur.py --ascii-only --length 20 --verbose
  python aegur.py --paranoid-mode --length 16 --show-password
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
            # Calcular hash SHA3 para auditoria
            sha3_hash = hashlib.sha3_256(password.encode()).hexdigest()
            print(f"SHA3-256 Hash: {sha3_hash}")
        # Sobrescrever senha após uso
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