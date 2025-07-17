//=============================================================================
// 4-bit Ripple Carry Adder - Integration Example
//=============================================================================
// Description: Example showing how to use the full adder IP in a multi-bit
//              ripple carry adder configuration.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

module ripple_carry_adder_4bit (
    input  logic [3:0] a_i,     // First 4-bit operand
    input  logic [3:0] b_i,     // Second 4-bit operand
    input  logic       cin_i,   // Carry input
    output logic [3:0] sum_o,   // 4-bit sum output
    output logic       cout_o   // Carry output
);

    // Internal carry signals
    logic [4:0] carry;

    // Connect input carry to first stage
    assign carry[0] = cin_i;

    // Generate 4 full adder instances
    genvar i;
    generate
        for (i = 0; i < 4; i = i + 1) begin : fa_chain
            full_adder fa_inst (
                .a_i(a_i[i]),
                .b_i(b_i[i]),
                .cin_i(carry[i]),
                .sum_o(sum_o[i]),
                .cout_o(carry[i+1])
            );
        end
    endgenerate

    // Final carry out
    assign cout_o = carry[4];

endmodule 