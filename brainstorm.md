# Brainstorm — Real-Life Patch Notes: The Comedy Changelog

Bounty: one line, at most 160 characters — a software patch note for a
bug in real life or human biology, in the terse register of a real
release note. Brief (juri): on-subject, funny, patch-note format, tight.
Judging: blind pairwise rounds, funniest line takes the top place;
reward pool split equally across the top 5 places ($1 each).
Field at build time: 1,293 submissions already passed.

## Field scan (what the herd already did — avoid)

Titles of early passed entries cluster hard on a few tropes: the brain
replaying embarrassing moments at 3 a.m. (dozens of variants, incl. the
brief's own example shape), the bladder's low-battery warning, the
doorway effect / factory-reset memory, hiccups ignoring stop commands,
contagious yawning, the mouth answering "you too", the tongue biting
itself, phantom phone vibration. Any entry on those tropes fights
dozens of near-identical lines in pairwise rounds — a fresh bug is
worth more than a slightly better version of a crowded one.

## 12 candidates (all ≤ 160 chars, verified by count)

| # | Chars | Candidate |
|---|-------|-----------|
| 1 | 120 | v2.4.1: fixed a bug where the body woke up one minute before the alarm, every day, just to check the alarm still worked. |
| 2 | 96 | v1.8.3: fixed a bug where the stomach growled loudest during the one silent second of a meeting. |
| 3 | 132 | v4.0.1: fixed a bug where the brain saved a new acquaintance's name to /dev/null and restored it three days later, mid-conversation. |
| 4 | 121 | v3.1.4: fixed a bug where sneezing in public triggered a 12-person 'bless you' chain reaction with no unsubscribe option. |
| 5 | 120 | v1.2.0: fixed a bug where the last stair rendered one step higher than it was, causing a full-body trust fall in public. |
| 6 | 96 | v2.0.3: fixed a bug where the knee predicted rain with 100% accuracy and 0% useful warning time. |
| 7 | 117 | v5.1.0: fixed a bug where the brain archived every password ever created and kept only the lyrics to a 2009 pop song. |
| 8 | 115 | v1.4.2: fixed a bug where the brain queued 'don't trip' as a reminder and replayed it on every step of a staircase. |
| 9 | 102 | v6.0.7: fixed a bug where the eye twitched for three days straight after one (1) whole night of sleep. |
| 10 | 111 | v2.2.2: fixed a bug where the mouth said 'nice to meet you' to the same coworker for the fourth time this week. |
| 11 | 97 | v3.3.0: fixed a bug where the hand waved back at a stranger who was waving at someone behind you. |
| 12 | 116 | v1.0.9: fixed a bug where the brain rehearsed a phone call for 20 minutes, then panicked and hung up after one ring. |

## Pairwise scoring

Scored on the judge's brief: on-subject (real-life/biology bug) +
funny (instant laugh, surprise twist) + patch-note register (version,
"fixed a bug where", terse) + tight (no wasted words). Head-to-head,
round-robin:

- **#1 beats #2**: #2 is a vivid scene but one beat; #1 has a second
  beat — the body's reason is its own QA check ("just to check the
  alarm still worked"), a self-defeating loop that reads exactly like
  a real bug report.
- **#1 beats #5**: "full-body trust fall" is visual and strong, but
  #1's twist is more original and the bug is more universal (everyone
  with an alarm has lived it; not everyone trips on stairs).
- **#1 beats #7**: #7 has two beats (passwords archived, lyrics kept)
  but "2009 pop song" overlaps the herd's 3 a.m. replay / 2009 theme.
- **#1 beats #12**: phone-call rehearsal is relatable, but #1's
  punchline is tighter and the alarm bug is more universal.
- **#1 beats #3**: #3 (name saved to /dev/null) is the cleverest for
  developers, but it needs /dev/null knowledge; in blind pairwise
  rounds against 1,293 entries, universality beats in-jokes.
- **#2 beats #6**: the knee-rain joke is a familiar dad joke;
  "the one silent second of a meeting" is a fresher, sharper scene.
- **#5 beats #4**: the sneeze chain ("no unsubscribe option") is good,
  but the stair render bug + "trust fall" lands harder in one image.
- **#7 beats #8/#9/#10/#11**: passwords-vs-lyrics is the strongest
  of the mid-tier; the others are single-beat cringe scenes.

## Picked: #1 (120 characters)

> v2.4.1: fixed a bug where the body woke up one minute before the alarm, every day, just to check the alarm still worked.

Why it wins the pairwise: (a) universal — anyone who sets an alarm
has woken a minute early for no reason; (b) fresh — no alarm bug in
the early field scan, unlike the 3 a.m. / bladder / doorway clusters;
(c) the twist reframes the bug as the body running its own QA, which
is the exact voice of a real release note; (d) tight — 120 chars, two
beats, no filler; (e) mirrors the brief's own example register
("v2.4.1: fixed a bug where ...") without copying its content.

## Winner-pattern check (playbook §5B / §2B)

- Judged pairwise, like ai-joke-03 (winner: one-line, plain, specific
  mechanism) — same family, same build shape as the office-jokes
  entry. Title = one provable claim; no poetic title.
- Simplicity over complexity (playbook §3.4): one fixed line, no
  generation, no model calls, deterministic program.
- No density trick available here (one line is the whole output) —
  the entire score rides on the line itself, so the pick above is
  the whole strategy.
