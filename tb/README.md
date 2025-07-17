# Full Adder Testbenches

This directory contains comprehensive testbenches for the full adder IP following Vyges conventions. Both UVM and cocotb testbenches are provided to support different verification methodologies and simulator preferences.

## Directory Structure

```
tb/
├── README.md                 # This file
├── Makefile                  # Main testbench Makefile
├── sv_tb/                    # SystemVerilog testbench
│   └── tb_full_adder.v      # Simple SystemVerilog testbench
├── uvm_tb/                   # UVM testbench
│   ├── Makefile             # UVM-specific Makefile
│   ├── full_adder_if.sv     # Virtual interface
│   ├── full_adder_pkg.sv    # UVM package with all components
│   └── tb_full_adder_uvm.sv # Top-level UVM testbench
└── cocotb/                   # Cocotb testbench
    ├── Makefile             # Cocotb-specific Makefile
    └── test_full_adder.py   # Python-based testbench
```

## Testbench Types

### 1. SystemVerilog Testbench (`sv_tb/`)

**Purpose**: Simple, direct verification approach
**Best for**: Quick verification, learning, simple designs
**Features**:
- Direct signal manipulation
- Manual test case generation
- Basic error reporting
- Waveform generation

**Usage**:
```bash
cd tb/sv_tb
make
```

### 2. UVM Testbench (`uvm_tb/`)

**Purpose**: Advanced verification methodology
**Best for**: Complex verification, reusable components, team environments
**Features**:
- Component-based architecture
- Reusable verification components
- Advanced features (coverage, sequences, factory patterns)
- Multiple test types
- Professional verification methodology

**Components**:
- **Transaction**: `full_adder_transaction` - Data structure for inputs/outputs
- **Driver**: `full_adder_driver` - Drives transactions to DUT
- **Monitor**: `full_adder_monitor` - Observes DUT interface
- **Scoreboard**: `full_adder_scoreboard` - Checks correctness
- **Agent**: `full_adder_agent` - Contains driver, monitor, sequencer
- **Environment**: `full_adder_env` - Contains all verification components
- **Sequences**: `basic_test_sequence`, `random_test_sequence`
- **Tests**: `basic_functionality_test`, `random_test`

**Usage**:
```bash
cd tb/uvm_tb
make test_basic SIM=questa
make test_random SIM=vcs
make gui SIM=questa  # For waveform viewing
```

### 3. Cocotb Testbench (`cocotb/`)

**Purpose**: Python-based verification
**Best for**: Python developers, rapid prototyping, custom verification logic
**Features**:
- Python-based test development
- Easy integration with Python libraries
- Cross-simulator compatibility
- Async/await support for complex scenarios

**Test Scenarios**:
- Basic functionality (all 8 input combinations)
- Random input testing (100 random cases)
- Edge case testing (rapid input changes)
- Reset functionality testing
- Timing analysis
- Coverage scenarios

**Usage**:
```bash
cd tb/cocotb
make test_basic SIM=icarus
make test_all SIM=verilator
```

## Simulator Support

### UVM Testbench
- **Questa/ModelSim**: Full support with GUI
- **VCS**: Full support with coverage
- **Xcelium**: Full support
- **Verilator**: Limited support (basic functionality)

### Cocotb Testbench
- **Icarus Verilog**: Full support
- **Verilator**: Full support with tracing
- **Questa/ModelSim**: Full support
- **VCS**: Full support

## Running Tests

### Quick Start

1. **SystemVerilog** (simplest):
   ```bash
   cd tb/sv_tb
   make
   ```

2. **UVM** (most comprehensive):
   ```bash
   cd tb/uvm_tb
   make test_all SIM=questa
   ```

3. **Cocotb** (Python-based):
   ```bash
   cd tb/cocotb
   make test_all SIM=icarus
   ```

### Advanced Usage

#### UVM Testbench
```bash
# Run specific test
make test_basic SIM=questa +UVM_TESTNAME=basic_functionality_test

# Run with GUI
make gui SIM=questa

# Run with coverage
make coverage SIM=questa

# Run with different simulator
make test_all SIM=vcs
```

#### Cocotb Testbench
```bash
# Run with different simulator
make test_basic SIM=verilator

# View waveforms (Verilator)
gtkwave full_adder.vcd

# Run specific test scenarios
python -m pytest test_full_adder.py::test_basic_functionality
```

## Test Coverage

All testbenches provide comprehensive coverage:

1. **Functional Coverage**:
   - All 8 input combinations (000, 001, 010, 011, 100, 101, 110, 111)
   - Expected outputs verification
   - Error detection and reporting

2. **Timing Coverage**:
   - Reset functionality
   - Propagation delays
   - Edge case timing

3. **Random Coverage**:
   - Random input combinations
   - Stress testing
   - Coverage-driven verification (UVM)

## Waveform Analysis

### UVM Testbench
```bash
cd tb/uvm_tb
make gui SIM=questa
# Use ModelSim GUI to view waveforms
```

### Cocotb Testbench
```bash
cd tb/cocotb
make SIM=verilator
gtkwave full_adder.vcd
```

### SystemVerilog Testbench
```bash
cd tb/sv_tb
make
gtkwave full_adder.vcd
```

## Verification Metrics

### UVM Testbench
- **Coverage**: Line, condition, FSM coverage
- **Assertions**: Built-in UVM assertions
- **Scoreboarding**: Automatic result checking
- **Reporting**: Detailed test reports

### Cocotb Testbench
- **Test Results**: Pass/fail statistics
- **Logging**: Detailed test execution logs
- **Performance**: Execution time tracking

## Troubleshooting

### Common Issues

1. **UVM Library Not Found**:
   ```bash
   export UVM_HOME=/path/to/uvm/library
   ```

2. **Cocotb Not Installed**:
   ```bash
   pip install cocotb
   ```

3. **Simulator Not Found**:
   ```bash
   # Add simulator to PATH
   export PATH=$PATH:/path/to/simulator/bin
   ```

### Debug Tips

1. **Enable Verbose Logging**:
   ```bash
   # UVM
   make run SIM=questa +UVM_VERBOSITY=UVM_HIGH

   # Cocotb
   export COCOTB_LOG_LEVEL=DEBUG
   ```

2. **Generate Waveforms**:
   ```bash
   # All testbenches support VCD generation
   # Use appropriate viewer based on simulator
   ```

## Performance Comparison

| Aspect | SystemVerilog | UVM | Cocotb |
|--------|---------------|-----|--------|
| Setup Time | Fast | Medium | Fast |
| Learning Curve | Low | High | Medium |
| Reusability | Low | High | Medium |
| Feature Richness | Basic | Advanced | Good |
| Simulator Support | Universal | Limited | Universal |
| Debug Capability | Basic | Advanced | Good |

## Recommendations

- **For Learning**: Start with SystemVerilog testbench
- **For Production**: Use UVM testbench
- **For Python Teams**: Use Cocotb testbench
- **For Quick Verification**: Use SystemVerilog or Cocotb
- **For Complex Projects**: Use UVM testbench

## Contributing

When adding new testbenches or modifying existing ones:

1. Follow Vyges naming conventions
2. Include proper module headers
3. Add comprehensive documentation
4. Update this README
5. Ensure cross-simulator compatibility
6. Add appropriate Makefiles

## References

- [UVM User Guide](https://www.accellera.org/downloads/standards/uvm)
- [Cocotb Documentation](https://docs.cocotb.org/)
- [SystemVerilog LRM](https://ieeexplore.ieee.org/document/8299595)
- [Vyges Conventions](../docs/full_adder_design_specification.md) 