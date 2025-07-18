#==============================================================================
# Full Adder Cocotb Makefile
#==============================================================================
# Description: Makefile for running cocotb testbench with various simulators
# Author:      Vyges Team
# Date:        2025-07-17
# Version:     1.0.0
#==============================================================================

# Defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Top level module (can be overridden)
TOPLEVEL ?= full_adder

# Python test file (can be overridden)
MODULE ?= test_full_adder

# RTL directory
RTL_DIR = $(PWD)/../../rtl

# Include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

# Additional simulator-specific settings
ifeq ($(SIM),icarus)
    # Icarus Verilog settings - compile only the specific file
    VERILOG_SOURCES = $(RTL_DIR)/$(TOPLEVEL).v
else ifeq ($(SIM),verilator)
    # Verilator settings - specify the exact file to compile
    VERILOG_SOURCES = $(RTL_DIR)/$(TOPLEVEL).v
    EXTRA_ARGS += --trace --trace-structs
else ifeq ($(SIM),questa)
    # Questa/ModelSim settings
    VERILOG_SOURCES = $(RTL_DIR)/$(TOPLEVEL).v
    EXTRA_ARGS += -do "run -all; quit"
else ifeq ($(SIM),vcs)
    # VCS settings
    VERILOG_SOURCES = $(RTL_DIR)/$(TOPLEVEL).v
    EXTRA_ARGS += -full64
endif

# Test targets for different implementations
.PHONY: test_carry_lookahead test_simple test_half_adder test_all_implementations clean

# Test carry lookahead implementation
test_carry_lookahead:
	$(MAKE) clean
	$(MAKE) SIM=$(SIM) MODULE=test_full_adder TOPLEVEL=full_adder

# Test simple XOR/AND implementation
test_simple:
	$(MAKE) clean
	$(MAKE) SIM=$(SIM) MODULE=test_full_adder_simple TOPLEVEL=full_adder_simple

# Test half adder modular implementation
test_half_adder:
	$(MAKE) clean
	$(MAKE) SIM=$(SIM) MODULE=test_full_adder_half_adder TOPLEVEL=full_adder_half_adder

# Test all implementations
test_all_implementations: test_carry_lookahead test_simple test_half_adder

# Test with enhanced testbench
test_enhanced:
	$(MAKE) clean
	$(MAKE) SIM=$(SIM) MODULE=test_all_implementations TOPLEVEL=full_adder

# Legacy targets for backward compatibility
test_basic: test_carry_lookahead
test_random: test_carry_lookahead
test_all: test_all_implementations

# Clean target
clean::
	rm -rf __pycache__
	rm -rf results.xml
	rm -rf dump.vcd
	rm -rf full_adder.vcd
	rm -rf full_adder_simple.vcd
	rm -rf full_adder_half_adder.vcd
	rm -rf sim_build
	rm -rf *.log
	rm -rf *.vcd
	rm -rf *.fst
	rm -rf *.ghw

# Help target
help:
	@echo "Available targets:"
	@echo "  test_carry_lookahead    - Test carry lookahead implementation"
	@echo "  test_simple             - Test simple XOR/AND implementation"
	@echo "  test_half_adder         - Test half adder modular implementation"
	@echo "  test_all_implementations - Test all three implementations"
	@echo "  test_enhanced           - Test with enhanced testbench"
	@echo "  clean                   - Clean build artifacts"
	@echo "  help                    - Show this help message"
	@echo ""
	@echo "Available simulators (set SIM=<simulator>):"
	@echo "  icarus        - Icarus Verilog (default)"
	@echo "  verilator     - Verilator"
	@echo "  questa        - Questa/ModelSim"
	@echo "  vcs           - VCS"
	@echo ""
	@echo "Example usage:"
	@echo "  make test_carry_lookahead SIM=icarus"
	@echo "  make test_simple SIM=verilator"
	@echo "  make test_all_implementations SIM=questa"
	@echo "  make test_enhanced SIM=icarus" 