# Experiments with P

Shots set at 1024 for full experiment

`network_qaoa_sim.py`

## Summary

For penalty values P ∈ [5, 50], p=1 and p=2 QAOA consistently samples globally optimal feasible solutions of the network QUBO, although these solutions appear with low probability and are not the most frequent measurement outcomes. As P increases, the energy landscape becomes increasingly constraint-dominated, leading to distributions concentrated on feasible but sub-optimal states, with optimal solutions residing in the distribution tails. Degenerate global minima are observed, resulting in multiple distinct optimal routing configurations with identical QUBO energy. 

## P = 5
```
Feasible? True

=== Reference ===
Best QUBO energy: -5.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=22.800
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=18.067
gamma1=1.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=14.730
gamma1=1.300, beta1=1.300, gamma2=1.100, beta2=0.100 -> E=13.186
gamma1=1.300, beta1=1.300, gamma2=1.100, beta2=1.100 -> E=10.939
gamma1=2.039, beta1=1.821, gamma2=1.341, beta2=1.451 -> E=23.799
gamma1=0.810, beta1=1.377, gamma2=1.136, beta2=1.152 -> E=19.075
gamma1=1.300, beta1=1.247, gamma2=1.213, beta2=1.100 -> E=10.541
gamma1=1.367, beta1=1.022, gamma2=1.131, beta2=1.114 -> E=16.114
gamma1=1.306, beta1=1.252, gamma2=1.215, beta2=1.149 -> E=9.638
gamma1=1.363, beta1=1.317, gamma2=1.254, beta2=1.180 -> E=7.728
gamma1=1.341, beta1=1.383, gamma2=1.297, beta2=1.238 -> E=10.767
gamma1=1.452, beta1=1.278, gamma2=1.241, beta2=1.198 -> E=20.549
gamma1=1.359, beta1=1.329, gamma2=1.279, beta2=1.139 -> E=10.439
gamma1=1.361, beta1=1.311, gamma2=1.264, beta2=1.184 -> E=8.677
gamma1=1.349, beta1=1.334, gamma2=1.246, beta2=1.189 -> E=7.324
gamma1=1.355, beta1=1.336, gamma2=1.238, beta2=1.191 -> E=6.840
gamma1=1.359, beta1=1.336, gamma2=1.233, beta2=1.199 -> E=7.386
gamma1=1.357, beta1=1.339, gamma2=1.240, beta2=1.191 -> E=7.057
gamma1=1.354, beta1=1.337, gamma2=1.232, beta2=1.183 -> E=6.353
gamma1=1.353, beta1=1.342, gamma2=1.228, beta2=1.176 -> E=5.802
gamma1=1.353, beta1=1.345, gamma2=1.220, beta2=1.170 -> E=5.546
gamma1=1.344, beta1=1.347, gamma2=1.222, beta2=1.167 -> E=5.175
gamma1=1.343, beta1=1.357, gamma2=1.223, beta2=1.163 -> E=5.148
gamma1=1.336, beta1=1.356, gamma2=1.215, beta2=1.161 -> E=4.528
gamma1=1.324, beta1=1.353, gamma2=1.203, beta2=1.152 -> E=5.713
gamma1=1.333, beta1=1.359, gamma2=1.214, beta2=1.170 -> E=4.607
gamma1=1.333, beta1=1.355, gamma2=1.219, beta2=1.160 -> E=5.077
gamma1=1.340, beta1=1.357, gamma2=1.206, beta2=1.160 -> E=4.647
gamma1=1.332, beta1=1.355, gamma2=1.215, beta2=1.159 -> E=4.635
gamma1=1.336, beta1=1.357, gamma2=1.216, beta2=1.160 -> E=4.430
gamma1=1.337, beta1=1.359, gamma2=1.216, beta2=1.160 -> E=4.637
gamma1=1.337, beta1=1.357, gamma2=1.215, beta2=1.160 -> E=4.528
gamma1=1.336, beta1=1.357, gamma2=1.215, beta2=1.161 -> E=4.731
gamma1=1.337, beta1=1.357, gamma2=1.216, beta2=1.161 -> E=4.791
gamma1=1.335, beta1=1.357, gamma2=1.216, beta2=1.160 -> E=4.478
gamma1=1.337, beta1=1.357, gamma2=1.216, beta2=1.161 -> E=4.660
gamma1=1.336, beta1=1.357, gamma2=1.216, beta2=1.160 -> E=3.874
gamma1=1.336, beta1=1.357, gamma2=1.216, beta2=1.160 -> E=4.400
gamma1=1.336, beta1=1.357, gamma2=1.216, beta2=1.160 -> E=5.045

Optimal parameters: [1.33630459 1.35720135 1.21558013 1.16040158]

=== Measured bests ===
Best ANY: 01100000 E= -5.0 count= 9 feasible? True
Best FEASIBLE: 01100000 E= -5.0 count= 9
Active flows: ['f_A_D', 'f_B_C']

Most frequent bitstring: 00000000
QUBO energy: 0.0
Active flows: []

Match reference? False

```

