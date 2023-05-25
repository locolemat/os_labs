#!/usr/bin/zsh

gcc -S ./reverse/my_reverse.c -o ./reverse/asm/my_reverse.o
gcc -S ./reverse/input_reverse.c -o ./reverse/asm/input_reverse_0.o
gcc -S ./reverse/input_reverse.c -o ./reverse/asm/input_reverse_1.o -O1
gcc -S ./reverse/input_reverse.c -o ./reverse/asm/input_reverse_2.o -O2
gcc -S ./reverse/input_reverse.c -o ./reverse/asm/input_reverse_3.o -O3
gcc -S ./reverse/input_reverse.c -o ./reverse/asm/input_reverse_FAST.o -Ofast
gcc -S ./reverse/input_reverse.c -o ./reverse/asm/input_reverse_SIZE.o -Oz
gcc -S ./fahr/fahr.c -o ./fahr/asm/fahr_0.o
gcc -S ./fahr/fahr.c -o ./fahr/asm/fahr_1.o -O1
gcc -S ./fahr/fahr.c -o ./fahr/asm/fahr_0.o -O2
gcc -S ./dasam/dasam.c -o ./dasam/asm/dasam_0.o
gcc -S ./dasam/dasam.c -o ./dasam/asm/dasam_1.o -O1
gcc -S ./dasam/dasam.c -o ./dasam/asm/dasam_2.o -O2
gcc -S ./dasam/dasam.c -o ./dasam/asm/dasam_3.o -O3
