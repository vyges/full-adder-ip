//=============================================================================
// Full Adder Virtual Interface
//=============================================================================
// Description: Virtual interface for full adder UVM testbench providing
//              clock and reset signals along with DUT interface.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

interface full_adder_if;
    // Clock and reset signals following Vyges conventions
    logic clk_i;
    logic reset_n_i;
    
    // DUT interface signals
    logic a_i;
    logic b_i;
    logic cin_i;
    logic sum_o;
    logic cout_o;
    
    // Clock generation
    initial begin
        clk_i = 0;
        forever #5 clk_i = ~clk_i; // 100MHz clock (10ns period)
    end
    
    // Reset generation
    initial begin
        reset_n_i = 0;
        #100 reset_n_i = 1;
    end
    
    // Modport for driver
    modport driver_mp(
        input  clk_i,
        input  reset_n_i,
        output a_i,
        output b_i,
        output cin_i,
        input  sum_o,
        input  cout_o
    );
    
    // Modport for monitor
    modport monitor_mp(
        input  clk_i,
        input  reset_n_i,
        input  a_i,
        input  b_i,
        input  cin_i,
        input  sum_o,
        input  cout_o
    );
    
    // Modport for DUT
    modport dut_mp(
        input  clk_i,
        input  reset_n_i,
        input  a_i,
        input  b_i,
        input  cin_i,
        output sum_o,
        output cout_o
    );
    
endinterface 