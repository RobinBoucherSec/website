# -*- coding: utf-8 -*-
"""
Outil de chiffrement Vigenère - Version avec améliorations
=========================================================
Fonctionnalités :
- Chiffrement Vigenère classique
- Amélioration Niveau 1 : Inversion du texte
- Amélioration Niveau 2 : Ajout de padding aléatoire
- Amélioration Niveau 3 : Double chiffrement avec clé transformée
"""

def vigenere_chiffrer(texte_clair: str, cle: str) -> str:
    """
    Chiffre un texte avec le chiffrement de Vigenère.
    ## Version classique utilisant une clé répétée.
    """
    ciphertext = []
    cle_repetee = (cle * (len(texte_clair) // len(cle) + 1)).lower()
    idx_cle = 0
    for char in texte_clair:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(cle_repetee[idx_cle]) - ord('a')
            chiffrer_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + base)
            ciphertext.append(chiffrer_char.upper())
            idx_cle += 1
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def vigenere_ameliorer_chiffrement(texte_clair: str, cle: str, niveau_securite: int = 1) -> str:
    """
    Chiffre avec des améliorations de sécurité selon le niveau choisi.
    ## Options :
    - Niveau 1 : Inversion du texte
    - Niveau 2 : Padding aléatoire
    - Niveau 3 : Double chiffrement avec clé transformée
    """

    ### AMÉLIORATION NIVEAU 1 : INVERSION DU TEXTE AVANT CHIFFREMENT
    if niveau_securite == 1:
        texte_inverse = texte_clair[::-1]  # Inverser le message
        return vigenere_chiffrer(texte_inverse, cle)

    ### AMÉLIORATION NIVEAU 2 : AJOUT DE CARACTÈRES DE PADDING ALÉATOIRES
    elif niveau_securite == 2:
        texte_inverse = texte_clair[::-1]
        texte_chiffre = vigenere_chiffrer(texte_inverse, cle)
        
        import random
        chars_padding = '!@#$%^&*()_+-=[]{}|;:,.<>?'
        resultat = []
        i = 0
        while i < len(texte_chiffre):
            taille_chunk = random.randint(3, 5)
            chunk = texte_chiffre[i:i+taille_chunk]
            resultat.append(chunk)
            if i + taille_chunk < len(texte_chiffre):
                resultat.append(random.choice(chars_padding))
            i += taille_chunk
        return ''.join(resultat)

    ### AMÉLIORATION NIVEAU 3 : DOUBLE CHIFFREMENT AVEC CLÉ TRANSFORMÉE
    elif niveau_securite == 3:
        premier_passage = vigenere_chiffrer(texte_clair, cle)

        # Transformation de la clé : inversion + décalage de +1 sur chaque caractère
        cle_transformee = ''.join(
            chr((ord(c.lower()) - ord('a') + 1) % 26 + ord('a'))
            for c in cle[::-1]
        )

        # Deuxième passage de chiffrement avec la clé modifiée
        return vigenere_chiffrer(premier_passage, cle_transformee)

    else:
        raise ValueError("Niveau de sécurité invalide. Utiliser 1, 2 ou 3.")

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Le chiffrement de Vigenère est une méthode polyalphabétique."
    cle = "securite"

    print("=== CHIFFREMENT CLASSIQUE ===")
    print(vigenere_chiffrer(texte, cle))

    print("
=== AMÉLIORATION NIVEAU 1 (INVERSION) ===")
    print(vigenere_ameliorer_chiffrement(texte, cle, 1))

    print("
=== AMÉLIORATION NIVEAU 2 (PADDING ALÉATOIRE) ===")
    print(vigenere_ameliorer_chiffrement(texte, cle, 2))

    print("
=== AMÉLIORATION NIVEAU 3 (DOUBLE CHIFFREMENT) ===")
    print(vigenere_ameliorer_chiffrement(texte, cle, 3))