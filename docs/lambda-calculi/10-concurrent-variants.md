# Concurrent Lambda Calculi and Process Variants

Extensions of lambda calculus designed for concurrent and parallel computation, including process calculi, actor models, and parallel evaluation strategies that capture communication, synchronization, and distributed computation.

## Overview

Concurrent variants of lambda calculus address:
- **Process Communication**: Message passing between concurrent processes
- **Synchronization**: Coordination of parallel activities
- **Mobility**: Processes and channels that can move between locations
- **Distribution**: Computation across multiple machines
- **Fault Tolerance**: Handling failures in concurrent systems

## Core Systems

### Pi-Calculus (π-calculus)

The foundational mobile process calculus for concurrent communication.

#### Syntax
```
Processes:
P, Q ::= 0                    -- Null process
       | x(y).P               -- Input on channel x, bind y
       | x̄⟨v⟩.P               -- Output value v on channel x
       | P | Q                -- Parallel composition
       | (νx)P                -- Restriction (create new channel x)
       | !P                   -- Replication
       | if v = w then P else Q  -- Conditional

Values: v, w ::= x | true | false | ...
```

#### Operational Semantics
```
Communication:
x̄⟨v⟩.P | x(y).Q →τ P | Q[v/y]

Scope Extrusion:
(νx)(x̄⟨y⟩.P | Q) | z(w).R →τ (νx)(P | Q) | R[y/w]  if y ∉ fn(R)

Structural Congruence:
P | Q ≡ Q | P                 -- Commutativity
(P | Q) | R ≡ P | (Q | R)     -- Associativity
P | 0 ≡ P                     -- Identity
```

#### Example: Simple Communication
```
-- Sender process
Sender = x̄⟨42⟩.0

-- Receiver process
Receiver = x(y).ȳ⟨y + 1⟩.0

-- Complete system
System = (νx)(Sender | Receiver | z(w).0)
-- Reduces to: (νx)(0 | ȳ⟨43⟩.0 | z(w).0) where y is bound to 42
```

### Actor Model

Computation as autonomous actors communicating via asynchronous message passing.

#### Core Principles
- **Actors**: Independent computational entities
- **Messages**: Asynchronous communication primitive
- **Behaviors**: How actors respond to messages
- **Fairness**: All messages eventually delivered

#### Actor Calculus Syntax
```
Actors: A ::= actor a with behavior B
Behaviors: B ::= recv m.B | send a m.B | new a.B | B + B
Messages: m ::= data | actor_reference
Systems: S ::= A | S || S | (ν a)S
```

#### Example: Counter Actor
```
Counter(n) = recv {
  inc → Counter(n+1),
  dec → Counter(n-1),
  get(reply_to) → send reply_to n.Counter(n)
}

-- Usage
System = Counter(0) ||
         send counter inc.
         send counter get(client).
         recv x.print(x)  -- Receives current count
```

### Join-Calculus

Based on chemical abstract machine metaphor with join patterns.

#### Syntax
```
Processes: P, Q ::= 0 | def D in P | x⟨v⟩ | P | Q
Join Patterns: J ::= x(y) | J ∧ J
Definitions: D ::= J ⊳ P | D ∧ D
```

#### Example: Synchronization Barrier
```
def barrier(n) ∧ wait() ⊳
  if n = 1 then proceed()
  else barrier(n-1) ∧ wait()
in
  barrier(3) | wait() | wait() | wait()
-- All three wait() calls must synchronize before proceeding
```

## Lambda Calculus Extensions for Concurrency

### Concurrent ML (CML) Style

Lambda calculus extended with first-class synchronous operations.

#### Core Constructs
```
Events: α event types representing potential communications
always : α → α event              -- Always ready event
never : α event                   -- Never ready event
wrap : α event → (α → β) → β event  -- Event transformation
choose : α event list → α event   -- Non-deterministic choice
sync : α event → α                -- Synchronize on event

Channels:
channel : unit → α chan × α chan  -- Create channel pair
send : α chan → α → α event      -- Send event
recv : α chan → α event          -- Receive event
```

#### Example: Producer-Consumer
```
producer ch =
  let rec loop n =
    sync (send ch n);
    loop (n + 1)
  in loop 0

consumer ch =
  let rec loop () =
    let x = sync (recv ch) in
    print x;
    loop ()
  in loop ()

system =
  let (send_ch, recv_ch) = channel () in
  producer send_ch || consumer recv_ch
```

