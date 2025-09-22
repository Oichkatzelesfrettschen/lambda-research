# Session Types

A type system for describing and verifying communication protocols, ensuring that concurrent processes follow prescribed interaction patterns and preventing communication errors.

## Overview

Session Types provide:
- **Protocol Description**: Types that specify communication sequences
- **Linear Communication**: Channels used exactly once per protocol step
- **Deadlock Freedom**: Static guarantees against communication deadlocks
- **Protocol Fidelity**: Ensures processes follow prescribed communication patterns
- **Resource Safety**: Proper channel management and cleanup
- **Duality**: Complementary types for communicating endpoints

## Syntax and Basic Types

```
Session Types:
S, T ::= end                    -- Session termination
       | !A.S                   -- Send value of type A, continue with S
       | ?A.S                   -- Receive value of type A, continue with S
       | ⊕{li : Si}i∈I         -- Internal choice (select)
       | &{li : Si}i∈I         -- External choice (branch)
       | μX.S                   -- Recursive session type
       | X                      -- Type variable

Base Types:
A, B ::= Int | Bool | String | Channel(S) | ...

Terms:
M, N ::= x | send M N | recv M | select l M | branch M {li → Ni}i∈I |
         close M | wait M | fork M | new
```

## Typing Rules

### Channel Communication
```
Γ ⊢ c : Channel(!A.S)    Γ ⊢ v : A
─────────────────────────────────────    (Send)
Γ ⊢ send c v : Channel(S)

Γ ⊢ c : Channel(?A.S)
─────────────────────────────────────    (Receive)
Γ ⊢ recv c : A × Channel(S)
```

### Choice Operations
```
Γ ⊢ c : Channel(⊕{li : Si}i∈I)    j ∈ I
─────────────────────────────────────    (Select)
Γ ⊢ select lj c : Channel(Sj)

Γ ⊢ c : Channel(&{li : Si}i∈I)    ∀i ∈ I. Γ ⊢ Mi : Channel(Si) → A
─────────────────────────────────────────────────────────────────    (Branch)
Γ ⊢ branch c {li → Mi}i∈I : A
```

### Session Management
```
─────────────────────────────────────    (New)
Γ ⊢ new : Channel(S) × Channel(S̄)

Γ ⊢ c : Channel(end)
─────────────────────────────────────    (Close)
Γ ⊢ close c : 1

Γ ⊢ c : Channel(end)
─────────────────────────────────────    (Wait)
Γ ⊢ wait c : 1
```

## Duality

Session types come in dual pairs (S and S̄):

```
end̄ = end
(!A.S)̄ = ?A.S̄
(?A.S)̄ = !A.S̄
(⊕{li : Si}i∈I)̄ = &{li : S̄i}i∈I
(&{li : Si}i∈I)̄ = ⊕{li : S̄i}i∈I
(μX.S)̄ = μX.S̄
```

Duality ensures that when one endpoint sends, the other receives, and choices are complementary.

## Key Properties

- **Type Safety**: Well-typed programs don't get stuck on communication
- **Deadlock Freedom**: No circular dependencies in communication
- **Protocol Fidelity**: Processes follow prescribed communication patterns
- **Progress**: Well-typed programs can always make progress
- **Linear Channel Usage**: Channels consumed linearly through protocol

## Historical Development

- **Honda (1993)**: Original session types for π-calculus
- **Takeuchi et al. (1994)**: Type checking algorithms
- **Honda et al. (1998)**: Subtyping and polymorphism
- **Gay & Hole (2005)**: Session types for functional languages
- **Wadler (2012)**: Session types as linear types
- **Lindley & Morris (2016)**: Functional session types

## Examples and Patterns

### Simple Request-Response
```
ClientType = !String.?Int.end
ServerType = ?String.!Int.end

client : Channel(ClientType) → Int
client c =
  let c' = send c "request" in
  let (response, c'') = recv c' in
  let _ = close c'' in
  response

server : Channel(ServerType) → Unit
server c =
  let (request, c') = recv c in
  let c'' = send c' 42 in
  close c''
```

### Calculator Service
```
CalcType = &{
  add  : ?Int.?Int.!Int.CalcType,
  mult : ?Int.?Int.!Int.CalcType,
  quit : end
}

calculator : Channel(CalcType) → Unit
calculator c =
  branch c {
    add  → λc'. let (x, c'') = recv c' in
                let (y, c''') = recv c'' in
                let c'''' = send c''' (x + y) in
                calculator c'''',
    mult → λc'. let (x, c'') = recv c' in
                let (y, c''') = recv c'' in
                let c'''' = send c''' (x * y) in
                calculator c'''',
    quit → λc'. close c'
  }
```

