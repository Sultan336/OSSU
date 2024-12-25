@0             // Load the address of register R0 into the memory address register (MAR)
   D=M             // Read the value stored in register R0 and store it in the D register 
   @INFINITE_LOOP  // Load the address of the label "INFINITE_LOOP" into the MAR
   D;JLE            // If D (the value from R0) is less than or equal to 0, jump to the label "INFINITE_LOOP" 
   @counter        // Load the address of the memory location "counter" into the MAR 
   M=D             // Store the value in D (height of the rectangle) into the "counter" memory location
   @SCREEN         // Load the address of the screen memory into the MAR
   D=A             // Store the address of the screen memory in the D register
   @address        // Load the address of the memory location "address" into the MAR
   M=D             // Store the screen memory address in the "address" memory location

(LOOP)
   @address        // Load the address of the "address" memory location into the MAR
   A=M             // Load the value stored in "address" (current screen memory address) into the accumulator
   M=-1             // Store -1 (black pixel) in the memory location pointed to by the accumulator
   @address        // Load the address of the "address" memory location into the MAR
   D=M             // Load the current screen memory address from "address" into the D register
   @32             // Load the immediate value 32 into the MAR
   D=D+A             // Add 32 (width of the screen in pixels) to the current address
   @address        // Load the address of the "address" memory location into the MAR
   M=D             // Store the updated address (next line of the rectangle) in the "address" memory location
   @counter        // Load the address of the "counter" memory location into the MAR
   MD=M-1             // Decrement the counter by 1
   @LOOP            // Load the address of the label "LOOP" into the MAR
   D;JGT            // If the counter is greater than 0, jump back to the label "LOOP"

(INFINITE_LOOP)
   @INFINITE_LOOP  // Load the address of the label "INFINITE_LOOP" into the MAR
   0;JMP            // Unconditionally jump to the label "INFINITE_LOOP" (infinite loop) 
