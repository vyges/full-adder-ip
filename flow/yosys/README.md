# Full Adder Yosys Synthesis Flow

## Overview

This directory contains the Yosys synthesis flow for all three full adder implementations:
- **Carry Lookahead Implementation** (`full_adder.v`)
- **Simple XOR/AND Implementation** (`full_adder_simple.v`)
- **Half Adder Modular Implementation** (`full_adder_half_adder.v`)

## Synthesis Results Summary

| Implementation | Total Cells | Logic Cells | Hierarchy | Area Efficiency |
|----------------|-------------|-------------|-----------|-----------------|
| Carry Lookahead | 5 | 5 primitive | Flat | Standard |
| Simple XOR/AND | 5 | 5 primitive | Flat | Standard |
| Half Adder | 3 | 1 OR + 2 half_adder | Hierarchical | Modular |

### Key Findings

1. **Identical Logic Complexity**: All three implementations synthesize to exactly 5 primitive logic cells
2. **Different Architectures**: 
   - Carry Lookahead & Simple: Flat design with 5 primitive cells
   - Half Adder: Hierarchical design with 2 half_adder instances + 1 OR gate
3. **Technology Mapping**: All implementations use the same cell types (AND, OR, XOR/XNOR, ANDNOT)

## Files

### Synthesis Scripts
- `synth_carry_lookahead.ys` - Synthesis script for carry lookahead implementation
- `synth_simple.ys` - Synthesis script for simple XOR/AND implementation  
- `synth_half_adder.ys` - Synthesis script for half adder modular implementation

### Output Files
- `*_synth.v` - Synthesized netlists
- `*_synth.json` - JSON representations for further processing
- `*_stats.txt` - Detailed synthesis statistics
- `*_hierarchy.txt` - Design hierarchy information
- `synthesis_report.md` - Comprehensive comparison report

### Makefile
- `Makefile` - Automated synthesis flow with targets for all implementations

## Usage

### Prerequisites
```bash
# Install Yosys
brew install yosys

# Install Graphviz (optional, for visualization)
brew install graphviz
```

### Running Synthesis

```bash
# Synthesize all implementations
make all

# Synthesize specific implementation
make carry_lookahead
make simple
make half_adder

# Generate comparison report
make report

# Clean synthesis artifacts
make clean

# Show help
make help
```

## Synthesis Flow

1. **RTL Reading**: Read SystemVerilog RTL with `-sv` flag
2. **Hierarchy Analysis**: Set top module and analyze design hierarchy
3. **Design Check**: Verify design integrity
4. **Synthesis**: Convert to generic gates using Yosys `synth` command
5. **Optimization**: Apply various optimization passes
6. **Technology Mapping**: Map to standard cell library using ABC
7. **Output Generation**: Generate netlist, JSON, and statistics

## Technology Mapping

All implementations are mapped to the following primitive cells:
- `$_AND_` - AND gate
- `$_OR_` - OR gate  
- `$_XOR_` - XOR gate
- `$_XNOR_` - XNOR gate
- `$_ANDNOT_` - AND-NOT gate

## Performance Analysis

### Area Comparison
- **Carry Lookahead**: 5 cells, flat design
- **Simple XOR/AND**: 5 cells, flat design  
- **Half Adder**: 3 cells (hierarchical), 5 total primitive cells

### Design Complexity
- **Carry Lookahead**: Most complex logic, optimized carry generation
- **Simple XOR/AND**: Straightforward implementation, easy to understand
- **Half Adder**: Modular design, reusable components

## Next Steps

1. **Timing Analysis**: Run static timing analysis on synthesized netlists
2. **Power Analysis**: Estimate power consumption for each implementation
3. **Place & Route**: Use OpenROAD for physical design
4. **Performance Validation**: Verify timing and functionality post-synthesis

## Integration with OpenROAD

The synthesized netlists can be used with OpenROAD for:
- Place and route
- Timing analysis
- Power analysis
- Physical verification

## Troubleshooting

### Common Issues

1. **SystemVerilog Syntax**: Ensure `-sv` flag is used for SystemVerilog files
2. **Graphviz Errors**: Install Graphviz or comment out visualization commands
3. **ABC Errors**: Verify ABC is properly installed with Yosys

### Debug Commands

```bash
# Check Yosys version
yosys --version

# Interactive Yosys session
yosys -i synth_carry_lookahead.ys

# Generate detailed logs
yosys -l yosys.log synth_carry_lookahead.ys
```

## References

- [Yosys Documentation](https://yosyshq.net/yosys/)
- [ABC Synthesis Tool](https://people.eecs.berkeley.edu/~alanmi/abc/)
- [OpenROAD Project](https://theopenroadproject.org/)
- [Vyges IP Development Guidelines](https://github.com/vyges/vyges)

## License

This synthesis flow is part of the Vyges Full Adder IP project and follows Vyges development conventions. 