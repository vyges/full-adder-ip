#!/usr/bin/env python3
"""
==============================================================================
Full Adder Cocotb Testbench
==============================================================================
Description: Cocotb testbench for full adder verification with comprehensive
             test scenarios including basic functionality, random testing, and
             edge cases.
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

class FullAdderTest:
    """Test class for full adder verification"""
    
    def __init__(self, dut):
        self.dut = dut
        self.clock = None
        self.test_count = 0
        self.pass_count = 0
        self.fail_count = 0
        
    async def setup(self):
        """Setup testbench with clock and reset"""
        logger.info("Setting up testbench...")
        
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
        
        logger.info("Testbench setup complete")
    
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
        logger.info("TEST SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total Tests: {self.test_count}")
        logger.info(f"Passed: {self.pass_count}")
        logger.info(f"Failed: {self.fail_count}")
        logger.info(f"Success Rate: {(self.pass_count/self.test_count)*100:.1f}%")
        logger.info("=" * 60)

@cocotb.test()
async def test_basic_functionality(dut):
    """Test basic full adder functionality with all 8 input combinations"""
    logger.info("Starting basic functionality test...")
    
    test = FullAdderTest(dut)
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
    assert test.fail_count == 0, f"Basic functionality test failed with {test.fail_count} failures"

@cocotb.test()
async def test_random_inputs(dut):
    """Test full adder with random input combinations"""
    logger.info("Starting random input test...")
    
    test = FullAdderTest(dut)
    await test.setup()
    
    # Test with random inputs
    num_tests = 100
    random.seed(42)  # Fixed seed for reproducible results
    
    for i in range(num_tests):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        cin_i = random.randint(0, 1)
        
        test.test_case(a_i, b_i, cin_i, f"Random_{i+1}")
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Random input test failed with {test.fail_count} failures"

@cocotb.test()
async def test_edge_cases(dut):
    """Test edge cases and timing"""
    logger.info("Starting edge case test...")
    
    test = FullAdderTest(dut)
    await test.setup()
    
    # Test rapid input changes
    for i in range(10):
        # Rapidly toggle inputs
        test.test_case(0, 0, 0, f"Edge_{i*3+1}")
        await Timer(1, units="ns")
        test.test_case(1, 1, 1, f"Edge_{i*3+2}")
        await Timer(1, units="ns")
        test.test_case(0, 1, 0, f"Edge_{i*3+3}")
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Edge case test failed with {test.fail_count} failures"

@cocotb.test()
async def test_reset_functionality(dut):
    """Test reset functionality"""
    logger.info("Starting reset functionality test...")
    
    test = FullAdderTest(dut)
    await test.setup()
    
    # Test normal operation
    test.test_case(1, 1, 1, "Before_Reset")
    await Timer(CLOCK_PERIOD_NS, units="ns")
    
    # Apply reset
    dut.reset_n_i.value = 0
    await Timer(RESET_DELAY_NS, units="ns")
    
    # Test during reset (outputs should be stable)
    test.test_case(0, 0, 0, "During_Reset")
    
    # Release reset
    dut.reset_n_i.value = 1
    await Timer(CLOCK_PERIOD_NS * 2, units="ns")
    
    # Test after reset
    test.test_case(1, 0, 1, "After_Reset")
    
    test.print_summary()
    assert test.fail_count == 0, f"Reset functionality test failed with {test.fail_count} failures"

@cocotb.test()
async def test_timing_analysis(dut):
    """Test timing and propagation delays"""
    logger.info("Starting timing analysis test...")
    
    test = FullAdderTest(dut)
    await test.setup()
    
    # Test setup and hold time requirements
    for i in range(5):
        # Apply inputs
        dut.a_i.value = i % 2
        dut.b_i.value = (i >> 1) % 2
        dut.cin_i.value = (i >> 2) % 2
        
        # Wait for propagation
        await Timer(CLOCK_PERIOD_NS // 2, units="ns")
        
        # Check outputs
        test.test_case(dut.a_i.value, dut.b_i.value, dut.cin_i.value, f"Timing_{i+1}")
        
        await Timer(CLOCK_PERIOD_NS // 2, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Timing analysis test failed with {test.fail_count} failures"

@cocotb.test()
async def test_coverage_scenarios(dut):
    """Test coverage scenarios for comprehensive verification"""
    logger.info("Starting coverage scenarios test...")
    
    test = FullAdderTest(dut)
    await test.setup()
    
    # Test specific scenarios for coverage
    scenarios = [
        # All zeros
        (0, 0, 0, "All_Zeros"),
        # All ones
        (1, 1, 1, "All_Ones"),
        # Single bit patterns
        (1, 0, 0, "Single_Bit_A"),
        (0, 1, 0, "Single_Bit_B"),
        (0, 0, 1, "Single_Bit_Cin"),
        # Two bit patterns
        (1, 1, 0, "Two_Bits_AB"),
        (1, 0, 1, "Two_Bits_ACin"),
        (0, 1, 1, "Two_Bits_BCin"),
    ]
    
    for a_i, b_i, cin_i, test_name in scenarios:
        test.test_case(a_i, b_i, cin_i, test_name)
        await Timer(CLOCK_PERIOD_NS, units="ns")
    
    test.print_summary()
    assert test.fail_count == 0, f"Coverage scenarios test failed with {test.fail_count} failures"

# Main test runner
async def run_all_tests(dut):
    """Run all tests in sequence"""
    logger.info("=" * 60)
    logger.info("FULL ADDER COCOTB TESTBENCH")
    logger.info("=" * 60)
    
    tests = [
        test_basic_functionality,
        test_random_inputs,
        test_edge_cases,
        test_reset_functionality,
        test_timing_analysis,
        test_coverage_scenarios
    ]
    
    for test_func in tests:
        try:
            await test_func(dut)
            logger.info(f"✓ {test_func.__name__} completed successfully")
        except Exception as e:
            logger.error(f"✗ {test_func.__name__} failed: {e}")
            raise
    
    logger.info("=" * 60)
    logger.info("ALL TESTS COMPLETED SUCCESSFULLY")
    logger.info("=" * 60)

# Optional: Run all tests if this file is executed directly
if __name__ == "__main__":
    # This would be called by cocotb framework
    pass 