## P = 10
```
Feasible? True

=== Reference ===
Best QUBO energy: -15.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=35.851
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=31.093
gamma1=1.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=20.063
gamma1=1.300, beta1=1.300, gamma2=1.100, beta2=0.100 -> E=21.369
gamma1=1.300, beta1=1.300, gamma2=0.100, beta2=1.100 -> E=39.264
gamma1=1.510, beta1=1.786, gamma2=0.042, beta2=-0.746 -> E=36.497
gamma1=1.380, beta1=1.486, gamma2=0.078, beta2=0.556 -> E=40.758
gamma1=1.423, beta1=1.300, gamma2=0.100, beta2=0.078 -> E=36.200
gamma1=1.055, beta1=1.320, gamma2=0.098, beta2=0.053 -> E=33.901
gamma1=1.300, beta1=1.294, gamma2=0.050, beta2=0.100 -> E=16.938
gamma1=1.292, beta1=1.201, gamma2=0.055, beta2=0.135 -> E=14.548
gamma1=1.202, beta1=1.186, gamma2=0.014, beta2=0.124 -> E=45.776
gamma1=1.299, beta1=1.183, gamma2=0.057, beta2=0.089 -> E=13.739
gamma1=1.396, beta1=1.173, gamma2=0.042, beta2=0.103 -> E=35.893
gamma1=1.295, beta1=1.184, gamma2=0.106, beta2=0.089 -> E=15.318
gamma1=1.297, beta1=1.171, gamma2=0.057, beta2=0.093 -> E=13.638
gamma1=1.274, beta1=1.172, gamma2=0.051, beta2=0.087 -> E=17.900
gamma1=1.298, beta1=1.171, gamma2=0.052, beta2=0.093 -> E=13.258
gamma1=1.308, beta1=1.170, gamma2=0.050, beta2=0.094 -> E=13.608
gamma1=1.299, beta1=1.169, gamma2=0.052, beta2=0.088 -> E=12.330
gamma1=1.297, beta1=1.166, gamma2=0.048, beta2=0.080 -> E=13.360
gamma1=1.299, beta1=1.167, gamma2=0.056, beta2=0.088 -> E=13.332
gamma1=1.298, beta1=1.168, gamma2=0.052, beta2=0.089 -> E=12.376
gamma1=1.298, beta1=1.170, gamma2=0.050, beta2=0.086 -> E=14.389
gamma1=1.298, beta1=1.170, gamma2=0.052, beta2=0.088 -> E=13.423
gamma1=1.300, beta1=1.169, gamma2=0.052, beta2=0.088 -> E=13.473
gamma1=1.299, beta1=1.170, gamma2=0.052, beta2=0.089 -> E=12.882
gamma1=1.299, beta1=1.170, gamma2=0.051, beta2=0.088 -> E=14.256
gamma1=1.298, beta1=1.169, gamma2=0.052, beta2=0.088 -> E=13.604
gamma1=1.299, beta1=1.170, gamma2=0.052, beta2=0.088 -> E=13.716
gamma1=1.299, beta1=1.169, gamma2=0.052, beta2=0.088 -> E=13.284
gamma1=1.299, beta1=1.169, gamma2=0.052, beta2=0.088 -> E=14.176
gamma1=1.299, beta1=1.169, gamma2=0.052, beta2=0.088 -> E=13.718
gamma1=1.299, beta1=1.170, gamma2=0.052, beta2=0.088 -> E=12.890
gamma1=1.299, beta1=1.170, gamma2=0.052, beta2=0.088 -> E=13.194

Optimal parameters: [1.29876084 1.16949701 0.05200683 0.088214  ]

=== Measured bests ===
Best ANY: 10010000 E= -15.0 count= 5 feasible? True
Best FEASIBLE: 10010000 E= -15.0 count= 5
Active flows: ['f_A_C', 'f_B_D']

Most frequent bitstring: 00000111
QUBO energy: -5.0
Active flows: ['f_B_E', 'f_E_C', 'f_E_D']

Match reference? False

```

