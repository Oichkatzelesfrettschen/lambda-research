# Quantum Lambda Calculi and Computation

Extensions of lambda calculus for quantum computation, incorporating quantum mechanical principles like superposition, entanglement, and measurement while respecting the no-cloning theorem and other quantum constraints.

## Overview

Quantum lambda calculi address:
- **Quantum States**: Superposition and entanglement as first-class values
- **No-Cloning**: Quantum information cannot be duplicated
- **Measurement**: Irreversible collapse of quantum superpositions
- **Reversibility**: Most quantum operations must be invertible
- **Linear Types**: Natural match for quantum resource constraints

## Fundamental Quantum Principles

### No-Cloning Theorem
Quantum states cannot be perfectly copied, which naturally leads to linear type systems:

```
-- Classical cloning (possible)
clone : A → A × A
clone x = (x, x)

-- Quantum cloning (impossible)
qclone : Qubit → Qubit × Qubit  -- Cannot exist!
```

### Quantum Superposition
Quantum states can exist in superposition of classical states:

```
-- Classical bit
Bit = {0, 1}

-- Quantum bit (qubit)
Qubit = α|0⟩ + β|1⟩  where |α|² + |β|² = 1
```

### Measurement and Collapse
Measurement causes irreversible collapse of superposition:

```
measure : Qubit ⊸ Bool
-- measure(α|0⟩ + β|1⟩) → 0 with probability |α|², 1 with probability |β|²
```

## Quantum Lambda Calculus (QLC)

### Syntax
```
Types:
  A, B ::= Qubit | Bool | A ⊸ B | A ⊗ B | !A | 0 | 1

Terms:
  M, N ::= x | λx.M | M N | ⟨M,N⟩ | let ⟨x,y⟩ = M in N |
           |0⟩ | |1⟩ | H M | X M | Z M | CNOT M N |
           measure M | new_qubit | discard M

Quantum Gates:
  H : Qubit ⊸ Qubit          -- Hadamard gate
  X : Qubit ⊸ Qubit          -- Pauli-X (NOT gate)
  Y : Qubit ⊸ Qubit          -- Pauli-Y gate
  Z : Qubit ⊸ Qubit          -- Pauli-Z gate
  CNOT : Qubit ⊸ Qubit ⊸ Qubit ⊗ Qubit  -- Controlled-NOT
```

### Quantum Type System
```
Linear Context: Γ ::= ∅ | Γ, x:A  (qubits used exactly once)
Classical Context: Δ ::= ∅ | Δ, x:!A  (classical data can be copied)

Typing Judgment: Δ; Γ ⊢ M : A

Basic Rules:
Δ; x:A ⊢ x : A                          (Qubit Variable)

Δ; Γ, x:A ⊢ M : B
─────────────────                        (Abstraction)
Δ; Γ ⊢ λx.M : A ⊸ B

Δ; Γ₁ ⊢ M : A ⊸ B    Δ; Γ₂ ⊢ N : A
─────────────────────────────────        (Application)
Δ; Γ₁, Γ₂ ⊢ M N : B
```

### Quantum Gate Operations
```
Hadamard Gate:
Δ; q:Qubit ⊢ H q : Qubit
H |0⟩ = (|0⟩ + |1⟩)/√2
H |1⟩ = (|0⟩ - |1⟩)/√2

Controlled-NOT:
Δ; c:Qubit, t:Qubit ⊢ CNOT c t : Qubit ⊗ Qubit
CNOT |00⟩ = |00⟩
CNOT |01⟩ = |01⟩
CNOT |10⟩ = |11⟩
CNOT |11⟩ = |10⟩

Measurement:
Δ; q:Qubit ⊢ measure q : Bool
-- Non-deterministic, collapses superposition
```

## Examples and Quantum Algorithms

