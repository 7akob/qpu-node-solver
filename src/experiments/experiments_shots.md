# Experiments with shots

P set at 30 for full experiment

`network_qaoa_sim.py`

## Summary

Increasing the number of measurement shots confirms that the QAOA circuit consistently encodes the global optimum with nonzero probability; however, at shallow depth the optimal solution remains in the low-probability tail rather than dominating the measurement distribution.

## Shots : 56
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=51.839
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=95.589
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=65.554
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=57.500
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=82.911
gamma1=-0.486, beta1=0.054, gamma2=-0.002, beta2=-0.458 -> E=60.250
gamma1=0.670, beta1=0.166, gamma2=0.045, beta2=-0.204 -> E=114.179
gamma1=0.175, beta1=0.276, gamma2=0.090, beta2=0.315 -> E=58.804
gamma1=0.313, beta1=0.252, gamma2=0.100, beta2=0.102 -> E=70.143
gamma1=0.280, beta1=0.397, gamma2=0.098, beta2=0.090 -> E=77.929
gamma1=0.306, beta1=0.300, gamma2=0.050, beta2=0.101 -> E=84.018
gamma1=0.303, beta1=0.263, gamma2=0.193, beta2=0.097 -> E=88.893
gamma1=0.341, beta1=0.311, gamma2=0.104, beta2=0.126 -> E=73.893
gamma1=0.267, beta1=0.252, gamma2=0.026, beta2=0.067 -> E=79.161
gamma1=0.334, beta1=0.303, gamma2=0.099, beta2=0.063 -> E=98.357
gamma1=0.318, beta1=0.296, gamma2=0.076, beta2=0.195 -> E=89.607
gamma1=0.266, beta1=0.286, gamma2=0.134, beta2=0.103 -> E=64.625
gamma1=0.304, beta1=0.299, gamma2=0.095, beta2=0.124 -> E=54.589
gamma1=0.303, beta1=0.301, gamma2=0.104, beta2=0.100 -> E=94.000
gamma1=0.294, beta1=0.298, gamma2=0.093, beta2=0.099 -> E=57.946
gamma1=0.302, beta1=0.295, gamma2=0.100, beta2=0.099 -> E=60.804
gamma1=0.300, beta1=0.310, gamma2=0.102, beta2=0.100 -> E=84.321
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=39.750
gamma1=0.310, beta1=0.294, gamma2=0.095, beta2=0.097 -> E=43.982
gamma1=0.303, beta1=0.301, gamma2=0.098, beta2=0.094 -> E=59.946
gamma1=0.308, beta1=0.305, gamma2=0.093, beta2=0.106 -> E=66.946
gamma1=0.304, beta1=0.303, gamma2=0.097, beta2=0.094 -> E=62.982
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.099 -> E=70.143
gamma1=0.302, beta1=0.300, gamma2=0.095, beta2=0.099 -> E=63.911
gamma1=0.304, beta1=0.300, gamma2=0.097, beta2=0.099 -> E=50.571
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.098 -> E=73.321
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=73.482
gamma1=0.303, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=65.429
gamma1=0.304, beta1=0.301, gamma2=0.096, beta2=0.099 -> E=47.786
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=74.964
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=75.018
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=65.375
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=55.571
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=63.214
gamma1=0.304, beta1=0.301, gamma2=0.097, beta2=0.099 -> E=70.054

Optimal parameters: [0.30367036 0.30070019 0.0968991  0.09880725]

=== Measured bests ===
Best ANY: 01000110 E= -53.0 count= 1 feasible? True
Best FEASIBLE: 01000110 E= -53.0 count= 1
Active flows: ['f_A_D', 'f_B_E', 'f_E_C']

Most frequent bitstring: 01001010
QUBO energy: -24.0
Active flows: ['f_A_D', 'f_A_E', 'f_E_C']

Match reference? False

