
# # String
# nomeInstrumento = 'Guitarra Eletrica'
# print(nomeInstrumento)

# # Caracters de Escape
# resenhaDoFilme = "O filme doi \"demais!\""
# resenhaDoFilme2 = "O filme foi \"demais!\""
# resenhaDoFilme3 = "O filme foi \ndemais!" # Quebra a linha \n
# minhasFotos = "meu computador\\fotos\\minhas fotos" # melhor pra direcao no windows
# print(resenhaDoFilme)
# print(resenhaDoFilme2)
# print(resenhaDoFilme3)
# print(minhasFotos)
# ########################################
a = "Diego"
b = "Lucas "
co= a + b 
print (co)
#len tamanho de uma variavel
tamanho = len(co)
print(tamanho)
# # metodos com string

print(co.lower())  #converter para minusculo
print(co.upper())  #converter para maiusculo
print(co.strip())  #remover caractere especial
 
string = " O Rato roeu a roupa do rei de roma"  
lista = string.split(" ") #Quebra por espacos ou letras
print(lista)                     

busca = string.find("rei") #busca
print(busca)   

string.replace("rei", "rainha")