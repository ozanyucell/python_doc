friends = ["Cem", "Sinem", "Ceren", "Ege"]
family = ["Arda", "Ares", "Dogan", "Ferda"]

if "Ceren" in family:       #False
    print("This is not going to be printed.")
elif "Arda" in friends:     #False
    print("This is not going to be printed.")
elif "Sinem" in family:     #False
    print("This is not going to be printed.") 
else:
    print("This is going to be printed.")