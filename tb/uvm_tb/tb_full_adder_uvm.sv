//=============================================================================
// Full Adder UVM Testbench Top Module
//=============================================================================
// Description: Top-level UVM testbench for full adder verification with
//              complete UVM methodology implementation.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

`timescale 1ns/1ps

module tb_full_adder_uvm;

    // Import UVM package
    import uvm_pkg::*;
    import full_adder_pkg::*;
    
    // Virtual interface instance
    full_adder_if vif();
    
    // DUT instance with clock and reset
    full_adder dut (
        .clk_i(vif.clk_i),
        .reset_n_i(vif.reset_n_i),
        .a_i(vif.a_i),
        .b_i(vif.b_i),
        .cin_i(vif.cin_i),
        .sum_o(vif.sum_o),
        .cout_o(vif.cout_o)
    );
    
    // UVM testbench initialization
    initial begin
        // Set virtual interface in config database
        uvm_config_db#(virtual full_adder_if)::set(null, "*", "vif", vif);
        
        // Set default test
        uvm_config_db#(string)::set(null, "*", "default_sequence", "basic_functionality_test");
        
        // Start UVM test
        run_test();
    end
    
    // Waveform dumping for debugging
    initial begin
        $dumpfile("full_adder_uvm.vcd");
        $dumpvars(0, tb_full_adder_uvm);
    end
    
    // Timeout mechanism
    initial begin
        #10000; // 10us timeout
        $display("Simulation timeout reached");
        $finish;
    end
    
    // Monitor simulation progress
    initial begin
        $display("=== Full Adder UVM Testbench Started ===");
        $display("Time: %0t", $time);
    end
    
    final begin
        $display("=== Full Adder UVM Testbench Completed ===");
        $display("Time: %0t", $time);
    end

endmodule 