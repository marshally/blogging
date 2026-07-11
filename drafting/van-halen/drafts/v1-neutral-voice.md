# Two Shapers, One Seat

*What forty years of Van Halen lineup drama teaches us about software teams*

---

Three minutes to showtime, and I was fumbling with a Bluetooth speaker at the base of the Golden Gate Bridge.

This past Fourth of July, San Francisco shot fireworks off the bridge itself — only the third time in the city's history that's happened. I used to design fireworks shows semi-professionally: pyrotechnics lead for Burning Man regionals, crew work on city-scale shoots. So there was no version of this where I watched from a beach a mile away. We hiked out to Fort Point to stand directly under the deck, close enough to feel the shells in our chests.

Which is how I found myself, at T-minus-three, wanting a soundtrack. No official audio reaches Fort Point, and a show that size deserves scoring. Scrolling my library, I remembered something: the album *1984* opens with a one-minute instrumental — that slow, swelling synth intro — before "Jump" detonates. If I timed it right, the swell would carry us through the countdown and the first salvo would land exactly on the first chord.

I timed it right. The opening shells came off the bridge deck as the synth resolved, "Jump" kicked in, and for the next several minutes an album recorded in 1983 scored a fireworks show like it had been commissioned for it. The crowd around us started singing.

I went home happy, fell down a Van Halen research hole, and came out the other side thinking about software teams. Bear with me.

## Same codebase, three CEOs

Here's what struck me reading forty years of Van Halen history: every story reads like an engineering-org postmortem. Creative-control disputes. A brilliant founder consolidating power. A beloved manager dying and being replaced by a partisan. A mis-hire. A quiet contributor pushed out, and the product audibly degrading afterward. Change the nouns and it's a Blind and Item on any tech gossip board.

But Van Halen offers something better than analogy: a natural experiment. The instrumental core of the band — Eddie and Alex Van Halen — stayed constant across every era, while the frontman role was recast three times. Same codebase, three CEOs. That's a rare controlled study in what happens to a team when you swap one role and hold the rest fixed.

To read the experiment, I'm borrowing two old frameworks from small-group research.

The first is Robert Bales' finding from the 1950s, one of the most replicated results in the field: groups reliably differentiate into a **task specialist** (who drives the work) and a **social-emotional specialist** (who holds the group together), these are almost never the same person, and the group's fate hangs on whether the two cooperate. That's the plot.

The second is Meredith Belbin's team-role model from his studies of management teams in the 1970s and 80s. Belbin identified nine recurring roles — we'll meet most of them below — and made a claim that his data kept supporting: teams fail not from lack of talent but from **uncovered roles and duplicated ones**. His famous "Apollo syndrome" finding showed that teams composed entirely of the smartest individuals routinely underperformed balanced ones. (Belbin's psychometric instrument has real academic critics; I'm using the model as a lens, not a diagnostic.) That's the cast sheet.

So: Belbin gives us the characters. Bales gives us the plot. Van Halen gives us the data.

## The cast sheet

**Eddie Van Halen — the Plant.** Belbin's Plant is the creative source, the generator of the ideas everyone else works within — brilliant, unorthodox, territorial. Eddie invented techniques (two-handed tapping) the way great engineers invent abstractions, and built his own gear and eventually his own studio the way they roll their own tooling. In the studio he was also Belbin's Completer Finisher, the obsessive perfectionist at the end of the pipeline. Software archetype: the architect-founder whose framework everyone else lives inside. On the two scoreboards that matter — loved by fans, revered by fellow practitioners — Eddie maxed both. Hold that thought; it becomes important.

**David Lee Roth — the Resource Investigator.** Outward-facing, magnetic, the band's interface to the world: showmanship, brand, deal energy. Belbin notes this role brings in opportunity and enthusiasm, and loses interest once the initial excitement fades. Software archetype: the founder-flavored PM or devrel star who comes back from the conference with three partnerships and no follow-through plan. Scoreboards: adored by fans; his actual vocal chops perennially discounted by musicians.

**Alex Van Halen — the Implementer.** Turns plans into reliable execution; disciplined; allergic to drama. Alex is the only member besides Eddie present in every lineup, across forty-plus years, without generating a single public conflict of his own. Among drummers he's canon — the craft is in details like the swinging double-kick and ride-bell work buried at the end of "Girl Gone Bad," the kind of thing you have to lean in to hear. Among casual fans he barely registers on best-drummer lists. Software archetype: the SRE or staff engineer whose pull requests are boring and essential. Scoreboards: low fan, high peer — the cleanest split in the band.

**Michael Anthony — the Teamworker.** Belbin's glue role: averts friction, supports others, morale infrastructure, chronically under-recognized because the contribution doesn't show up in attributable output. Anthony is respected by musicians not for bass virtuosity — his playing is praised as rock-solid, nothing more — but for his high, bright backing harmonies, so essential to the band's sound that outlets covering the band converged on the same epithet: the secret weapon. Software archetype: the glue person from Tanya Reilly's famous talk — the engineer doing the code reviews, the onboarding, the invisible cohesion work. Scoreboards: low fan, high peer, and the peer admiration is *for the glue itself*. Remember him. This story ends badly.

