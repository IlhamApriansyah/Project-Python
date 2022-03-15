hobi = []
stop = False
i = 0

#mengisi hobi
while(not stop):
    hobi_baru = raw_input("Masukan hobi mu yang ke-{}: ".format(i))
    hobi.append(hobi_baru)

    i += 1

    tanya = raw_input("Mau diisi lagi? (y/t): ")
    if(tanya == "t"):
        stop = True

#cetak semua hobi
print "=" * 10
print "Kamu memiliki {} hobi".format(len(hobi))

for hb in hobi:
    print "- {}".format(hb)
