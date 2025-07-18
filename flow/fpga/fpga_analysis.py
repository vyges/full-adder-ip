#!/usr/bin/env python3
"""
FPGA Resource Analysis Script for Full Adder Implementations
============================================================
Analyzes synthesized FPGA netlists to extract LUT counts and resource utilization.
"""

import re
import sys
from pathlib import Path

def analyze_fpga_resources(netlist_file):
    """Analyze FPGA resource utilization in a synthesized netlist."""
    with open(netlist_file, 'r') as f:
        content = f.read()
    
    # Count different FPGA primitives
    resource_counts = {}
    
    # Find all FPGA primitive instances
    primitive_patterns = {
        'LUT': r'LUT[0-9]+',
        'FDRE': r'FDRE',
        'FDSE': r'FDSE',
        'CARRY4': r'CARRY4',
        'MUXF7': r'MUXF7',
        'MUXF8': r'MUXF8',
        'DSP48E1': r'DSP48E1',
        'RAMB36E1': r'RAMB36E1',
        'BUFG': r'BUFG',
        'IBUF': r'IBUF',
        'OBUF': r'OBUF'
    }
    
    for resource_type, pattern in primitive_patterns.items():
        matches = re.findall(pattern, content)
        resource_counts[resource_type] = len(matches)
    
    # Count LUT types specifically
    lut_patterns = {
        'LUT1': r'LUT1',
        'LUT2': r'LUT2',
        'LUT3': r'LUT3',
        'LUT4': r'LUT4',
        'LUT5': r'LUT5',
        'LUT6': r'LUT6'
    }
    
    lut_counts = {}
    for lut_type, pattern in lut_patterns.items():
        matches = re.findall(pattern, content)
        lut_counts[lut_type] = len(matches)
    
    # Calculate total LUTs
    total_luts = sum(lut_counts.values())
    
    # Count module instances (for hierarchical designs)
    module_instances = {}
    module_pattern = r'(\w+)\s+(\w+)\s*\('
    for match in re.finditer(module_pattern, content):
        module_name = match.group(1)
        instance_name = match.group(2)
        # Skip Verilog keywords and primitives
        if (module_name not in ['module', 'input', 'output', 'wire', 'reg', 'assign'] and
            not module_name.startswith('LUT') and
            not module_name.startswith('FD') and
            not module_name.startswith('CARRY') and
            not module_name.startswith('MUX') and
            not module_name.startswith('DSP') and
            not module_name.startswith('RAMB') and
            not module_name.startswith('BUF') and
            not module_name.startswith('IBUF') and
            not module_name.startswith('OBUF')):
            if module_name not in module_instances:
                module_instances[module_name] = 0
            module_instances[module_name] += 1
    
    return {
        'resource_counts': resource_counts,
        'lut_counts': lut_counts,
        'total_luts': total_luts,
        'module_instances': module_instances,
        'file': netlist_file
    }

def generate_fpga_report(results):
    """Generate FPGA resource analysis report."""
    report = []
    report.append("# FPGA Resource Analysis Report")
    report.append("")
    report.append("## Summary")
    report.append("")
    report.append("| Implementation | Total LUTs | Flip-Flops | Design Style |")
    report.append("|----------------|------------|------------|--------------|")
    
    for impl_name, result in results.items():
        total_luts = result['total_luts']
        flip_flops = result['resource_counts'].get('FDRE', 0) + result['resource_counts'].get('FDSE', 0)
        style = "Hierarchical" if result['module_instances'] else "Flat"
        report.append(f"| {impl_name.replace('_', ' ').title()} | {total_luts} | {flip_flops} | {style} |")
    
    report.append("")
    report.append("## Detailed Analysis")
    report.append("")
    
    for impl_name, result in results.items():
        report.append(f"### {impl_name.replace('_', ' ').title()} Implementation")
        report.append("")
        report.append(f"**File**: `{result['file']}`")
        report.append("")
        
        # LUT breakdown
        report.append("**LUT Utilization:**")
        for lut_type, count in result['lut_counts'].items():
            if count > 0:
                report.append(f"- {lut_type}: {count}")
        report.append(f"- **Total LUTs**: {result['total_luts']}")
        report.append("")
        
        # Other resources
        report.append("**Other Resources:**")
        for resource, count in result['resource_counts'].items():
            if count > 0 and resource not in ['FDRE', 'FDSE']:
                report.append(f"- {resource}: {count}")
        report.append("")
        
        # Module instances
        if result['module_instances']:
            report.append("**Module Instances:**")
            for module, count in result['module_instances'].items():
                report.append(f"- {module}: {count}")
            report.append("")
        
        report.append("---")
        report.append("")
    
    return "\n".join(report)

def main():
    """Main function to analyze all FPGA implementations."""
    implementations = [
        'carry_lookahead',
        'simple', 
        'half_adder'
    ]
    
    results = {}
    
    for impl in implementations:
        netlist_file = f"full_adder_{impl}_fpga.v"
        if Path(netlist_file).exists():
            results[impl] = analyze_fpga_resources(netlist_file)
        else:
            print(f"Warning: {netlist_file} not found. Run synthesis first.")
    
    if results:
        # Generate report
        report = generate_fpga_report(results)
        
        # Write report to file
        with open('fpga_analysis_report.md', 'w') as f:
            f.write(report)
        
        print("FPGA analysis report generated: fpga_analysis_report.md")
        
        # Print summary to console
        print("\n=== FPGA Resource Summary ===")
        print("Implementation | Total LUTs | Flip-Flops | Design Style")
        print("---------------|------------|------------|--------------")
        for impl_name, result in results.items():
            total_luts = result['total_luts']
            flip_flops = result['resource_counts'].get('FDRE', 0) + result['resource_counts'].get('FDSE', 0)
            style = "Hierarchical" if result['module_instances'] else "Flat"
            print(f"{impl_name.replace('_', ' ').title():14} | {total_luts:10} | {flip_flops:10} | {style}")
    else:
        print("No FPGA netlists found. Please run synthesis first.")

if __name__ == "__main__":
    main() 