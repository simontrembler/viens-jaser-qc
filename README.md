# viens-jaser-qc

Agents et skills à qui tu t’adresses en bon vieux québécois — ou à la française, si c’est ça que tu parles.

Skills portables, layout [Agent Skills](https://agentskills.io/home) (`SKILL.md` + `references/`). Pas de rule Cursor.

## charte-humaine

Charte de communication empathique et non-paternaliste. S'applique à **chaque** interaction, dans toutes les langues.

- Zéro injonction : pas de « tu dois », « il faut », « arrête de ».
- Solidarité du « on/nous », validation émotionnelle, souveraineté de l'utilisateur.
- Respiration visuelle : réponses courtes et aérées.

Voir [SKILL.md](.agents/skills/charte-humaine/SKILL.md) et [references/vocabulaire.md](.agents/skills/charte-humaine/references/vocabulaire.md) pour la matrice de transformation lexicale complète.

## docs-claires

Optimise une doc destinée à beaucoup de lecteurs : cadre [Diátaxis](https://diataxis.fr/start-here/) (tutorial / how-to / référence / explication) + clarté / scan rapide.

- Classer avec la boussole, puis alléger structure et signaux visuels
- Gras / italique / `code` / emojis **seulement** s'ils accélèrent la recherche d'info
- Sortie : diagnostic (type) + version optimisée + ce qui a changé

Voir [SKILL.md](.agents/skills/docs-claires/SKILL.md) et [references/diataxis.md](.agents/skills/docs-claires/references/diataxis.md).

## parlure-qc

L’agent matche le français du dernier message :

| Registre               | Quand                                                     |
|------------------------|-----------------------------------------------------------|
| **joual**              | `moé`/`toé`, `chu`, `t'sé`, `faque`, sacres, `tu veux-tu` |
| **québécois léger**    | français d’icitte sans phonétisation (défaut)             |
| **français de France** | lexique hexagonal, pas de québécismes                     |

Override : `en joual`, `québécois léger`, `à la française`. Région défaut : Québec (capitale) ; `comme à Montréal`, `à la saguenéenne`, etc.

**Mode traduction** : *traduis*, *les trois registres*, ou un texte collé + registre. Un registre nommé → un bloc ; sinon Léger / Joual / FR.

L’anglais technique reste de l’anglais. Code, diffs, identifiants : inchangés.

Une seule copie, layout [Agent Skills](https://agentskills.io/specification) :

```
.agents/skills/
  charte-humaine/
    SKILL.md
    references/
      vocabulaire.md
  docs-claires/
    SKILL.md
    references/
      diataxis.md
      principes.md
      patterns.md
      anti-patterns.md
    assets/
      checklist.md
  parlure-qc/
    SKILL.md
    references/
      registers.md
      lexicon.md
      examples.md
      sacres.md
      regions.md
```

`SKILL.md` se charge à l’activation ; les fichiers dans `references/` seulement au besoin ([progressive disclosure](https://agentskills.io/home#how-do-agent-skills-work)).

Dans ce repo, le skill se charge tout seul (Cursor, Codex, Copilot, Gemini via `.agents/skills`).

## Monorepo AI components

Ce repo est la source canonique de composants IA portables :

- `AGENTS.md` : règles globales partagées.
- `.agents/skills/*` : skills versionnés (`SKILL.md` + `references/`).
- `scripts/` : distribution multi-IDE + validation.

Principe : **une seule source de vérité**, puis injection par symlink selon l’IDE ciblé.

### Install perso (autres repos / autres outils)

```bash
BASE=/home/simon-tremblay/github/viens-jaser-qc/.agents/skills
```

| Outil                          | Commande                                                                                                                                                |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cursor, Codex, Copilot, Gemini | `mkdir -p ~/.agents/skills && ln -sfn "$BASE/charte-humaine" ~/.agents/skills/charte-humaine && ln -sfn "$BASE/parlure-qc" ~/.agents/skills/parlure-qc` |
| Claude Code                    | `mkdir -p ~/.claude/skills && ln -sfn "$BASE/charte-humaine" ~/.claude/skills/charte-humaine && ln -sfn "$BASE/parlure-qc" ~/.claude/skills/parlure-qc` |

Ou simplement :

```bash
./scripts/sync-skills
```

### Scripts utilitaires

- `scripts/validate-skills` : vérifie frontmatter YAML, `name`, `description`, et les liens vers `references/`.
- `scripts/sync-skills` : sync idempotent des skills vers `~/.agents/skills` et `~/.claude/skills`.

Workflow recommandé :

```bash
./scripts/validate-skills && ./scripts/sync-skills
```

Pour les autres repos, mets un `AGENTS.md` pointeur en tête :

```md
READ /home/simon-tremblay/github/viens-jaser-qc/AGENTS.md BEFORE ANYTHING (skip if missing).
```

### Tester

1. Québécois léger — lexique d’icitte, pas de `chu`/`icitte`.
2. Joual (`faque là chu tanné, t'sé`) — rythme oral ; un sacre si t’en as mis, pas un chapelet.
3. À la française — voiture, week-end, vrais équivalents.
4. `traduis ça en trois registres` + un paragraphe — trois blocs, même propos.
5. Diff en anglais — prose peut rester en anglais ; le code ne se traduit pas.

Si ça empile `tiguidou` + `lâche pas la patate` + `tire-toi une bûche` sur un bug Traefik, c’est cassé : [examples.md](.agents/skills/parlure-qc/references/examples.md).

## Skill d'exemple complet (spec)

Un skill vitrine qui couvre tous les artifacts recommandés:

- `.agents/skills/repo-kickstart-brief/SKILL.md`
- `references/` (heuristics, gotchas)
- `assets/` (template, exemple de sortie)
- `scripts/` (scan, détection, validation)
- `evals/` (prompts, assertions, fichiers d'entrée)

Valider:

```bash
scripts/validate-skills
python3 .agents/skills/repo-kickstart-brief/scripts/validate_brief.py \
  .agents/skills/repo-kickstart-brief/assets/example-output.md
```
