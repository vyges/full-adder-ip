`timescale 1ns/1ps

module tb_full_adder_half_adder;

    // Testbench signals - following Vyges conventions
    logic clk_i, reset_n_i;
    logic a_i, b_i, cin_i;
    logic sum_o, cout_o;
    logic expected_sum, expected_cout;
    
    // Clock generation
    initial begin
        clk_i = 0;
        forever #5 clk_i = ~clk_i;
    end
    
    // Reset generation
    initial begin
        reset_n_i = 0;
        #10 reset_n_i = 1;
    end
    
    // Instantiate the half adder modular full adder module
    full_adder_half_adder dut (
        .clk_i(clk_i),
        .reset_n_i(reset_n_i),
        .a_i(a_i),
        .b_i(b_i),
        .cin_i(cin_i),
        .sum_o(sum_o),
        .cout_o(cout_o)
    );
    
    // Test stimulus and monitoring
    initial begin
        $display("=== Full Adder Half Adder Modular Testbench ===");
        $display("Time\ta_i\tb_i\tcin_i\tsum_o\tcout_o\tExpected sum_o\tExpected cout_o\tStatus");
        $display("----------------------------------------------------------------------------");
        
        // Test all 8 possible input combinations
        test_case(1'b0, 1'b0, 1'b0); // 0 + 0 + 0 = 0
        test_case(1'b0, 1'b0, 1'b1); // 0 + 0 + 1 = 1
        test_case(1'b0, 1'b1, 1'b0); // 0 + 1 + 0 = 1
        test_case(1'b0, 1'b1, 1'b1); // 0 + 1 + 1 = 2 (carry)
        test_case(1'b1, 1'b0, 1'b0); // 1 + 0 + 0 = 1
        test_case(1'b1, 1'b0, 1'b1); // 1 + 0 + 1 = 2 (carry)
        test_case(1'b1, 1'b1, 1'b0); // 1 + 1 + 0 = 2 (carry)
        test_case(1'b1, 1'b1, 1'b1); // 1 + 1 + 1 = 3 (carry)
        
        // Additional delay for waveform viewing
        #10;
        
        $display("=== Testbench Complete ===");
        $finish;
    end
    
    // Task to test a specific input combination
    task test_case(input logic test_a, test_b, test_cin);
        begin
            // Apply inputs
            a_i = test_a;
            b_i = test_b;
            cin_i = test_cin;
            
            // Calculate expected outputs
            expected_sum = test_a ^ test_b ^ test_cin;
            expected_cout = (test_a & test_b) | ((test_a ^ test_b) & test_cin);
            
            // Wait for propagation delay
            #1;
            
            // Display results
            $display("%0t\t%b\t%b\t%b\t%b\t%b\t%b\t\t%b\t\t%s", 
                     $time, a_i, b_i, cin_i, sum_o, cout_o, expected_sum, expected_cout,
                     (sum_o === expected_sum && cout_o === expected_cout) ? "PASS" : "FAIL");
            
            // Verify outputs
            if (sum_o !== expected_sum || cout_o !== expected_cout) begin
                $error("Test failed for a_i=%b, b_i=%b, cin_i=%b", test_a, test_b, test_cin);
                $error("Expected: sum_o=%b, cout_o=%b", expected_sum, expected_cout);
                $error("Got: sum_o=%b, cout_o=%b", sum_o, cout_o);
            end
        end
    endtask
    
    // Optional: Generate VCD file for waveform viewing
    initial begin
        $dumpfile("full_adder_half_adder.vcd");
        $dumpvars(0, tb_full_adder_half_adder);
    end

endmodule 