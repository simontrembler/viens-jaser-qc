---
name: docs-claires
description: >-
  Optimize documentation for clarity and low cognitive load using Diátaxis
  (tutorial, how-to, reference, explanation) plus scan-friendly structure,
  literary clarity, and strategic bold/italic/code/emojis. Use when rewriting
  docs, READMEs, runbooks, guides, or any text meant for many readers — even if
  they say "rends ça plus clair", "allège la lecture", "Diátaxis", or "optimise
  la doc" without naming this skill.
metadata:
  author: simontrembler
---

# docs-claires

Optimiser une documentation consultée par un grand nombre de personnes.

Intentions (verbatim) :

- skill de clarté litéraire, réduire la charge mentale, accélerer la compréhension via tweaks visuels, répérer l'information le plus rapidement, réduire l'attention nécessaire à la tâche, attention span des gens est en baisse, utiliser les emojis si ça accélère la recherche d'information, utiliser le formattage (bold, italic, code, etc) là où ça peut alléger la lecture et améliorer la compréhension

Cadre structurel : [Diátaxis](https://diataxis.fr/start-here/) — quatre besoins, quatre formes. La clarté visuelle s'applique **après** (ou en même temps que) le bon type.

## Procédure

1. **Lire** le texte source tel quel.
2. **Classer** avec la boussole Diátaxis (ci-dessous) : un type dominant. Si le texte mélange plusieurs types → le dire dans le diagnostic et proposer un découpage ou un type prioritaire.
3. **Diagnostiquer** en 3–5 points : flou de type, charge mentale, info enterrée, digressions hors-type.
4. **Réécrire** pour le type choisi + clarté / scan / formatage.
5. **Aligner** tout tableau Markdown (colonnes droites, espaces padding) — comme un *Format Document* VS Code.
6. **Vérifier** [assets/checklist.md](assets/checklist.md).
7. **Livrer** : diagnostic (avec type) + version optimisée + « ce qui a changé ».

Une amélioration à la fois reste valide ([workflow Diátaxis](https://diataxis.fr/how-to-use-diataxis/)) : si Simon veut un petit tweak seulement, faire **un** pas utile plutôt qu'une refonte totale.

### Boussole (décision rapide)

| Le contenu…      | …et sert…                               | → type          |
|------------------|-----------------------------------------|-----------------|
| l'**action**     | l'**acquisition** de compétence (étude) | **Tutorial**    |
| l'**action**     | l'**application** (travail)             | **How-to**      |
| la **cognition** | l'**application** (travail)             | **Référence**   |
| la **cognition** | l'**acquisition** (étude)               | **Explication** |

Questions : *action ou cognition ?* *étude ou travail ?*

### Quand charger

- Détail des 4 types + pièges de mélange → [references/diataxis.md](references/diataxis.md)
- Principes de clarté / scan → [references/principes.md](references/principes.md)
- Patterns de réécriture → [references/patterns.md](references/patterns.md)
- Anti-patterns → [references/anti-patterns.md](references/anti-patterns.md)

## Règles rapides (tous types)

| Faire                                                   | Éviter                                                    |
|---------------------------------------------------------|-----------------------------------------------------------|
| Un job Diátaxis par page (ou section clairement bornée) | Tutoriel + explication + référence dans le même flux      |
| Titres qui disent le besoin (`How to…`, `About…`)       | Titres vagues (`Notes`, `Divers`, `Overview` fourre-tout) |
| **Gras** pour l'ancre scannable                         | Gras partout                                              |
| `code` pour commandes, chemins, IDs                     | Code décoratif                                            |
| Emoji de section **si** ça accélère le scan             | Emoji à chaque phrase                                     |
| Lier vers l'autre type au lieu d'y digresser            | Polluer un how-to avec de la théorie                      |
| Tableaux Markdown **alignés** (pipes + padding)         | Tableaux croches / colonnes irrégulières                  |

### Tableaux Markdown (alignement)

Tout tableau dans la version optimisée (et dans le skill lui-même) doit être formaté « droit » :

- Une espace de chaque côté du contenu de cellule quand c’est possible : `| cellule |`
- Largeur de colonne = plus long contenu de la colonne (header inclus)
- Ligne séparateur `|---|` alignée sur la même largeur
- Pipes verticaux alignés d’une ligne à l’autre (équivalent *Format Document* / prettier markdown)

Détail + avant/après → section **Tableaux alignés** dans [references/patterns.md](references/patterns.md).

## Sortie

```markdown
## Diagnostic
- Type Diátaxis : tutorial | how-to | référence | explication
- …
- (si mélange) Proposition de découpage : …

## Version optimisée
…

## Ce qui a changé
- …
```

Si Simon demande seulement la version finale : livrer la version optimisée seule (le type peut rester en une ligne en tête).

## Interaction avec les autres skills

- **charte-humaine** : ton compagnon autour de la doc.
- **parlure-qc** : registre de l'accompagnement ; le document technique garde son registre source sauf demande contraire.
