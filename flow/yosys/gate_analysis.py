#!/usr/bin/env python3
"""
Gate-Level Analysis Script for Full Adder Implementations
=========================================================
Analyzes synthesized netlists to extract detailed gate counts and statistics.
"""

import re
import sys
from pathlib import Path

def analyze_gates(netlist_file):
    """Analyze gate counts in a synthesized netlist."""
    with open(netlist_file, 'r') as f:
        content = f.read()
    
    # Count different gate types
    gate_counts = {}
    
    # Find all gate instances
    gate_patterns = {
        'AND': r'\\\$_AND_\s+',
        'OR': r'\\\$_OR_\s+',
        'XOR': r'\\\$_XOR_\s+',
        'XNOR': r'\\\$_XNOR_\s+',
        'ANDNOT': r'\\\$_ANDNOT_\s+',
        'NAND': r'\\\$_NAND_\s+',
        'NOR': r'\\\$_NOR_\s+',
        'NOT': r'\\\$_NOT_\s+',
        'MUX': r'\\\$_MUX_\s+',
        'DFF': r'\\\$_DFF_\s+',
        'LATCH': r'\\\$_DLATCH_\s+'
    }
    
    for gate_type, pattern in gate_patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            gate_counts[gate_type] = len(matches)
    
    # Count module instances (excluding primitive gates)
    module_instances = {}
    module_pattern = r'(\w+)\s+(\w+)\s*\('
    for match in re.finditer(module_pattern, content):
        module_name = match.group(1)
        instance_name = match.group(2)
        # Skip primitive gates and Verilog keywords
        if (module_name not in ['module', 'input', 'output', 'wire', '\\$_AND_', 
                               '\\$_OR_', '\\$_XOR_', '\\$_XNOR_', '\\$_ANDNOT_',
                               '\\$_NAND_', '\\$_NOR_', '\\$_NOT_', '\\$_MUX_',
                               '\\$_DFF_', '\\$_DLATCH_'] and
            not module_name.startswith('\\$_')):
            if module_name not in module_instances:
                module_instances[module_name] = 0
            module_instances[module_name] += 1
    
    # Count total gates (including module instances for hierarchical designs)
    total_primitive_gates = sum(gate_counts.values())
    
    # For hierarchical designs, add gates from module instances
    if module_instances:
        # Count gates in half_adder module (2 gates per instance)
        if 'half_adder' in module_instances:
            total_primitive_gates += module_instances['half_adder'] * 2  # 1 XOR + 1 AND per half_adder
    
    # Calculate transistor counts (approximate)
    transistor_counts = {
        'AND': 6,      # 2-input AND: 6 transistors
        'OR': 6,       # 2-input OR: 6 transistors
        'XOR': 8,      # 2-input XOR: 8 transistors
        'XNOR': 8,     # 2-input XNOR: 8 transistors
        'ANDNOT': 4,   # AND-NOT: 4 transistors
        'NAND': 4,     # 2-input NAND: 4 transistors
        'NOR': 4,      # 2-input NOR: 4 transistors
        'NOT': 2,      # NOT: 2 transistors
        'MUX': 12,     # 2:1 MUX: 12 transistors
        'DFF': 20,     # DFF: ~20 transistors
        'LATCH': 12    # Latch: ~12 transistors
    }
    
    total_transistors = sum(gate_counts.get(gate, 0) * count 
                           for gate, count in transistor_counts.items())
    
    # Add transistors from module instances
    if module_instances and 'half_adder' in module_instances:
        # Each half_adder has 1 XOR (8 transistors) + 1 AND (6 transistors) = 14 transistors
        total_transistors += module_instances['half_adder'] * 14
    
    return {
        'gate_counts': gate_counts,
        'module_instances': module_instances,
        'total_primitive_gates': total_primitive_gates,
        'total_transistors': total_transistors,
        'file': netlist_file
    }

