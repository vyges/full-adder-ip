//=============================================================================
// Full Adder UVM Testbench Package
//=============================================================================
// Description: UVM package containing all testbench components for full adder
//              verification including transactions, agents, and tests.
// Author:      Vyges Team
// Date:        2025-07-17
// Version:     1.0.0
//=============================================================================

package full_adder_pkg;

    import uvm_pkg::*;
    `include "uvm_macros.svh"

    // Transaction class for full adder inputs/outputs
    class full_adder_transaction extends uvm_sequence_item;
        `uvm_object_utils(full_adder_transaction)
        
        rand logic a_i;
        rand logic b_i;
        rand logic cin_i;
        logic sum_o;
        logic cout_o;
        logic expected_sum;
        logic expected_cout;
        
        constraint valid_inputs {
            // All inputs are binary (0 or 1)
            a_i inside {0, 1};
            b_i inside {0, 1};
            cin_i inside {0, 1};
        }
        
        function new(string name = "full_adder_transaction");
            super.new(name);
        endfunction
        
        function string convert2string();
            return $sformatf("a_i=%b, b_i=%b, cin_i=%b, sum_o=%b, cout_o=%b, expected_sum=%b, expected_cout=%b",
                           a_i, b_i, cin_i, sum_o, cout_o, expected_sum, expected_cout);
        endfunction
        
        function void do_copy(uvm_object rhs);
            full_adder_transaction rhs_;
            if (!$cast(rhs_, rhs)) begin
                `uvm_fatal("DO_COPY", "Cast failed")
                return;
            end
            super.do_copy(rhs);
            a_i = rhs_.a_i;
            b_i = rhs_.b_i;
            cin_i = rhs_.cin_i;
            sum_o = rhs_.sum_o;
            cout_o = rhs_.cout_o;
            expected_sum = rhs_.expected_sum;
            expected_cout = rhs_.expected_cout;
        endfunction
        
        function bit do_compare(uvm_object rhs, uvm_comparer comparer);
            full_adder_transaction rhs_;
            if (!$cast(rhs_, rhs)) begin
                `uvm_fatal("DO_COMPARE", "Cast failed")
                return 0;
            end
            return (super.do_compare(rhs, comparer) &&
                   a_i == rhs_.a_i &&
                   b_i == rhs_.b_i &&
                   cin_i == rhs_.cin_i &&
                   sum_o == rhs_.sum_o &&
                   cout_o == rhs_.cout_o &&
                   expected_sum == rhs_.expected_sum &&
                   expected_cout == rhs_.expected_cout);
        endfunction
        
        // Calculate expected outputs based on full adder logic
        function void calculate_expected();
            expected_sum = a_i ^ b_i ^ cin_i;
            expected_cout = (a_i & b_i) | ((a_i ^ b_i) & cin_i);
        endfunction
        
    endclass

    // Driver class
    class full_adder_driver extends uvm_driver #(full_adder_transaction);
        `uvm_component_utils(full_adder_driver)
        
        virtual full_adder_if vif;
        
        function new(string name = "full_adder_driver", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        
        function void build_phase(uvm_phase phase);
            super.build_phase(phase);
            if (!uvm_config_db#(virtual full_adder_if)::get(this, "", "vif", vif)) begin
                `uvm_fatal("DRIVER", "Virtual interface not found")
            end
        endfunction
        
        task run_phase(uvm_phase phase);
            full_adder_transaction tr;
            
            forever begin
                seq_item_port.get_next_item(tr);
                drive_transaction(tr);
                seq_item_port.item_done();
            end
        endtask
        
        task drive_transaction(full_adder_transaction tr);
            @(posedge vif.clk_i);
            vif.a_i <= tr.a_i;
            vif.b_i <= tr.b_i;
            vif.cin_i <= tr.cin_i;
            `uvm_info("DRIVER", $sformatf("Driving: a_i=%b, b_i=%b, cin_i=%b", tr.a_i, tr.b_i, tr.cin_i), UVM_MEDIUM)
        endtask
        
    endclass

    // Monitor class
    class full_adder_monitor extends uvm_monitor;
        `uvm_component_utils(full_adder_monitor)
        
        virtual full_adder_if vif;
        uvm_analysis_port #(full_adder_transaction) ap;
        
        function new(string name = "full_adder_monitor", uvm_component parent = null);
            super.new(name, parent);
            ap = new("ap", this);
        endfunction
        
        function void build_phase(uvm_phase phase);
            super.build_phase(phase);
            if (!uvm_config_db#(virtual full_adder_if)::get(this, "", "vif", vif)) begin
                `uvm_fatal("MONITOR", "Virtual interface not found")
            end
        endfunction
        
        task run_phase(uvm_phase phase);
            full_adder_transaction tr;
            
            forever begin
                @(posedge vif.clk_i);
                tr = full_adder_transaction::type_id::create("tr");
                tr.a_i = vif.a_i;
                tr.b_i = vif.b_i;
                tr.cin_i = vif.cin_i;
                tr.sum_o = vif.sum_o;
                tr.cout_o = vif.cout_o;
                tr.calculate_expected();
                ap.write(tr);
                `uvm_info("MONITOR", tr.convert2string(), UVM_MEDIUM)
            end
        endtask
        
    endclass

    // Scoreboard class
    class full_adder_scoreboard extends uvm_scoreboard;
        `uvm_component_utils(full_adder_scoreboard)
        
        uvm_analysis_imp #(full_adder_transaction, full_adder_scoreboard) ap_imp;
        int total_tests = 0;
        int passed_tests = 0;
        int failed_tests = 0;
        
        function new(string name = "full_adder_scoreboard", uvm_component parent = null);
            super.new(name, parent);
            ap_imp = new("ap_imp", this);
        endfunction
        
        function void write(full_adder_transaction tr);
            total_tests++;
            
            if (tr.sum_o === tr.expected_sum && tr.cout_o === tr.expected_cout) begin
                passed_tests++;
                `uvm_info("SCOREBOARD", $sformatf("PASS: %s", tr.convert2string()), UVM_MEDIUM)
            end else begin
                failed_tests++;
                `uvm_error("SCOREBOARD", $sformatf("FAIL: Expected sum_o=%b, cout_o=%b, Got sum_o=%b, cout_o=%b",
                                                  tr.expected_sum, tr.expected_cout, tr.sum_o, tr.cout_o))
            end
        endfunction
        
        function void report_phase(uvm_phase phase);
            `uvm_info("SCOREBOARD", $sformatf("Test Summary: Total=%0d, Passed=%0d, Failed=%0d", 
                                            total_tests, passed_tests, failed_tests), UVM_LOW)
        endfunction
        
    endclass

    // Agent class
    class full_adder_agent extends uvm_agent;
        `uvm_component_utils(full_adder_agent)
        
        full_adder_driver driver;
        full_adder_monitor monitor;
        uvm_sequencer #(full_adder_transaction) sequencer;
        
        function new(string name = "full_adder_agent", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        
        function void build_phase(uvm_phase phase);
            super.build_phase(phase);
            
            monitor = full_adder_monitor::type_id::create("monitor", this);
            
            if (get_is_active() == UVM_ACTIVE) begin
                driver = full_adder_driver::type_id::create("driver", this);
                sequencer = uvm_sequencer#(full_adder_transaction)::type_id::create("sequencer", this);
            end
        endfunction
        
        function void connect_phase(uvm_phase phase);
            if (get_is_active() == UVM_ACTIVE) begin
                driver.seq_item_port.connect(sequencer.seq_item_export);
            end
        endfunction
        
    endclass

    // Environment class
    class full_adder_env extends uvm_env;
        `uvm_component_utils(full_adder_env)
        
        full_adder_agent agent;
        full_adder_scoreboard scoreboard;
        
        function new(string name = "full_adder_env", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        
        function void build_phase(uvm_phase phase);
            super.build_phase(phase);
            agent = full_adder_agent::type_id::create("agent", this);
            scoreboard = full_adder_scoreboard::type_id::create("scoreboard", this);
        endfunction
        
        function void connect_phase(uvm_phase phase);
            agent.monitor.ap.connect(scoreboard.ap_imp);
        endfunction
        
    endclass

    // Sequence for basic functionality test
    class basic_test_sequence extends uvm_sequence #(full_adder_transaction);
        `uvm_object_utils(basic_test_sequence)
        
        function new(string name = "basic_test_sequence");
            super.new(name);
        endfunction
        
        task body();
            full_adder_transaction tr;
            
            // Test all 8 possible input combinations
            for (int i = 0; i < 8; i++) begin
                tr = full_adder_transaction::type_id::create("tr");
                start_item(tr);
                tr.a_i = i[2];
                tr.b_i = i[1];
                tr.cin_i = i[0];
                tr.calculate_expected();
                finish_item(tr);
            end
        endtask
        
    endclass

    // Random test sequence
    class random_test_sequence extends uvm_sequence #(full_adder_transaction);
        `uvm_object_utils(random_test_sequence)
        
        int num_transactions = 100;
        
        function new(string name = "random_test_sequence");
            super.new(name);
        endfunction
        
        task body();
            full_adder_transaction tr;
            
            repeat (num_transactions) begin
                tr = full_adder_transaction::type_id::create("tr");
                start_item(tr);
                assert(tr.randomize());
                tr.calculate_expected();
                finish_item(tr);
            end
        endtask
        
    endclass

    // Base test class
    class full_adder_base_test extends uvm_test;
        `uvm_component_utils(full_adder_base_test)
        
        full_adder_env env;
        
        function new(string name = "full_adder_base_test", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        
        function void build_phase(uvm_phase phase);
            super.build_phase(phase);
            env = full_adder_env::type_id::create("env", this);
        endfunction
        
        task run_phase(uvm_phase phase);
            phase.raise_objection(this);
            #1000; // Allow time for test completion
            phase.drop_objection(this);
        endtask
        
    endclass

    // Basic functionality test
    class basic_functionality_test extends full_adder_base_test;
        `uvm_component_utils(basic_functionality_test)
        
        function new(string name = "basic_functionality_test", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        
        task run_phase(uvm_phase phase);
            basic_test_sequence seq;
            
            phase.raise_objection(this);
            seq = basic_test_sequence::type_id::create("seq");
            seq.start(env.agent.sequencer);
            phase.drop_objection(this);
        endtask
        
    endclass

    // Random test
    class random_test extends full_adder_base_test;
        `uvm_component_utils(random_test)
        
        function new(string name = "random_test", uvm_component parent = null);
            super.new(name, parent);
        endfunction
        
        task run_phase(uvm_phase phase);
            random_test_sequence seq;
            
            phase.raise_objection(this);
            seq = random_test_sequence::type_id::create("seq");
            seq.start(env.agent.sequencer);
            phase.drop_objection(this);
        endtask
        
    endclass

endpackage 