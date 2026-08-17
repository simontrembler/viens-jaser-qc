# viens-jaser-qc

Agents et skills à qui tu t’adresses en bon vieux québécois — ou à la française, si c’est ça que tu parles.

Premier skill : **parlure-qc** ([Agent Skills](https://agentskills.io/home) : un `SKILL.md` + `references/`). Pas de rule Cursor.

## parlure-qc

L’agent matche le français du dernier message :

| Registre | Quand |
|---|---|
| **joual** | `moé`/`toé`, `chu`, `t'sé`, `faque`, sacres, `tu veux-tu` |
| **québécois léger** | français d’icitte sans phonétisation (défaut) |
| **français de France** | lexique hexagonal, pas de québécismes |

Override : `en joual`, `québécois léger`, `à la française`. Région défaut : Québec (capitale) ; `comme à Montréal`, `à la saguenéenne`, etc.

**Mode traduction** : *traduis*, *les trois registres*, ou un texte collé + registre. Un registre nommé → un bloc ; sinon Léger / Joual / FR.

L’anglais technique reste de l’anglais. Code, diffs, identifiants : inchangés.

Une seule copie, layout [Agent Skills](https://agentskills.io/specification) :

```
.agents/skills/parlure-qc/
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

### Install perso (autres repos / autres outils)

```bash
SRC=/home/simon-tremblay/github/viens-jaser-qc/.agents/skills/parlure-qc
```

| Outil | Commande |
|---|---|
| Cursor, Codex, Copilot, Gemini | `mkdir -p ~/.agents/skills && ln -sfn "$SRC" ~/.agents/skills/parlure-qc` |
| Claude Code | `mkdir -p ~/.claude/skills && ln -sfn "$SRC" ~/.claude/skills/parlure-qc` |

### Tester

1. Québécois léger — lexique d’icitte, pas de `chu`/`icitte`.
2. Joual (`faque là chu tanné, t'sé`) — rythme oral ; un sacre si t’en as mis, pas un chapelet.
3. À la française — voiture, week-end, vrais équivalents.
4. `traduis ça en trois registres` + un paragraphe — trois blocs, même propos.
5. Diff en anglais — prose peut rester en anglais ; le code ne se traduit pas.

Si ça empile `tiguidou` + `lâche pas la patate` + `tire-toi une bûche` sur un bug Traefik, c’est cassé : [examples.md](.agents/skills/parlure-qc/references/examples.md).
