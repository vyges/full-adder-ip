//=============================================================================
// Half Adder Module
//=============================================================================
// Description: Basic half adder module for modular full adder implementation.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

module half_adder (
    input  logic a_i,     // First input bit
    input  logic b_i,     // Second input bit
    output logic sum_o,   // Sum output
    output logic cout_o   // Carry output
);

    // Half adder logic: Sum = A XOR B, Cout = A AND B
    assign sum_o = a_i ^ b_i;
    assign cout_o = a_i & b_i;

endmodule

//=============================================================================
// Full Adder - Half Adder Modular Implementation
//=============================================================================
// Description: Full adder using two half adder modules for modular design.
//              Provides clear hierarchical structure and reusability.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

`timescale 1ns/1ps

module full_adder_half_adder (
    input  logic clk_i,     // Clock input (for UVM compatibility)
    input  logic reset_n_i, // Active low reset (for UVM compatibility)
    input  logic a_i,       // First input bit
    input  logic b_i,       // Second input bit
    input  logic cin_i,     // Carry input from previous stage
    output logic sum_o,     // Sum output
    output logic cout_o     // Carry output to next stage
);

    // Internal signals
    logic sum1;    // Sum from first half adder
    logic cout1;   // Carry from first half adder
    logic cout2;   // Carry from second half adder

    // First half adder: A + B
    half_adder ha1 (
        .a_i(a_i),
        .b_i(b_i),
        .sum_o(sum1),
        .cout_o(cout1)
    );

    // Second half adder: sum1 + Cin
    half_adder ha2 (
        .a_i(sum1),
        .b_i(cin_i),
        .sum_o(sum_o),
        .cout_o(cout2)
    );

    // Final carry: cout1 OR cout2
    assign cout_o = cout1 | cout2;

endmodule 