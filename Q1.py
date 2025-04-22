def even_index_chars(word):
    i = 0
    while i < len(word):
        print(word[i], end='')
        i = i + 2 
    print()  
even_index_chars("DoctorPhenomenal") 
even_index_chars("Geeks")
