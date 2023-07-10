import RSA_functions

print("Choose the prie no.s here")
inputt=input()
p1,p2=inputt.split()
p1,p2=int(p1),int(p2)

possible_keys=RSA_functions.public_key(p1,p2)

#choose any key from possible_keys
print(possible_keys)

key_select=int(input("What ky do you want to selct?"))

a=open("sample_text.txt","r")
a=a.read()
# print(a)

RSA_functions.text(a)

b=open("word.txt","r")
b=b.read()

RSA_functions.cipher_encrypt(p1,p2,key_select,b)
print("success")
