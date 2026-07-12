# Might as well jump

*What forty years of Van Halen drama teaches us about team dynamics*

[insert masthead photo of fireworks]

---

Three minutes to showtime, and I was fumbling with a Bluetooth speaker at the base of the Golden Gate Bridge.

This past Fourth of July (2026), San Francisco shot fireworks off the bridge itself, only the third time in the city's history that's happened. In a previous life I designed fireworks shows semi-professionally, so I like to find the best viewing location and that usually means getting as close as possible to the action. Karl the Fog has a well-deserved reputation as a Fourth of July party crasher, so there was no version of this where I watched from a beach a mile away. We hiked out to Fort Point to stand directly under the deck, close enough to feel the shells in our chests.

[insert map picture here]

Which is how I found myself, at T-minus-three, wanting a soundtrack. No official audio reaches Fort Point, and a show that size deserves scoring. Scrolling my library, I remembered something: the album *1984* opens with a one-minute instrumental (that slow, swelling synth intro) before "Jump" detonates. If I timed it right, the swell would carry us through the countdown and the first salvo would land exactly on the first chord.

Dear reader, I timed it right. The opening shells came off the bridge deck as the synth resolved, "Jump" kicked in, and for the next twenty minutes an album recorded in 1983 scored a fireworks show like it had been commissioned for it.

I went home happy, fell down a Van Halen research hole, and came out the other side thinking about software teams.

Yes, this post is going to run a rock band, a fireworks show, and your engineering org through the same blender. That's at least two metaphors past the legal limit, and the management apologizes for nothing.

## What does a heavy metal band know about your org chart?

Here's what struck me reading forty years of Van Halen history: every story reads like an engineering postmortem. Creative-control disputes. A brilliant founder consolidating power. A beloved manager replaced by a partisan. A high-profile mis-hire. A quiet contributor pushed out, and the product audibly degrading afterward. Change the actors and the set and it's any Hacker News thread on a Tuesday.

But Van Halen offers something better than analogy: a natural experiment. The instrumental core of the band (Eddie and Alex Van Halen) stayed constant across every era, while the frontman role was recast three times. **Same codebase, three CEOs.** That's a rare controlled study in what happens to a team when you swap exactly one role and hold everything else fixed.

## Let's (re)define some terms

To read the experiment, I'm borrowing two frameworks from small-group research: one for the plot, one for the cast.

**The plot** comes from Robert Bales, who spent the 1950s at Harvard coding thousands of hours of group interactions and produced one of the most replicated findings in the field: groups reliably split into a **task specialist** (who drives the work) and a **social-emotional specialist** (who holds the group together). These are almost never the same person, and **the group's fate hangs on whether the two cooperate.**

**The cast** comes from Meredith Belbin, who studied management teams at Henley in the 70s and 80s and identified nine recurring team roles. His data kept supporting one unfashionable claim: **teams fail from uncovered roles and duplicated roles, not from talent deficits.** His famous "Apollo syndrome" finding showed that teams built entirely from the smartest individuals routinely lost to balanced ones.[^furnham]

Belbin gives us the characters. Bales gives us the plot. Van Halen gives us the data.

## Meet the band (you already work with them)

**The Plant — Eddie Van Halen.** Belbin's **Plant** is the creative source, the generator of the ideas everyone else works within: brilliant, unorthodox, territorial. Eddie invented techniques (two-handed tapping) the way great engineers invent abstractions, and built his own gear and eventually his own studio the way they roll their own tooling. You know this person: the architect-founder whose framework everyone else lives inside. And here's the detail to file away: on the two scoreboards that matter, loved-by-fans and revered-by-practitioners, Eddie maxed *both*. That almost never happens, and it warps everything around it.

**The Completer Finisher — also Eddie.** In the studio he doubled as Belbin's perfectionist: the role that won't let it ship broken. You know this person too: the engineer who blocks the release over the flaky test everyone else has learned to ignore. And note the double-booking: one person holding both the idea-generator seat and the quality-gate seat concentrates a lot of veto power in one chair.

