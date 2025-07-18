//==============================================================================
// Verilator Wrapper for Full Adder Testbench
//==============================================================================
// Description: C++ wrapper to run the Verilator-generated testbench
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//==============================================================================

#include "obj_dir/Vtb_full_adder.h"
#include "obj_dir/Vtb_full_adder___024root.h"
#include <verilated.h>
#include <verilated_vcd_c.h>
#include <iostream>

// Time stamp function required by Verilator
double sc_time_stamp() { return 0; }

int main(int argc, char** argv) {
    // Initialize Verilator
    Verilated::commandArgs(argc, argv);
    
    // Create the testbench instance
    Vtb_full_adder* top = new Vtb_full_adder;
    
    // Initialize trace
    VerilatedVcdC* tfp = new VerilatedVcdC;
    Verilated::traceEverOn(true);
    top->trace(tfp, 99);
    tfp->open("full_adder.vcd");
    
    // Initialize the design
    top->rootp->tb_full_adder__DOT__clk_i = 0;
    top->rootp->tb_full_adder__DOT__reset_n_i = 0;
    top->eval();
    
    // Run the simulation
    int time = 0;
    while (!Verilated::gotFinish() && time < 1000) {
        // Toggle clock
        top->rootp->tb_full_adder__DOT__clk_i = !top->rootp->tb_full_adder__DOT__clk_i;
        
        // Evaluate the design
        top->eval();
        
        // Dump trace
        tfp->dump(time);
        
        time++;
    }
    
    // Cleanup
    tfp->close();
    delete top;
    delete tfp;
    
    std::cout << "Verilator simulation completed successfully!" << std::endl;
    return 0;
} 