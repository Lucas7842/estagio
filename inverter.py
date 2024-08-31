def inverter_string(s):
    
    string_invertida = ""
  
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida
string_original = "Galadriel"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