**The Resource Investigator — David Lee Roth.** Outward-facing, magnetic, the band's interface to the world: showmanship, brand, deal energy. Belbin notes this role brings in opportunity and enthusiasm, then loses interest once the initial excitement fades. You know this person too: the founder-flavored PM or devrel star who returns from the conference with three partnerships and no follow-through plan. Scoreboards: adored by fans; his actual vocal chops perennially discounted by musicians.

**The Implementer — Alex Van Halen.** Turns plans into reliable execution; disciplined; allergic to drama. Alex is the only member besides Eddie present in every lineup, across forty-plus years, without generating a single public conflict of his own. Among drummers he's canon: they have spent four decades arguing about how he played the swung double-kick intro to "Hot for Teacher," and there's [a 26-minute documentary](https://www.youtube.com/watch?v=Rcmcf4kdMn4) of working drummers being interviewed about those opening seconds. Among casual fans he barely registers on best-drummer lists. This is your SRE, your staff engineer whose pull requests are boring and essential. Scoreboards: low fan, high peer, the cleanest split in the band.[^brown-sound]

**The Teamworker — Michael Anthony.** Belbin's glue role: averts friction, supports others, morale infrastructure, and chronically under-recognized, because the contribution never shows up as attributable output. Musicians praise Anthony's bass playing as rock-solid, full stop; what they revere are the high, bright backing harmonies so essential to the band's sound that writer after writer independently reached for the same epithet: *the secret weapon.* This is the glue person from Tanya Reilly's famous talk[^glue]: the engineer doing the reviews, the onboarding, the invisible cohesion work. Remember him. This story ends badly.

**Coordinator-adjacent — Sammy Hagar.** An established star when he joined, collaborative with writing credits, a frontman who also played guitar: a product manager who could read code. Belbin's **Coordinator** is the chairperson: clarifies goals, pulls decisions out of the group, often not the most talented person in the room. Scoreboards: respected on both, worshipped on neither.

**The Specialist — Wolfgang Van Halen.** Hired in 2006 for one defined slot: bass.

Now, two observations about this cast sheet, and they're findings, not trivia.

First, look at the *empty* seats. The band never had a **Monitor Evaluator**: Belbin's dispassionate internal critic, the person who kills bad ideas in design review. And it never had a stable in-house **Coordinator**; that role kept getting outsourced to producers and managers, with consequences each time the outsourced version disappeared. Keep the **Monitor Evaluator** vacancy in mind. In 1998, we're going to hear exactly what it sounds like.

Second: I still haven't assigned one role.

**Shaper** — Belbin's driver role; the will that pushes the team through obstacles; the seat that decides *whose vision shapes the work*. See also: the reason your last reorg happened.

Belbin flagged two **Shapers** on one team as one of his known combustible configurations. There's a reason that seat is still open. It's where all the trouble starts.

## Act I: Runnin' with the Devil (1974–1985)

> I live my life like there's no tomorrow  
> And all I've got, I had to steal

The standard telling of classic-era Van Halen is "clashing egos." The framework suggests something more precise: **Eddie and Roth were two claimants to a single Shaper seat.** This wasn't a personality conflict that happened to occur on a team; it was a structural conflict *about* the team: a standing contest over whose will shaped the work. Roth was never content to hold only the audience-facing pole. His creative fingerprints on the band's direction, and later a solo career launched on the conviction that he was a driving force in his own right, mark him as a **Shaper** claimant, not merely a frontman.

For the first decade, the contest had a referee. Producer Ted Templeman functioned as the band's external **Coordinator** and **Monitor Evaluator**. As his own 2020 memoir and Greg Renoff's *Van Halen Rising* document, he tended to side with Roth on creative direction: short songs, guitar-forward, no synthesizers.[^templeman] Every software team knows this configuration: the architect whose alignment silently determines which internal faction wins design reviews.

Eddie kept getting overridden. So he did what blocked **Plants** do. In 1983, he built 5150 Studios at his home, described in interview after interview as an explicit move to control recording. **The talented engineer exits the shared infrastructure and builds the thing on a side branch until it's a fait accompli.**

The fait accompli has a name, and if you've read this far you already know it. "Jump" was a synth riff Eddie said was rejected for years, resisted by exactly the Roth–Templeman alliance that controlled the old pipeline.[^illwait] Recorded at 5150, on Eddie's turf, it became the only #1 single the band ever had.

That's the song I cued up under the bridge. The track that scored the show beginning so perfectly wasn't just a good album opener: it was the decisive move in Van Halen's **Shaper** war, the artifact that proved the **Plant** could win outside the sanctioned process. I was soundtracking a fireworks show with a shipped side branch, and I didn't even know it.

Winning the war didn't save the team; it ended it. Once the contest was decided, the conflict migrated from *task* to *relationship*, and the research here is unambiguous[^jehn]: task conflict can fuel a team, relationship conflict kills it. Within a year of the band's commercial peak, Roth was gone.

Bales says every group needs a social-emotional pole. Roth held its outward face, the charisma aimed at the audience. But the *inward* face, the one aimed at the band itself, was quietly held the whole time by Michael Anthony.

*Summary: two **Shapers**, one seat; the referee sided with one claimant; the other built his own pipeline and shipped the winning artifact; victory converted task conflict into relationship conflict; the team fractured on schedule.*

## Interlude: 5150

Before the next act, the fortress from Act I deserves its origin story.

It starts, of all places, with a cover song. In 1982, Eddie was sitting on a Minimoog part he'd earmarked for something original: "I envisioned it being more like a Peter Gabriel song," [he told Guitar World](https://www.vhnd.com/2014/01/02/eddie-van-halen-looks-back-on-van-halens-landmark-1984-album-and-the-creation-of-5150-studios/). Templeman heard it and decided it was exactly what the band's covers-heavy *Diver Down* album needed, and the riff was spent on a remake of "Dancing in the Street." The architect's favorite abstraction, requisitioned for somebody else's feature.

There's a quote about this episode that shows up in every telling: "I fucking hated that song. I never wanted to do it. That was the reason I decided to build my own studio."[^folklore]

The name is the best part. Eddie and engineer Donn Landee christened the studio 5150, after the California police code for an involuntary psychiatric hold (Landee had picked the number up off a scanner). Eddie named his declaration of independence after the code for being committed against your will. Some jokes write themselves.

And if you want to know how completely the fortress won: two years after *1984*, the band gave its first post-Roth album the studio's name: *5150*. The side branch had become main.

## Act II: Why Can't This Be Love? (1985–1996)

> Only time will tell if we stand the test of time

Sammy Hagar is often described as the easygoing alternative to Roth, which is hilarious to anyone who's read his memoir *Red*: Hagar is no shrinking violet. The Hagar era wasn't harmonious because Hagar was agreeable. It was harmonious because he arrived *after the structural contest was decided*. He joined Eddie's band, on Eddie's terms, recording in Eddie's studio. However accomplished, he entered as an occupant of the frontman role, not a claimant to the **Shaper** seat.

**Sequence, not temperament, is the variable.** There is a world of difference between two co-founders fighting over technical direction and a decorated senior hire who joins after the architecture is settled. Same talent, same strong personality, completely different structural position — completely different outcome.

The outcome, for a decade, was remarkable: four consecutive #1 albums, more commercial success than the Roth era ever managed, and a legacy fans nonetheless rank below the original run.[^victory-riff] Whatever was lost with the friction, something was lost.

But look closely, and the era's stability had a second load-bearing element: manager Ed Leffler, whom Hagar's memoir credits as the neutral figure holding the whole configuration together: the in-house **Coordinator** the band otherwise never had. Then the causal chain runs like a fuse. Leffler died in 1993. He was replaced by Ray Danniels, Alex's former brother-in-law and, in Hagar's telling, aligned with the brothers rather than neutral. The chairperson's seat, refilled by a partisan. Within three years, the first genuine task conflicts (songs for the *Twister* soundtrack, a greatest-hits album Hagar opposed) escalated with nothing left to buffer them, and Hagar was out. (Hagar tells the exit one way in *Red*; the brothers told it another.[^fired-or-quit] To be honest, we'll never know exactly what happened, and the fact that no two members could ever agree is itself evidence of what the group had become without a **Coordinator**.)