```

## Shots : 512
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=65.688
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=95.402
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=81.916
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=80.398
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=111.682
gamma1=-0.204, beta1=0.025, gamma2=-0.149, beta2=-0.680 -> E=80.889
gamma1=0.058, beta1=0.168, gamma2=-0.020, beta2=0.500 -> E=93.633
gamma1=0.229, beta1=0.261, gamma2=0.065, beta2=-0.134 -> E=156.209
gamma1=0.324, beta1=0.256, gamma2=0.100, beta2=0.100 -> E=111.793
gamma1=0.295, beta1=0.397, gamma2=0.099, beta2=0.122 -> E=70.684
gamma1=0.294, beta1=0.297, gamma2=0.051, beta2=0.110 -> E=75.023
gamma1=0.212, beta1=0.286, gamma2=0.125, beta2=0.138 -> E=178.348
gamma1=0.322, beta1=0.291, gamma2=0.107, beta2=0.144 -> E=113.131
gamma1=0.341, beta1=0.319, gamma2=0.089, beta2=0.012 -> E=103.318
gamma1=0.341, beta1=0.295, gamma2=0.105, beta2=0.127 -> E=85.686
gamma1=0.293, beta1=0.297, gamma2=0.103, beta2=0.110 -> E=67.955
gamma1=0.289, beta1=0.302, gamma2=0.107, beta2=0.079 -> E=76.262
gamma1=0.301, beta1=0.295, gamma2=0.100, beta2=0.099 -> E=60.719
gamma1=0.307, beta1=0.288, gamma2=0.101, beta2=0.100 -> E=70.746
gamma1=0.301, beta1=0.295, gamma2=0.095, beta2=0.101 -> E=61.615
gamma1=0.294, beta1=0.292, gamma2=0.098, beta2=0.093 -> E=62.707
gamma1=0.302, beta1=0.299, gamma2=0.100, beta2=0.097 -> E=64.801
gamma1=0.300, beta1=0.296, gamma2=0.100, beta2=0.100 -> E=57.395
gamma1=0.298, beta1=0.296, gamma2=0.101, beta2=0.102 -> E=66.387
gamma1=0.300, beta1=0.296, gamma2=0.100, beta2=0.100 -> E=62.648
gamma1=0.299, beta1=0.296, gamma2=0.100, beta2=0.099 -> E=62.664
gamma1=0.300, beta1=0.296, gamma2=0.101, beta2=0.100 -> E=63.480
gamma1=0.300, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=55.666
gamma1=0.299, beta1=0.294, gamma2=0.099, beta2=0.101 -> E=56.514
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=65.254
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=54.361
gamma1=0.300, beta1=0.295, gamma2=0.100, beta2=0.101 -> E=60.910
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=64.668
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=66.088
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=60.545
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.100 -> E=54.014
gamma1=0.299, beta1=0.295, gamma2=0.100, beta2=0.101 -> E=61.043

Optimal parameters: [0.29945708 0.29500954 0.09973957 0.10049346]

=== Measured bests ===
Best ANY: 01100000 E= -55.0 count= 1 feasible? True
Best FEASIBLE: 01100000 E= -55.0 count= 1
Active flows: ['f_A_D', 'f_B_C']

Most frequent bitstring: 00110000
QUBO energy: -24.0
Active flows: ['f_B_C', 'f_B_D']

Match reference? False

```

## Shots : 1024
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=64.229
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=92.021
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=82.020
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=77.557
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=104.673
gamma1=-0.216, beta1=-0.030, gamma2=-0.147, beta2=-0.651 -> E=88.979
gamma1=0.111, beta1=0.179, gamma2=0.009, beta2=0.537 -> E=108.171
gamma1=0.245, beta1=0.265, gamma2=0.073, beta2=-0.140 -> E=69.845
gamma1=0.327, beta1=0.258, gamma2=0.100, beta2=0.100 -> E=113.629
gamma1=0.260, beta1=0.392, gamma2=0.099, beta2=0.098 -> E=86.042
gamma1=0.318, beta1=0.307, gamma2=0.054, beta2=0.100 -> E=95.396
gamma1=0.303, beta1=0.268, gamma2=0.195, beta2=0.097 -> E=73.209
gamma1=0.305, beta1=0.303, gamma2=0.103, beta2=0.150 -> E=61.031
gamma1=0.219, beta1=0.258, gamma2=0.086, beta2=0.165 -> E=185.436
gamma1=0.343, beta1=0.325, gamma2=0.118, beta2=0.169 -> E=88.139
gamma1=0.303, beta1=0.307, gamma2=0.094, beta2=0.158 -> E=46.264
gamma1=0.288, beta1=0.304, gamma2=0.084, beta2=0.175 -> E=85.131
gamma1=0.305, beta1=0.303, gamma2=0.092, beta2=0.158 -> E=49.116
gamma1=0.305, beta1=0.311, gamma2=0.087, beta2=0.152 -> E=59.405
gamma1=0.299, beta1=0.304, gamma2=0.093, beta2=0.156 -> E=60.160
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.165 -> E=46.162
gamma1=0.313, beta1=0.308, gamma2=0.096, beta2=0.172 -> E=55.372
gamma1=0.302, beta1=0.310, gamma2=0.097, beta2=0.168 -> E=51.988
gamma1=0.306, beta1=0.310, gamma2=0.098, beta2=0.165 -> E=48.200
gamma1=0.307, beta1=0.313, gamma2=0.096, beta2=0.164 -> E=46.384
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=46.294
gamma1=0.307, beta1=0.311, gamma2=0.096, beta2=0.166 -> E=46.826
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=49.497
gamma1=0.307, beta1=0.312, gamma2=0.097, beta2=0.165 -> E=49.582
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=45.652
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.165 -> E=46.636
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=44.117
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=45.995
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=44.383
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=50.032
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=44.577
gamma1=0.306, beta1=0.311, gamma2=0.097, beta2=0.166 -> E=47.500

