#==============================================================================
# Full Adder UVM Testbench Makefile
#==============================================================================
# Description: Makefile for running UVM testbench with various simulators
# Author:      Vyges Team
# Date:        2025-07-17
# Version:     1.0.0
#==============================================================================

# Defaults
SIM ?= questa
TOPLEVEL = tb_full_adder_uvm

# UVM version and library path
UVM_VERSION ?= 1.2
UVM_HOME ?= $(shell find /opt -name "uvm-$(UVM_VERSION)" -type d 2>/dev/null | head -1)
ifndef UVM_HOME
    UVM_HOME ?= /usr/local/uvm-$(UVM_VERSION)
endif

# Source files
RTL_SOURCES = ../../rtl/full_adder.v
UVM_SOURCES = full_adder_if.sv full_adder_pkg.sv tb_full_adder_uvm.sv

# Compiler flags
VLOG_FLAGS = -sv -mfcu -suppress 2181
VSIM_FLAGS = -c -do "run -all; quit"

# Simulator-specific settings
ifeq ($(SIM),questa)
    # Questa/ModelSim settings
    VLOG = vlog
    VSIM = vsim
    VLOG_FLAGS += +incdir+$(UVM_HOME)/src $(UVM_HOME)/src/uvm_pkg.sv
    VSIM_FLAGS += -sv_lib uvm_dpi
else ifeq ($(SIM),vcs)
    # VCS settings
    VLOG = vcs
    VSIM = simv
    VLOG_FLAGS += -full64 -sverilog +incdir+$(UVM_HOME)/src
    VLOG_FLAGS += +define+UVM_OBJECT_MUST_HAVE_CONSTRUCTOR
    VSIM_FLAGS = -c -do "run -all; quit"
else ifeq ($(SIM),xrun)
    # Xcelium settings
    VLOG = xrun
    VSIM = xrun
    VLOG_FLAGS += -64bit -sv -uvm -uvmhome $(UVM_HOME)
    VSIM_FLAGS = -R -c
else ifeq ($(SIM),verilator)
    # Verilator settings (limited UVM support)
    VLOG = verilator
    VSIM = obj_dir/V$(TOPLEVEL)
    VLOG_FLAGS += --cc --exe --build -CFLAGS "-I$(UVM_HOME)/src"
    VSIM_FLAGS = --trace --trace-structs
endif

# Default target
all: compile run

# Compile target
compile:
	@echo "Compiling UVM testbench with $(SIM)..."
	@echo "UVM_HOME: $(UVM_HOME)"
ifeq ($(SIM),questa)
	$(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(UVM_SOURCES)
else ifeq ($(SIM),vcs)
	$(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(UVM_SOURCES) -o $(VSIM)
else ifeq ($(SIM),xrun)
	$(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(UVM_SOURCES)
else ifeq ($(SIM),verilator)
	$(VLOG) $(VLOG_FLAGS) $(RTL_SOURCES) $(UVM_SOURCES) -o $(VSIM)
endif
	@echo "Compilation complete"

# Run target
run:
	@echo "Running UVM testbench..."
ifeq ($(SIM),questa)
	$(VSIM) $(VSIM_FLAGS) $(TOPLEVEL) -sv_lib uvm_dpi
else ifeq ($(SIM),vcs)
	./$(VSIM) $(VSIM_FLAGS)
else ifeq ($(SIM),xrun)
	$(VSIM) $(VSIM_FLAGS) $(TOPLEVEL)
else ifeq ($(SIM),verilator)
	./$(VSIM) $(VSIM_FLAGS)
endif
	@echo "Simulation complete"

# GUI target for Questa
gui:
ifeq ($(SIM),questa)
	$(VSIM) -gui $(TOPLEVEL) -sv_lib uvm_dpi
else
	@echo "GUI mode only supported with Questa/ModelSim"
endif

# Waveform viewing
waves:
ifeq ($(SIM),questa)
	$(VSIM) -view vsim.wlf
else ifeq ($(SIM),vcs)
	@echo "Use DVE or Verdi to view VCS waveforms"
else ifeq ($(SIM),xrun)
	@echo "Use SimVision to view Xcelium waveforms"
else ifeq ($(SIM),verilator)
	@echo "Use GTKWave to view Verilator waveforms: gtkwave full_adder_uvm.vcd"
endif

# Test targets
test_basic: compile
	@echo "Running basic functionality test..."
	$(VSIM) $(VSIM_FLAGS) $(TOPLEVEL) +UVM_TESTNAME=basic_functionality_test

test_random: compile
	@echo "Running random test..."
	$(VSIM) $(VSIM_FLAGS) $(TOPLEVEL) +UVM_TESTNAME=random_test

test_all: test_basic test_random

# Coverage target
coverage:
ifeq ($(SIM),questa)
	$(VSIM) $(VSIM_FLAGS) $(TOPLEVEL) -coverage -cvgperinstance
else ifeq ($(SIM),vcs)
	$(VLOG) $(VLOG_FLAGS) -cm line+cond+fsm $(RTL_SOURCES) $(UVM_SOURCES) -o $(VSIM)
	./$(VSIM) $(VSIM_FLAGS) -cm line+cond+fsm
else
	@echo "Coverage not configured for $(SIM)"
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
	rm -rf *.vdb
	rm -rf *.ucdb
	rm -rf *.xml
	rm -rf *.html
	rm -rf *.txt

# Help target
help:
	@echo "Full Adder UVM Testbench Makefile"
	@echo "=================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all           - Compile and run (default)"
	@echo "  compile       - Compile the design and testbench"
	@echo "  run           - Run the simulation"
	@echo "  gui           - Run with GUI (Questa only)"
	@echo "  waves         - View waveforms"
	@echo "  test_basic    - Run basic functionality test"
	@echo "  test_random   - Run random test"
	@echo "  test_all      - Run all tests"
	@echo "  coverage      - Run with coverage collection"
	@echo "  clean         - Clean build artifacts"
	@echo "  help          - Show this help message"
	@echo ""
	@echo "Available simulators (set SIM=<simulator>):"
	@echo "  questa        - Questa/ModelSim (default)"
	@echo "  vcs           - VCS"
	@echo "  xrun          - Xcelium"
	@echo "  verilator     - Verilator (limited UVM support)"
	@echo ""
	@echo "Environment variables:"
	@echo "  UVM_HOME      - Path to UVM library (auto-detected)"
	@echo "  UVM_VERSION   - UVM version (default: 1.2)"
	@echo ""
	@echo "Example usage:"
	@echo "  make test_basic SIM=questa"
	@echo "  make gui SIM=questa"
	@echo "  make test_all SIM=vcs"

.PHONY: all compile run gui waves test_basic test_random test_all coverage clean help 