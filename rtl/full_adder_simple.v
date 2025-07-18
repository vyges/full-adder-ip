//=============================================================================
// Full Adder - Simple XOR/AND Implementation
//=============================================================================
// Description: Full adder using direct XOR and AND gate implementation.
//              Most basic approach with minimal gate count.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

`timescale 1ns/1ps

module full_adder_simple (
    input  logic clk_i,     // Clock input (for UVM compatibility)
    input  logic reset_n_i, // Active low reset (for UVM compatibility)
    input  logic a_i,       // First input bit
    input  logic b_i,       // Second input bit
    input  logic cin_i,     // Carry input from previous stage
    output logic sum_o,     // Sum output
    output logic cout_o     // Carry output to next stage
);

    // Sum = A XOR B XOR Cin (three-input XOR)
    assign sum_o = a_i ^ b_i ^ cin_i;
    
    // Cout = (A AND B) OR ((A XOR B) AND Cin)
    // This can be broken down as:
    // - Generate: A AND B (when both A and B are 1)
    // - Propagate: (A XOR B) AND Cin (when exactly one of A or B is 1, and Cin is 1)
    assign cout_o = (a_i & b_i) | ((a_i ^ b_i) & cin_i);

endmodule 