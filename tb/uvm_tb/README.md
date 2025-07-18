# Full Adder UVM Testbench

This directory contains comprehensive UVM testbenches for verifying all three full adder implementations.

## Overview

The UVM testbench provides industry-standard verification methodology for the full adder IP with support for:
- **Carry Lookahead Implementation** (`full_adder.v`)
- **Simple XOR/AND Implementation** (`full_adder_simple.v`) 
- **Half Adder Modular Implementation** (`full_adder_half_adder.v`)

## Testbench Files

### UVM Components
- `full_adder_if.sv` - Virtual interface for full adder signals
- `full_adder_pkg.sv` - Complete UVM package with transactions, agents, and tests
- `tb_full_adder_uvm.sv` - Top-level UVM testbench

### Simplified SystemVerilog Testbenches
- `tb_full_adder_simple_sv.sv` - Simplified testbench for carry lookahead
- `tb_full_adder_simple_impl.sv` - Simplified testbench for simple implementation
- `tb_full_adder_half_adder_impl.sv` - Simplified testbench for half adder implementation

### Configuration
- `Makefile` - Build and simulation configuration for commercial simulators
- `Makefile.simple` - Build and simulation configuration for open-source simulators

## Supported Simulators

### Commercial Simulators (Full UVM Support)
- **Questa/ModelSim** - Complete UVM support with GUI
- **VCS** - Synopsys VCS with full UVM capabilities
- **Xcelium** - Cadence Xcelium with UVM support

### Open-Source Simulators (Simplified Testing)
- **Icarus Verilog** - Fast compilation and simulation
- **Verilator** - High-speed compiled simulation (limited timing support)

## Test Results

### ✅ All Implementations Verified Successfully

#### Carry Lookahead Implementation
```
=== Full Adder Simple SystemVerilog Testbench ===
PASS Test 1: a_i=0, b_i=0, cin_i=0, sum_o=0, cout_o=0
PASS Test 2: a_i=1, b_i=0, cin_i=0, sum_o=1, cout_o=0
PASS Test 3: a_i=0, b_i=1, cin_i=0, sum_o=1, cout_o=0
PASS Test 4: a_i=1, b_i=1, cin_i=0, sum_o=0, cout_o=1
PASS Test 5: a_i=0, b_i=0, cin_i=1, sum_o=1, cout_o=0
PASS Test 6: a_i=1, b_i=0, cin_i=1, sum_o=0, cout_o=1
PASS Test 7: a_i=0, b_i=1, cin_i=1, sum_o=0, cout_o=1
PASS Test 8: a_i=1, b_i=1, cin_i=1, sum_o=1, cout_o=1
=== Test Summary ===
Total Tests: 8
Passed: 8
Failed: 0
Success Rate: 100.0%
=== ALL TESTS PASSED ===
```

#### Simple XOR/AND Implementation
```
=== Full Adder Simple Implementation Testbench ===
PASS Test 1: a_i=0, b_i=0, cin_i=0, sum_o=0, cout_o=0
PASS Test 2: a_i=1, b_i=0, cin_i=0, sum_o=1, cout_o=0
PASS Test 3: a_i=0, b_i=1, cin_i=0, sum_o=1, cout_o=0
PASS Test 4: a_i=1, b_i=1, cin_i=0, sum_o=0, cout_o=1
PASS Test 5: a_i=0, b_i=0, cin_i=1, sum_o=1, cout_o=0
PASS Test 6: a_i=1, b_i=0, cin_i=1, sum_o=0, cout_o=1
PASS Test 7: a_i=0, b_i=1, cin_i=1, sum_o=0, cout_o=1
PASS Test 8: a_i=1, b_i=1, cin_i=1, sum_o=1, cout_o=1
=== Test Summary ===
Total Tests: 8
Passed: 8
Failed: 0
Success Rate: 100.0%
=== ALL TESTS PASSED ===
```

#### Half Adder Modular Implementation
```
=== Full Adder Half Adder Implementation Testbench ===
PASS Test 1: a_i=0, b_i=0, cin_i=0, sum_o=0, cout_o=0
PASS Test 2: a_i=1, b_i=0, cin_i=0, sum_o=1, cout_o=0
PASS Test 3: a_i=0, b_i=1, cin_i=0, sum_o=1, cout_o=0
PASS Test 4: a_i=1, b_i=1, cin_i=0, sum_o=0, cout_o=1
PASS Test 5: a_i=0, b_i=0, cin_i=1, sum_o=1, cout_o=0
PASS Test 6: a_i=1, b_i=0, cin_i=1, sum_o=0, cout_o=1
PASS Test 7: a_i=0, b_i=1, cin_i=1, sum_o=0, cout_o=1
PASS Test 8: a_i=1, b_i=1, cin_i=1, sum_o=1, cout_o=1
=== Test Summary ===
Total Tests: 8
Passed: 8
Failed: 0
Success Rate: 100.0%
=== ALL TESTS PASSED ===
```

