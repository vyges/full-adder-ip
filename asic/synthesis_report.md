=== Full Adder Synthesis Comparison Report ===
Generated: Sat Aug 16 05:53:55 UTC 2025

## Carry Lookahead Implementation
```

10. Printing statistics.

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

## Simple Implementation
```

10. Printing statistics.

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

## Half Adder Implementation
```

10. Printing statistics.

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