### Quantum Teleportation
```
teleport : Qubit ⊸ (Qubit ⊗ Qubit) ⊸ (Bool ⊗ Bool ⊗ Qubit)
teleport ψ entangled_pair =
  let ⟨a, b⟩ = entangled_pair in
  let ⟨ψ', a'⟩ = CNOT ψ a in
  let ψ'' = H ψ' in
  let x = measure ψ'' in
  let y = measure a' in
  let b' = if x then X b else b in
  let b'' = if y then Z b' else b' in
  ⟨x, y, b''⟩

-- Creates entangled pair for teleportation
create_bell_pair : 1 ⊸ (Qubit ⊗ Qubit)
create_bell_pair _ =
  let a = |0⟩ in
  let b = |0⟩ in
  let a' = H a in
  CNOT a' b
```

### Deutsch-Jozsa Algorithm
```
-- Determine if function is constant or balanced with one query
deutsch_jozsa : (Qubit ⊸ Qubit) ⊸ Bool
deutsch_jozsa f =
  let x = |0⟩ in
  let y = |1⟩ in
  let x' = H x in
  let y' = H y in
  let ⟨x'', y''⟩ = f ⟨x', y'⟩ in
  let x''' = H x'' in
  measure x'''  -- Returns 0 if constant, 1 if balanced
```

### Grover's Search Algorithm
```
-- Quantum search in unsorted database
grover_iteration : (Qubit List ⊸ Qubit List) ⊸ Qubit List ⊸ Qubit List
grover_iteration oracle qubits =
  let qubits' = oracle qubits in
  let qubits'' = map H qubits' in
  let qubits''' = phase_flip_zero qubits'' in
  map H qubits'''

grover_search : Nat → (Qubit List ⊸ Qubit List) ⊸ Qubit List ⊸ Qubit List
grover_search 0 oracle qubits = qubits
grover_search n oracle qubits =
  grover_search (n-1) oracle (grover_iteration oracle qubits)
```

## Advanced Quantum Features

### Quantum Control Flow
```
-- Quantum conditional based on qubit measurement
qif : Qubit ⊸ (1 ⊸ A) ⊸ (1 ⊸ A) ⊸ A
qif q then_branch else_branch =
  let b = measure q in
  if b then then_branch () else else_branch ()

-- Quantum loops with superposition termination
qwhile : (Qubit ⊸ (Bool ⊗ Qubit)) ⊸ Qubit ⊸ Qubit
qwhile test_and_update q =
  let ⟨continue, q'⟩ = test_and_update q in
  if continue then qwhile test_and_update q' else q'
```

### Quantum Data Structures
```
-- Quantum lists with superposition of lengths
QList : Type → Type
qnil : QList A
qcons : A ⊸ QList A ⊸ QList A

-- Quantum trees for quantum algorithms
QTree : Type → Type
qleaf : A ⊸ QTree A
qnode : QTree A ⊸ QTree A ⊸ QTree A

-- Quantum amplitude encoding
quantum_encode : [Complex] → Qubit List
quantum_amplitude : Qubit List → [Complex]
```

### Higher-Order Quantum Operations
```
-- Quantum function composition
qcompose : (B ⊸ C) ⊸ (A ⊸ B) ⊸ (A ⊸ C)
qcompose g f = λx. g (f x)

-- Quantum mapping over quantum lists
qmap : (A ⊸ B) ⊸ QList A ⊸ QList B
qmap f qnil = qnil
qmap f (qcons x xs) = qcons (f x) (qmap f xs)

-- Quantum fold with linear accumulator
qfold : (A ⊸ B ⊸ B) ⊸ B ⊸ QList A ⊸ B
qfold f acc qnil = acc
qfold f acc (qcons x xs) = qfold f (f x acc) xs
```

## Quantum Process Calculi

### Quantum Pi-Calculus
```
Processes:
P, Q ::= 0                    -- Null process
       | c?q.P                -- Receive qubit on channel c
       | c!q.P                -- Send qubit on channel c
       | P | Q                -- Parallel composition
       | (νc)P                -- Create new quantum channel
       | [q = |0⟩]P, Q        -- Quantum pattern matching

Quantum Channels:
Classical: c : !Qubit.T
Quantum: c : Qubit ⊸ T  (linear use)
```

