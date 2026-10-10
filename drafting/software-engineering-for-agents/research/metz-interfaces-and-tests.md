# Research ledger: Metz, interfaces, and tests

Checked 2026-10-10. Internal planning reference. Primary verification establishes what these sources teach, not universal correctness guarantees. Paraphrases only. The extension to agents and recursively composed modules belongs to Marshall's series.

## Sources

| ID | Primary source | Date / version |
|---|---|---|
| T1 | Sandi Metz, [Magic Tricks of Testing, RailsConf slide deck](https://speakerdeck.com/skmetz/magic-tricks-of-testing-railsconf) | Posted 2013-04-30, slides dated 2013-04-27 |
| T2 | Sandi Metz, Katrina Owen, TJ Stankus, [99 Bottles of OOP, Ruby sample](https://sandimetz.com/99bottles-sample-ruby), sections 1.1.1 and 2.2 | Second edition, version 2.2, 2024-10-18 |
| T3 | Sandi Metz, POODR source examples: [chapter_9b.rb](https://raw.githubusercontent.com/skmetz/poodr/master/chapter_9b.rb), [chapter_9f.rb](https://raw.githubusercontent.com/skmetz/poodr/master/chapter_9f.rb) | Undated source files, current `master` checked |
| T4 | Addison-Wesley / InformIT, [Practical Object-Oriented Design, second edition](https://www.informit.com/store/practical-object-oriented-design-an-agile-primer-using-9780134445588) | 2018 edition |

## Verified primary claims

### M01: Describe what callers can request

The *99 Bottles* sample distinguishes the sender's intention from the receiver's implementation and advocates keeping callers ignorant of implementation detail. It sketches a public API in terms of requests and returned results, then tests the returned behavior. This is a concrete basis for a compact behavioral contract that callers can understand without knowing internal mechanics. That final “compact contract” formulation is our application. [T2](https://sandimetz.com/99bottles-sample-ruby)

### M02: Choose assertions by message direction and type

Metz's unit-testing defaults distinguish queries from commands and the object's viewpoint:

| Message | Default test |
|---|---|
| Incoming query | Assert its returned result. |
| Incoming command | Assert direct publicly observable effects. |
| Message to self / private method | Avoid direct assertions and call expectations. |
| Outgoing query | Avoid asserting its result or requiring its invocation. |
| Outgoing command | Expect the required message and arguments to be sent. |

Her caveats allow private tests that save development cost and outgoing-command effect assertions when stable and cheap. These are defaults with exceptions. [T1, slides 54, 82, 108–111, 133–137, 173–174](https://speakerdeck.com/skmetz/magic-tricks-of-testing-railsconf)

### M03: Test doubles must track the real interface

The POODR examples inject a double supplying a query result into the object under test. Another example changes the real collaborator's method name while leaving the double unchanged, so the isolated caller test can pass despite incompatible collaboration. Metz extracts a shared interface test and includes it for the real object and double. [T3, chapter 9b](https://raw.githubusercontent.com/skmetz/poodr/master/chapter_9b.rb), [chapter 9f](https://raw.githubusercontent.com/skmetz/poodr/master/chapter_9f.rb)

The shown shared assertion checks whether the object responds to the required message. It does not verify arbitrary semantic equivalence. Our implication: verifying doubles against a shared protocol prevents one class of false confidence, while behavioral conformance and integration can require further checks. A stub that supplies a query result is distinct from an expectation that the query must be called.

## Proposed application to the series

### M04: Public and private depend on the chosen boundary

A child module can expose a public interface to its parent while remaining an implementation detail of the larger module. Apply the message viewpoint separately at each boundary. The outer contract should describe behavior required by outer callers, without freezing which child or helper produces it. This is our composition model informed by [M01](#m01-describe-what-callers-can-request) and [M02](#m02-choose-assertions-by-message-direction-and-type), not a verified quotation or named Metz framework.

Preserve the outer behavioral tests during an internal rewrite. Child contract tests remain valuable while that child abstraction exists. If a rewrite removes the child, its dedicated tests can retire while the enclosing module's obligations remain. Private-method tests used as temporary scaffolding do not automatically become durable outer contracts.

### M05: Human review governs the contract agents implement

Marshall's synthesis: humans review seams, responsibilities, behavior examples, and contract tests. Agents receive the relevant interface and task context, implement internals, and demonstrate conformance. Tests of an outgoing command establish that the requested interaction occurred. Tests of its receiver establish the receiver's behavior. Neither alone proves the whole system's behavior under all conditions. Keep required integration, state, error, and operational evidence explicit.

## Secondary leads and verification limits

The local POODR skill supplied search leads only. T4 verifies the book's chapter structure: interfaces, composition, and testing. The precise chapter 4 prose was not available from the inspected primary pages, so do not present a reconstructed public/private definition as a verified book quotation. The primary sample in T2 has three authors and belongs to *99 Bottles*, not POODR.

## Folklore / unsubstantiated

No evidence here establishes token savings, an optimal agent hierarchy, or complete specifications from a passing test suite.

## Do-not-use ledger

Exclude invented POODR quotations/page numbers, “Metz bans private tests without exceptions,” “every outgoing call must be mocked,” and “a shared interface test proves complete behavioral compatibility.” Do not interpret permission to retire a removed child's tests as permission to discard still-required outer behavior.
