# Full Adder Cocotb Testbench

This directory contains comprehensive cocotb testbenches for verifying all three full adder implementations.

## Overview

The cocotb testbench provides Python-based verification for the full adder IP with support for:
- **Carry Lookahead Implementation** (`full_adder.v`)
- **Simple XOR/AND Implementation** (`full_adder_simple.v`) 
- **Half Adder Modular Implementation** (`full_adder_half_adder.v`)

## Testbench Files

### Core Testbench
- `test_full_adder.py` - Original comprehensive testbench with all test scenarios
- `test_all_implementations.py` - Enhanced testbench for testing all three implementations

### Configuration
- `Makefile` - Build and simulation configuration for multiple simulators

## Supported Simulators

The testbench supports multiple simulators:
- **Icarus Verilog** (default) - Fast compilation, interpreted simulation
- **Verilator** - High-speed compiled simulation with C++ wrapper
- **Questa/ModelSim** - Commercial simulator support
- **VCS** - Synopsys VCS support

## Test Scenarios

### Basic Functionality Tests
- All 8 input combinations (000, 001, 010, 011, 100, 101, 110, 111)
- Expected output verification for sum and carry

### Advanced Test Scenarios
- **Random Input Testing** - 100 random input combinations
- **Edge Case Testing** - Rapid input changes and timing
- **Reset Functionality** - Reset behavior verification
- **Timing Analysis** - Propagation delay testing
- **Coverage Scenarios** - Comprehensive coverage testing

## Usage

### Prerequisites
```bash
# Install cocotb
pip install cocotb

# For specific simulators
pip install cocotb[icarus]      # Icarus Verilog
pip install cocotb[verilator]   # Verilator
pip install cocotb[questa]      # Questa/ModelSim
pip install cocotb[vcs]         # VCS
```

### Running Tests

#### Test Individual Implementations
```bash
# Test carry lookahead implementation
make test_carry_lookahead SIM=icarus

# Test simple XOR/AND implementation  
make test_simple SIM=verilator

# Test half adder modular implementation
make test_half_adder SIM=questa
```

#### Test All Implementations
```bash
# Test all three implementations
make test_all_implementations SIM=icarus

# Use enhanced testbench
make test_enhanced SIM=verilator
```

#### Legacy Commands (Backward Compatible)
```bash
# Original test commands still work
make test_basic SIM=icarus
make test_random SIM=verilator
make test_all SIM=questa
```

### Simulator-Specific Examples

#### Icarus Verilog
```bash
make test_carry_lookahead SIM=icarus
```

#### Verilator
```bash
make test_simple SIM=verilator
```

#### Questa/ModelSim
```bash
make test_half_adder SIM=questa
```

#### VCS
```bash
make test_all_implementations SIM=vcs
```

## Test Output

### Success Example
```
==============================================================================
FULL ADDER COCOTB TESTBENCH
==============================================================================
[INFO] Setting up testbench for Carry Lookahead...
[INFO] Testbench setup complete for Carry Lookahead
[INFO] [Carry Lookahead] PASS 0+0+0=0: a_i=0, b_i=0, cin_i=0, sum_o=0, cout_o=0
[INFO] [Carry Lookahead] PASS 0+0+1=1: a_i=0, b_i=0, cin_i=1, sum_o=1, cout_o=0
...
==============================================================================
TEST SUMMARY - Carry Lookahead
==============================================================================
Total Tests: 8
Passed: 8
Failed: 0
Success Rate: 100.0%
==============================================================================
```

### Error Example
```
[ERROR] [Simple XOR/AND] FAIL 1+1+1=3: a_i=1, b_i=1, cin_i=1, 
        sum_o=0 (expected 1), cout_o=1 (expected 1)
```

## Test Configuration

### Timing Parameters
- **Clock Period**: 10ns (100MHz)
- **Reset Delay**: 100ns
- **Test Timeout**: 10000ns

### Test Counts
- **Basic Tests**: 8 combinations
- **Random Tests**: 100 combinations
- **Edge Case Tests**: 30 combinations
- **Coverage Tests**: 8 scenarios

## Waveform Generation

The testbench generates VCD waveforms for analysis:
- `full_adder.vcd` - Carry lookahead implementation
- `full_adder_simple.vcd` - Simple implementation
- `full_adder_half_adder.vcd` - Half adder implementation

## Cleanup

```bash
# Clean all build artifacts
make clean
```

This removes:
- Python cache files
- Simulation build directories
- Waveform files
- Log files

## Integration with CI/CD

The testbench is designed for continuous integration:

```yaml
# Example GitHub Actions workflow
- name: Run Cocotb Tests
  run: |
    cd tb/cocotb
    make test_all_implementations SIM=icarus
    make test_all_implementations SIM=verilator
```

## Troubleshooting

### Common Issues

1. **Simulator Not Found**
   ```bash
   # Check simulator installation
   which iverilog    # Icarus
   which verilator    # Verilator
   ```

2. **Cocotb Not Installed**
   ```bash
   pip install cocotb
   ```

3. **Import Errors**
   - Ensure cocotb is in Python path
   - Check simulator-specific cocotb installation

### Debug Mode
```bash
# Enable verbose logging
export COCOTB_LOG_LEVEL=DEBUG
make test_carry_lookahead SIM=icarus
```

## Performance Comparison

| Simulator | Compilation | Simulation Speed | Memory Usage |
|-----------|-------------|------------------|--------------|
| Icarus    | Fast        | Moderate         | Low          |
| Verilator | Slow        | Very Fast        | High         |
| Questa    | Moderate    | Fast             | High         |
| VCS       | Moderate    | Fast             | High         |

## Contributing

When adding new tests:
1. Follow the existing test structure
2. Add proper logging and assertions
3. Update the Makefile if needed
4. Document new test scenarios

## License

This testbench follows the same license as the main project. 