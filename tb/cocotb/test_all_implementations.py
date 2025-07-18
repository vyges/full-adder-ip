#!/usr/bin/env python3
"""
==============================================================================
Full Adder All Implementations Cocotb Testbench
==============================================================================
Description: Enhanced cocotb testbench for testing all three full adder
             implementations: carry lookahead, simple XOR/AND, and half adder modular.
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test configuration
CLOCK_PERIOD_NS = 10  # 100MHz clock
RESET_DELAY_NS = 100
TEST_TIMEOUT_NS = 10000

class FullAdderTest:
    """Test class for full adder verification"""
    
    def __init__(self, dut, implementation_name=""):
        self.dut = dut
        self.clock = None
        self.test_count = 0
        self.pass_count = 0
        self.fail_count = 0
        self.implementation_name = implementation_name
        
    async def setup(self):
        """Setup testbench with clock and reset"""
        logger.info(f"Setting up testbench for {self.implementation_name}...")
        
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
        
        logger.info(f"Testbench setup complete for {self.implementation_name}")
    
    def calculate_expected(self, a_i, b_i, cin_i):
        """Calculate expected outputs for full adder"""
        expected_sum = a_i ^ b_i ^ cin_i
        expected_cout = (a_i & b_i) | ((a_i ^ b_i) & cin_i)
        return expected_sum, expected_cout
    
    def test_case(self, a_i, b_i, cin_i, test_name=""):
        """Test a specific input combination"""
        self.test_count += 1
        
        # Apply inputs
        self.dut.a_i.value = a_i
        self.dut.b_i.value = b_i
        self.dut.cin_i.value = cin_i
        
        # Get actual outputs
        sum_o = self.dut.sum_o.value
        cout_o = self.dut.cout_o.value
        
        # Calculate expected outputs
        expected_sum, expected_cout = self.calculate_expected(a_i, b_i, cin_i)
        
        # Check results
        if sum_o == expected_sum and cout_o == expected_cout:
            self.pass_count += 1
            logger.info(f"[{self.implementation_name}] PASS {test_name}: a_i={a_i}, b_i={b_i}, cin_i={cin_i}, "
                       f"sum_o={sum_o}, cout_o={cout_o}")
        else:
            self.fail_count += 1
            logger.error(f"[{self.implementation_name}] FAIL {test_name}: a_i={a_i}, b_i={b_i}, cin_i={cin_i}, "
                        f"sum_o={sum_o} (expected {expected_sum}), "
                        f"cout_o={cout_o} (expected {expected_cout})")
            assert False, f"Test failed for {self.implementation_name} with inputs a_i={a_i}, b_i={b_i}, cin_i={cin_i}"
    
    def print_summary(self):
        """Print test summary"""
        logger.info("=" * 60)
        logger.info(f"TEST SUMMARY - {self.implementation_name}")
        logger.info("=" * 60)
        logger.info(f"Total Tests: {self.test_count}")
        logger.info(f"Passed: {self.pass_count}")
        logger.info(f"Failed: {self.fail_count}")
        logger.info(f"Success Rate: {(self.pass_count/self.test_count)*100:.1f}%")
        logger.info("=" * 60)

@cocotb.test()
async def test_carry_lookahead_implementation(dut):
    """Test carry lookahead implementation"""
    logger.info("Starting carry lookahead implementation test...")
    
    test = FullAdderTest(dut, "Carry Lookahead")
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
        test.test_case(a_i, b_i, cin_i, test_name)
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Carry lookahead test failed with {test.fail_count} failures"

@cocotb.test()
async def test_simple_implementation(dut):
    """Test simple XOR/AND implementation"""
    logger.info("Starting simple XOR/AND implementation test...")
    
    test = FullAdderTest(dut, "Simple XOR/AND")
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
        test.test_case(a_i, b_i, cin_i, test_name)
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Simple implementation test failed with {test.fail_count} failures"

@cocotb.test()
async def test_half_adder_implementation(dut):
    """Test half adder modular implementation"""
    logger.info("Starting half adder modular implementation test...")
    
    test = FullAdderTest(dut, "Half Adder Modular")
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
        test.test_case(a_i, b_i, cin_i, test_name)
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Half adder implementation test failed with {test.fail_count} failures"

@cocotb.test()
async def test_all_implementations_comprehensive(dut):
    """Comprehensive test for all implementations with random inputs"""
    logger.info("Starting comprehensive test for all implementations...")
    
    # Get implementation name from environment or default
    implementation = os.environ.get('IMPLEMENTATION', 'Unknown')
    test = FullAdderTest(dut, implementation)
    await test.setup()
    
    # Test with random inputs
    num_tests = 50
    random.seed(42)  # Fixed seed for reproducible results
    
    for i in range(num_tests):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        cin_i = random.randint(0, 1)
        
        test.test_case(a_i, b_i, cin_i, f"Random_{i+1}")
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Comprehensive test failed with {test.fail_count} failures"

# Main test runner
async def run_all_implementation_tests(dut):
    """Run all implementation tests in sequence"""
    logger.info("=" * 60)
    logger.info("FULL ADDER ALL IMPLEMENTATIONS COCOTB TESTBENCH")
    logger.info("=" * 60)
    
    tests = [
        test_carry_lookahead_implementation,
        test_simple_implementation,
        test_half_adder_implementation,
        test_all_implementations_comprehensive
    ]
    
    for test_func in tests:
        try:
            await test_func(dut)
            logger.info(f"✓ {test_func.__name__} completed successfully")
        except Exception as e:
            logger.error(f"✗ {test_func.__name__} failed: {e}")
            raise
    
    logger.info("=" * 60)
    logger.info("ALL IMPLEMENTATION TESTS COMPLETED SUCCESSFULLY")
    logger.info("=" * 60)

# Optional: Run all tests if this file is executed directly
if __name__ == "__main__":
    # This would be called by cocotb framework
    pass 