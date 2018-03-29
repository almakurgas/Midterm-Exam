"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def uvelikaslova(recenica):
    nova_recenica = ""
    for karakter in recenica:
        broj_slova = ord(karakter)
        if broj_slova > 96 and broj_slova < 123:
            broj_velikog_slova = broj_slova -32
            karakter = chr(broj_velikog_slova)

        nova_recenica = nova_recenica + karakter
    return nova_recenica
recenica = input("Unesite recenicu:")
recenica_velikim_slovima= uvelikaslova(recenica)
print(recenica_velikim_slovima)






def main():
    # Test your function here
    pass

main()