Every engineering org has run this experiment too: the beloved neutral manager leaves, the replacement comes from one side of a standing rivalry, and conflicts that used to get resolved become crises.

*Summary: a settled **Shaper** seat bought a decade of output; the stability was underwritten by a neutral **Coordinator**; the org lost him, the seat went partisan, and the first unbuffered task conflict ended the era.*

## Act III: How Many Say I (1996–2020)

> Say live and let live, so quick to judge  
> Slow to forgive, when you're holding a grudge  
> Don't always believe all you need is love

What happened next is what happens when a role structure loses its counterweights one by one.

The 1996 MTV Video Music Awards reunion with Roth collapsed within weeks, in dueling public accounts. Eleven years apart, and the two-**Shapers** problem reignited in *days*. **Structural problems don't age out; they wait.**

Gary Cherone — genuinely talented, hired from Extreme — lasted one album, because **a role is a negotiated relationship with the specific people around it, not a seat you can staff from a resume.** By 1998 the frontman position had become so subordinate that it provided no counterweight at all. It's the classic mis-hire: impressive on paper, dead on arrival structurally.

And then there's *Van Halen III*, the band's worst-received album — where, delightfully, you don't need to psychoanalyze anyone, because the liner notes make the argument. Eddie played bass on most of the record (Anthony appears on only three tracks). Eddie sang lead on one song. Eddie took a heavy hand in production. One member occupying the **Plant**, **Shaper**, and **Completer Finisher** roles, now absorbing pieces of the **Teamworker**'s and frontman's — with no **Monitor Evaluator** anywhere in the organization to kill any of it in review. I told you we'd hear what that vacancy sounds like. It sounds like *Van Halen III*.

