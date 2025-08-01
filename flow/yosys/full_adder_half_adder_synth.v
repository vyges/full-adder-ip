/* Generated by Yosys 0.55 (git sha1 60f126cd00c94892782470192d6c9f7abebe7c05, clang++ 17.0.0 -fPIC -O3) */

module full_adder_half_adder(clk_i, reset_n_i, a_i, b_i, cin_i, sum_o, cout_o);
  input a_i;
  wire a_i;
  input b_i;
  wire b_i;
  input cin_i;
  wire cin_i;
  input clk_i;
  wire clk_i;
  wire cout1;
  wire cout2;
  output cout_o;
  wire cout_o;
  input reset_n_i;
  wire reset_n_i;
  wire sum1;
  output sum_o;
  wire sum_o;
  \$_OR_  _0_ (
    .A(cout2),
    .B(cout1),
    .Y(cout_o)
  );
  half_adder ha1 (
    .a_i(a_i),
    .b_i(b_i),
    .cout_o(cout1),
    .sum_o(sum1)
  );
  half_adder ha2 (
    .a_i(sum1),
    .b_i(cin_i),
    .cout_o(cout2),
    .sum_o(sum_o)
  );
endmodule

module half_adder(a_i, b_i, sum_o, cout_o);
  input a_i;
  wire a_i;
  input b_i;
  wire b_i;
  output cout_o;
  wire cout_o;
  output sum_o;
  wire sum_o;
  \$_XOR_  _0_ (
    .A(b_i),
    .B(a_i),
    .Y(sum_o)
  );
  \$_AND_  _1_ (
    .A(b_i),
    .B(a_i),
    .Y(cout_o)
  );
endmodule
