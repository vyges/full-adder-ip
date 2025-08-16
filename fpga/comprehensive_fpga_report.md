# Full Adder FPGA Synthesis Comprehensive Report
Generated: Sat Aug 16 05:53:57 UTC 2025

## FPGA Resource Analysis

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

## Synthesis Statistics

### Carry Lookahead Implementation
```

12. Printing statistics.

=== full_adder ===

   Number of wires:                 10
   Number of wire bits:             10
   Number of public wires:           7
   Number of public wire bits:       7
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  5
     $_ANDNOT_                       1
     $_AND_                          1
     $_OR_                           1
     $_XNOR_                         2

```

### Simple Implementation
```

12. Printing statistics.

=== full_adder_simple ===

   Number of wires:                 10
   Number of wire bits:             10
   Number of public wires:           7
   Number of public wire bits:       7
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  5
     $_ANDNOT_                       1
     $_AND_                          1
     $_OR_                           1
     $_XNOR_                         2

```

### Half Adder Implementation
```

12. Printing statistics.

=== full_adder_half_adder ===

   Number of wires:                 10
   Number of wire bits:             10
   Number of public wires:          10
   Number of public wire bits:      10
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  3
     $_OR_                           1
     half_adder                      2

=== half_adder ===

   Number of wires:                  4
   Number of wire bits:              4
   Number of public wires:           4
   Number of public wire bits:       4
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  2
     $_AND_                          1
     $_XOR_                          1

=== design hierarchy ===

   full_adder_half_adder             1
     half_adder                      2

   Number of wires:                 18
   Number of wire bits:             18
   Number of public wires:          18
   Number of public wire bits:      18
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  5
     $_AND_                          2
     $_OR_                           1
     $_XOR_                          2

```
