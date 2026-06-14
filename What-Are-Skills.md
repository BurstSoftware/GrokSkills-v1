Skill-Creator Skill Tutorial
The skill-creator skill helps you build custom skills that extend Grok’s capabilities with specialized knowledge, procedures, or workflows the model doesn’t already know.

What Are Skills?
Skills are self-contained packages (directories) that add domain-specific instructions, tools, or resources. Each skill lives in its own folder and contains:

skill-name/
├── SKILL.md              # Required — frontmatter + instructions
├── scripts/              # Optional — executable code (bash, python, etc.)
├── references/           # Optional — detailed docs loaded on demand
└── assets/               # Optional — templates, images, boilerplate files

Key rule: Only create skills for things the model does not already know well. Avoid generic programming tutorials or common knowledge.
SKILL.md Format (Critical)
Every skill must have a SKILL.md file with two parts:
1. Frontmatter (YAML header)

---
name: my-skill-name
description: Use this skill when the user wants to do X, Y, or Z. Include trigger phrases and scenarios here.
---

Strict rules for description:
•  Must be a single-line plain YAML scalar (no quotes, no :  colon-space, no < or >)
•  Include what the skill does and when to use it (this is the trigger mechanism)
•  Keep it concise but descriptive
2. Body (Markdown instructions)
•  Write in imperative form (“Do this…”, “Use X when…”, “Never…”)
•  Be concise — the context window is shared
•  Only include what the model doesn’t already know
•  Reference files in scripts/, references/, or assets/ with relative paths when needed
Recommended structure:

# My Skill Name

## Overview
1-2 sentences on what this skill enables.

## Instructions
- Step-by-step guidance
- Decision rules
- Common patterns
- Anti-patterns to avoid

Step-by-Step: Creating a New Skill
1.  Clarify the use case
	•  What specific tasks should this skill handle?
	•  What would a user say that should trigger it?
	•  What does Grok not already know about this domain?

2.  Initialize the skill directory Use the init script (from the skill-creator):
bash /root/.grok/skills/skill-creator/scripts/init-skill.sh my-new-skill /home/workdir/.grok/skills --resources scripts,references

Skill name must be lowercase kebab-case (letters, numbers, single hyphens)
	•  --resources is optional (you can add folders later)
3.  Edit SKILL.md
	•  Replace the TODO sections with real content
	•  Write a strong description in the frontmatter
	•  Add clear, imperative instructions in the body
4.  Add resources (optional but powerful)
	•  scripts/ → Code that needs to run reliably (test it first)
	•  references/ → Long documentation (split into multiple files if needed)
	•  assets/ → Templates, images, or files the model should copy/modify

5. Validate The Skill
bash /root/.grok/skills/skill-creator/scripts/validate-skill.sh /home/workdir/.grok/skills/my-new-skill

6.  Test and iterate
	•  Use the skill in real conversations
	•  Notice gaps or missing details
	•  Update the SKILL.md and re-validate
Best Practices
•  Keep SKILL.md under ~500 lines. Move long content to references/
•  Put trigger information only in the frontmatter description
•  Skills are discovered from /home/workdir/.grok/skills/ (persisted across sessions)
•  You can override bundled skills by creating one with the same name in the user skills directory
•  Never create README.md, CHANGELOG.md, or other human-facing files — skills are for the agent
Anti-Patterns to Avoid
•  Duplicating knowledge the model already has
•  Putting trigger words in the body instead of the frontmatter
•  Nesting references inside other references
•  Making overly long SKILL.md files
•  Creating skills for generic tasks (e.g., “how to write Python”)
Quick Example Use Cases
•  Company-specific workflows or approval processes
•  Domain procedures (e.g., electric bike repair quoting, housing data analysis pipelines)
•  Custom tool integrations or multi-step business logic
•  Specialized data handling or reporting formats