### Recursive Protocol
```
StreamType = μX. ⊕{
  data : !String.X,
  end  : end
}

producer : [String] → Channel(StreamType) → Unit
producer [] c =
  let c' = select end c in
  close c'
producer (x::xs) c =
  let c' = select data c in
  let c'' = send c' x in
  producer xs c''
```

## Advanced Features

### Polymorphic Session Types
```
∀α. !α.?α.end    -- Polymorphic echo service
```

### Session Type Subtyping
```
S <: T if:
- end <: end
- !A.S <: !B.T if A <: B and S <: T
- ?A.S <: ?B.T if B <: A and S <: T (contravariant)
- ⊕{li : Si}i∈I <: ⊕{lj : Tj}j∈J if I ⊆ J and ∀i∈I. Si <: Ti
```

### Multiparty Session Types
```
Global Type: G ::= p → q : {li(Ai).Gi}i∈I | end | μt.G | t

Local Projection: G ↾ p gives local session type for participant p
```

## Implementation Strategies

### Linear Type System Integration
```
-- Rust-like ownership for channels
fn use_channel(ch: Channel<Send<i32, End>>) {
    let ch = ch.send(42);  // ch consumed and returned
    ch.close();            // ch consumed, cannot use again
}
```

### Runtime Monitoring
```
-- Dynamic checking when static checking insufficient
monitor_protocol(channel, expected_type) {
    while (!protocol_complete) {
        action = get_next_action(channel);
        check_action_allowed(action, expected_type);
        update_protocol_state(expected_type, action);
    }
}
```

### Code Generation
```
-- Generate communication skeletons from protocol specifications
protocol Calculator {
    choice {
        add(Int, Int) -> Int,
        multiply(Int, Int) -> Int,
        quit() -> ()
    }
}

-- Generates client and server stubs automatically
```

## Applications

### Distributed Systems
- Microservice communication protocols
- API contract verification
- Message queue pattern enforcement

### Web Development
- WebSocket protocol specification
- REST API behavior description
- Client-server interaction verification

### Concurrent Programming
- Actor system type safety
- Concurrent data structure protocols
- Lock-free algorithm verification

### Blockchain and Smart Contracts
- State channel protocols
- Transaction pattern verification
- Consensus algorithm communication

## Theoretical Foundations

### Correspondence to Linear Logic
```
Session Type    Linear Logic
!A.S           A ⊸ S
?A.S           A ⊗ S
⊕{li : Si}     ⊕i Si
&{li : Si}     &i Si
end            1
```

### Process Calculus Embedding
- π-calculus with session types
- Correspondence between typing and behavioral equivalence
- Translation to concurrent lambda calculus

### Cut Elimination and Deadlock Freedom
- Well-typed process networks correspond to cut-free proofs
- Cut elimination guarantees deadlock freedom
- Progress theorem ensures liveness

## Extensions and Research Directions

### Exception Handling
```
ExceptionType = !String.end
NormalType = ?Int.!Int.end
ProtocolWithExceptions = NormalType ⊕ ExceptionType
```

### Time and Timeouts
```
TimedType = timeout(5s, ?Int.!Int.end, !String.end)
```

### Resource Bounds
```
BoundedType = ?Int[n].!Int[m].end    -- at most n inputs, m outputs
```

### Security Types
```
SecureType = encrypt(Key, ?Secret.!Secret.end)
```

## Tools and Languages

### Languages with Session Types
- **Links**: Functional web programming with session types
- **Scribble**: Protocol description language
- **MPST**: Multiparty session types implementation
- **Rust**: Ownership system supports session type patterns

### Verification Tools
- **Scribble**: Global protocol specification and projection
- **Session-C**: C with session types
- **GO**: Goroutine communication verification

## Resources

- **Papers**: See [papers/bibliography.md](/papers/bibliography.md) for session type foundations
- **Implementations**: Session type checkers and runtime systems
- **Tutorials**: Protocol specification and verification examples
- **Applications**: Distributed systems and concurrent programming case studies

## Related Systems

- [Linear Lambda Calculus](/../06-linear-lambda-calculus/) - Resource-aware foundation
- [Concurrent Variants](/../10-concurrent-variants/) - Process calculi foundations
- [Substructural Types](/../09-substructural-types/) - General resource logics
- [Pi-Calculus](/../10-concurrent-variants/) - Mobile process communication

---

*Session Types provide a principled approach to communication protocol verification, ensuring that concurrent processes interact safely and follow prescribed communication patterns.*