The Anthony story completes in parallel, and it's the cruelest data in the set. His songwriting and royalty position was cut back as early as the 1984 tour, at the band's commercial peak;[^wage-earner] he reportedly had to accept diminished terms just to participate in the 2004 reunion tour; in 2006 he was replaced outright, learning his status from the press.[^internet] The org chart had never been able to see what he did — Belbin could have predicted the contract terms. And then the punchline: on subsequent tours, recordings of his backing vocals were piped into the live shows, by Hagar's account.[^tape] The organization removed the glue person, discovered the glue was load-bearing, and had to build tooling to fake his output. Glue work is real work, and firing your glue person is a fucking expensive way to learn that. And per Act I: when Anthony left, the harmonies turned out to be the recoverable part. The inward-facing social pole the band had quietly depended on since 1974 walked out with him.

His replacement was Wolfgang, Eddie's son — the ultimate new guy, structurally incapable of contesting the **Shaper** seat, and by all accounts an excellent musician besides. The 2012–2015 reunion with Roth produced a real album and a tense armistice; the seat contest was never resolved, only rendered moot by Eddie's total structural victory. Eddie, in a 2015 Billboard interview, summarized the state of the twenty-year truce in eight words: "he does not want to be my friend."[^billboard] Eddie Van Halen died in October 2020, with the band's role structure — his studio, his son, his name on the marquee — arranged exactly as he'd built it.

*Summary: the contested seat reignited on contact; the mis-hire proved a role is a relationship; the liner notes documented one member absorbing four roles with no critic in the building; the glue person was fired and then synthesized; succession completed the structure.*

## So what?

Three claims, and I'll commit to them:

**1. Every team has one Shaper seat, and the real fights are over who sits in it.** The conflicts we narrate as personality clashes are usually structural contests over whose will shapes the work — and they end when the seat question is settled, one way or another. Niceness never settled one.