Optimal parameters: [0.3058733  0.3109792  0.09690345 0.16554753]

=== Measured bests ===
Best ANY: 10010000 E= -55.0 count= 3 feasible? True
Best FEASIBLE: 10010000 E= -55.0 count= 3
Active flows: ['f_A_C', 'f_B_D']

Most frequent bitstring: 01001010
QUBO energy: -24.0
Active flows: ['f_A_D', 'f_A_E', 'f_E_C']

Match reference? False

```

## Shots : 2048
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=62.081
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=92.654
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=86.109
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=76.018
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=109.168
gamma1=-0.188, beta1=-0.084, gamma2=-0.123, beta2=-0.652 -> E=98.978
gamma1=0.139, beta1=0.173, gamma2=0.026, beta2=0.550 -> E=99.925
gamma1=0.182, beta1=0.300, gamma2=0.100, beta2=0.058 -> E=33.767
gamma1=-0.005, beta1=0.275, gamma2=0.086, beta2=-0.105 -> E=45.046
gamma1=0.178, beta1=0.252, gamma2=0.100, beta2=0.070 -> E=52.730
gamma1=0.133, beta1=0.367, gamma2=0.098, beta2=0.113 -> E=100.628
gamma1=0.183, beta1=0.300, gamma2=0.050, beta2=0.057 -> E=40.385
gamma1=0.197, beta1=0.307, gamma2=0.113, beta2=-0.040 -> E=26.165
gamma1=0.216, beta1=0.267, gamma2=0.052, beta2=-0.105 -> E=183.583
gamma1=0.177, beta1=0.344, gamma2=0.137, beta2=-0.028 -> E=54.616
gamma1=0.186, beta1=0.304, gamma2=0.110, beta2=-0.044 -> E=23.308
gamma1=0.188, beta1=0.293, gamma2=0.095, beta2=-0.060 -> E=20.328
gamma1=0.186, beta1=0.270, gamma2=0.105, beta2=-0.057 -> E=21.484
gamma1=0.189, beta1=0.294, gamma2=0.098, beta2=-0.063 -> E=17.102
gamma1=0.186, beta1=0.296, gamma2=0.102, beta2=-0.072 -> E=24.496
gamma1=0.190, beta1=0.298, gamma2=0.096, beta2=-0.064 -> E=18.377
gamma1=0.198, beta1=0.291, gamma2=0.101, beta2=-0.063 -> E=33.952
gamma1=0.189, beta1=0.291, gamma2=0.094, beta2=-0.066 -> E=18.539
gamma1=0.181, beta1=0.295, gamma2=0.095, beta2=-0.058 -> E=37.329
gamma1=0.193, beta1=0.292, gamma2=0.100, beta2=-0.062 -> E=17.416
gamma1=0.188, beta1=0.293, gamma2=0.098, beta2=-0.061 -> E=19.375
gamma1=0.188, beta1=0.294, gamma2=0.098, beta2=-0.063 -> E=18.749
gamma1=0.189, beta1=0.294, gamma2=0.098, beta2=-0.063 -> E=19.741
gamma1=0.188, beta1=0.293, gamma2=0.098, beta2=-0.063 -> E=17.084
gamma1=0.188, beta1=0.294, gamma2=0.098, beta2=-0.064 -> E=20.543
gamma1=0.188, beta1=0.293, gamma2=0.098, beta2=-0.064 -> E=19.481
gamma1=0.188, beta1=0.293, gamma2=0.098, beta2=-0.062 -> E=21.529
gamma1=0.189, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=16.456
gamma1=0.189, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=18.024
gamma1=0.189, beta1=0.293, gamma2=0.099, beta2=-0.063 -> E=19.028
gamma1=0.188, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=18.006
gamma1=0.189, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=19.870
gamma1=0.189, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=16.705
gamma1=0.189, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=19.232
gamma1=0.189, beta1=0.294, gamma2=0.099, beta2=-0.063 -> E=16.988

Optimal parameters: [ 0.18863396  0.29356232  0.09866334 -0.06341307]

=== Measured bests ===
Best ANY: 10010000 E= -55.0 count= 31 feasible? True
Best FEASIBLE: 10010000 E= -55.0 count= 31
Active flows: ['f_A_C', 'f_B_D']

Most frequent bitstring: 00001111
QUBO energy: -51.0
Active flows: ['f_A_E', 'f_B_E', 'f_E_C', 'f_E_D']

Match reference? False

```

