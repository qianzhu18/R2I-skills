# Evidence Rubric

Use this file when deciding how strong a claim is allowed to be in learning, interview, or resume output.

## Rubric

### Tier A: Hard Evidence

Use when directly supported by:

- code
- tests
- config
- CI files
- docs with explicit claims

Allowed framing:
- direct technical facts
- clear module responsibilities
- verified workflows

### Tier B: Strong Inference

Use when the repo strongly suggests the claim through:

- naming
- architecture boundaries
- repeated patterns
- script behavior

Allowed framing:
- "appears to"
- "likely"
- "suggests"

Do not present Tier B as certain business fact.

### Tier C: Interview Framing

Use when translating evidence into a useful speaking angle.

Allowed framing:
- why the design matters
- what tradeoff might be worth discussing
- what claim an interviewer may pressure-test

Tier C is presentation guidance, not proof.

### Tier D: Needs Verification

Use when a stronger bullet would need:

- a metric
- adoption numbers
- production usage
- ownership scope

Label this explicitly as `metric to verify` or `claim to verify`.

## Red Flags

Downgrade confidence when:

- the repo is mostly generated
- the project is tutorial-sized
- the architecture claim is based on one filename
- the business value is not visible in code or docs

## Output Discipline

Learning docs should lean on Tier A and Tier B.

Interview prep may use Tier C.

Resume output must clearly separate Tier A/B from Tier D.