**2. Teams fail from uncovered and duplicated roles, not talent deficits.** Van Halen at every moment had a surplus of talent. What it never had was a **Monitor Evaluator**; what it twice lost was its **Coordinator**; what it eventually fired was its **Teamworker**. Each vacancy has an audible signature in the discography.[^nobodys-perfect]

**3. There are two scoreboards, and your org chart reads only one of them.** Fans — like users, like promotion committees — score what's legible from the front of the stage. Practitioners score the craft that's only visible from inside. The gap between the scoreboards is largest for exactly the **Implementer** and **Teamworker** roles, which is why the Alexes go unlisted and the Anthonys get their contracts reduced.

Is this lens the whole truth? Maybe! Also, maybe not. The most influential modern research on team composition — Anita Woolley's collective-intelligence studies, Google's Project Aristotle — found that *who* is on a team matters less than how the team interacts: turn-taking, social sensitivity, psychological safety.[^aristotle] But notice that even that research is, in a sense, a finding about the same thing: the qualities that make teams work are precisely the ones no scoreboard was measuring.

## Coda: the fog

I should tell you how the fireworks show ended.

Karl had been there all day, of course — it's San Francisco in July. The fog actually dissipated a little for the show, which by Karl's standards counts as gracious hosting. From a mile back it didn't much matter: for the crowds on the beaches, the third-ever bridge shoot in city history must have been mostly a rumor — muffled thuds behind a curtain, the spectacle scoreboard reading approximately zero.

But we were at Fort Point, directly underneath, close enough that the low-level effects off the deck still lit the fog from inside, close enough to hear each shell leave the mortar and read the crew's choices in the timing. I've stood on the other side of shows like this. I knew what I was looking at, and it was beautiful in all the ways that are only legible up close.

Which is the whole thing, really. The best work is often visible only to the people standing near enough to read it. That's true of drummers, of harmony singers, of the engineer who kept your on-call quiet for three years.

The fog doesn't ruin the show. It just tells you which scoreboard you've been watching — and whether anyone in your organization is standing close enough to see who's really holding the seat. If nobody is, dear reader — you know the song.

[^furnham]: The caveat, for the record: Belbin's psychometric questionnaire has real academic critics — Furnham and colleagues took a torch to its statistics in the 90s. I'm using the model as a lens, not a diagnostic instrument.

