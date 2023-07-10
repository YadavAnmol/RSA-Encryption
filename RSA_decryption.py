import RSA_functions

print("choose 2 prime no2 and  the public key that you have")
inputt=input()
P1,P2,key_select=inputt.split()
P1,P2,key_select=int(P1),int(P2),int(key_select)

print("for the given public key the following private keys are available")
print(RSA_functions.private_key(P1,P2,key_select))

new_key=int(input())

print("You have selected",new_key,P1*P2,"as your private key")

b=open("encrypt_data.txt","r")
b=b.read()
RSA_functions.plain_encrypt(b,P1,P2,new_key)
print("success")

