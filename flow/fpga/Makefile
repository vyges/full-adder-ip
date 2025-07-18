#==============================================================================
# Full Adder FPGA Synthesis Makefile
#==============================================================================
# Description: Makefile for running Yosys FPGA synthesis on all full adder implementations
# Target: Xilinx 7-series FPGAs
# Author:      Vyges Team
# Date:        2025-07-17
# Version:     1.0.0
#==============================================================================

# Yosys executable
YOSYS = yosys

# FPGA synthesis targets
.PHONY: all carry_lookahead simple half_adder clean help fpga_analysis comprehensive_report

# Default target
all: carry_lookahead simple half_adder

# Synthesize carry lookahead implementation for FPGA
carry_lookahead:
	@echo "Synthesizing carry lookahead implementation for FPGA..."
	$(YOSYS) synth_carry_lookahead_fpga.ys
	@echo "Carry lookahead FPGA synthesis complete"

# Synthesize simple implementation for FPGA
simple:
	@echo "Synthesizing simple implementation for FPGA..."
	$(YOSYS) synth_simple_fpga.ys
	@echo "Simple implementation FPGA synthesis complete"

# Synthesize half adder implementation for FPGA
half_adder:
	@echo "Synthesizing half adder implementation for FPGA..."
	$(YOSYS) synth_half_adder_fpga.ys
	@echo "Half adder implementation FPGA synthesis complete"

# Generate FPGA resource analysis report
fpga_analysis: all
	@echo "Generating FPGA resource analysis report..."
	python3 fpga_analysis.py
	@echo "FPGA analysis report generated"

# Generate comprehensive FPGA report
comprehensive_report: all fpga_analysis
	@echo "Generating comprehensive FPGA report..."
	@echo "# Full Adder FPGA Synthesis Comprehensive Report" > comprehensive_fpga_report.md
	@echo "Generated: $(shell date)" >> comprehensive_fpga_report.md
	@echo "" >> comprehensive_fpga_report.md
	@echo "## FPGA Resource Analysis" >> comprehensive_fpga_report.md
	@echo "" >> comprehensive_fpga_report.md
	@cat fpga_analysis_report.md >> comprehensive_fpga_report.md
	@echo "" >> comprehensive_fpga_report.md
	@echo "## Synthesis Statistics" >> comprehensive_fpga_report.md
	@echo "" >> comprehensive_fpga_report.md
	@echo "### Carry Lookahead Implementation" >> comprehensive_fpga_report.md
	@echo "\`\`\`" >> comprehensive_fpga_report.md
	@cat full_adder_carry_lookahead_fpga_stats.txt >> comprehensive_fpga_report.md
	@echo "\`\`\`" >> comprehensive_fpga_report.md
	@echo "" >> comprehensive_fpga_report.md
	@echo "### Simple Implementation" >> comprehensive_fpga_report.md
	@echo "\`\`\`" >> comprehensive_fpga_report.md
	@cat full_adder_simple_fpga_stats.txt >> comprehensive_fpga_report.md
	@echo "\`\`\`" >> comprehensive_fpga_report.md
	@echo "" >> comprehensive_fpga_report.md
	@echo "### Half Adder Implementation" >> comprehensive_fpga_report.md
	@echo "\`\`\`" >> comprehensive_fpga_report.md
	@cat full_adder_half_adder_fpga_stats.txt >> comprehensive_fpga_report.md
	@echo "\`\`\`" >> comprehensive_fpga_report.md
	@echo "Comprehensive FPGA report generated: comprehensive_fpga_report.md"

# Clean target
clean:
	rm -f *.v
	rm -f *.json
	rm -f *.txt
	rm -f fpga_analysis_report.md
	rm -f comprehensive_fpga_report.md

# Help target
help:
	@echo "Full Adder FPGA Synthesis Makefile"
	@echo "=================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all                 - Synthesize all implementations for FPGA"
	@echo "  carry_lookahead     - Synthesize carry lookahead implementation"
	@echo "  simple              - Synthesize simple implementation"
	@echo "  half_adder          - Synthesize half adder implementation"
	@echo "  fpga_analysis       - Generate FPGA resource analysis report"
	@echo "  comprehensive_report - Generate comprehensive FPGA analysis report"
	@echo "  clean               - Clean synthesis artifacts"
	@echo "  help                - Show this help message"
	@echo ""
	@echo "Generated files:"
	@echo "  *_fpga.v            - Synthesized FPGA netlists"
	@echo "  *_fpga.json         - JSON representation of netlists"
	@echo "  *_fpga_stats.txt    - Synthesis statistics"
	@echo "  *_fpga_hierarchy.txt - Design hierarchy"
	@echo "  *_fpga_resources.txt - FPGA resource utilization"
	@echo "  fpga_analysis_report.md - FPGA resource analysis report"
	@echo "  comprehensive_fpga_report.md - Complete FPGA analysis report" 