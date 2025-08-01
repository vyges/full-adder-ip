#==============================================================================
# Full Adder Testbench Master Makefile
#==============================================================================
# Description: Master Makefile for running all testbench types (SystemVerilog,
#              and cocotb) with various simulators.
# Author:      Vyges Team
# Date:        2025-07-17
# Version:     1.0.0
#==============================================================================

# Defaults
TESTBENCH_TYPE ?= sv
SIM ?= icarus

# Available testbench types
TB_TYPES = sv cocotb

# Available simulators
SV_SIMS = icarus verilator
COCOTB_SIMS = icarus verilator

# Help target
help:
	@echo "Full Adder Testbench Master Makefile"
	@echo "===================================="
	@echo ""
	@echo "Available testbench types (set TESTBENCH_TYPE=<type>):"
	@echo "  sv      - SystemVerilog testbench (default)"
	@echo "  cocotb  - Cocotb testbench"
	@echo ""
	@echo "Available simulators by testbench type:"
	@echo "  SystemVerilog: $(SV_SIMS)"
	@echo "  Cocotb:        $(COCOTB_SIMS)"
	@echo ""
	@echo "Usage examples:"
	@echo "  make test_basic                    # Run basic test with default settings"
	@echo "  make test_all                      # Run all tests with default settings"
	@echo "  make test_all TESTBENCH_TYPE=cocotb SIM=verilator"
	@echo "  make clean                         # Clean all testbench artifacts"
	@echo "  make help                          # Show this help message"
	@echo ""
	@echo "Individual testbench directories:"
	@echo "  sv_tb/     - SystemVerilog testbench"
	@echo "  cocotb/    - Cocotb testbench"

# Validation functions
define validate_testbench_type
		echo "Error: Invalid TESTBENCH_TYPE '$(TESTBENCH_TYPE)'. Valid types: $(TB_TYPES)"; \
		exit 1; \
	fi
endef

define validate_simulator
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			if [ "$(filter $(SIM),$(SV_SIMS))" = "" ]; then \
				echo "Error: Simulator '$(SIM)' not supported for SystemVerilog testbench"; \
				echo "Supported simulators: $(SV_SIMS)"; \
				exit 1; \
			fi \
			;; \
				exit 1; \
			fi \
			;; \
		cocotb) \
			if [ "$(filter $(SIM),$(COCOTB_SIMS))" = "" ]; then \
				echo "Error: Simulator '$(SIM)' not supported for Cocotb testbench"; \
				echo "Supported simulators: $(COCOTB_SIMS)"; \
				exit 1; \
			fi \
			;; \
	esac
endef

# Test targets
test_basic: validate_testbench_type validate_simulator
	@echo "Running basic test with $(TESTBENCH_TYPE) testbench using $(SIM) simulator..."
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			cd sv_tb && $(MAKE) test_basic SIM=$(SIM) || exit 1; \
			;; \
			;; \
		cocotb) \
			cd cocotb && $(MAKE) test_basic SIM=$(SIM) || exit 1; \
			;; \
	esac
	@echo "Basic test completed successfully!"

test_random: validate_testbench_type validate_simulator
	@echo "Running random test with $(TESTBENCH_TYPE) testbench using $(SIM) simulator..."
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			cd sv_tb && $(MAKE) test_random SIM=$(SIM) || exit 1; \
			;; \
			;; \
		cocotb) \
			cd cocotb && $(MAKE) test_random SIM=$(SIM) || exit 1; \
			;; \
	esac
	@echo "Random test completed successfully!"

test_all: validate_testbench_type validate_simulator
	@echo "Running all tests with $(TESTBENCH_TYPE) testbench using $(SIM) simulator..."
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			cd sv_tb && $(MAKE) test_all SIM=$(SIM) || exit 1; \
			;; \
			;; \
		cocotb) \
			cd cocotb && $(MAKE) test_all SIM=$(SIM) || exit 1; \
			;; \
	esac
	@echo "All tests completed successfully!"

coverage: validate_testbench_type validate_simulator
		exit 1; \
	fi
	@echo "Coverage completed successfully!"

gui: validate_testbench_type validate_simulator
		exit 1; \
	fi
	@echo "GUI target not implemented for current simulators"

# Waveform viewing
waves: validate_testbench_type validate_simulator
	@echo "Viewing waveforms for $(TESTBENCH_TYPE) testbench..."
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			cd sv_tb && $(MAKE) waves SIM=$(SIM) || exit 1; \
			;; \
			;; \
		cocotb) \
			cd cocotb && $(MAKE) waves SIM=$(SIM) || exit 1; \
			;; \
	esac

# Compile target
compile: validate_testbench_type validate_simulator
	@echo "Compiling $(TESTBENCH_TYPE) testbench using $(SIM) simulator..."
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			cd sv_tb && $(MAKE) compile SIM=$(SIM) || exit 1; \
			;; \
			;; \
		cocotb) \
			cd cocotb && $(MAKE) compile SIM=$(SIM) || exit 1; \
			;; \
	esac
	@echo "Compilation completed successfully!"

# Run target
run: validate_testbench_type validate_simulator
	@echo "Running $(TESTBENCH_TYPE) testbench using $(SIM) simulator..."
	@case "$(TESTBENCH_TYPE)" in \
		sv) \
			cd sv_tb && $(MAKE) run SIM=$(SIM) || exit 1; \
			;; \
			;; \
		cocotb) \
			cd cocotb && $(MAKE) run SIM=$(SIM) || exit 1; \
			;; \
	esac
	@echo "Simulation completed successfully!"

# Clean target
clean:
	@echo "Cleaning all testbench artifacts..."
	@for tb_type in $(TB_TYPES); do \
		if [ -d "$$tb_type"_tb ]; then \
			cd "$$tb_type"_tb && $(MAKE) clean && cd ..; \
		fi; \
		if [ -d "$$tb_type" ]; then \
			cd "$$tb_type" && $(MAKE) clean && cd ..; \
		fi; \
	done
	@echo "Clean completed successfully!"

# Test all testbench types
test_all_types:
	@echo "Testing all testbench types..."
	@for tb_type in $(TB_TYPES); do \
		echo "Testing $$tb_type testbench..."; \
		$(MAKE) test_basic TESTBENCH_TYPE=$$tb_type SIM=icarus || exit 1; \
	done
	@echo "All testbench types tested successfully!"

# Performance comparison
benchmark:
	@echo "Running performance benchmark..."
	@echo "SystemVerilog testbench:"
	@time $(MAKE) test_basic TESTBENCH_TYPE=sv SIM=icarus > /dev/null 2>&1
	@echo "Cocotb testbench:"
	@time $(MAKE) test_basic TESTBENCH_TYPE=cocotb SIM=icarus > /dev/null 2>&1
	@echo "Benchmark completed!"

# Status target
status:
	@echo "Testbench Status:"
	@echo "================="
	@echo "Testbench Type: $(TESTBENCH_TYPE)"
	@echo "Simulator: $(SIM)"
	@echo ""
	@echo "Available testbench types: $(TB_TYPES)"
	@echo "Available simulators for $(TESTBENCH_TYPE):"
	@case "$(TESTBENCH_TYPE)" in \
		sv) echo "  $(SV_SIMS)" ;; \
		cocotb) echo "  $(COCOTB_SIMS)" ;; \
	esac

.PHONY: help test_basic test_random test_all coverage gui waves compile run clean test_all_types benchmark status