### Parallel Lambda Calculus

Lambda calculus with explicit parallelism constructs.

#### Syntax Extension
```
M, N ::= ... | M || N | future M | force M | fork M

Types: A ::= ... | A par | future A
```

#### Operational Semantics
```
Parallel Evaluation:
M || N →|| M' || N'  if M →* M' and N →* N'

Future Creation:
future M → M'  where M' evaluates M in parallel

Future Forcing:
force (future v) → v
force (future M) → blocks until M reduces to value
```

### Distributed Lambda Calculus

Lambda calculus extended for distributed computation.

#### Location-Aware Syntax
```
Terms: M, N ::= ... | M@l | here | there l
Locations: l ∈ Locations
Types: A ::= ... | A@l
```

#### Migration and Remote Execution
```
-- Execute computation at remote location
remote_exec : ∀l. (unit → α)@here → α@l
remote_exec f = (f ())@l

-- Mobile code pattern
mobile_agent : Location → (Data → Result) → Result
mobile_agent dest f =
  let computation = λ().f (fetch_local_data dest) in
  sync (remote_exec@dest computation)
```

## Advanced Concurrent Features

### Session-Typed Pi-Calculus

Pi-calculus with session types for protocol verification.

```
Session Types: S ::= !A.S | ?A.S | ⊕{li:Si} | &{li:Si} | end

Typed Processes:
x:S ⊢ P  -- Process P uses channel x according to session type S

Example - Binary Session:
client : !Nat.?Nat.end ⊢ x̄⟨42⟩.x(y).0
server : ?Nat.!Nat.end ⊢ x(z).x̄⟨z*2⟩.0
```

### Higher-Order Pi-Calculus

Pi-calculus where processes can be passed as messages.

```
Higher-Order Messages:
x̄⟨P⟩.Q | x(Y).R → Q | R[P/Y]

Mobile Code Example:
Server = request(code, data).
         (νresult)(code⟨data,result⟩ | result(answer).reply⟨answer⟩)

Client = server̄⟨λ(d,r).r̄⟨process(d)⟩, my_data⟩.
         reply(result).use_result(result)
```

### Ambient Calculus

Process calculus with hierarchical locations (ambients).

```
Processes: P ::= 0 | P|P | (νn)P | !P | M.P | n[P]
Capabilities: M ::= in n | out n | open n

Mobility Rules:
n[in m.P | Q] | m[R] → m[n[P | Q] | R]    -- Enter ambient
m[n[out m.P | Q] | R] → n[P | Q] | m[R]   -- Exit ambient
open n.P | n[Q] → P | Q                   -- Dissolve ambient
```

## Type Systems for Concurrency

### Linear Types for Processes
```
-- Channels must be used exactly once
Channel : Protocol → Linear Type
send_once : ∀A. Channel(!A.end) ⊸ A ⊸ 1
recv_once : ∀A. Channel(?A.end) ⊸ A
```

### Effect Types for Concurrency
```
-- Track communication effects
Communication : Effect
Pure : Effect
send : ∀A. Channel A → A → Computation Communication 1
pure_comp : ∀A. A → Computation Pure A
```

### Region Types for Distribution
```
-- Track location and ownership
Region : Location → Type → Type
at : ∀l A. A → Computation (Region l A)
migrate : ∀l₁ l₂ A. Region l₁ A → Computation (Region l₂ A)
```

## Implementation Strategies

### Actor Runtime Systems
```
-- Actor message queues and scheduling
data Actor = Actor {
  behavior : Message → Behavior,
  mailbox  : Queue Message,
  state    : State
}

schedule_actors : [Actor] → IO ()
schedule_actors actors =
  forConcurrently actors process_messages
```

### Process Virtual Machines
```
-- Pi-calculus abstract machine
data Instruction =
  | Send Channel Value
  | Recv Channel Variable
  | Parallel [Process]
  | Restrict Channel Process

execute : [Instruction] → Environment → IO Environment
```

### Distributed Runtime
```
-- Location-transparent communication
send_message : NodeId → Message → IO ()
receive_message : IO (NodeId, Message)
migrate_process : Process → NodeId → IO ()
```

## Applications and Case Studies

