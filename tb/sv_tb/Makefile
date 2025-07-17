#==============================================================================
# Full Adder SystemVerilog Testbench Makefile
#==============================================================================
# Description: Makefile for running SystemVerilog testbench with various
#              simulators including Icarus Verilog and Verilator.
# Author:      Vyges Team
# Date:        2025-07-17
# Version:     1.0.0
#==============================================================================

# Defaults
SIM ?= icarus
TOPLEVEL = tb_full_adder

# Source files
RTL_SOURCES = ../../rtl/full_adder.v
TB_SOURCES = tb_full_adder.v

# Simulator-specific settings
ifeq ($(SIM),icarus)
    # Icarus Verilog settings
    VLOG = iverilog
    VVP = vvp
    VLOG_FLAGS = -g2012 -I ../../rtl
    SIM_EXEC = simv.out
    COMPILE = $(VLOG) $(VLOG_FLAGS) -o $(SIM_EXEC) $(RTL_SOURCES) $(TB_SOURCES)
    RUN = $(VVP) $(SIM_EXEC)
else ifeq ($(SIM),verilator)
    # Verilator settings
    VLOG = verilator
    VLOG_FLAGS = --cc --exe --build --trace --top-module $(TOPLEVEL)
    VLOG_FLAGS += -I ../../rtl
    SIM_EXEC = obj_dir/V$(TOPLEVEL)
    COMPILE = $(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(TB_SOURCES)
    RUN = ./$(SIM_EXEC)
else ifeq ($(SIM),questa)
    # Questa/ModelSim settings
    VLOG = vlog
    VSIM = vsim
    VLOG_FLAGS = -sv -I ../../rtl
    VSIM_FLAGS = -c -do "run -all; quit"
    COMPILE = $(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(TB_SOURCES)
    RUN = $(VSIM) $(VSIM_FLAGS) $(TOPLEVEL)
else ifeq ($(SIM),vcs)
    # VCS settings
    VLOG = vcs
    VLOG_FLAGS = -full64 -sverilog -I ../../rtl
    SIM_EXEC = simv
    COMPILE = $(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(TB_SOURCES) -o $(SIM_EXEC)
    RUN = ./$(SIM_EXEC)
endif

# Default target
all: compile run

# Compile target
compile:
	@echo "Compiling SystemVerilog testbench with $(SIM)..."
	$(COMPILE)
	@echo "Compilation complete"

# Run target
run: compile
	@echo "Running SystemVerilog testbench..."
	$(RUN)
	@echo "Simulation complete"

# Test targets
test_basic: run
	@echo "Basic functionality test completed"

test_random: run
	@echo "Random input test completed"

test_all: test_basic test_random
	@echo "All tests completed"

# Waveform viewing
waves:
ifeq ($(SIM),icarus)
	@echo "Use GTKWave to view waveforms: gtkwave full_adder.vcd"
else ifeq ($(SIM),verilator)
	@echo "Use GTKWave to view waveforms: gtkwave full_adder_uvm.vcd"
else ifeq ($(SIM),questa)
	$(VSIM) -view vsim.wlf
else ifeq ($(SIM),vcs)
	@echo "Use DVE or Verdi to view VCS waveforms"
endif

# Clean target
clean:
	rm -rf work
	rm -rf transcript
	rm -rf vsim.wlf
	rm -rf *.log
	rm -rf *.vcd
	rm -rf *.fst
	rm -rf *.ghw
	rm -rf simv
	rm -rf simv.daidir
	rm -rf csrc
	rm -rf ucli.key
	rm -rf *.so
	rm -rf obj_dir
	rm -rf *.exe
	rm -rf *.o
	rm -rf *.a
	rm -rf *.d
	rm -rf simv.out

# Help target
help:
	@echo "Full Adder SystemVerilog Testbench Makefile"
	@echo "==========================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all           - Compile and run (default)"
	@echo "  compile       - Compile the design and testbench"
	@echo "  run           - Run the simulation"
	@echo "  test_basic    - Run basic functionality test"
	@echo "  test_random   - Run random input test"
	@echo "  test_all      - Run all tests"
	@echo "  waves         - View waveforms"
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
	@echo "  make waves SIM=questa"

.PHONY: all compile run test_basic test_random test_all waves clean help 