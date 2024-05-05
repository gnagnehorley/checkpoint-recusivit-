def est_palindrome(mot):
    # Fonction récursive pour vérifier si le mot est un palindrome
    def est_palindrome_rec(mot):
        # Condition d'arrêt : un mot vide ou un mot contenant un seul caractère est un palindrome
        if len(mot) <= 1:
            return True
        # Comparaison des caractères situés aux extrémités du mot
        if mot[0] == mot[-1]:
            # Si les caractères sont égaux, on teste le reste du mot
            return est_palindrome_rec(mot[1:-1])
        else:
            # Si les caractères sont différents, le mot n'est pas un palindrome
            return False

    # Appel de la fonction récursive pour vérifier si le mot est un palindrome
    return est_palindrome_rec(mot)

# Exemples d'utilisation
print(est_palindrome("radar"))  # Devrait afficher True
print(est_palindrome("hello"))  # Devrait afficher False
print(est_palindrome("level"))  # Devrait afficher True