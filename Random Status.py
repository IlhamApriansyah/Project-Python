import random

Status		= ['Psatir','Psarkas','Wibu','Pengoding']
Greeting	= ['Yooo','hallo','Yahallo','Yahaha']
Gender		= ['Laki-laki','Perempuan','Ndak punya','LGBTQHD']
Job			= ['Sekolah','Guru anak tk','Pengacara','Hikkikomori']
Hobby		= ['Turu','Main game','Ngoprek']

print('Statusmu hari ini :\n')

def output():
	print('\n====== ' +	random.choice(Greeting) + ' =======')

	print('\n====== statusku ' +	random.choice(Status) + ' =======')

	print('\n====== kelaminku ' +	random.choice(Gender) + ' =======')

	print('\n====== dan aku punya hobby ' +	random.choice(Hobby) + ' =======')
	
	print('\n====== untuk saat ini, pekerjaanku ' +	random.choice(Job) + ' =======')

output()
