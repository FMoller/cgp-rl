#$ -S /bin/bash

problema=(C17 cm42a cm82a cm138a)
genmax=(3000000 3200000 2000000 4800000)
tamanho=(100 100 100 100)
semente=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26)
for j in 0 1 2 3
do
	for i in 0 2 4 6 8 10 12 14 16 18 20 22 24
	do
		echo "Solving problem:${problema[j]} with SAM - seed:${semente[i]}"
		./bin/cgp tables/${problema[j]}.ep seed=${semente[i]} ncol=${tamanho[j]} maxgen=${genmax[j]} mutation=1 resultados/${problema[j]}_${semente[i]} &
		./bin/cgp tables/${problema[j]}.ep seed=${semente[i+1]} ncol=${tamanho[j]} maxgen=${genmax[j]} mutation=1 resultados/${problema[j]}_${semente[i+1]}
	done
done