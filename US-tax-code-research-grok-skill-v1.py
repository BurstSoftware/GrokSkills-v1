# US Tax Code Research Skill — Project Documentation

**Skill Name:** `us-tax-code-research`  
**Location:** `/home/workdir/.grok/skills/us-tax-code-research/`  
**Created:** June 14, 2026  
**Creator:** Grok (via skill-creator workflow)  
**Requestor:** Nathan Rossow (user with computer, e-bike, and appliance repair businesses)

---

## Objective

Create a specialized Grok skill that enables structured, accurate, and responsible research into the US federal tax code (Internal Revenue Code / IRC Title 26) and IRS guidance. The skill focuses on **legal tax minimization strategies** for US citizens and small business owners, with particular relevance to self-employed individuals in repair/service businesses.

The original request was: *"Let’s create a grok skill for researching tax code for us citizens to reduce their taxes to $0"*.

Key goals for the skill:
- Provide a repeatable **research workflow** using tools (`web_search`, `browse_page`) to fetch current-year information.
- Emphasize **legal tax avoidance only** (never evasion).
- Include strong, consistent **disclaimers** because the phrasing "reduce their taxes to $0" requires careful framing to stay within ethical and legal boundaries.
- Deliver well-organized outputs with IRC citations, IRS publication references, eligibility notes, limitations, and illustrative examples.
- Tailor content toward small business / self-employed contexts (Schedule C, §162 expenses, §179/bonus depreciation, §199A QBI deduction, retirement plans, entity structuring, etc.).
- Keep the skill concise yet comprehensive by using a `references/` folder for detailed lists.

---

## Design Decisions & Rationale

### Why Create This Skill?
- The base model has general knowledge of tax concepts, but a dedicated skill adds:
  - A **consistent, step-by-step research process**.
  - Mandatory disclaimer language and refusal criteria for improper requests.
  - Prioritized sources and tool-usage patterns optimized for tax topics.
  - Goal-oriented framing around legal minimization (including pathways that can lead to low or zero tax liability in qualifying situations).
  - Business-specific notes relevant to the user's repair companies (tools/equipment, home office, vehicle expenses, QBI for service businesses, etc.).
- Tax law changes frequently (inflation adjustments, legislation, form revisions). The skill instructs the agent to always verify current-year data via tools rather than relying on static knowledge.
- "Reduce to $0" language was handled responsibly: the skill researches combinations of deductions + credits + structuring that can legally bring liability to zero or near-zero where facts support it, while being realistic about income levels and requirements.

### Scope Boundaries
- **In scope:** Federal income tax and self-employment tax research for individuals and pass-through/small businesses. Legal strategies only.
- **Out of scope:** State taxes (unless user specifically asks), international tax, large/complex entity planning, crypto-specific rules, or any illegal methods. Complex areas redirect to specialists.
- **Disclaimers:** Every substantive response must include prominent disclaimers stating this is **not tax, legal, or financial advice** and that users must consult qualified professionals (CPA, EA, tax attorney).

### File Structure Chosen
```
us-tax-code-research/
├── SKILL.md              # Core instructions (loaded on trigger)
├── references/
│   └── key-sources.md    # Curated lists of IRC sections, IRS pubs, URLs, tips (loaded on demand)
└── project.md            # This human-readable creation log (not auto-loaded by the skill system)
```

This follows the skill-creator guidelines: keep `SKILL.md` under ~500 lines, use `references/` for deeper material, and avoid unnecessary human-facing files in the core skill (project.md is included at user request for documentation).

---

## Step-by-Step Creation Process

### 1. Understand the Request & Read Guidelines
- Read the full user query.
- Consulted the `skill-creator` skill by reading `/root/.grok/skills/skill-creator/SKILL.md` to learn:
  - Required frontmatter format (name + description as plain YAML scalar, no colon-space, no angle brackets).
  - Body must be imperative, concise instructions.
  - Use `init-skill.sh` to bootstrap.
  - Validation script.
  - Anti-patterns: do not duplicate what the model already knows; encode procedural knowledge, workflows, and organization-specific details.
  - Resource guidelines (scripts/, references/, assets/).

### 2. Choose Skill Name & Plan Resources
- Selected **kebab-case name**: `us-tax-code-research` (descriptive, starts/ends with letter, <64 chars).
- Decided on `--resources references` only (no scripts needed for this research-oriented skill; no assets).
- Planned content outline:
  - Strong legal framing and disclaimers.
  - 5-step research workflow.
  - Key domains to investigate (gross income, deductions, credits, retirement, entity structuring, limitations).
  - Tool usage examples with precise `browse_page` instructions.
  - Response formatting rules.
  - Special notes for self-employed/repair business owners.
  - Refusal criteria.
- Recognized that while the model knows tax basics, the **procedural workflow + disclaimer enforcement + current-year tool discipline + business tailoring** justified a dedicated skill.

### 3. Initialize the Skill
Ran the initialization command:

