# FPGA Resource Analysis Report

## Summary

| Implementation | Total LUTs | Flip-Flops | Design Style |
|----------------|------------|------------|--------------|
| Carry Lookahead | 0 | 0 | Hierarchical |
| Simple | 0 | 0 | Hierarchical |
| Half Adder | 0 | 0 | Hierarchical |

## Detailed Analysis

### Carry Lookahead Implementation

**File**: `full_adder_carry_lookahead_fpga.v`

**LUT Utilization:**
- **Total LUTs**: 0

**Other Resources:**

**Module Instances:**
- _AND_: 1
- _XNOR_: 2
- _ANDNOT_: 1
- _OR_: 1

---

### Simple Implementation

**File**: `full_adder_simple_fpga.v`

**LUT Utilization:**
- **Total LUTs**: 0

**Other Resources:**

**Module Instances:**
- _XNOR_: 2
- _AND_: 1
- _ANDNOT_: 1
- _OR_: 1

---

### Half Adder Implementation

**File**: `full_adder_half_adder_fpga.v`

**LUT Utilization:**
- **Total LUTs**: 0

**Other Resources:**

**Module Instances:**
- _OR_: 1
- half_adder: 2
- _XOR_: 1
- _AND_: 1

---