def generate_gate_report():
    """Generate comprehensive gate analysis report."""
    netlists = {
        'Carry Lookahead': 'full_adder_carry_lookahead_synth.v',
        'Simple XOR/AND': 'full_adder_simple_synth.v',
        'Half Adder': 'full_adder_half_adder_synth.v'
    }
    
    results = {}
    for impl_name, netlist_file in netlists.items():
        if Path(netlist_file).exists():
            results[impl_name] = analyze_gates(netlist_file)
    
    # Generate report
    report = []
    report.append("# Full Adder Gate-Level Analysis Report")
    report.append("=" * 50)
    report.append("")
    
    # Summary table
    report.append("## Gate Count Summary")
    report.append("")
    report.append("| Implementation | Primitive Gates | Transistors | Design Style |")
    report.append("|----------------|-----------------|-------------|--------------|")
    
    for impl_name, result in results.items():
        gates = result['total_primitive_gates']
        transistors = result['total_transistors']
        # Determine design style based on actual module instances (not primitive gates)
        actual_modules = {k: v for k, v in result['module_instances'].items() 
                         if not k.startswith('_') and k not in ['\\$_AND_', '\\$_OR_', '\\$_XOR_', '\\$_XNOR_', '\\$_ANDNOT_']}
        style = "Hierarchical" if actual_modules else "Flat"
        report.append(f"| {impl_name} | {gates} | {transistors} | {style} |")
    
    report.append("")
    
    # Detailed analysis for each implementation
    for impl_name, result in results.items():
        report.append(f"## {impl_name} Implementation")
        report.append("")
        
        # Gate breakdown
        report.append("### Gate Breakdown")
        report.append("")
        if result['gate_counts']:
            report.append("| Gate Type | Count | Transistors |")
            report.append("|-----------|-------|-------------|")
            for gate_type, count in sorted(result['gate_counts'].items()):
                transistors = count * {
                    'AND': 6, 'OR': 6, 'XOR': 8, 'XNOR': 8, 
                    'ANDNOT': 4, 'NAND': 4, 'NOR': 4, 'NOT': 2
                }.get(gate_type, 6)
                report.append(f"| {gate_type} | {count} | {transistors} |")
        else:
            report.append("No primitive gates found.")
        
        report.append("")
        
        # Module instances
        if result['module_instances']:
            report.append("### Module Instances")
            report.append("")
            report.append("| Module | Instances |")
            report.append("|--------|-----------|")
            for module, count in result['module_instances'].items():
                report.append(f"| {module} | {count} |")
            report.append("")
        
        # Total statistics
        report.append("### Total Statistics")
        report.append("")
        report.append(f"- **Primitive Gates**: {result['total_primitive_gates']}")
        report.append(f"- **Estimated Transistors**: {result['total_transistors']}")
        actual_modules = {k: v for k, v in result['module_instances'].items() 
                         if not k.startswith('_') and k not in ['\\$_AND_', '\\$_OR_', '\\$_XOR_', '\\$_XNOR_', '\\$_ANDNOT_']}
        report.append(f"- **Design Style**: {'Hierarchical' if actual_modules else 'Flat'}")
        report.append("")
        
        # Logic complexity analysis
        report.append("### Logic Complexity Analysis")
        report.append("")
        
        if impl_name == "Carry Lookahead":
            report.append("- **Carry Generation**: Optimized carry lookahead logic")
            report.append("- **Sum Generation**: XNOR-based sum calculation")
            report.append("- **Advantage**: Fast carry propagation")
        elif impl_name == "Simple XOR/AND":
            report.append("- **Carry Generation**: Standard AND-OR logic")
            report.append("- **Sum Generation**: Cascaded XNOR gates")
            report.append("- **Advantage**: Simple and straightforward")
        elif impl_name == "Half Adder":
            report.append("- **Carry Generation**: Two half-adder instances + OR gate")
            report.append("- **Sum Generation**: Cascaded half-adder sum outputs")
            report.append("- **Advantage**: Modular and reusable design")
        
        report.append("")
    
    # Performance comparison
    report.append("## Performance Comparison")
    report.append("")
    report.append("### Area Efficiency")
    report.append("")
    report.append("1. **Half Adder Implementation**: Most modular, reusable components")
    report.append("2. **Simple XOR/AND**: Standard implementation, good balance")
    report.append("3. **Carry Lookahead**: Optimized for speed, similar area")
    report.append("")
    
    report.append("### Design Trade-offs")
    report.append("")
    report.append("- **Area**: All implementations use similar transistor counts (~40-48)")
    report.append("- **Speed**: Carry lookahead optimized for fast carry propagation")
    report.append("- **Modularity**: Half adder implementation most modular")
    report.append("- **Complexity**: Simple XOR/AND easiest to understand")
    report.append("")
    
    # Technology considerations
    report.append("## Technology Considerations")
    report.append("")
    report.append("### Standard Cell Mapping")
    report.append("")
    report.append("All implementations map to standard cell library:")
    report.append("- AND, OR, XOR, XNOR gates")
    report.append("- AND-NOT gates for optimized logic")
    report.append("- Compatible with most CMOS processes")
    report.append("")
    
    report.append("### Power Considerations")
    report.append("")
    report.append("- **Static Power**: Minimal (combinational logic)")
    report.append("- **Dynamic Power**: Proportional to switching activity")
    report.append("- **Clock Power**: Only for clock/reset signals (minimal)")
    report.append("")
    
    return "\n".join(report)

if __name__ == "__main__":
    report = generate_gate_report()
    
    # Write to file
    with open("gate_analysis_report.md", "w") as f:
        f.write(report)
    
    print("Gate analysis report generated: gate_analysis_report.md")
    print("\n" + "="*50)
    print(report) 