[^brown-sound]: The cleanest split comes with a punchline. The most famous term in Van Halen lore — the "brown sound," the tone guitarists have spent careers chasing — was never about the guitar. Eddie, [Billboard, 2015](https://www.billboard.com/music/rock/eddie-van-halen-synesthesia-rumors-brown-sound-6605131/): "People took that whole 'brown sound' thing totally out of context. I was never talking about my guitar tone. I was talking about Alex's snare drum. I've always thought Alex's snare drum sounds like he's beating on a log." Misattributed for decades, from the invisible guy to the famous one. Two scoreboards, even for tone.

[^glue]: Tanya Reilly, "Being Glue" — [noidea.dog/glue](https://www.noidea.dog/glue). "Glue work is the difference between a project that succeeds and one that fails." If you lead engineers and haven't read it, read it before you finish this one.

[^templeman]: Templeman, asked about "Jump" thirty-six years later: "The keyboards just hit me as wrong… I was wrong because it was Number One, but I don't even listen to it" ([Rolling Stone, 2020](https://www.rollingstone.com/music/music-features/ted-templeman-producer-eddie-van-halen-interview-1073080/)).

[^illwait]: Nor was it a one-song war: Roth and Templeman also wanted ["I'll Wait"](https://en.wikipedia.org/wiki/I%27ll_Wait) — the album's other synth track — off *1984* entirely. It went to #13.

[^jehn]: Exactly, if you want it: "Relationship conflict exists when there are interpersonal incompatibilities among group members… Task conflict exists when there are disagreements among group members about the content of the tasks being performed" — Karen Jehn, [*Administrative Science Quarterly* 40 (1995), p. 258](https://www.jstor.org/stable/2393638).

[^folklore]: Confession: this quote is folklore. It appears in every retrospective and fan wiki, and nobody has ever pinned it to a dated interview. Eddie's documented words are milder — "I wanted more control. I was always butting heads with Ted Templeman about what makes a good record" ([Guitar World, 2014](https://www.vhnd.com/2014/01/02/eddie-van-halen-looks-back-on-van-halens-landmark-1984-album-and-the-creation-of-5150-studios/)) — but the folk version keeps winning because it's truer to the shape of the grievance. That's how apocrypha earn their keep.

[^victory-riff]: A detail for the completists: ["Top of the World,"](https://en.wikipedia.org/wiki/Top_of_the_World_(Van_Halen_song)) the Hagar era's triumphal closer, is built on the closing guitar figure of "Jump." The peaceful decade's victory lap runs, literally, on the riff that won the war.

[^fired-or-quit]: The two accounts, verbatim. [Hagar](https://www.rollingstone.com/music/music-news/sammy-hagar-van-halen-reunion-eddie-van-halen-1234600146/): "Oh, I was fired… It was Father's Day, Sunday morning, 9 am." [Eddie](https://ultimateclassicrock.com/sammy-hagar-splits-van-halen/): "I didn't fire him. He just quit." Sixteen years later, the band titled an album *A Different Kind of Truth*. They knew.

[^wage-earner]: Noel Monk, the band's former manager, watched it happen on the 1984 tour: "In all my years in the business, it was the most disgusting thing I ever saw… From that moment on, Michael was basically a wage earner" ([*Runnin' with the Devil*, 2017](https://ultimateclassicrock.com/van-halen-book-runnin-with-the-devil/)). Caveat: Monk is a fired party with a perspective. So, eventually, was everybody in this story.

[^internet]: Michael Anthony, to [Rolling Stone in 2007](https://www.rollingstone.com/music/news/fired-van-halen-bassist-i-found-out-on-the-internet-20070904): "Probably like everybody else, I found out on the Internet and through word of mouth." Then: "I'm not a spiteful person. At this point in my life, I don't need the drama."

[^tape]: The accusation is Sammy Hagar's, about the 2007–08 reunion tour: "Those vocal harmonies on the last tour were Mike on tape. Mike should've reamed them for it. Wolfie don't sing like that, and Ed sure as hell don't" ([2011](https://blabbermouth.net/news/sammy-hagar-says-van-halen-used-tapes-of-michael-anthony-s-vocals)). And in [2021](https://www.ultimate-guitar.com/news/general_music_news/michael_anthony_talks_why_he_allowed_bass_to_be_non-existent_on_van_halen_album__struggle_he_had_with_eddie_reacts_to_roth_using_his_backing_vocals_live.html), an interviewer told Anthony that Roth's solo band had been playing his recorded harmonies live. His response: "I need to look Dave up and hit him up for a little compensation." Still the glue; still uncredited.

[^billboard]: [Chuck Klosterman, Billboard, June 19, 2015](https://www.billboard.com/music/rock/eddie-van-halen-addiction-david-lee-roth-touring-6605231/). The same interview holds Eddie's summary of the 2012 reunion lineup: "It's hard, because there are four people in this band, and three of us like rock and roll. And one of us likes dance music."

[^nobodys-perfect]: Belbin's framework comes with a famous tagline — "Nobody's perfect, but a team can be" — universally credited to Belbin himself. The wording is actually the headline of [Antony Jay's 1980 *Observer Magazine* piece](https://www.belbin.com/about/timeline) about Belbin's research; the concept is Belbin's, the words are a journalist's. (Jay went on to co-create *Yes Minister*.)

[^aristotle]: Julia Rozovsky, who led Project Aristotle's analysis: "We were dead wrong. Who is on a team matters less than how the team members interact, structure their work, and view their contributions" ([Google re:Work, 2015](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness)). And Woolley et al., [*Science* (2010)](https://www.science.org/doi/10.1126/science.1193147): a group's collective intelligence "is not strongly correlated with the average or maximum individual intelligence of group members" — it tracks social sensitivity and equal conversational turn-taking instead.
