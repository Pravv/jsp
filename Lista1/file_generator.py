from subprocess import call

for i in range(40):
	if i == 0: continue;
	call('touch zad'+str(i)+".py")