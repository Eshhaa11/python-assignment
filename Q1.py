def even_index(word):
    i = 0
    while i < len(word):
        print(word[i], end='')
        i = i + 2 
    print()  
    
even_index("DoctorPhenomenal") 
even_index("Geeks")
