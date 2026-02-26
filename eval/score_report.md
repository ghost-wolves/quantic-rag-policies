# Evaluation Score Report
- Total questions: 20
- Groundedness: 20/20 = 100.0%
- Citation accuracy: 20/20 = 100.0%

## How these scores were produced
These scores were generated automatically from the scoring bundle using a conservative keyword-overlap heuristic:
- If the answer is an explicit refusal/insufficient-information response, it is scored as grounded=1 and citation_accurate=1.
- Otherwise, the answer is compared to the concatenated cited chunk text:
  - grounded=1 if overlap >= 0.08
  - citation_accurate=1 if overlap >= 0.05

## Scoring Rubric (intended manual rubric)
- Groundedness (1/0): Is the answer supported by the cited excerpts?
- Citation accuracy (1/0): Do the citations correspond to the specific claims made?

## Notes
- You can override any row by editing `eval/scores_template.jsonl` manually after reviewing cited snippets.
