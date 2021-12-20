Challenge Prompt - 
```py

pt=int(flag.hex(),16)

def gen():
    p,q=getPrime(512),getPrime(512)
    e,n=65537,p*q
    ct=pow(pt,e,n)
    d=pow(e,-1,(p-1)*(q-1))
    return ct,d,n,[p,q]

if __name__ == '__main__':
    ct,d1,n,pq=gen()
    print(pq)
    d2=int(input("> "))
    if d2!=d1:
        if pow(ct,d2,n)==pt:
            print(f"Good Job!!\n{flag.decode()}")
        else:
            print("bruh")
    else:
        print("Are you for real??")        
```

So This looks just like a normal RSA except for the fact that we cannot use decrypting key as d which is generall calculated as `d = pow(e,-1,phi)`. So we just need to find some other number say d' which also satisfies `d'.e = 1 mod phi(n)`

so now we can either add something which gives 0 under mod phi like `d' = d+k*phi(n) so here e.d' = e.(d+k*phi(n)) mod phi(n)` which is `e.d + e.k.phi(n) mod phi(n)` which is indeed  `1`.

Or we can multiply something which gives 1 under mod phi like `d' = d*(something) so that ed' = 1 mod phi(n) ` 
so we already know such a number i.e `e*d`. so we can choose `something = (e.d)^j` hence for `j=1` `d' = d.e.d or d^2.e` we could have chosen any number for j and got `somthing = d^(j+1)*e^(j)` here 

we can also combine these 2 to find more numbers which can decrypt our message.
Hence
`decrypting key = d.(ed)^(j)+phi(n)*k` where we can chose any j,k