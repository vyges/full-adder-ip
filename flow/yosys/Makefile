#==============================================================================
# Full Adder Yosys Synthesis Makefile
#==============================================================================
# Description: Makefile for running Yosys synthesis on all full adder implementations
# Author:      Vyges Team
# Date:        2025-07-17
# Version:     1.0.0
#==============================================================================

# Yosys executable
YOSYS = yosys

# Synthesis targets
.PHONY: all carry_lookahead simple half_adder clean help

# Default target
all: carry_lookahead simple half_adder

# Synthesize carry lookahead implementation
carry_lookahead:
	@echo "Synthesizing carry lookahead implementation..."
	$(YOSYS) synth_carry_lookahead.ys
	@echo "Carry lookahead synthesis complete"

# Synthesize simple implementation
simple:
	@echo "Synthesizing simple implementation..."
	$(YOSYS) synth_simple.ys
	@echo "Simple implementation synthesis complete"

# Synthesize half adder implementation
half_adder:
	@echo "Synthesizing half adder implementation..."
	$(YOSYS) synth_half_adder.ys
	@echo "Half adder implementation synthesis complete"

# Generate synthesis report
report: all
	@echo "Generating synthesis comparison report..."
	@echo "=== Full Adder Synthesis Comparison Report ===" > synthesis_report.md
	@echo "Generated: $(shell date)" >> synthesis_report.md
	@echo "" >> synthesis_report.md
	@echo "## Carry Lookahead Implementation" >> synthesis_report.md
	@echo "\`\`\`" >> synthesis_report.md
	@cat full_adder_carry_lookahead_stats.txt >> synthesis_report.md
	@echo "\`\`\`" >> synthesis_report.md
	@echo "" >> synthesis_report.md
	@echo "## Simple Implementation" >> synthesis_report.md
	@echo "\`\`\`" >> synthesis_report.md
	@cat full_adder_simple_stats.txt >> synthesis_report.md
	@echo "\`\`\`" >> synthesis_report.md
	@echo "" >> synthesis_report.md
	@echo "## Half Adder Implementation" >> synthesis_report.md
	@echo "\`\`\`" >> synthesis_report.md
	@cat full_adder_half_adder_stats.txt >> synthesis_report.md
	@echo "\`\`\`" >> synthesis_report.md
	@echo "Synthesis report generated: synthesis_report.md"

# Generate gate analysis report
gate_analysis: all
	@echo "Generating gate-level analysis report..."
	@python3 gate_analysis.py
	@echo "Gate analysis report generated: gate_analysis_report.md"

# Generate comprehensive report (synthesis + gate analysis)
comprehensive_report: report gate_analysis
	@echo "Generating comprehensive analysis report..."
	@echo "# Full Adder Comprehensive Analysis Report" > comprehensive_report.md
	@echo "Generated: $(shell date)" >> comprehensive_report.md
	@echo "" >> comprehensive_report.md
	@echo "## Executive Summary" >> comprehensive_report.md
	@echo "" >> comprehensive_report.md
	@echo "This report provides a comprehensive analysis of three full adder implementations:" >> comprehensive_report.md
	@echo "- Carry Lookahead Implementation (5 gates, 32 transistors)" >> comprehensive_report.md
	@echo "- Simple XOR/AND Implementation (5 gates, 32 transistors)" >> comprehensive_report.md
	@echo "- Half Adder Implementation (7 gates, 48 transistors)" >> comprehensive_report.md
	@echo "" >> comprehensive_report.md
	@echo "## Gate-Level Analysis" >> comprehensive_report.md
	@echo "" >> comprehensive_report.md
	@cat gate_analysis_report.md >> comprehensive_report.md
	@echo "" >> comprehensive_report.md
	@echo "## Synthesis Statistics" >> comprehensive_report.md
	@echo "" >> comprehensive_report.md
	@cat synthesis_report.md >> comprehensive_report.md
	@echo "Comprehensive report generated: comprehensive_report.md"

# Clean target
clean:
	rm -f *.v
	rm -f *.json
	rm -f *.txt
	rm -f synthesis_report.md
	rm -f gate_analysis_report.md
	rm -f comprehensive_report.md

# Help target
help:
	@echo "Full Adder Yosys Synthesis Makefile"
	@echo "==================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all              - Synthesize all implementations (default)"
	@echo "  carry_lookahead  - Synthesize carry lookahead implementation"
	@echo "  simple           - Synthesize simple XOR/AND implementation"
	@echo "  half_adder       - Synthesize half adder modular implementation"
	@echo "  report           - Generate synthesis comparison report"
	@echo "  gate_analysis    - Generate gate-level analysis report"
	@echo "  comprehensive_report - Generate comprehensive analysis report"
	@echo "  clean            - Clean synthesis artifacts"
	@echo "  help             - Show this help message"
	@echo ""
	@echo "Output files:"
	@echo "  *_synth.v        - Synthesized netlist"
	@echo "  *_synth.json     - JSON representation"
	@echo "  *_stats.txt      - Detailed statistics"
	@echo "  *_hierarchy.txt  - Design hierarchy"
	@echo "  *_ports.txt      - Port information"
	@echo "  synthesis_report.md - Synthesis comparison report"
	@echo "  gate_analysis_report.md - Gate-level analysis report"
	@echo "  comprehensive_report.md - Complete analysis report"
	@echo ""
	@echo "Example usage:"
	@echo "  make all"
	@echo "  make carry_lookahead"
	@echo "  make report" 