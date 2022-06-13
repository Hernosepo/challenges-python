# Given an array (arr) the function countSmileys
# should return the total number of smiling faces.

# Rules for a smiling face:

# Obligatorio: ojos  :    : or ;
# Opcional   : nariz :    - or ~
# Obligatorio: boca  :    ) or D

# Posibles = :) :-) :~) :D :-D :~D ;) ;-) ;~) ;D ;-D ;~D 

# No additional characters
# fonts validos = [":",";","-","~",")","D"]
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

def count_smileys(arr):
    count = 0

    ojos = [":", ";"]
    bocas = [")", "D"]
    narices = ["-", "~"]

    for llave, parte in enumerate(arr):
        if len(parte) == 2:
            if parte[0] in ojos and parte[1] in bocas:
                count += 1
        elif len(parte) == 3:
            if parte[0] in ojos and parte[1] in narices and parte[2] in bocas:
                count += 1
    return count



print(count_smileys([':D',':~)',';~D',':)'])) # 4 porque todas son validas