### Microservices Architecture
```
-- Service composition with session types
AuthService : !Credentials.?Token.end
UserService : !Token.!UserId.?UserData.end
OrderService : !Token.!Order.?Confirmation.end

-- Orchestrated workflow
checkout_flow : Credentials → Order → Confirmation
checkout_flow creds order =
  let token = auth_service⟨creds⟩ in
  let user = user_service⟨token, user_id⟩ in
  order_service⟨token, order⟩
```

### Blockchain Consensus
```
-- Consensus protocol as concurrent processes
Validator(state, view) = recv {
  prepare(v, view') → if view' > view
                      then broadcast commit(v, view').Validator(state, view')
                      else Validator(state, view),
  commit(v, view') → if valid(v, state)
                     then Validator(apply(v, state), view')
                     else Validator(state, view)
}
```

### IoT Device Networks
```
-- Mobile computation for edge devices
Device(location, capabilities) = recv {
  task(computation) → if can_execute(computation, capabilities)
                      then execute(computation).Device(location, capabilities)
                      else forward_to_cloud(computation).Device(location, capabilities),
  migrate(new_location) → Device(new_location, capabilities)
}
```

## Formal Methods and Verification

### Bisimulation Equivalence
```
-- Process equivalence based on observable behavior
P ∼ Q iff ∀α. P →α P' ⟹ ∃Q'. Q →α Q' ∧ P' ∼ Q'
             Q →α Q' ⟹ ∃P'. P →α P' ∧ P' ∼ Q'
```

### Deadlock Detection
```
-- Static analysis for communication deadlocks
deadlock_free : Process → Bool
deadlock_free P = ∀reachable_state s. can_progress(s)
```

### Liveness Properties
```
-- Temporal logic specifications
eventually_receives : Process → Channel → LTL_Formula
eventually_receives P ch = □◇(receives(P, ch))
```

## Performance Considerations

### Scheduling Strategies
- **Work-Stealing**: Balance load across processing units
- **Priority-Based**: Prioritize time-critical processes
- **Fair Scheduling**: Ensure all processes make progress

### Communication Optimization
- **Message Batching**: Reduce communication overhead
- **Zero-Copy**: Avoid unnecessary data copying
- **Locality-Aware**: Minimize cross-node communication

### Scalability Patterns
- **Sharding**: Partition state across nodes
- **Replication**: Duplicate critical processes
- **Load Balancing**: Distribute work evenly

## Research Directions

### Quantum Process Calculi
```
-- Quantum communication and entanglement
QProcess ::= qsend⟨qubit⟩ | qrecv(qubit) | measure(qubit)
entangle : QProcess → QProcess → QProcess
```

### Probabilistic Concurrency
```
-- Stochastic process behavior
PProcess ::= P ⊕p Q  -- Choose P with probability p, Q with (1-p)
```

### Blockchain-Native Calculi
```
-- Smart contract interaction patterns
Contract ::= state(State).recv{transaction → update(State)}
invoke : ContractAddr → Transaction → Result
```

## Tools and Languages

### Process Calculus Tools
- **Mobility Workbench**: Pi-calculus analysis
- **UPPAAL**: Timed automata verification
- **TLA+**: Specification and verification of concurrent systems

### Actor Languages
- **Erlang/Elixir**: Fault-tolerant actor systems
- **Akka**: JVM-based actor framework
- **Orleans**: Distributed actor framework

### Concurrent Functional Languages
- **Concurrent Haskell**: STM and parallel strategies
- **Go**: Goroutines and channels
- **Rust**: Safe concurrency with ownership

## Resources

- **Papers**: See [papers/bibliography.md](/papers/bibliography.md) for concurrent calculi research
- **Implementations**: Process calculus interpreters and actor systems
- **Tutorials**: Concurrent programming patterns and verification
- **Case Studies**: Distributed systems and parallel algorithms

## Related Systems

- [Session Types](/../07-session-types/) - Communication protocol types
- [Linear Lambda Calculus](/../06-linear-lambda-calculus/) - Resource-aware concurrency
- [Quantum Variants](/../11-quantum-variants/) - Quantum process calculi
- [Modal Types](/../19-modal-types/) - Distributed computation types

---

*Concurrent variants of lambda calculus provide formal foundations for understanding and implementing concurrent, parallel, and distributed computation while maintaining mathematical rigor and practical applicability.*