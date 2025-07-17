//=============================================================================
// Full Adder - Carry Lookahead Implementation
//=============================================================================
// Description: Full adder using propagate and generate logic for optimal
//              performance and scalability to multi-bit adders.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

module full_adder (
    input  logic clk_i,     // Clock input (for UVM compatibility)
    input  logic reset_n_i, // Active low reset (for UVM compatibility)
    input  logic a_i,       // First input bit
    input  logic b_i,       // Second input bit
    input  logic cin_i,     // Carry input from previous stage
    output logic sum_o,     // Sum output
    output logic cout_o     // Carry output to next stage
);

    // Internal signals
    logic p;   // Propagate signal: P = A XOR B
    logic g;   // Generate signal: G = A AND B
    logic c1;  // Intermediate carry signal

    // Combinational logic (not clocked for full adder)
    // Propagate signal: P = A XOR B
    assign p = a_i ^ b_i;
    
    // Generate signal: G = A AND B
    assign g = a_i & b_i;
    
    // Intermediate carry: C1 = G OR (P AND Cin)
    assign c1 = g | (p & cin_i);
    
    // Sum output: Sum = P XOR Cin
    assign sum_o = p ^ cin_i;
    
    // Carry output: Cout = C1
    assign cout_o = c1;

endmodule