**Sammy Hagar — Coordinator-adjacent.** An established star in his own right when he joined, collaborative with writing credits, a frontman who also played guitar — a singer who could read code. Belbin's Coordinator is the chairperson: clarifies goals, pulls decisions out of the group, often not the most talented person in the room. Scoreboards: respected on both, worshipped on neither.

**Wolfgang Van Halen — the Specialist.** Hired in 2006 for one defined slot: bass. We'll get to what that hire actually meant.

Two more things about this cast sheet, and they're findings, not trivia. First, look at the empty seats: the band never had a **Monitor Evaluator** — Belbin's dispassionate internal critic, the person who kills bad ideas in design review — and never had a stable in-house **Coordinator**, a role it kept outsourcing to producers and managers, with consequences each time the outsourced version disappeared. Keep the Monitor Evaluator vacancy in mind; in 1998 we'll hear exactly what it sounds like.

Second: I haven't assigned Belbin's **Shaper** — the driver role, the will that pushes the team through obstacles, the seat of *whose vision shapes the work*. Belbin warned that two Shapers on one team is one of his known combustible configurations.

There's a reason that seat is still open. It's where all the trouble starts.

## Act I: Two Shapers, one seat (1974–1985)

The standard telling of classic-era Van Halen is "clashing egos." The framework suggests something more precise: Eddie and Roth were two claimants to a single Shaper seat. This wasn't a personality conflict that happened to occur on a team; it was a structural conflict *about* the team — a standing contest over whose will shaped the work. Roth was never content to hold only the audience-facing pole. His creative fingerprints on the band's direction, and later a solo career launched on the conviction that he was a driving force in his own right, mark him as a Shaper claimant, not merely a frontman.

For the first decade, the contest had a referee. Producer Ted Templeman functioned as the band's external Coordinator and Monitor Evaluator — and, as his own 2020 memoir and Greg Renoff's *Van Halen Rising* document, he tended to side with Roth on creative direction: short songs, guitar-forward, no synthesizers. Every software team knows this configuration: the principal architect or board member whose alignment silently determines which internal faction wins design reviews. Eddie kept losing the reviews.

So he did what blocked Plants do. In 1983, Eddie built 5150 Studios at his home — described in interview after interview as an explicit move to control recording. The architect, tired of losing design reviews, exits the shared infrastructure and builds the thing on a side branch until it's a fait accompli.

The fait accompli has a name, and if you've read this far you already know it. "Jump" was a synth riff Eddie has said was rejected for years — resisted by exactly the Roth–Templeman alliance that controlled the old pipeline. Recorded at 5150, on Eddie's turf, it became the only #1 single the band ever had.

That's the song I cued up under the bridge. The track that scored the fireworks so perfectly wasn't just a good album opener — it was the decisive move in the Shaper war, the artifact that proved the Plant could win outside the sanctioned process. I was soundtracking a fireworks show with a shipped side branch.

Winning the war didn't save the team; it ended it. Once the contest was decided, the conflict migrated from *task* to *relationship* — and the research (Karen Jehn's, if you want the citation) is clear that task conflict can fuel a team while relationship conflict kills it. Within a year of the band's commercial peak, Roth was gone.

One more thing about Act I that pays off later. Bales says every group needs a social-emotional pole. Roth held its outward face — the charisma aimed at the audience. But the *inward* face, the one aimed at the band itself, was quietly held the whole time by Michael Anthony. File that away.

## Act II: The settled seat (1985–1996)

Sammy Hagar is often described as the easygoing alternative to Roth, which is funny to anyone who's read his memoir *Red* — Hagar is nobody's shrinking violet. The Hagar era wasn't harmonious because Hagar was agreeable. It was harmonious because he arrived *after the structural contest was decided*. He joined Eddie's band, on Eddie's terms, recording in Eddie's studio. However accomplished, he entered as an occupant of the frontman role, not a claimant to the Shaper seat.

Sequence, not temperament, is the variable. Software translation: there is a world of difference between two co-founders fighting over technical direction and a decorated senior hire who joins after the architecture is settled. Same talent, same strong personality, completely different structural position — and completely different outcome.

The outcome, for a decade, was remarkable: four consecutive #1 albums, more commercial success than the Roth era ever had, and a legacy that fans nonetheless rank below the original run. Whatever was lost with the friction, something was lost.

But look closely and the era's stability had a second load-bearing element: manager Ed Leffler, whom Hagar's memoir credits as the neutral figure holding the whole configuration together — the in-house Coordinator the band otherwise never had. Then the causal chain runs like a fuse. Leffler died in 1993. He was replaced by Ray Danniels — Alex's former brother-in-law, and in Hagar's telling, aligned with the brothers rather than neutral. The chairperson's seat, refilled by a partisan. Within three years, the first genuine task conflicts — songs for the *Twister* soundtrack, a greatest-hits album Hagar opposed — escalated with nothing to buffer them, and Hagar was out. (Hagar tells the exit one way in *Red*; the brothers told it another. The fact that no two members ever agreed on what happened is itself evidence of what the group had become without a Coordinator.)

