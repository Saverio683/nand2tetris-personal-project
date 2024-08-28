// The inputs of this program are the current values stored in R0 and
// R1 (i.e., the two top RAM locations). The program computes the product R0*R1 and stores the result in
// R2. We assume (in this program) that R0>=0, R1>=0, and R0*R1<32768. Your program need not test
// these conditions, but rather assume that they hold. The supplied Mult.tst and Mult.cmp scripts will test
// your program on several representative data values.
    @0      // Carica l'indirizzo di RAM[0], il secondo fattore
    D=M     // Salvo il valore di RAM[0] in D
    @END
    D;JEQ   // Se RAM[0] = 0, termina
    @a
    M=D     // a = RAM[0]
    @i      // contatore
    M=D     // i = a
(LOOP)
    @i
    D=M     // D = i
    @END
    D;JEQ   //If i = 0 goto END
    @1
    D=M     // D = RAM[1]
    @2
    M=M+D
    @i
    M=M-1   //i--
    @LOOP
    0;JMP
(END)
    @END
    0;JMP