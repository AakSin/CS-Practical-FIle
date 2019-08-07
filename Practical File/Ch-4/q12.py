st="hello mello is tello is"
st=st.lower()
ac=ec=ic=uc=oc=0
for i in st:
    if i=="a":
        ac+=1
    elif i=="e":
        ec+=1
    elif i=="o":
        oc+=1
    elif i=="i":
        ic+=1
    elif i=="u":
        uc+=1
print("a appaers",ac,"times")
print("e appaers",ec,"times")
print("i appaers",ic,"times")
print("o appaers",oc,"times")
print("u appaers",uc,"times")