## P = 15
```
Feasible? True

=== Reference ===
Best QUBO energy: -25.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=46.397
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=47.824
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=49.358
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=46.828
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=70.756
gamma1=0.242, beta1=0.180, gamma2=0.082, beta2=-0.891 -> E=48.619
gamma1=0.133, beta1=-0.047, gamma2=0.050, beta2=0.415 -> E=46.268
gamma1=0.028, beta1=0.119, gamma2=0.018, beta2=0.567 -> E=118.560
gamma1=0.090, beta1=-0.050, gamma2=0.050, beta2=0.389 -> E=43.167
gamma1=0.112, beta1=-0.121, gamma2=0.049, beta2=0.323 -> E=41.075
gamma1=0.033, beta1=-0.137, gamma2=0.049, beta2=0.264 -> E=31.628
gamma1=-0.134, beta1=-0.147, gamma2=0.048, beta2=0.154 -> E=50.770
gamma1=0.031, beta1=-0.140, gamma2=0.098, beta2=0.267 -> E=22.444
gamma1=0.083, beta1=-0.197, gamma2=0.160, beta2=0.251 -> E=55.664
gamma1=0.011, beta1=-0.173, gamma2=0.093, beta2=0.298 -> E=36.536
gamma1=-0.032, beta1=-0.075, gamma2=0.128, beta2=0.237 -> E=59.763
gamma1=0.041, beta1=-0.146, gamma2=0.056, beta2=0.242 -> E=30.313
gamma1=0.040, beta1=-0.138, gamma2=0.096, beta2=0.275 -> E=25.646
gamma1=0.017, beta1=-0.121, gamma2=0.104, beta2=0.260 -> E=31.479
gamma1=0.034, beta1=-0.140, gamma2=0.101, beta2=0.264 -> E=24.284
gamma1=0.027, beta1=-0.149, gamma2=0.100, beta2=0.269 -> E=21.311
gamma1=0.017, beta1=-0.146, gamma2=0.099, beta2=0.271 -> E=29.024
gamma1=0.027, beta1=-0.148, gamma2=0.104, beta2=0.270 -> E=20.062
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.264 -> E=17.227
gamma1=0.031, beta1=-0.156, gamma2=0.117, beta2=0.260 -> E=18.062
gamma1=0.040, beta1=-0.156, gamma2=0.110, beta2=0.270 -> E=20.821
gamma1=0.031, beta1=-0.157, gamma2=0.106, beta2=0.263 -> E=20.165
gamma1=0.032, beta1=-0.152, gamma2=0.108, beta2=0.264 -> E=18.580
gamma1=0.034, beta1=-0.154, gamma2=0.109, beta2=0.266 -> E=18.210
gamma1=0.032, beta1=-0.153, gamma2=0.108, beta2=0.265 -> E=17.310
gamma1=0.031, beta1=-0.153, gamma2=0.109, beta2=0.265 -> E=17.780
gamma1=0.032, beta1=-0.153, gamma2=0.108, beta2=0.264 -> E=18.363
gamma1=0.033, beta1=-0.153, gamma2=0.109, beta2=0.265 -> E=17.692
gamma1=0.032, beta1=-0.154, gamma2=0.108, beta2=0.264 -> E=17.749
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.264 -> E=18.079
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.265 -> E=18.458
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.264 -> E=18.512
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.265 -> E=18.313
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.264 -> E=20.199
gamma1=0.032, beta1=-0.153, gamma2=0.109, beta2=0.264 -> E=17.479

Optimal parameters: [ 0.03192123 -0.15313664  0.10856377  0.26449202]

=== Measured bests ===
Best ANY: 01100000 E= -25.0 count= 23 feasible? True
Best FEASIBLE: 01100000 E= -25.0 count= 23
Active flows: ['f_A_D', 'f_B_C']

Most frequent bitstring: 01000110
QUBO energy: -23.0
Active flows: ['f_A_D', 'f_B_E', 'f_E_C']

Match reference? False

```

