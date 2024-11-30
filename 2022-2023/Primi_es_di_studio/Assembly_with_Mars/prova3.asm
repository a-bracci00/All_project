#selezioniamo il massimo da un vettore
.globl main

.data
	vector: .word 4,3,-5,500
	rez: .word 0

.text

main:
	#carichiamo i valori della memoria nei registri
	lw $t0, vector		#A
	lw $t1, vector + 4	#B
	lw $t2, vector + 8	#C
	lw $t3, vector + 12	#D

	#assumiamo che il massimo è $st0 e testiamo questa ipotesi finchè non diventa vero
	blt $t1, $t0, checkC
	move $t0, $t1
	#j checkC
checkC:
	blt $t2, $t0, end
	move $t0, $t3
	#j end
checkD:
	blt $t3, $t0, end
	move $t0, $t3
	#j end
end:
	sw $t0, rez
	
	