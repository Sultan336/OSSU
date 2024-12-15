🚀 **Explaining CPU.hdl Step-by-Step**
--------------------------------------

The **CPU** (Central Processing Unit) is like the **brain** 🧠 of the computer. It executes instructions and coordinates actions with memory and other components. Let’s break it down into its core parts and how they work together.

### 📝 **Instruction Types**

The CPU executes two types of instructions:

1.  **A-Instruction (instruction\[15\] = 0)**:
    
    *   Sets a value in the **A Register** (address or constant).
        
2.  **C-Instruction (instruction\[15\] = 1)**:
    
    *   Performs computations using the **ALU**.
        
    *   Can store results in **A**, **D**, or **memory (M)**.
        
    *   Can also decide whether to jump to a new instruction.
        

### 🧩 **Parts of the CPU**

#### 1️⃣ **Instruction Decoder**

*   Splits the input instruction into **A-instruction** or **C-instruction**.
    
*   If the first bit (instruction\[15\]) is:
    
    *   **0**: It’s an A-instruction.
        
    *   **1**: It’s a C-instruction.
        
*   Example:
    
    *   0000000000010101 → A-instruction: Load **21** into the A Register.
        
    *   1110110000010000 → C-instruction: Compute **D = D + 1**.
        

#### 2️⃣ **Registers (A and D)**

*   **A Register 🗂️**:
    
    *   Stores an address or a constant value.
        
    *   Can also hold the target address for memory operations or jumps.
        
    *   Connected to the **Memory Address Output (addressM)**.
        
*   **D Register 📥**:
    
    *   Holds a value for computations.
        
    *   Used for temporary storage in calculations.
        

#### 3️⃣ **ALU (Arithmetic Logic Unit)**

*   The **ALU** is like a super-calculator 🧮 that performs:
    
    *   Math: Add, subtract, etc.
        
    *   Logic: AND, OR, NOT, etc.
        
*   Inputs:
    
    *   **D Register (x)**.
        
    *   **A Register or Memory (y)**.
        
*   Outputs:
    
    *   **Result (outM)**.
        
    *   Flags:
        
        *   **Zero (zr)**: True if result is 0.
            
        *   **Negative (ng)**: True if result is negative.
            

#### 4️⃣ **Program Counter (PC) 📍**

*   The PC decides the **next instruction** to execute.
    
*   Behaviors:
    
    *   Increment to the next instruction.
        
    *   Jump to a new instruction (if specified in C-instruction).
        
    *   Reset to **0** when reset=1.
        

### ⚙️ **How It All Works Together**

1.  **Fetch**:
    
    *   The CPU gets an instruction from memory.
        
2.  **Decode**:
    
    *   If it’s an A-instruction, load the value into the A Register.
        
    *   If it’s a C-instruction, configure the ALU and decide the next step.
        
3.  **Execute**:
    
    *   Perform the computation using the ALU.
        
4.  **Write Back**:
    
    *   Save the result to D, A, or Memory.
        
5.  **Jump**:
    
    *   If a jump condition is true, update the PC to a new address.
        

### 🎮 **Example Walkthrough**

#### Instruction Sequence:

1.  **@5**: A-instruction → Load **5** into A Register.
    
2.  **D=A**: C-instruction → Set **D = 5**.
    
3.  **@10**: A-instruction → Load **10** into A Register.

4.  D=D+A: C-instruction → Add D (5) and A (10) → D = 15.

### **Real-World Analogy**

Think of the Hack CPU as the brain of a small robot:

*   **ARegister**: The robot's map, pointing to specific locations in its memory.
    
*   **DRegister**: The robot's notebook, storing intermediate results or data for ongoing tasks.
    
*   **ALU**: The calculator, performing operations like addition or comparisons.
    
*   **Program Counter (PC)**: The robot's step tracker, determining what it should do next.
  
