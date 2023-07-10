def text(data):

    data=data.replace('\n',' ')
    data=data.lower()
    alpha='abcdefghijklmnopqrstuvwxyz ' 

    main_text=''

    for i in range(len(data)):
        if(data[i] in alpha):
            main_text+=str(data[i])
    
    mod=[x for x in main_text.split()]
    f=open("word.txt","w")

    for i in range(len(mod)):
        f.write(mod[i])
        f.write("\n")
        f.flush()
    return


def gcd(prime1,prime2):
    if(prime2>prime1):
        prime1,prime2=prime2,prime1
    
    while(prime2!=0):
        temp=prime1
        prime1=prime2
        prime2=temp%prime2
    return(prime1)

#finding the public key

def public_key(prime1,prime2):
    n=(prime1)*(prime2)

    # how many no. are coprime with the product between 1 and product
    coprime=(prime1-1)*(prime2-1)
    possiblekeys=[]

    k=0
    for i in range(2,coprime):
        if(gcd(i,coprime)==1):
            if(gcd(i,n)==1):
                k+=1
                possiblekeys.append(i)
                if(k>20):
                    break
    return(possiblekeys)

def encrypt(prime1,prime2,key,index):
    product=prime1*prime2
    # new_index is the formula for encryption
    new_index=(index**key)%product
    return(new_index)

def cipher_encrypt(prime1,prime2,key_new,plaindata):
    final_encrypt=''
    alpha='abcdefghijklmnopqrstuvwxyz'
    plaindata=plaindata.replace('/n',' ')

    for i in range(len(plaindata)):

        if(plaindata[i] in alpha):
            c=alpha.index(plaindata[i])
            c=encrypt(prime1,prime2,key_new,c)
            final_encrypt+=str(c)+','
        else:
            final_encrypt+=str(plaindata[i])
    
    l=[x for x in final_encrypt.split()]

    f=open("encrypt_data.txt",'w')
    for i in range(len(l)):
            f.write(l[i])
            f.write("\n")
    f.flush()
    return

def private_key(prime1,prime2,encryption_key):
    coprime=(prime1-1)*(prime2-1)

    #Range has been set so as to remove the obvious wrong answers
    for i in range(coprime//encryption_key,coprime):
        temp=(encryption_key*i)%coprime
        if(temp==1):
            pivot=i
            break
    
    decryption_keys=[]	# for storing the possible decrypted keys

    for i in range(20):
        decryption_keys.append(coprime*i+pivot)
    return(decryption_keys)

def decrypt_this(prime1,prime2,key,index):
	product=prime1*prime2
	index=int(index)
	new_index=(index**key)%product 	#This is RSA formula for decryption
	return new_index

def plain_encrypt(encrypted_data,prime1,prime2,key2_select):
    alpha="abcdefghijklmnopqrstuvwxyz"
    encrypted_data=encrypted_data.replace('\n',' ')

    decrypted_data=''
    temp=[x for x in encrypted_data.split()]

    for i in range(len(temp)):
        temp1=[x for x in temp[i].split(',')]
        temp1.pop(len(temp1)-1)
        for j in range(len(temp1)):
            new_index=decrypt_this(prime1,prime2,key2_select,temp1[j])
            decrypted_data+=str(alpha[new_index])
        decrypted_data=decrypted_data+'\n'
    
    l=[x for x in decrypted_data.split()]
    f=open("data_decrypted.txt","w")
    for i in range(len(l)):
        f.write(l[i])
        f.write("\n")
        f.flush()
    return