## UVM Testbench Components

### Transaction Class
- `full_adder_transaction` - UVM sequence item with input/output data
- Random constraint generation for comprehensive testing
- Expected output calculation and comparison

### Driver Class
- `full_adder_driver` - Drives transactions to DUT interface
- Clock-synchronized signal driving
- Proper handshaking with sequencer

### Monitor Class
- `full_adder_monitor` - Observes DUT behavior
- Transaction capture and analysis port
- Real-time verification feedback

### Scoreboard Class
- `full_adder_scoreboard` - Functional verification
- Expected vs actual output comparison
- Test statistics and reporting

### Agent Class
- `full_adder_agent` - Complete verification component
- Driver, monitor, and sequencer integration
- Configurable active/passive modes

### Test Classes
- `basic_functionality_test` - All 8 input combinations
- `random_test` - Random input verification
- `coverage_test` - Coverage-driven testing

## Usage

### Prerequisites
```bash
# For commercial simulators
# Questa/ModelSim, VCS, or Xcelium must be installed
# UVM library must be available

# For open-source simulators
# Icarus Verilog and/or Verilator must be installed
```

### Running Tests

#### Commercial Simulators (Full UVM)
```bash
# Questa/ModelSim
make test_basic SIM=questa
make gui SIM=questa

# VCS
make test_all SIM=vcs

# Xcelium
make test_basic SIM=xrun
```

#### Open-Source Simulators (Simplified)
```bash
# Icarus Verilog
make -f Makefile.simple test_carry_lookahead SIM=icarus
make -f Makefile.simple test_simple SIM=icarus
make -f Makefile.simple test_half_adder SIM=icarus

# Manual compilation
iverilog -g2012 ../../rtl/full_adder.v tb_full_adder_simple_sv.sv
vvp a.out
```

### Test All Implementations
```bash
# Using simplified testbenches
iverilog -g2012 ../../rtl/full_adder.v tb_full_adder_simple_sv.sv && vvp a.out
iverilog -g2012 ../../rtl/full_adder_simple.v tb_full_adder_simple_impl.sv && vvp a.out
iverilog -g2012 ../../rtl/full_adder_half_adder.v tb_full_adder_half_adder_impl.sv && vvp a.out
```

## Waveform Generation

The testbench generates VCD waveforms for analysis:
- `full_adder_simple_sv.vcd` - Carry lookahead implementation
- `full_adder_simple_impl.vcd` - Simple implementation
- `full_adder_half_adder_impl.vcd` - Half adder implementation

### Viewing Waveforms
```bash
# GTKWave (open-source)
gtkwave full_adder_simple_sv.vcd

# Questa/ModelSim
make waves SIM=questa
```

## Coverage Analysis

### Available Coverage Types
- **Line Coverage** - Statement execution
- **Condition Coverage** - Boolean expression evaluation
- **FSM Coverage** - State machine transitions
- **Toggle Coverage** - Signal transitions

### Running Coverage
```bash
# Questa/ModelSim
make coverage SIM=questa

# VCS
make coverage SIM=vcs
```

## Integration with CI/CD

The testbench is designed for continuous integration:

```yaml
# Example GitHub Actions workflow
- name: Run UVM Tests
  run: |
    cd tb/uvm_tb
    make -f Makefile.simple test_all SIM=icarus
```

## Troubleshooting

### Common Issues

1. **UVM Library Not Found**
   ```bash
   # Set UVM_HOME environment variable
   export UVM_HOME=/path/to/uvm/library
   ```

2. **Simulator Not Available**
   ```bash
   # Use simplified testbenches with open-source simulators
   make -f Makefile.simple test_carry_lookahead SIM=icarus
   ```

3. **Compilation Errors**
   ```bash
   # Check SystemVerilog syntax
   # Ensure all dependencies are included
   # Verify module names match
   ```

### Debug Mode
```bash
# Enable verbose logging
export UVM_VERBOSITY=UVM_HIGH
make test_basic SIM=questa
```

## Performance Comparison

| Simulator | UVM Support | Compilation Speed | Simulation Speed | Memory Usage |
|-----------|-------------|-------------------|------------------|--------------|
| Questa    | Full        | Moderate          | Fast             | High          |
| VCS       | Full        | Fast              | Very Fast        | High          |
| Xcelium   | Full        | Moderate          | Fast             | High          |
| Icarus    | None        | Very Fast         | Moderate         | Low           |
| Verilator | Limited     | Slow              | Very Fast        | High          |

## Contributing

When adding new tests:
1. Follow UVM methodology guidelines
2. Add proper coverage points
3. Update the Makefile if needed
4. Document new test scenarios

## License

This testbench follows the same license as the main project. 