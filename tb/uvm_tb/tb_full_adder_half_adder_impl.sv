//=============================================================================
// Full Adder Half Adder Implementation Testbench
//=============================================================================
// Description: SystemVerilog testbench for full_adder_half_adder implementation
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

`timescale 1ns/1ps

module tb_full_adder_half_adder_impl;

    // Clock and reset signals
    logic clk_i;
    logic reset_n_i;
    
    // DUT signals
    logic a_i, b_i, cin_i;
    logic sum_o, cout_o;
    
    // Test signals
    logic [2:0] test_vector;
    logic [1:0] expected_output;
    int test_count = 0;
    int pass_count = 0;
    int fail_count = 0;
    
    // DUT instance - testing half adder implementation
    full_adder_half_adder dut (
        .clk_i(clk_i),
        .reset_n_i(reset_n_i),
        .a_i(a_i),
        .b_i(b_i),
        .cin_i(cin_i),
        .sum_o(sum_o),
        .cout_o(cout_o)
    );
    
    // Clock generation
    initial begin
        clk_i = 0;
        forever #5 clk_i = ~clk_i; // 100MHz clock
    end
    
    // Test stimulus
    initial begin
        $display("=== Full Adder Half Adder Implementation Testbench ===");
        $display("Time: %0t", $time);
        
        // Initialize signals
        reset_n_i = 0;
        a_i = 0;
        b_i = 0;
        cin_i = 0;
        
        // Apply reset
        #100;
        reset_n_i = 1;
        #20;
        
        // Test all 8 input combinations
        for (int i = 0; i < 8; i++) begin
            test_vector = i[2:0];
            a_i = test_vector[0];
            b_i = test_vector[1];
            cin_i = test_vector[2];
            
            // Calculate expected output
            expected_output[0] = a_i ^ b_i ^ cin_i; // sum
            expected_output[1] = (a_i & b_i) | ((a_i ^ b_i) & cin_i); // carry
            
            // Wait for propagation
            @(posedge clk_i);
            #1; // Small delay for combinational logic
            
            // Check results
            test_count++;
            if (sum_o === expected_output[0] && cout_o === expected_output[1]) begin
                pass_count++;
                $display("PASS Test %0d: a_i=%b, b_i=%b, cin_i=%b, sum_o=%b, cout_o=%b", 
                        test_count, a_i, b_i, cin_i, sum_o, cout_o);
            end else begin
                fail_count++;
                $display("FAIL Test %0d: a_i=%b, b_i=%b, cin_i=%b, sum_o=%b (expected %b), cout_o=%b (expected %b)", 
                        test_count, a_i, b_i, cin_i, sum_o, expected_output[0], cout_o, expected_output[1]);
            end
            
            #10; // Wait between tests
        end
        
        // Print summary
        $display("=== Test Summary ===");
        $display("Total Tests: %0d", test_count);
        $display("Passed: %0d", pass_count);
        $display("Failed: %0d", fail_count);
        $display("Success Rate: %0.1f%%", (pass_count * 100.0) / test_count);
        
        if (fail_count == 0) begin
            $display("=== ALL TESTS PASSED ===");
        end else begin
            $display("=== SOME TESTS FAILED ===");
        end
        
        $finish;
    end
    
    // Waveform dumping
    initial begin
        $dumpfile("full_adder_half_adder_impl.vcd");
        $dumpvars(0, tb_full_adder_half_adder_impl);
    end
    
    // Timeout
    initial begin
        #10000; // 10us timeout
        $display("Simulation timeout reached");
        $finish;
    end

endmodule 