Every engineering org has run this experiment too: the beloved neutral manager leaves, the replacement comes from one side of a standing rivalry, and conflicts that used to be routine suddenly aren't.

## Act III: Role collapse (1996–2020)

What happened next is what happens when a role structure loses its counterweights one by one.

The 1996 MTV Video Music Awards reunion with Roth collapsed within weeks, in dueling public accounts. Eleven years apart, and the two-Shapers problem reignited in days. Structural problems don't age out; they wait.

Gary Cherone — genuinely talented, hired from Extreme — lasted one album. He failed not for lack of ability but because a role is a negotiated relationship with the specific people around it, not a seat you can staff from a resume. By 1998 the frontman position had become so subordinate that it provided no counterweight at all. Every engineering leader has lived this hire: impressive on paper, dead on arrival structurally.

And then there's *Van Halen III*, the band's worst-received album — where you don't need to psychoanalyze anyone, because the liner notes make the argument. Eddie played bass on most of the record (Anthony appears on only three tracks). Eddie sang lead on one song. Eddie took a heavy hand in production. One member occupying the Plant, Shaper, Completer Finisher, and now pieces of the Teamworker's and frontman's roles — with no Monitor Evaluator anywhere in the organization to kill any of it in review. I told you we'd hear what that vacancy sounds like. It sounds like *Van Halen III*.

The Anthony story completes in parallel, and it's the cruelest data in the set. His songwriting and royalty position was reduced in the late 90s; he reportedly had to accept diminished terms just to participate in the 2004 reunion tour; in 2006 he was replaced outright, by several accounts learning his status from the press. The org chart had never been able to see what he did — Belbin could have predicted the contract terms. And then the punchline: on subsequent tours, recordings of his backing vocals were reportedly piped into the live shows. The organization removed the glue person, discovered the glue was load-bearing, and had to build tooling to fake his output. If you've watched a company lay off its glue engineers and then spin up a committee to replace what they did for free, you know this one. And per Act I: when Anthony left, the band didn't just lose harmonies — it lost the inward-facing social pole it had quietly depended on since 1974.

His replacement was Wolfgang, Eddie's son — the ultimate new guy, structurally incapable of contesting the Shaper seat, and by all accounts an excellent musician besides. The 2012–2015 reunion with Roth produced a real album and a tense armistice; the seat contest was never resolved, only rendered moot by Eddie's total structural victory. Eddie, in a 2015 Billboard interview, put the state of the twenty-year truce in nine words: "he does not want to be my friend." Eddie Van Halen died in October 2020, with the band's role structure — his studio, his son, his name on the marquee — arranged exactly as he'd built it.

## What the experiment showed

Three claims, which I think generalize well past rock bands:

**Every team has one Shaper seat, and the real fights are over who sits in it.** The conflicts we narrate as personality clashes are often structural contests over whose will shapes the work — and they end when the seat question is settled, one way or another, not when anyone becomes nicer.

**Teams fail from uncovered and duplicated roles, not talent deficits.** Van Halen at every moment had a surplus of talent. What it never had was a Monitor Evaluator; what it twice lost was its Coordinator; what it eventually fired was its Teamworker. Each vacancy has an audible signature in the discography.

**There are two scoreboards, and your org chart reads only one of them.** Fans — like users, like promotion committees — score what's legible from the front of the stage. Practitioners score the craft that's only visible from inside. The gap between the scoreboards is largest for exactly the Implementer and Teamworker roles, which is why the Alexes go unlisted and the Anthonys get their contracts reduced.

Honesty requires one complication. The most influential modern research on team composition — Anita Woolley's collective-intelligence studies, Google's Project Aristotle — found that *who* is on a team matters less than how the team interacts: turn-taking, social sensitivity, psychological safety. The role lens is a lens, not a law. But I'd note that even that research is, in a sense, a finding about the same thing: the qualities that make teams work are precisely the ones no scoreboard was measuring.

## Coda: the fog

I should tell you how the fireworks show ended.

The fog came in. Of course it did; it's San Francisco in July. By mid-show the upper bursts were vanishing into gray, and for the crowds on the beaches a mile back, the third-ever bridge shoot in city history must have been mostly a rumor — muffled thuds behind a curtain, the spectacle scoreboard reading near zero.

But we were at Fort Point, directly underneath, close enough that the low-level effects off the deck still lit the fog from inside, close enough to hear each shell leave the mortar and read the crew's choices in the timing. I've stood on the other side of shows like this. I knew what I was looking at, and it was beautiful — not despite being illegible from a distance, but in all the ways that are only legible up close.

Which is the whole thing, really. The best work is often visible only to the people standing near enough to read it. That's true of drummers, of harmony singers, of the engineer who kept your on-call quiet for three years.

The fog doesn't ruin the show. It just tells you which scoreboard you've been watching.
