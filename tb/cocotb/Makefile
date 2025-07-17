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

# Top level module
TOPLEVEL = full_adder

# Python test file
MODULE = test_full_adder

# Include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

# Additional simulator-specific settings
ifeq ($(SIM),icarus)
    # Icarus Verilog settings
    COMPILE_ARGS += -I $(PWD)/../../rtl
    VERILOG_SOURCES += $(PWD)/../../rtl/full_adder.v
else ifeq ($(SIM),verilator)
    # Verilator settings
    COMPILE_ARGS += -I $(PWD)/../../rtl
    VERILOG_SOURCES += $(PWD)/../../rtl/full_adder.v
    EXTRA_ARGS += --trace --trace-structs
else ifeq ($(SIM),questa)
    # Questa/ModelSim settings
    COMPILE_ARGS += -I $(PWD)/../../rtl
    VERILOG_SOURCES += $(PWD)/../../rtl/full_adder.v
    EXTRA_ARGS += -do "run -all; quit"
else ifeq ($(SIM),vcs)
    # VCS settings
    COMPILE_ARGS += -I $(PWD)/../../rtl
    VERILOG_SOURCES += $(PWD)/../../rtl/full_adder.v
    EXTRA_ARGS += -full64
endif

# Test targets
.PHONY: test_basic test_random test_all clean

test_basic:
	$(MAKE) SIM=$(SIM) MODULE=test_full_adder TOPLEVEL=full_adder

test_random:
	$(MAKE) SIM=$(SIM) MODULE=test_full_adder TOPLEVEL=full_adder

test_all: test_basic test_random

# Clean target
clean::
	rm -rf __pycache__
	rm -rf results.xml
	rm -rf dump.vcd
	rm -rf full_adder.vcd
	rm -rf sim_build
	rm -rf *.log
	rm -rf *.vcd
	rm -rf *.fst
	rm -rf *.ghw

# Help target
help:
	@echo "Available targets:"
	@echo "  test_basic    - Run basic functionality tests"
	@echo "  test_random   - Run random input tests"
	@echo "  test_all      - Run all tests"
	@echo "  clean         - Clean build artifacts"
	@echo "  help          - Show this help message"
	@echo ""
	@echo "Available simulators (set SIM=<simulator>):"
	@echo "  icarus        - Icarus Verilog (default)"
	@echo "  verilator     - Verilator"
	@echo "  questa        - Questa/ModelSim"
	@echo "  vcs           - VCS"
	@echo ""
	@echo "Example usage:"
	@echo "  make test_basic SIM=icarus"
	@echo "  make test_all SIM=verilator" 