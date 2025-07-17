# Full Adder IP

A configurable full adder IP with three implementation approaches, following Vyges conventions for hardware IP development.

## Overview

The Full Adder IP provides three different implementation approaches for the fundamental digital arithmetic component that performs addition of three binary inputs and produces sum and carry outputs. Each implementation is optimized for different use cases and performance requirements.

## IP Information

- **IP Name**: `vyges/full-adder-ip`
- **Version**: 1.0.0
- **License**: Apache-2.0
- **Maturity**: Production
- **Target**: ASIC, FPGA
- **Design Type**: Digital Combinational Logic

## Implementation Approaches

### 1. Carry Lookahead Implementation (`full_adder.v`) - **Recommended**
- **Use Case**: Multi-bit adders, performance-critical applications
- **Features**: Propagate and generate logic, scalable design
- **Gate Count**: 6 gates
- **Performance**: Best for larger designs

### 2. Simple XOR/AND Implementation (`full_adder_simple.v`)
- **Use Case**: Single full adder, area/power critical designs
- **Features**: Minimal gate count, direct implementation
- **Gate Count**: 5 gates
- **Performance**: Most efficient for single instances

### 3. Half Adder Modular Implementation (`full_adder_half_adder.v`)
- **Use Case**: Educational projects, modular design demonstrations
- **Features**: Hierarchical structure, reusable components
- **Gate Count**: 6 gates
- **Performance**: Good for educational purposes

## Module Interface

```systemverilog
module full_adder (
    input  logic clk_i,     // Clock input (for UVM compatibility)
    input  logic reset_n_i, // Active low reset (for UVM compatibility)
    input  logic a_i,       // First input bit
    input  logic b_i,       // Second input bit
    input  logic cin_i,     // Carry input from previous stage
    output logic sum_o,     // Sum output
    output logic cout_o     // Carry output to next stage
);
```

## Truth Table

| a_i | b_i | cin_i | sum_o | cout_o | Decimal Result |
|-----|-----|-------|-------|--------|----------------|
| 0   | 0   | 0     | 0     | 0      | 0 + 0 + 0 = 0  |
| 0   | 0   | 1     | 1     | 0      | 0 + 0 + 1 = 1  |
| 0   | 1   | 0     | 1     | 0      | 0 + 1 + 0 = 1  |
| 0   | 1   | 1     | 0     | 1      | 0 + 1 + 1 = 2  |
| 1   | 0   | 0     | 1     | 0      | 1 + 0 + 0 = 1  |
| 1   | 0   | 1     | 0     | 1      | 1 + 0 + 1 = 2  |
| 1   | 1   | 0     | 0     | 1      | 1 + 1 + 0 = 2  |
| 1   | 1   | 1     | 1     | 1      | 1 + 1 + 1 = 3  |

## Quick Start

### Simulation

#### SystemVerilog Testbench (Simplest)
```bash
# Using Icarus Verilog
cd tb/sv_tb
make test_basic SIM=icarus

# Using Verilator
make test_all SIM=verilator
```

#### UVM Testbench (Most Comprehensive)
```bash
# Using Questa/ModelSim
cd tb/uvm_tb
make test_basic SIM=questa
make gui SIM=questa  # For waveform viewing

# Using VCS
make test_all SIM=vcs
```

#### Cocotb Testbench (Python-based)
```bash
# Using Icarus Verilog
cd tb/cocotb
make test_basic SIM=icarus

# Using Verilator
make test_all SIM=verilator
```

#### Master Makefile (All Testbench Types)
```bash
# Run any testbench type from the main tb directory
cd tb
make test_basic TESTBENCH_TYPE=sv SIM=icarus
make test_all TESTBENCH_TYPE=uvm SIM=questa
make test_all TESTBENCH_TYPE=cocotb SIM=verilator

# Test all three testbench types
make test_all_types
```

### Instantiation Example

```systemverilog
// Carry Lookahead Implementation (Recommended)
full_adder fa_inst (
    .clk_i(clk),
    .reset_n_i(reset_n),
    .a_i(a),
    .b_i(b),
    .cin_i(cin),
    .sum_o(sum),
    .cout_o(cout)
);
```

### Multi-bit Adder Example

See `integration/ripple_carry_adder.v` for a complete 4-bit ripple carry adder example.

## File Structure