## P = 20
```
Feasible? True

=== Reference ===
Best QUBO energy: -35.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=54.817
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=60.173
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=100.455
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=54.031
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=1.100 -> E=43.139
gamma1=0.187, beta1=-0.666, gamma2=1.117, beta2=1.331 -> E=76.185
gamma1=0.232, beta1=0.776, gamma2=1.110, beta2=1.238 -> E=63.692
gamma1=0.176, beta1=0.282, gamma2=1.100, beta2=1.100 -> E=58.746
gamma1=0.544, beta1=0.248, gamma2=1.101, beta2=1.120 -> E=59.311
gamma1=0.300, beta1=0.301, gamma2=1.150, beta2=1.100 -> E=31.474
gamma1=0.308, beta1=0.393, gamma2=1.188, beta2=1.102 -> E=38.396
gamma1=0.300, beta1=0.300, gamma2=1.150, beta2=1.150 -> E=25.548
gamma1=0.343, beta1=0.247, gamma2=1.216, beta2=1.182 -> E=46.586
gamma1=0.304, beta1=0.321, gamma2=1.129, beta2=1.190 -> E=23.879
gamma1=0.315, beta1=0.312, gamma2=1.142, beta2=1.204 -> E=25.237
gamma1=0.301, beta1=0.318, gamma2=1.128, beta2=1.191 -> E=25.218
gamma1=0.300, beta1=0.329, gamma2=1.135, beta2=1.190 -> E=21.884
gamma1=0.304, beta1=0.338, gamma2=1.138, beta2=1.188 -> E=22.016
gamma1=0.300, beta1=0.331, gamma2=1.132, beta2=1.194 -> E=24.002
gamma1=0.296, beta1=0.327, gamma2=1.142, beta2=1.184 -> E=29.310
gamma1=0.298, beta1=0.330, gamma2=1.132, beta2=1.188 -> E=25.148
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.200 -> E=18.898
gamma1=0.308, beta1=0.334, gamma2=1.134, beta2=1.207 -> E=22.233
gamma1=0.302, beta1=0.328, gamma2=1.141, beta2=1.200 -> E=20.200
gamma1=0.301, beta1=0.331, gamma2=1.136, beta2=1.200 -> E=23.529
gamma1=0.303, beta1=0.328, gamma2=1.135, beta2=1.199 -> E=19.896
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=22.446
gamma1=0.303, beta1=0.331, gamma2=1.136, beta2=1.200 -> E=21.438
gamma1=0.302, beta1=0.330, gamma2=1.135, beta2=1.200 -> E=20.343
gamma1=0.302, beta1=0.329, gamma2=1.136, beta2=1.200 -> E=20.687
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=18.714
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=19.149
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=21.437
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=19.895
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=21.417
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=23.208
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=21.448
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=24.218
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=21.294
gamma1=0.302, beta1=0.330, gamma2=1.136, beta2=1.199 -> E=19.310

Optimal parameters: [0.30193853 0.3300481  1.13611634 1.19924037]

=== Measured bests ===
Best ANY: 01100000 E= -35.0 count= 21 feasible? True
Best FEASIBLE: 01100000 E= -35.0 count= 21
Active flows: ['f_A_D', 'f_B_C']

Most frequent bitstring: 10100001
QUBO energy: 5.0
Active flows: ['f_A_C', 'f_B_C', 'f_E_D']

Match reference? False

```

