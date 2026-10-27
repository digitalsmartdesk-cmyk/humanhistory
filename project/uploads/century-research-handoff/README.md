# The last hundred years: project handoff

A 17-chapter evidence project on what the last ~100 years of advancement have done to humanity, including whether they left humanity uniquely exposed to catastrophe. Figures are current to dates between 13 and 28 October 2026.

## Hypothesis (stated and tested only in Chapter 16)
Humanity has made itself vulnerable to catastrophic outcomes through the last 100 years of advancement, unlike any other 100 years of advancement in known history.

Chapter 16's results (my judgment, not source findings): realised loss, not supported (the worst share losses came earlier); size of the worst case, supported as a model result only; reach, supported in kind but not in novelty; reversibility, mixed; dependence and margins, cannot be compared on these figures; defenses, mixed. "Unlike any other 100 years" cannot be tested from 19 selected events.

## Contents
- `pages/` the 21 standalone HTML pages (open in any browser; Google Fonts load online). `00-overview.html` indexes the rest.
- `source/` the Python generators. Run from the folder of the chapter: `cd source/build4 && python3 build_ch16.py`. Chapters 1-5 and 12-17 use `build4/common.py`, which reads CSS from `build2/defenses_template.html`. Outputs are written next to the script. Chapters 7, 8 and 9-11 come from `build2/build_past.py`, `build2/build_defenses.py` and `build3/build_nature.py`. The two science pages come from `source/build/` (`build.py`, `data1.py`, `data2.py`). The generators for the vulnerability chapter and the industrial timeline were not kept, so edit those two pages' HTML directly.
- `notes/defenses-research-notes.txt` research notes behind Chapter 8.

## Chapters
| # | Page | Published (private artifact) |
|---|------|------|
| 1 | The appearance of human life | https://claude.ai/artifact/7qSxXu33DCKP9HftfxH3Dc |
| 2 | The pace of change | https://claude.ai/artifact/Ut88jmTViQUCc7jbfrZd1b |
| 3 | Life and health | https://claude.ai/artifact/79PSVNjqzAqJkcuARmF5wg |
| 4 | Food, wealth and comfort | https://claude.ai/artifact/M7CcrBF81bKsbmrs98iQCq |
| 5 | Knowledge and connection | https://claude.ai/artifact/1yPcv32YXUWW2jYuRESSNG |
| 6 | A century of vulnerability | https://claude.ai/artifact/SJ3PdrbEz1U14tZftAh7p5 |
| 7 | The record of catastrophes | https://claude.ai/artifact/21WkXcCqVbi5EXSyYgitEL |
| 8 | Defenses built | https://claude.ai/artifact/GgfHSBg2uJFXYtAS7QzhRU |
| 9 | Nature at risk | https://claude.ai/artifact/B7jDvigTvytm2ioPUncLbZ |
| 10 | Nature's catastrophes | https://claude.ai/artifact/NUTcZosxAhd7YLJJ5s85BQ |
| 11 | Nature defended | https://claude.ai/artifact/Xdv42PDasn3ETek7T5x8oB |
| 12 | Work, inequality and population | https://claude.ai/artifact/SNJrCBY4SongkYejYANqSt |
| 13 | Literacy, wisdom and knowledge | https://claude.ai/artifact/PtP9Rvnfn7VatTSYdnv6Y9 |
| 14 | Mind and wellbeing | https://claude.ai/artifact/9RZVCJrqYMM9PkrBB3YXEp |
| 15 | Power and governance | https://claude.ai/artifact/Q1B1ZSSMUHxtXhi72heMg4 |
| 16 | The comparison | https://claude.ai/artifact/6Q4xocHoggdkKuRGv4HUEa |
| 17 | What would change the balance | https://claude.ai/artifact/VLRHDtiF4NdbNchLpzeUBN |
| - | Overview | https://claude.ai/artifact/JoUuQJjxqMzn18Fr9Jdd2t |
| s1 | Industrial breakthroughs | https://claude.ai/artifact/EZXNpDinrBjMrY6HYzkxiS |
| s2 | Science 1825-1925 | https://claude.ai/artifact/NJViUDxqQQfGjmSwVynETQ |
| s3 | Science 1925-2025 | https://claude.ai/artifact/32HDo7P7ycKcZG6obVjPug |

The artifact links are private until shared from each page's Share menu.

## Conventions used on every page
- Solid bars are the source's own figure. Hatched bars are my arithmetic, a rough figure or a prediction.
- Each entry has a "How solid" note. A missing figure is shown as "No figure found".
- Sections headed "What the record shows" are my reading and are flagged as such. Each page ends with "What this chapter cannot show", then sources tagged P (primary or institution's own page) or S (secondary), and a footer listing my arithmetic and general-knowledge statements.
- Pages were read through a summarizing tool, so check figures against the originals before citing them.

## Known gaps and items to refresh
- Chapter 7 relies mostly on Wikipedia. Several later chapters rely on news reports of V-Dem, Transparency International, IRENA and IEA figures.
- Chapters 12-15 rarely reach back to 1925, so the two centuries cannot be compared on them. Chapter 13 gives no verdict.
- Still moving as of 28 October 2026: New START status (reports conflict), the pandemic agreement's access annex (due back by May 2027; outcome of the September 2026 meeting not found), COP31 (9-20 November 2026, Antalya), the plastics treaty, and EU AI Act dates.
- Chapter 14 includes suicide statistics and an offered support note; keep that if you edit it.
- Not done: a century-by-century tally of losses, which Chapter 17 names as the evidence that would settle "unlike any other 100 years".
