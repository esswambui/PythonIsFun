def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.islower ():
                translation = translation + "ess"
            elif letter.isupper ():
                translation = translation + "ESS"
        else:
         translation = translation + letter
    return translation

print ( translate (input ("Enter aphrase ")))