```
full-adder-ip/
├── rtl/
│   ├── full_adder.v              # Carry lookahead implementation
│   ├── full_adder_simple.v       # Simple XOR/AND implementation
│   └── full_adder_half_adder.v   # Half adder modular implementation
├── tb/
│   ├── README.md                 # Testbench documentation
│   ├── Makefile                  # Master testbench Makefile
│   ├── sv_tb/                    # SystemVerilog testbench
│   │   ├── Makefile             # SystemVerilog Makefile
│   │   └── tb_full_adder.v      # Universal testbench
│   ├── uvm_tb/                   # UVM testbench
│   │   ├── Makefile             # UVM Makefile
│   │   ├── full_adder_if.sv     # Virtual interface
│   │   ├── full_adder_pkg.sv    # UVM package with all components
│   │   └── tb_full_adder_uvm.sv # Top-level UVM testbench
│   └── cocotb/                   # Cocotb testbench
│       ├── Makefile             # Cocotb Makefile
│       └── test_full_adder.py   # Python-based testbench
├── docs/
│   ├── full_adder_design_specification.md   # Complete design specification
│   ├── full_adder.md            # Detailed documentation
│   └── full_adder_3.svg         # Block diagram
├── integration/
│   └── ripple_carry_adder.v      # Multi-bit example
├── vyges-metadata.json          # IP metadata
├── .vyges-ai-context.json       # AI development context
└── README.md                    # This file
```

## Testbench Types

### 1. SystemVerilog Testbench (`tb/sv_tb/`)
- **Purpose**: Simple, direct verification approach
- **Best for**: Quick verification, learning, simple designs
- **Features**: Direct signal manipulation, manual test case generation, basic error reporting
- **Simulators**: Icarus Verilog, Verilator, Questa/ModelSim, VCS

### 2. UVM Testbench (`tb/uvm_tb/`)
- **Purpose**: Advanced verification methodology
- **Best for**: Complex verification, reusable components, team environments
- **Features**: Component-based architecture, reusable verification components, advanced features (coverage, sequences, factory patterns)
- **Components**: Transaction, Driver, Monitor, Scoreboard, Agent, Environment, Sequences, Tests
- **Simulators**: Questa/ModelSim, VCS, Xcelium, Verilator (limited)

### 3. Cocotb Testbench (`tb/cocotb/`)
- **Purpose**: Python-based verification
- **Best for**: Python developers, rapid prototyping, custom verification logic
- **Features**: Python-based test development, easy integration with Python libraries, cross-simulator compatibility, async/await support
- **Test Scenarios**: Basic functionality, random input testing, edge cases, reset functionality, timing analysis, coverage scenarios
- **Simulators**: Icarus Verilog, Verilator, Questa/ModelSim, VCS

## Performance Specifications

| Parameter | Value | Units |
|-----------|-------|-------|
| Max Frequency | 500 | MHz |
| Propagation Delay | 300 | ps |
| Area (ASIC) | 50 | μm² |
| Power | 0.1 | mW |
| LUT Count (FPGA) | 3 | LUTs |

## Tool Support

- **Simulators**: Verilator, Icarus Verilog, ModelSim/QuestaSim, VCS, Xcelium
- **Synthesis**: OpenLane (ASIC), Vivado (FPGA), Yosys
- **PDKs**: Sky130B, GF180MCU
- **Linting**: Verilator (clean)
- **Verification**: UVM, Cocotb, SystemVerilog

## Test Coverage

- ✅ 100% functional coverage (all 8 input combinations)
- ✅ Timing analysis
- ✅ Universal testbench compatibility
- ✅ VCD waveform generation
- ✅ UVM methodology implementation
- ✅ Python-based verification with Cocotb
- ✅ Cross-simulator compatibility

## Vyges Compliance

This IP follows all Vyges conventions:
- ✅ Snake_case naming for modules and files
- ✅ Signal suffixes (_i, _o) for direction
- ✅ Required module headers with metadata
- ✅ Proper file organization
- ✅ Comprehensive documentation
- ✅ Universal testbench compatibility
- ✅ Multiple verification methodologies

## Documentation

- [Design Specification](docs/full_adder_design_specification.md) - Complete technical specification and implementation guide
- [Testbench Documentation](tb/README.md) - Comprehensive guide for all testbench types
- [Block Diagram](docs/full_adder_3.svg) - Visual representation

## License

Apache-2.0 License - see [LICENSE](LICENSE) file for details.

## Contributing

This IP follows Vyges development conventions. See `.vyges-ai-context.json` for development guidelines.

## References

- [Full Adder Explanation](https://www.geeksforgeeks.org/digital-logic/full-adder-in-digital-logic/)
- [UVM User Guide](https://www.accellera.org/downloads/standards/uvm)
- [Cocotb Documentation](https://docs.cocotb.org/)
- [Vyges IP Development Guide](https://vyges.com/docs/ip-development)