### Quantum Communication Example
```
-- Quantum key distribution protocol
QKD_Alice = (νkey_channel)
  let alice_bits = random_bits(n) in
  let alice_bases = random_bases(n) in
  let qubits = prepare_qubits(alice_bits, alice_bases) in
  key_channel!qubits.
  public_channel?bob_bases.
  let shared_key = extract_key(alice_bits, alice_bases, bob_bases) in
  secure_channel!shared_key.0

QKD_Bob =
  key_channel?qubits.
  let bob_bases = random_bases(n) in
  let bob_bits = measure_qubits(qubits, bob_bases) in
  public_channel!bob_bases.
  secure_channel?alice_key.
  let shared_key = extract_key(bob_bits, bob_bases, alice_bases) in
  use_key(shared_key)
```

## Quantum Error Correction

### Quantum Error Correction Codes
```
-- Three-qubit bit-flip code
encode_3bit : Qubit ⊸ (Qubit ⊗ Qubit ⊗ Qubit)
encode_3bit q =
  let q1 = q in
  let q2 = |0⟩ in
  let q3 = |0⟩ in
  let ⟨q1', q2'⟩ = CNOT q1 q2 in
  let ⟨q1'', q3'⟩ = CNOT q1' q3 in
  ⟨q1'', q2', q3'⟩

decode_3bit : (Qubit ⊗ Qubit ⊗ Qubit) ⊸ Qubit
decode_3bit ⟨q1, q2, q3⟩ =
  let s1 = measure (CNOT q1 (CNOT q2 |0⟩)) in
  let s2 = measure (CNOT q1 (CNOT q3 |0⟩)) in
  match (s1, s2) with
    | (0, 0) → q1  -- No error
    | (0, 1) → X q1  -- Error on q3
    | (1, 0) → X q1  -- Error on q2
    | (1, 1) → q1    -- Error on q1 (corrected by syndrome)
```

### Stabilizer Codes
```
-- General stabilizer code framework
Stabilizer : [QubitOperator] → QuantumCode
encode_stabilizer : Stabilizer → Qubit List ⊸ Qubit List
decode_stabilizer : Stabilizer → Qubit List ⊸ Qubit List

-- Surface code for topological quantum error correction
surface_code : Nat → Nat → Stabilizer
surface_code width height =
  generate_stabilizers(width, height, face_operators, vertex_operators)
```

## Quantum Types and Effects

### Quantum Effect System
```
Effects: ε ::= Pure | Quantum | Measurement | Entanglement

Quantum Computation Type:
QComp : Effect → Type → Type

-- Pure quantum operations (reversible)
hadamard : Qubit → QComp Quantum Qubit
cnot : Qubit × Qubit → QComp Quantum (Qubit × Qubit)

-- Measurement effects (irreversible)
measure : Qubit → QComp Measurement Bool

-- Entanglement effects
entangle : Qubit × Qubit → QComp Entanglement (Qubit × Qubit)
```

### Quantum Monads
```
-- Quantum computation as monadic effect
QState : Type → Type
return : A → QState A
bind : QState A → (A → QState B) → QState B

-- Quantum operations in monadic style
bell_state : QState (Qubit × Qubit)
bell_state = do
  q1 ← new_qubit |0⟩
  q2 ← new_qubit |0⟩
  q1' ← hadamard q1
  ⟨q1'', q2'⟩ ← cnot ⟨q1', q2⟩
  return ⟨q1'', q2'⟩
```

## Quantum Machine Models

### Quantum Abstract Machine
```
-- Stack-based quantum machine
data QInstruction =
  | QLoad Qubit           -- Load qubit onto stack
  | QGate QuantumGate     -- Apply gate to top qubits
  | QMeasure              -- Measure top qubit
  | QJump Condition Addr  -- Conditional jump based on measurement
  | QCall Function        -- Call quantum subroutine

execute_quantum : [QInstruction] → QubitsStack → QubitsStack
```