## P = 30
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=62.848
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=95.716
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=82.500
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=80.082
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=105.148
gamma1=-0.251, beta1=-0.030, gamma2=-0.189, beta2=-0.610 -> E=138.456
gamma1=0.193, beta1=0.236, gamma2=0.044, beta2=0.581 -> E=128.992
gamma1=0.247, beta1=0.268, gamma2=0.072, beta2=-0.141 -> E=74.252
gamma1=0.251, beta1=0.300, gamma2=0.100, beta2=0.111 -> E=71.509
gamma1=0.399, beta1=0.289, gamma2=0.091, beta2=0.107 -> E=43.295
gamma1=0.597, beta1=0.269, gamma2=0.073, beta2=0.116 -> E=51.978
gamma1=0.393, beta1=0.240, gamma2=0.091, beta2=0.114 -> E=49.184
gamma1=0.380, beta1=0.358, gamma2=0.071, beta2=0.174 -> E=65.859
gamma1=0.403, beta1=0.291, gamma2=0.139, beta2=0.120 -> E=64.801
gamma1=0.391, beta1=0.298, gamma2=0.038, beta2=0.023 -> E=46.385
gamma1=0.401, beta1=0.296, gamma2=0.134, beta2=0.083 -> E=56.144
gamma1=0.386, beta1=0.291, gamma2=0.091, beta2=0.108 -> E=57.494
gamma1=0.423, beta1=0.290, gamma2=0.085, beta2=0.109 -> E=185.445
gamma1=0.399, beta1=0.290, gamma2=0.094, beta2=0.110 -> E=49.037
gamma1=0.399, beta1=0.288, gamma2=0.097, beta2=0.100 -> E=52.676
gamma1=0.399, beta1=0.294, gamma2=0.091, beta2=0.106 -> E=47.903
gamma1=0.403, beta1=0.284, gamma2=0.083, beta2=0.107 -> E=60.499
gamma1=0.400, beta1=0.289, gamma2=0.093, beta2=0.111 -> E=51.376
gamma1=0.400, beta1=0.289, gamma2=0.090, beta2=0.107 -> E=48.992
gamma1=0.396, beta1=0.289, gamma2=0.090, beta2=0.107 -> E=38.835
gamma1=0.395, beta1=0.288, gamma2=0.088, beta2=0.107 -> E=46.653
gamma1=0.396, beta1=0.289, gamma2=0.090, beta2=0.107 -> E=45.339
gamma1=0.396, beta1=0.289, gamma2=0.091, beta2=0.106 -> E=41.929
gamma1=0.396, beta1=0.289, gamma2=0.090, beta2=0.107 -> E=43.381
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=38.104
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.105 -> E=46.979
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=40.545
gamma1=0.396, beta1=0.290, gamma2=0.089, beta2=0.107 -> E=40.484
gamma1=0.397, beta1=0.289, gamma2=0.089, beta2=0.107 -> E=41.569
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=41.786
gamma1=0.396, beta1=0.289, gamma2=0.090, beta2=0.106 -> E=42.012
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=42.900
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=39.396
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=42.660
gamma1=0.396, beta1=0.289, gamma2=0.089, beta2=0.106 -> E=44.300

Optimal parameters: [0.39631294 0.28927377 0.08939449 0.10622296]

=== Measured bests ===
Best ANY: 10010000 E= -55.0 count= 11 feasible? True
Best FEASIBLE: 10010000 E= -55.0 count= 11
Active flows: ['f_A_C', 'f_B_D']

Most frequent bitstring: 00001111
QUBO energy: -51.0
Active flows: ['f_A_E', 'f_B_E', 'f_E_C', 'f_E_D']

Match reference? False
```

## P = 50
```
Feasible? True

