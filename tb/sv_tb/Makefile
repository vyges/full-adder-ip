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

# OS detection for Verilator paths
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
    # macOS with Homebrew
    VERILATOR_INCLUDE = /opt/homebrew/Cellar/verilator/5.038/share/verilator/include
    VERILATOR_VLTSTD = /opt/homebrew/Cellar/verilator/5.038/share/verilator/include/vltstd
else
    # Linux (Ubuntu/Debian)
    VERILATOR_INCLUDE = /usr/share/verilator/include
    VERILATOR_VLTSTD = /usr/share/verilator/include/vltstd
endif

# Source files
RTL_SOURCES = ../../rtl/full_adder.v ../../rtl/full_adder_simple.v ../../rtl/full_adder_half_adder.v
TB_SOURCES = tb_full_adder.v tb_full_adder_simple.v tb_full_adder_half_adder.v

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
    VLOG_FLAGS = --cc --build --trace --top-module $(TOPLEVEL) --timing
    VLOG_FLAGS += -I../../rtl
    SIM_EXEC = verilator_sim
    COMPILE = $(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(TB_SOURCES) && \
              c++ -I. -Iobj_dir -I$(VERILATOR_INCLUDE) \
              -I$(VERILATOR_VLTSTD) \
              -std=gnu++20 verilator_wrapper.cpp obj_dir/libVtb_full_adder.a \
              obj_dir/libverilated.a -o $(SIM_EXEC)
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

# Individual implementation tests
test_carry_lookahead:
	@echo "Testing Carry Lookahead Implementation..."
	$(VLOG) $(VLOG_FLAGS) -o simv_carry_lookahead.out ../../rtl/full_adder.v tb_full_adder.v
	$(VVP) simv_carry_lookahead.out
	@echo "Carry Lookahead test completed"

test_simple:
	@echo "Testing Simple XOR/AND Implementation..."
ifeq ($(SIM),verilator)
	verilator --cc --build --trace --top-module tb_full_adder_simple --timing -I../../rtl ../../rtl/full_adder_simple.v tb_full_adder_simple.v && \
	c++ -I. -Iobj_dir -I$(VERILATOR_INCLUDE) \
	-I$(VERILATOR_VLTSTD) \
	-std=gnu++20 verilator_wrapper_simple.cpp obj_dir/libVtb_full_adder_simple.a \
	obj_dir/libverilated.a -o verilator_simple_sim && \
	./verilator_simple_sim
else
	$(VLOG) $(VLOG_FLAGS) -o simv_simple.out ../../rtl/full_adder_simple.v tb_full_adder_simple.v
	$(VVP) simv_simple.out
endif
	@echo "Simple implementation test completed"

test_half_adder:
	@echo "Testing Half Adder Modular Implementation..."
ifeq ($(SIM),verilator)
	verilator --cc --build --trace --top-module tb_full_adder_half_adder --timing -I../../rtl ../../rtl/full_adder_half_adder.v tb_full_adder_half_adder.v && \
	c++ -I. -Iobj_dir -I$(VERILATOR_INCLUDE) \
	-I$(VERILATOR_VLTSTD) \
	-std=gnu++20 verilator_wrapper_half_adder.cpp obj_dir/libVtb_full_adder_half_adder.a \
	obj_dir/libverilated.a -o verilator_half_adder_sim && \
	./verilator_half_adder_sim
else
	$(VLOG) $(VLOG_FLAGS) -o simv_half_adder.out ../../rtl/full_adder_half_adder.v tb_full_adder_half_adder.v
	$(VVP) simv_half_adder.out
endif
	@echo "Half Adder modular test completed"

test_all_implementations: test_carry_lookahead test_simple test_half_adder
	@echo "All three implementations tested successfully!"

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

# Debug target
debug:
	@echo "OS Detection Debug Info:"
	@echo "  UNAME_S: $(UNAME_S)"
	@echo "  VERILATOR_INCLUDE: $(VERILATOR_INCLUDE)"
	@echo "  VERILATOR_VLTSTD: $(VERILATOR_VLTSTD)"
	@echo "  SIM: $(SIM)"

# Help target
help:
	@echo "Full Adder SystemVerilog Testbench Makefile"
	@echo "==========================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all                    - Compile and run (default)"
	@echo "  compile                - Compile the design and testbench"
	@echo "  run                    - Run the simulation"
	@echo "  test_basic             - Run basic functionality test"
	@echo "  test_random            - Run random input test"
	@echo "  test_all               - Run all tests"
	@echo "  test_carry_lookahead   - Test carry lookahead implementation"
	@echo "  test_simple            - Test simple XOR/AND implementation"
	@echo "  test_half_adder        - Test half adder modular implementation"
	@echo "  test_all_implementations - Test all three implementations"
	@echo "  waves                  - View waveforms"
	@echo "  clean                  - Clean build artifacts"
	@echo "  debug                  - Show OS detection and path info"
	@echo "  help                   - Show this help message"
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

.PHONY: all compile run test_basic test_random test_all waves clean debug help 