### Quantum Turing Machine
```
-- Quantum generalization of Turing machine
QTM = (Q, Σ, δ, q₀, F)
where δ : Q × Σ → Superposition(Q × Σ × {L,R})

-- Evolution as unitary transformation
evolve : QTMState → QTMState
evolve state = apply_superposition_of_transitions(state)
```

## Quantum Compilation and Optimization

### Circuit Compilation
```
-- Compile quantum lambda terms to quantum circuits
compile_to_circuit : QuantumTerm → QuantumCircuit
compile_to_circuit term =
  let normalized = normalize_term(term) in
  let gates = extract_gates(normalized) in
  optimize_circuit(gates)

-- Circuit optimization passes
optimize_circuit : QuantumCircuit → QuantumCircuit
optimize_circuit circuit =
  circuit
  |> remove_redundant_gates
  |> merge_single_qubit_rotations
  |> minimize_cnot_count
  |> parallelize_commuting_gates
```

### Quantum Resource Estimation
```
-- Estimate quantum resources needed
estimate_resources : QuantumProgram → ResourceEstimate
estimate_resources program = {
  qubit_count = count_qubits(program),
  gate_count = count_gates(program),
  circuit_depth = calculate_depth(program),
  error_budget = estimate_errors(program)
}
```

## Applications

### Quantum Cryptography
```
-- Quantum key distribution
quantum_key_distribution : Channel → SharedKey
-- Post-quantum cryptography
lattice_based_encryption : PublicKey → Message → QuantumSecureCiphertext
```

### Quantum Simulation
```
-- Simulate quantum chemistry
simulate_molecule : MolecularHamiltonian → GroundStateEnergy
-- Quantum optimization
quantum_approximate_optimization : CostFunction → OptimalParameters
```

### Quantum Machine Learning
```
-- Quantum neural networks
quantum_neural_network : QuantumData → ClassificationResult
-- Variational quantum algorithms
variational_quantum_eigensolver : Hamiltonian → GroundState
```

## Implementation Challenges

### Decoherence and Noise
```
-- Model quantum noise in computation
NoiseModel : QuantumOperation → NoisyQuantumOperation
simulate_with_noise : NoiseModel → QuantumProgram → ClassicalResult

-- Error mitigation techniques
zero_noise_extrapolation : [NoisyResult] → IdealResult
readout_error_mitigation : MeasurementResults → CorrectedResults
```

### Quantum-Classical Interface
```
-- Hybrid quantum-classical algorithms
hybrid_computation : ClassicalData → QuantumSubroutine → ClassicalResult
quantum_classical_optimization : Objective → Parameters → OptimalParameters
```

## Tools and Simulators

### Quantum Programming Languages
- **Qiskit**: Python framework for quantum computing
- **Cirq**: Google's quantum programming framework
- **Q#**: Microsoft's quantum programming language
- **Quipper**: Functional quantum programming language

### Quantum Simulators
- **QuTiP**: Quantum toolbox in Python
- **Forest**: Rigetti's quantum cloud services
- **IBM Quantum Experience**: Cloud-based quantum computing
- **Amazon Braket**: AWS quantum computing service

## Resources

- **Papers**: See [papers/bibliography.md](papers/bibliography.md) for quantum computation foundations
- **Implementations**: Quantum lambda calculus interpreters and simulators
- **Tutorials**: Quantum programming and algorithm development
- **Hardware**: Current quantum computing platforms and architectures

## Related Systems

- [Linear Lambda Calculus](../06-linear-lambda-calculus/) - Resource-aware foundation
- [Substructural Types](../09-substructural-types/) - Resource management principles
- [Concurrent Variants](../10-concurrent-variants/) - Process calculi for quantum communication
- [Modal Types](../19-modal-types/) - Quantum logic and necessity

---

*Quantum variants of lambda calculus provide formal foundations for quantum computation while respecting quantum mechanical constraints, enabling the development of quantum algorithms and protocols with mathematical rigor.*