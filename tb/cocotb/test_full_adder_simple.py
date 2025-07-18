#!/usr/bin/env python3
"""
==============================================================================
Full Adder Simple Implementation Cocotb Testbench
==============================================================================
Description: Cocotb testbench for full_adder_simple verification
Author:      Vyges Team
Date:        2025-07-17
Version:     1.0.0
==============================================================================
"""

import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock
from cocotb.handle import ModifiableObject
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test configuration
CLOCK_PERIOD_NS = 10  # 100MHz clock
RESET_DELAY_NS = 100
TEST_TIMEOUT_NS = 10000

class FullAdderSimpleTest:
    """Test class for full_adder_simple verification"""
    
    def __init__(self, dut):
        self.dut = dut
        self.clock = None
        self.test_count = 0
        self.pass_count = 0
        self.fail_count = 0
        
    async def setup(self):
        """Setup testbench with clock and reset"""
        logger.info("Setting up testbench for full_adder_simple...")
        
        # Create clock
        self.clock = Clock(self.dut.clk_i, CLOCK_PERIOD_NS, units="ns")
        cocotb.start_soon(self.clock.start())
        
        # Initialize signals
        self.dut.reset_n_i.value = 0
        self.dut.a_i.value = 0
        self.dut.b_i.value = 0
        self.dut.cin_i.value = 0
        
        # Apply reset
        await Timer(RESET_DELAY_NS, units="ns")
        self.dut.reset_n_i.value = 1
        await Timer(CLOCK_PERIOD_NS * 2, units="ns")
        
        logger.info("Testbench setup complete for full_adder_simple")
    
    def calculate_expected(self, a_i, b_i, cin_i):
        """Calculate expected outputs for full adder"""
        expected_sum = a_i ^ b_i ^ cin_i
        expected_cout = (a_i & b_i) | ((a_i ^ b_i) & cin_i)
        return expected_sum, expected_cout
    
    async def test_case(self, a_i, b_i, cin_i, test_name=""):
        """Test a specific input combination"""
        self.test_count += 1
        
        # Apply inputs
        self.dut.a_i.value = a_i
        self.dut.b_i.value = b_i
        self.dut.cin_i.value = cin_i
        
        # Wait for combinational logic to settle
        await Timer(1, units="ns")
        
        # Get actual outputs
        sum_o = int(self.dut.sum_o.value)
        cout_o = int(self.dut.cout_o.value)
        
        # Calculate expected outputs
        expected_sum, expected_cout = self.calculate_expected(a_i, b_i, cin_i)
        
        # Check results
        if sum_o == expected_sum and cout_o == expected_cout:
            self.pass_count += 1
            logger.info(f"PASS {test_name}: a_i={a_i}, b_i={b_i}, cin_i={cin_i}, "
                       f"sum_o={sum_o}, cout_o={cout_o}")
        else:
            self.fail_count += 1
            logger.error(f"FAIL {test_name}: a_i={a_i}, b_i={b_i}, cin_i={cin_i}, "
                        f"sum_o={sum_o} (expected {expected_sum}), "
                        f"cout_o={cout_o} (expected {expected_cout})")
            assert False, f"Test failed for inputs a_i={a_i}, b_i={b_i}, cin_i={cin_i}"
    
    def print_summary(self):
        """Print test summary"""
        logger.info("=" * 60)
        logger.info("FULL ADDER SIMPLE TEST SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total Tests: {self.test_count}")
        logger.info(f"Passed: {self.pass_count}")
        logger.info(f"Failed: {self.fail_count}")
        logger.info(f"Success Rate: {(self.pass_count/self.test_count)*100:.1f}%")
        logger.info("=" * 60)

@cocotb.test()
async def test_basic_functionality_simple(dut):
    """Test basic full_adder_simple functionality with all 8 input combinations"""
    logger.info("Starting basic functionality test for full_adder_simple...")
    
    test = FullAdderSimpleTest(dut)
    await test.setup()
    
    # Test all 8 possible input combinations
    test_cases = [
        (0, 0, 0, "0+0+0=0"),
        (0, 0, 1, "0+0+1=1"),
        (0, 1, 0, "0+1+0=1"),
        (0, 1, 1, "0+1+1=2"),
        (1, 0, 0, "1+0+0=1"),
        (1, 0, 1, "1+0+1=2"),
        (1, 1, 0, "1+1+0=2"),
        (1, 1, 1, "1+1+1=3")
    ]
    
    for a_i, b_i, cin_i, test_name in test_cases:
        await test.test_case(a_i, b_i, cin_i, test_name)
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Basic functionality test failed with {test.fail_count} failures"

@cocotb.test()
async def test_random_inputs_simple(dut):
    """Test full_adder_simple with random input combinations"""
    logger.info("Starting random input test for full_adder_simple...")
    
    test = FullAdderSimpleTest(dut)
    await test.setup()
    
    # Test with random inputs
    num_tests = 50  # Reduced for faster execution
    random.seed(42)  # Fixed seed for reproducible results
    
    for i in range(num_tests):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        cin_i = random.randint(0, 1)
        
        await test.test_case(a_i, b_i, cin_i, f"Random_{i+1}")
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Random input test failed with {test.fail_count} failures" 