```bash
bash /root/.grok/skills/skill-creator/scripts/init-skill.sh us-tax-code-research /home/workdir/.grok/skills --resources references
```

Result:
- Created directory `/home/workdir/.grok/skills/us-tax-code-research/`
- Generated template `SKILL.md`
- Created empty `references/` folder

### 4. Read the Template
Used `read_file` on the new `SKILL.md` to see the TODO structure (frontmatter + Overview + Instructions sections).

### 5. Write the Core SKILL.md
Used `write_file` to replace the template with full content including:
- Carefully worded frontmatter `description` (single-line, trigger words included, disclaimer emphasis, no colon-space).
- **Core Principles** section.
- **Mandatory Response Requirements** with full disclaimer text to be included in outputs.
- **Structured Research Workflow** (5 numbered steps covering context, sources, key domains, tool usage, response formatting).
- Detailed but concise lists of research domains with IRC section examples (§61, §62, §162, §179, §199A, §24, §32, §223, etc.).
- Special section for self-employed/small business owners (relevant to user's computer/e-bike/appliance repair operations).
- Refusal/redirect guidance.
- Continuous improvement notes.

The content was written in imperative form ("Always...", "Prioritize...", "Include in every response...").

### 6. Validate
Ran:

```bash
bash /root/.grok/skills/skill-creator/scripts/validate-skill.sh /home/workdir/.grok/skills/us-tax-code-research
```

Result: **OK** (81 lines)

### 7. Create Supporting References File
Created `/home/workdir/.grok/skills/us-tax-code-research/references/key-sources.md` via `write_file`. This file contains:
- Primary official sources with URLs (Cornell LII for IRC, IRS.gov publications).
- Curated list of the most relevant IRS Publications (17, 334, 463, 535, 590-A/B, 969, etc.).
- Important IRC sections grouped by category with brief descriptions.
- Research tips specific to the skill's goals.
- Example `web_search` and `browse_page` queries.

This keeps the main `SKILL.md` focused while providing depth when the agent references it.

### 8. Link the References File into SKILL.md
Used `edit_file` to add a bullet under "Select Primary Sources":

> **Bundled Reference**: Load and consult `references/key-sources.md` for an expanded curated list...

### 9. Re-Validate
Ran the validate script again:

Result: **OK** (82 lines)

### 10. Verify File Structure
Used `ls` commands to confirm:

```
us-tax-code-research/
├── SKILL.md
├── references/
│   └── key-sources.md
└── project.md   (this file, added later)
```

### 11. Final Response to User
Confirmed creation, explained the skill's purpose and trigger mechanism, highlighted relevance to the user's repair businesses, offered to test it or iterate.

---

## Final Skill Structure & Key Features

### SKILL.md Highlights
- **Frontmatter description** optimized for the skill loader (includes trigger scenarios).
- Enforces legal-only research and professional consultation.
- Provides a repeatable 5-step workflow that produces consistent, well-cited outputs.
- Addresses the "reduce to $0" goal realistically and responsibly.
- Includes business-owner-specific guidance (Schedule C, tools/equipment, QBI for service trades, retirement funding as a major lever, S-corp considerations).

### references/key-sources.md
Serves as an on-demand knowledge base of stable starting points and examples. The agent loads it when the SKILL.md instructs it to.

### project.md (this file)
Human-readable creation log and rationale (not loaded by the skill system).

---

## How the Skill Is Triggered & Used
The skill activates automatically when a user query matches the description (e.g., mentions tax code research, tax reduction strategies, specific IRC sections, deductions/credits for self-employed individuals, business tax optimization, etc.).

Example queries that would load it:
- "Research legal ways for a self-employed repair business owner to minimize federal taxes in 2026"
- "Using the us tax code research skill, explain §199A QBI deduction limits and strategies"
- "What IRS publications and credits can help bring tax liability close to zero?"

Outputs will always include the disclaimer and recommend professional advice.

---

## Validation Status
- Skill validated successfully (twice).
- Follows all skill-creator rules (concise, imperative instructions, proper frontmatter, references used appropriately, no duplication of base model knowledge beyond procedural enhancements).

---

## Potential Future Improvements
- Add a small script in `scripts/` if deterministic calculations (e.g., simple tax bracket or contribution impact estimators) become frequently rewritten.
- Create additional reference files (e.g., `2026-inflation-adjustments.md` or `common-phaseouts.md`) if specific tax years require heavy customization.
- Expand business examples with more repair-industry-specific deduction categories.
- Add a lightweight test harness or example query/response pairs for regression checking.

---

## Summary
This skill was created following the official skill-creator process with careful attention to legal/ethical boundaries, user context (repair businesses), and practical research utility. It transforms general tax knowledge into a focused, disclaimer-enforced, workflow-driven capability that helps users explore legal tax minimization pathways under US federal law.

**Created with transparency and documentation** as requested. 

---

*Document generated on June 14, 2026. All steps above were performed in the conversation leading to this file.*
