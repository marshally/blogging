# Research ledger: replaceable modules and Phoenix

Checked 2026-10-10. Internal research, not post prose. Claims below separate author positions from Marshall's proposed synthesis. “Verified primary” confirms what an author argues, not that the argument guarantees correct software.

## Verified primary writing

### R01: Ousterhout's abstraction supports composition

Ousterhout describes abstractions that hide implementation complexity behind simple interfaces, isolate changes, and allow other components to work together. His modular-design notes say layers should provide different abstractions and interfaces include behavioral constraints. This supports reasoning about a composed system through abstractions. These sources do not prescribe a recursive agent hierarchy, require one large file, or establish that component tests prove system correctness. Sources: [Designing Abstractions](https://web.stanford.edu/~ouster/CS349W/lectures/abstraction.html) (undated lecture notes), [Modular Design](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign) (Winter 2018).

### R02: Phoenix preserves the knowledge needed for replacement

Chad Fowler's [The Phoenix Primitives](https://chadfowler.com/regenerative-software/3mjfruwwuck2d/) (2026-04-13) identifies behavioral specifications, evaluations, context boundaries, and provenance as durable artifacts around regenerable implementation. His context boundaries include integration contracts, event schemas, and shared data formats. This directly supports discussing replaceable internals behind preserved external expectations. It is a proposed architectural model, not evidence that any passing suite makes arbitrary replacement safe.

### R03: Replaceability requires architectural constraints

In [Compile to Architecture](https://aicoding.leaflet.pub/3mgfsrk75ac2l) (2026-03-06), Fowler connects current regeneration ideas to his earlier Wunderlist system. He describes services being rewritten within a stable structure and attributes replaceability to predictable communication, data ownership, suitable component boundaries, and independently verifiable behavior. His evaluation examples include API contracts, domain invariants, event consistency, property tests, and integration tests. The connection is explicit in Fowler's own retrospective, rather than an analogy supplied by this series.

### R04: The grain must preserve coherent behavior

[The Regenerative Grain](https://chadfowler.com/regenerative-software/3mfai4nqg6224/) (2026-02-19) proposes units with understandable behavior, mutation ownership, versioned contracts, and independently evaluable boundaries. Fowler warns against excessive fragmentation and explicitly allows property tests and simulations beyond boundary tests. He also says well-shaped individual components do not automatically produce a well-shaped system: orchestration and integration need contracts too. He presents deletion safety as a heuristic.

## Early talk evidence and intermediary limits

### R05: Replacement predates the current Phoenix essays

Fowler's *Kill “Microservices” Before It's Too Late*, delivered at Rocky Mountain Ruby on 2016-09-30 and published 2016-10-20, supplies the early software connection. The [timestamped transcript](https://www.rubyevents.org/talks/kill-microservices-before-its-too-late) reports code replacement within a retained system structure (08:50–09:08), discarding decoupled components (14:20–14:42), and treating components as replaceable (17:40–18:40). These are the speaker's reported experiences, not a controlled comparison.

The talk is primary speaker material accessed through an intermediary transcript with visible transcription errors. The recording could not be fetched during this check, so verify audio before quoting verbatim. Ignore the page's AI summary: it reverses his distinction between the system as asset and code as liability. The precise early blog article Marshall remembers remains unidentified. The 2013 immutable-infrastructure article was checked but is not a substitute for this software argument.

## Proposed synthesis

### R06: Recursive modules and human-reviewed behavioral contracts

Marshall's model: modules can contain further functional domains behind internal boundaries. Callers receive compact interface knowledge. Humans review externally observed behavior and its tests, while agents implement or replace internals against those expectations. The same discipline can recur inside the module. Humans steer seams, responsibilities, and required behavior.

This combines [R01](#r01-ousterhouts-abstraction-supports-composition) with [R02–R04](#r02-phoenix-preserves-the-knowledge-needed-for-replacement). Attribute the combined agent workflow to Marshall. Tests supply evidence for the behaviors and conditions they cover. Composition, hidden dependencies, state migration, and operational requirements can still demand additional evidence.

## Folklore / unsubstantiated

No evidence here establishes a universal module size, guarantees token savings from recursion, or makes reviewed tests exhaustive specifications.

## Do-not-use ledger

Do not conflate Chad Fowler with Martin Fowler, Phoenix Architecture with *The Phoenix Project*, an external contract with only a method signature, or passing interface tests with blanket correctness. Do not attribute Marshall's full workflow to either author. No fabricated quote was encountered. The Phoenix reference resolves strongly to Chad Fowler's current series, although Marshall has not named a specific installment.
