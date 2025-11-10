# iqm-project

## Step 1 - Run it locally
After writing codebase I tested it locally in an venv envoirement and go the following result:
```
Best sample (binary values): {'f_A_C': np.int8(1), 'f_A_D': np.int8(1), 'f_A_E': np.int8(1), 'f_B_C': np.int8(1), 'f_B_D': np.int8(0), 'f_B_E': np.int8(1), 'f_E_C': np.int8(1), 'f_E_D': np.int8(0)} Energy: -212.0 Interpreting flows (active arcs = 1 means 1 unit flow): f_A_C f_A_D f_A_E f_B_C f_B_E f_E_C Sink C demand 3, received 3 Sink D demand 2, received 1
```


Results from testing the iqm connection and running a test circuit, terminal:
```
 UserWarning: Your IQM Client version 31.0.0 was built for a different version of IQM Server. You might encounter issues. For the best experience, consider using a version of IQM Client that satisfies 32.1.1 <= iqm-client < 33.0.
  warnings.warn(version_incompatibility_msg)
Connected to IQM backend: IQM Backend
Test circuit result: {'11': 484, '10': 29, '00': 470, '01': 17}
Best sample (binary values):
{'f_A_C': np.int8(1), 'f_A_D': np.int8(1), 'f_A_E': np.int8(1), 'f_B_C': np.int8(1), 'f_B_D': np.int8(1), 'f_B_E': np.int8(0), 'f_E_C': np.int8(0), 'f_E_D': np.int8(0)}
Energy: -212.0
```

result on iqm:
```
[ { "11": 484, "00": 470 } ]
```