## Shots : 4096
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=60.874
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=92.851
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=84.156
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=75.038
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=110.216
gamma1=-0.193, beta1=-0.059, gamma2=-0.119, beta2=-0.661 -> E=92.852
gamma1=0.119, beta1=0.168, gamma2=0.020, beta2=0.540 -> E=82.229
gamma1=0.203, beta1=0.230, gamma2=0.057, beta2=-0.115 -> E=82.056
gamma1=0.329, beta1=0.260, gamma2=0.100, beta2=0.100 -> E=116.341
gamma1=0.252, beta1=0.388, gamma2=0.099, beta2=0.102 -> E=83.035
gamma1=0.315, beta1=0.308, gamma2=0.053, beta2=0.100 -> E=90.328
gamma1=0.309, beta1=0.267, gamma2=0.194, beta2=0.103 -> E=78.896
gamma1=0.338, beta1=0.321, gamma2=0.105, beta2=0.075 -> E=98.521
gamma1=0.256, beta1=0.244, gamma2=0.060, beta2=0.158 -> E=86.726
gamma1=0.329, beta1=0.315, gamma2=0.101, beta2=0.138 -> E=109.733
gamma1=0.287, beta1=0.272, gamma2=0.078, beta2=0.008 -> E=74.870
gamma1=0.347, beta1=0.309, gamma2=0.086, beta2=0.104 -> E=97.715
gamma1=0.296, beta1=0.309, gamma2=0.092, beta2=0.100 -> E=68.065
gamma1=0.291, beta1=0.299, gamma2=0.123, beta2=0.099 -> E=81.830
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.105 -> E=60.608
gamma1=0.297, beta1=0.291, gamma2=0.095, beta2=0.105 -> E=66.113
gamma1=0.304, beta1=0.300, gamma2=0.098, beta2=0.105 -> E=59.771
gamma1=0.310, beta1=0.301, gamma2=0.105, beta2=0.106 -> E=78.969
gamma1=0.303, beta1=0.303, gamma2=0.094, beta2=0.105 -> E=62.565
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=58.491
gamma1=0.306, beta1=0.301, gamma2=0.100, beta2=0.106 -> E=62.716
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.106 -> E=58.628
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=59.650
gamma1=0.305, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=59.803
gamma1=0.304, beta1=0.301, gamma2=0.099, beta2=0.105 -> E=58.692
gamma1=0.305, beta1=0.301, gamma2=0.099, beta2=0.105 -> E=58.509
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=59.021
gamma1=0.304, beta1=0.301, gamma2=0.099, beta2=0.105 -> E=60.127
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=58.882
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=60.529
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=57.071
gamma1=0.304, beta1=0.301, gamma2=0.098, beta2=0.105 -> E=57.084

Optimal parameters: [0.30439333 0.300685   0.09839952 0.10536032]

