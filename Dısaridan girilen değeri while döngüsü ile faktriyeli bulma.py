i=1
carpim=1
fak=int(input("faktöriyelini bulmak istediğiniz sayiyi giriniz"))
while True:
    if i < fak:
        i=i+1
        carpim=carpim*i
    else:
        print(carpim)
        break
