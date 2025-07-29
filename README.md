# Full Adder IP

[![Vyges IP](https://img.shields.io/badge/Vyges-IP%20Template-blue?style=flat&logo=github)](https://vyges.com)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Maturity](https://img.shields.io/badge/Maturity-Production-brightgreen)](https://vyges.com/docs/maturity-levels)
[![Target](https://img.shields.io/badge/Target-ASIC%20%7C%20FPGA-orange)](https://vyges.com/docs/target-platforms)
[![Verification](https://img.shields.io/badge/Verification-Cocotb%20%7C%20SystemVerilog-purple)](https://vyges.com/docs/verification)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-blue?style=flat&logo=github)](https://vyges.github.io/full-adder-ip/)
[![Repository](https://img.shields.io/badge/Repository-GitHub-black?style=flat&logo=github)](https://github.com/vyges/full-adder-ip)
[![Issues](https://img.shields.io/badge/Issues-GitHub-orange?style=flat&logo=github)](https://github.com/vyges/full-adder-ip/issues)
[![Pull Requests](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat&logo=github)](https://github.com/vyges/full-adder-ip/pulls)

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

## 📊 Reports & Documentation

- **[GitHub Pages](https://vyges.github.io/full-adder-ip/)** - Live documentation and reports
- **[Synthesis Reports](https://vyges.github.io/full-adder-ip/flow/yosys/comprehensive_report.md)** - ASIC synthesis analysis
- **[FPGA Reports](https://vyges.github.io/full-adder-ip/flow/fpga/comprehensive_fpga_report.md)** - FPGA resource analysis
- **[Test Reports](https://vyges.github.io/full-adder-ip/test/)** - Verification and test results

## Implementation Approaches

### 1. Carry Lookahead Implementation (`full_adder.v`) - **Recommended**
- **Use Case**: Multi-bit adders, performance-critical applications
- **Features**: Propagate and generate logic, scalable design
- **Gate Count**: 5 primitive gates (32 transistors)
- **Design Style**: Flat design
- **Performance**: Best for larger designs

### 2. Simple XOR/AND Implementation (`full_adder_simple.v`)
- **Use Case**: Single full adder, area/power critical designs
- **Features**: Minimal gate count, direct implementation
- **Gate Count**: 5 primitive gates (32 transistors)
- **Design Style**: Flat design
- **Performance**: Most efficient for single instances

### 3. Half Adder Modular Implementation (`full_adder_half_adder.v`)
- **Use Case**: Educational projects, modular design demonstrations
- **Features**: Hierarchical structure, reusable components
- **Gate Count**: 7 primitive gates (48 transistors)
- **Design Style**: Hierarchical design
- **Performance**: Good for educational purposes

## Module Interface

```systemverilog
module full_adder (
    input  logic clk_i,     // Clock input
    input  logic reset_n_i, // Active low reset
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
make test_all TESTBENCH_TYPE=cocotb SIM=verilator

# Test all three testbench types
make test_all_types
```

### Synthesis

#### ASIC Synthesis (Yosys)
```bash
# Navigate to ASIC synthesis directory
cd flow/yosys

# Synthesize all implementations
make all

# Synthesize specific implementation
make carry_lookahead
make simple
make half_adder

# Generate gate analysis report
make gate_analysis

# Generate comprehensive report (synthesis + gate analysis)
make comprehensive_report

# Show available targets
make help
```

#### FPGA Synthesis (Yosys)
```bash
# Navigate to FPGA synthesis directory
cd flow/fpga

# Synthesize all implementations for FPGA
make all

# Synthesize specific implementation
make carry_lookahead
make simple
make half_adder

# Generate FPGA resource analysis
make fpga_analysis

# Generate comprehensive FPGA report
make comprehensive_report

# Show available targets
make help
```

#### Synthesis Analysis
**ASIC Synthesis** automatically generates:
- **Synthesized netlists** (`*_synth.v`)
- **Gate count statistics** (`*_stats.txt`)
- **Gate-level analysis report** (`gate_analysis_report.md`)
- **Comprehensive analysis** (`comprehensive_report.md`)

**FPGA Synthesis** automatically generates:
- **FPGA netlists** (`*_fpga.v`)
- **LUT estimation reports** (`fpga_resource_analysis_report.md`)
- **FPGA resource analysis** (`comprehensive_fpga_report.md`)

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
│   └── cocotb/                   # Cocotb testbench
│       ├── Makefile             # Cocotb Makefile
│       └── test_full_adder.py   # Python-based testbench
├── flow/
│   ├── yosys/                    # ASIC synthesis flow
│   │   ├── Makefile             # ASIC synthesis Makefile
│   │   ├── gate_analysis.py     # Gate-level analysis script
│   │   ├── synth_*.ys           # ASIC synthesis scripts
│   │   └── README.md            # ASIC synthesis documentation
│   └── fpga/                     # FPGA synthesis flow
│       ├── Makefile             # FPGA synthesis Makefile
│       ├── fpga_resource_analysis.py # FPGA resource analysis script
│       ├── synth_*_fpga.ys      # FPGA synthesis scripts
│       └── README.md            # FPGA synthesis documentation
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
- **Simulators**: Icarus Verilog, Verilator

### 2. Cocotb Testbench (`tb/cocotb/`)
- **Purpose**: Python-based verification
- **Best for**: Python developers, rapid prototyping, custom verification logic
- **Features**: Python-based test development, easy integration with Python libraries, cross-simulator compatibility, async/await support
- **Test Scenarios**: Basic functionality, random input testing, edge cases, reset functionality, timing analysis, coverage scenarios
- **Simulators**: Icarus Verilog, Verilator

## Performance Specifications

### ASIC Gate-Level Analysis

| Implementation | Primitive Gates | Transistors | Design Style | Area Efficiency |
|----------------|-----------------|-------------|--------------|-----------------|
| Carry Lookahead | 5 | 32 | Flat | Standard |
| Simple XOR/AND | 5 | 32 | Flat | Standard |
| Half Adder | 7 | 48 | Hierarchical | Modular |

### FPGA Resource Analysis

| Implementation | Estimated LUTs | Design Style | FPGA Compatibility |
|----------------|----------------|--------------|-------------------|
| Carry Lookahead | 5 | Flat | All Xilinx 7-series |
| Simple XOR/AND | 5 | Flat | All Xilinx 7-series |
| Half Adder | 7 | Hierarchical | All Xilinx 7-series |

### Performance Metrics

| Parameter | Value | Units |
|-----------|-------|-------|
| Max Frequency | 500 | MHz |
| Propagation Delay | 300 | ps |
| Area (ASIC) | 50 | μm² |
| Power | 0.1 | mW |
| LUT Count (FPGA) | 3 | LUTs |

### Gate Breakdown

**Carry Lookahead & Simple Implementations:**
- 1 AND gate (6 transistors)
- 1 ANDNOT gate (4 transistors)
- 1 OR gate (6 transistors)
- 2 XNOR gates (16 transistors)
- **Total**: 5 gates, 32 transistors

**Half Adder Implementation:**
- 1 AND gate (6 transistors)
- 1 OR gate (6 transistors)
- 1 XOR gate (8 transistors)
- 2 half_adder instances (28 transistors)
- **Total**: 7 gates, 48 transistors

## Tool Support

- **Simulators**: Verilator, Icarus Verilog
- **ASIC Synthesis**: Yosys (with ABC technology mapping)
- **FPGA Synthesis**: Yosys (Xilinx 7-series)
- **PDKs**: Sky130B, GF180MCU
- **FPGAs**: Xilinx 7-series (Artix-7, Kintex-7, Virtex-7)
- **Linting**: Verilator (clean)
- **Verification**: Cocotb, SystemVerilog
- **Analysis**: Automated gate-level and FPGA resource analysis

## Test Coverage

- ✅ 100% functional coverage (all 8 input combinations)
- ✅ Timing analysis
- ✅ Universal testbench compatibility
- ✅ VCD waveform generation
- ✅ Python-based verification with Cocotb
- ✅ Cross-simulator compatibility
- ✅ Gate-level synthesis and analysis
- ✅ Transistor count estimation

## Vyges Compliance

This IP follows all Vyges conventions:
- ✅ Snake_case naming for modules and files
- ✅ Signal suffixes (_i, _o) for direction
- ✅ Required module headers with metadata
- ✅ Proper file organization
- ✅ Comprehensive documentation
- ✅ Multiple verification methodologies

## Documentation

- [Design Specification](docs/full_adder_design_specification.md) - Complete technical specification and implementation guide
- [Testbench Documentation](tb/README.md) - Comprehensive guide for all testbench types
- [Block Diagram](docs/full_adder_3.svg) - Visual representation

## License

Apache-2.0 License - see [LICENSE](LICENSE) file for details.

**Important**: The Apache-2.0 license applies to the **hardware IP content** (RTL, documentation, testbenches, etc.) that you create using this template. The template structure, build processes, tooling workflows, and AI context/processing engine are provided as-is for your use but are not themselves licensed under Apache-2.0.

For detailed licensing information, see [LICENSE_SCOPE.md](LICENSE_SCOPE.md).

## Contributing

This IP follows Vyges development conventions. See `.vyges-ai-context.json` for development guidelines.

## References

- [Full Adder Explanation](https://www.geeksforgeeks.org/digital-logic/full-adder-in-digital-logic/)
- [Cocotb Documentation](https://docs.cocotb.org/)
- [Vyges IP Development Guide](https://vyges.com/docs/ip-development)
