i=0
j=0
while i>=0 and i<=10:
    while j>=0 and j<=10:
        carpim=i*j
        print(i, "*", j, "=" ,carpim)
        j=j+1
    i=i+1
    j=0 #eğer bunu yazmazsan i=0 dan sonraki değerlerde j hep 11 olur ve j döngüsüne girmez ve sadece 0 ın çarpım tablosunu yazdırır.