=== Measured bests ===
Best ANY: 10010000 E= -55.0 count= 10 feasible? True
Best FEASIBLE: 10010000 E= -55.0 count= 10
Active flows: ['f_A_C', 'f_B_D']

Most frequent bitstring: 00110000
QUBO energy: -24.0
Active flows: ['f_B_C', 'f_B_D']

Match reference? False

```

## Shots : 8192
```
Feasible? True

=== Reference ===
Best QUBO energy: -55.0
Best bitstring: 01100000
Active flows: ['f_A_D', 'f_B_C']

=== QAOA p=2 ===
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=61.622
gamma1=1.300, beta1=0.300, gamma2=0.100, beta2=0.100 -> E=92.425
gamma1=0.300, beta1=1.300, gamma2=0.100, beta2=0.100 -> E=81.798
gamma1=0.300, beta1=0.300, gamma2=1.100, beta2=0.100 -> E=75.834
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=1.100 -> E=109.353
gamma1=-0.197, beta1=-0.026, gamma2=-0.129, beta2=-0.671 -> E=107.358
gamma1=0.146, beta1=0.199, gamma2=0.029, beta2=0.559 -> E=68.313
gamma1=0.148, beta1=0.200, gamma2=0.030, beta2=-0.056 -> E=89.198
gamma1=0.327, beta1=0.258, gamma2=0.100, beta2=0.100 -> E=115.319
gamma1=0.255, beta1=0.389, gamma2=0.099, beta2=0.103 -> E=84.548
gamma1=0.317, beta1=0.308, gamma2=0.053, beta2=0.100 -> E=92.810
gamma1=0.302, beta1=0.264, gamma2=0.193, beta2=0.105 -> E=73.092
gamma1=0.327, beta1=0.315, gamma2=0.107, beta2=0.061 -> E=107.120
gamma1=0.277, beta1=0.259, gamma2=0.068, beta2=0.182 -> E=79.349
gamma1=0.340, beta1=0.319, gamma2=0.105, beta2=0.123 -> E=93.662
gamma1=0.265, beta1=0.251, gamma2=0.070, beta2=0.026 -> E=86.581
gamma1=0.349, beta1=0.306, gamma2=0.093, beta2=0.099 -> E=81.496
gamma1=0.298, beta1=0.308, gamma2=0.091, beta2=0.100 -> E=68.420
gamma1=0.292, beta1=0.302, gamma2=0.124, beta2=0.102 -> E=87.463
gamma1=0.300, beta1=0.300, gamma2=0.100, beta2=0.095 -> E=62.076
gamma1=0.299, beta1=0.291, gamma2=0.096, beta2=0.100 -> E=62.661
gamma1=0.305, beta1=0.300, gamma2=0.099, beta2=0.100 -> E=58.650
gamma1=0.313, beta1=0.298, gamma2=0.103, beta2=0.101 -> E=81.361
gamma1=0.304, beta1=0.302, gamma2=0.094, beta2=0.100 -> E=57.856
gamma1=0.307, beta1=0.303, gamma2=0.094, beta2=0.100 -> E=57.427
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=55.516
gamma1=0.307, beta1=0.307, gamma2=0.094, beta2=0.106 -> E=57.155
gamma1=0.307, beta1=0.303, gamma2=0.093, beta2=0.103 -> E=57.542
gamma1=0.309, beta1=0.305, gamma2=0.094, beta2=0.101 -> E=57.518
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=56.899
gamma1=0.306, beta1=0.305, gamma2=0.093, beta2=0.102 -> E=57.836
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.501
gamma1=0.307, beta1=0.304, gamma2=0.093, beta2=0.101 -> E=57.842
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.039
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.680
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.217
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.127
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.655
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=57.236
gamma1=0.307, beta1=0.304, gamma2=0.094, beta2=0.102 -> E=56.917

Optimal parameters: [0.30681815 0.30398984 0.09369141 0.10220302]

=== Measured bests ===
Best ANY: 10010000 E= -55.0 count= 10 feasible? True
Best FEASIBLE: 10010000 E= -55.0 count= 10
Active flows: ['f_A_C', 'f_B_D']

Most frequent bitstring: 00110000
QUBO energy: -24.0
Active flows: ['f_B_C', 'f_B_D']

Match reference? False

```