=== Reference ===
Best QUBO energy: -95.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=122.918
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=145.515
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=142.092
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=124.809
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=176.091
gamma1=-0.071, beta1=-0.015, gamma2=0.069, beta2=-0.773 -> E=193.359
gamma1=0.189, beta1=0.206, gamma2=0.091, beta2=0.578 -> E=155.399
gamma1=0.232, beta1=0.242, gamma2=0.094, beta2=-0.133 -> E=86.169
gamma1=0.156, beta1=0.178, gamma2=0.088, beta2=-0.623 -> E=230.157
gamma1=0.108, beta1=0.246, gamma2=0.098, beta2=-0.115 -> E=78.848
gamma1=0.094, beta1=0.160, gamma2=0.025, beta2=0.108 -> E=110.054
gamma1=0.104, beta1=0.199, gamma2=0.105, beta2=-0.131 -> E=116.577
gamma1=0.105, beta1=0.344, gamma2=0.084, beta2=-0.100 -> E=109.454
gamma1=0.104, beta1=0.242, gamma2=0.052, beta2=-0.132 -> E=121.312
gamma1=0.105, beta1=0.224, gamma2=0.195, beta2=-0.106 -> E=121.274
gamma1=0.101, beta1=0.254, gamma2=0.104, beta2=-0.163 -> E=128.810
gamma1=0.111, beta1=0.201, gamma2=0.046, beta2=-0.042 -> E=61.985
gamma1=0.153, beta1=0.179, gamma2=0.005, beta2=0.035 -> E=136.159
gamma1=0.094, beta1=0.183, gamma2=0.021, beta2=-0.078 -> E=172.117
gamma1=0.100, beta1=0.204, gamma2=0.043, beta2=-0.037 -> E=137.723
gamma1=0.127, beta1=0.194, gamma2=0.063, beta2=-0.047 -> E=198.492
gamma1=0.110, beta1=0.205, gamma2=0.047, beta2=-0.045 -> E=66.002
gamma1=0.117, beta1=0.206, gamma2=0.039, beta2=-0.041 -> E=35.232
gamma1=0.127, beta1=0.205, gamma2=0.041, beta2=-0.042 -> E=201.304
gamma1=0.117, beta1=0.208, gamma2=0.041, beta2=-0.037 -> E=35.772
gamma1=0.110, beta1=0.208, gamma2=0.032, beta2=-0.039 -> E=60.074
gamma1=0.122, beta1=0.206, gamma2=0.038, beta2=-0.041 -> E=97.612
gamma1=0.117, beta1=0.205, gamma2=0.038, beta2=-0.041 -> E=34.179
gamma1=0.115, beta1=0.206, gamma2=0.037, beta2=-0.040 -> E=33.201
gamma1=0.115, beta1=0.206, gamma2=0.036, beta2=-0.040 -> E=31.688
gamma1=0.116, beta1=0.206, gamma2=0.035, beta2=-0.040 -> E=34.848
gamma1=0.115, beta1=0.206, gamma2=0.036, beta2=-0.040 -> E=29.953
gamma1=0.116, beta1=0.207, gamma2=0.036, beta2=-0.041 -> E=35.385
gamma1=0.115, beta1=0.206, gamma2=0.036, beta2=-0.041 -> E=32.548
gamma1=0.116, beta1=0.205, gamma2=0.036, beta2=-0.041 -> E=29.857
gamma1=0.115, beta1=0.204, gamma2=0.036, beta2=-0.041 -> E=32.248
gamma1=0.116, beta1=0.205, gamma2=0.036, beta2=-0.041 -> E=37.296
gamma1=0.116, beta1=0.205, gamma2=0.036, beta2=-0.041 -> E=33.301
gamma1=0.116, beta1=0.205, gamma2=0.036, beta2=-0.041 -> E=30.673
gamma1=0.116, beta1=0.205, gamma2=0.036, beta2=-0.041 -> E=35.290

Optimal parameters: [ 0.11563555  0.20491384  0.03585327 -0.04093898]

=== Measured bests ===
Best ANY: 01100000 E= -95.0 count= 22 feasible? True
Best FEASIBLE: 01100000 E= -95.0 count= 22
Active flows: ['f_A_D', 'f_B_C']

Most frequent bitstring: 00011010
QUBO energy: -93.0
Active flows: ['f_B_D', 'f_A_E', 'f_E_C']

Match reference? False

```