import os
#PROGRAM PEMESANAN KAMAR HOTEL



def print_menu():
	print(1* "-")
	print("		    ")
	print("			  SELAMAT DATANG DI HOTEL")
	print("		    ")
	print("				ALEXANDRA")
	print("		    ")
	print("	Jl.Kota Baru NO.174,Kode Pos 771447 No Hp. 0896-3622-8978 ")
	print("	                 Pontianak Kalimantan Barat")
	print("	     ")
	print("			Hotel ALEXANDRA Menyediakan :")
	print("	     ")
	print("		~ Kenyamanan")
	print("		~ Ketenangan")
	print("		~ Kebersihan Yang Terjamin")
	print("		~ Serta Tempat Berkumpul Yang Nyaman")
	print("")
	print(80* "-")
	print('Silahkan Mengisi Pilihan Yang Anda Inginkan ?')
	print("	     ")
	print(' 	1.Masuk')
	print('	2.Keluar')
	print("	     ")
loop=True
while loop:	
	print_menu()
	pilihan=int(input("Masukkan Pilihan[1/2]: "))
	print(1* "-")
	os.system('cls')
	if (pilihan==1) :
		print("	     ")
		print("                         SILAHKAN MASUKKAN BIODATA ANDA")
		print(80* "-")
		print("	     ")
		nama=input("Masukkan Nama Anda		: ").upper()
		nohp=input("Masukkan No Hp Anda		: (0896)")
		if len(nohp)!=7 and len(nohp)!=8:
			os.system('cls')
			input("No Hp Anda Tidak Terdaftar")
			continue
		ktp=input("Masukkan No Induk Keluarga	: ")
		tl=input("Masukkan Tempat Lahir Anda	: ").upper()
		tt=input("Masukkan Tanggal Lahir Anda	: ")
		print("	     ")	
		os.system('cls')
	elif (pilihan==2):
		exit()
	else:
		print("Pilihan Yang Anda Masukkan Salah Silahkan Coba Lagi")
		continue
	print("	     ")
	print("                 SILAHKAN MENGISI TIPE KAMAR YANG ANDA INGINKAN ")
	print(80* "-")
	print("	     ")
	print("1. Single Room")
	print("2. Twin Room")
	print("3. Double Room")
	print("4. Triple Room")
	print("	     ")
	
	tipe=int(input("Masukkan Tipe Kamar Yang Anda Pilih : "))
	os.system('cls')
	
	if (tipe==1) :
		kamar ="Single Room"
		tarif =["500.000","1.000.000","1.500.000","2.000.000","2.500.000","3.000.000","3.500.000"]
		print("       SILAHKAN MENGISI BERAPA LAMA ANDA INGIN MENGINAP DIHOTEL KAMI")
		print(80* "-")
		waktu =int(input("Masukkan Berapa Hari Anda Ingin Menginap : "))
		os.system('cls')
		if (waktu==1):
			tarif2=tarif[0]
		elif (waktu==2):
			tarif2=tarif[1]
		elif (waktu==3):
			tarif2=tarif[2]
		elif (waktu==4):
			tarif2=tarif[3]
		elif (waktu==5):
			tarif2=tarif[4]
		elif (waktu==6):
			tarif2=tarif[5]
		elif (waktu==7):
			tarif2=tarif[6]
		else :
			os.system('cls')
			print("Waktu yang Anda Isi Salah")
			continue
		
	elif (tipe==2) :
		kamar ="Twin Room"
		tarif =["1.000.000","1.500.000","2.000.000","2.500.000","3.000.000","3.500.000","4.000.000"]
		print("       SILAHKAN MENGISI BERAPA LAMA ANDA INGIN MENGINAP DIHOTEL KAMI")
		print(80* "-")
		waktu =int(input("Masukkan Berapa Hari Anda Ingin Menginap: "))
		os.system('cls')
		if (waktu==1):
			tarif2=tarif[0]
		elif (waktu==2):
			tarif2=tarif[1]
		elif (waktu==3):
			tarif2=tarif[2]
		elif (waktu==4):
			tarif2=tarif[3]
		elif (waktu==5):
			tarif2=tarif[4]
		elif (waktu==6):
			tarif2=tarif[5]
		elif (waktu==7):
			tarif2=tarif[6]
		os.system('cls')
		
	elif (tipe==3) :
		kamar ="Double Room"
		tarif =["1.500.000","2.000.000","2.500.000","3.000.000","3.500.000","4.000.000","4.500.000"]
		print("       SILAHKAN MENGISI BERAPA LAMA ANDA INGIN MENGINAP DIHOTEL KAMI")
		print(80* "-")
		waktu =int(input("Masukkan Berapa Hari Anda Ingin Menginap: "))
		os.system('cls')
		if (waktu==1):
			tarif2=tarif[0]
		elif (waktu==2):
			tarif2=tarif[1]
		elif (waktu==3):
			tarif2=tarif[2]
		elif (waktu==4):
			tarif2=tarif[3]
		elif (waktu==5):
			tarif2=tarif[4]
		elif (waktu==6):
			tarif2=tarif[5]
		elif (waktu==7):
			tarif2=tarif[6]
		os.system('cls')
		
	elif (tipe==4) :
		kamar ="Triple Room"
		tarif =["2.000.000","2.500.000","3.000.000","3.500.000","4.000.000","4.500.000","5.000.000"]
		print("       SILAHKAN MENGISI BERAPA LAMA ANDA INGIN MENGINAP DIHOTEL KAMI")
		print(80* "-")
		waktu =int(input("Masukkan Berapa Hari Anda Ingin Menginap: "))
		os.system('cls')
		if (waktu==1):
			tarif2=tarif[0]
		elif (waktu==2):
			tarif2=tarif[1]
		elif (waktu==3):
			tarif2=tarif[2]
		elif (waktu==4):
			tarif2=tarif[3]
		elif (waktu==5):
			tarif2=tarif[4]
		elif (waktu==6):
			tarif2=tarif[5]
		elif (waktu==7):
			tarif2=tarif[6]
		os.system('cls')
		
	else :
		print("Pilihan Yang Anda Pilih Salah Silahkan Coba Lagi")
		continue
		
		break
	#Ini adalah Hasil
	
	print("")
	print("		    ")
	print("			KWITANSI PEMBAYARAN PEMESANAN HOTEL")
	print(80* "-")
	print("")
	print("		Nama			: " + str(nama))
	print("")
	print("		No Hp 			: (0896)" + str(nohp))
	print("")
	print("		No Induk Keluarga	: " +str(ktp))
	print("")
	print("		Tempat Tanggal Lahir	: " +str(tl) +","+str(tt))
	print("")
	print("		Tipe Kamar 		: " +str(kamar))
	print("")
	print("		Waktu 			: " +str(waktu)+" Malam ")
	print("")
	print("		Biaya 			: " +"Rp."+str(tarif2)+",00-")
	print("")
	print("		Silahkan Anda Membayar Di BANK Terdekat")
	print("")
	print("")
	print("Terima Kasih Atas Kepercayaan Yang Anda Berikan Kepada Kami,Semoga Anda Senang.")
	print("")
	print("	Mohon Maaf Hotel Kami Melayani Pemesanan Kamar Hanya 7 Malam.")
	print("")
	print(80* "-")
	x=''
	while x!='y' and x!='t':
		x=input("Apakah Anda Ingin Memesan Kamar Lagi [Y/T] : ")	
		if x=='y':
			os.system('cls')
			print("Silahkan Pilih Lagi")
		elif x=='t':
			os.system('cls')
			print("Terima Kasih")
		
exit()
