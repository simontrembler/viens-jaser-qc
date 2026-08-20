# Patterns de réécriture

Choisir d'abord le type Diátaxis ([diataxis.md](diataxis.md)), puis appliquer le pattern qui match.

## Patterns par type

### Tutorial → leçon guidée

```markdown
## Ce qu'on va accomplir
En suivant ce tutoriel, on aura … (résultat visible).

## Prérequis (minimal)
…

## Étapes
1. Fais X. Tu devrais voir …
2. Fais Y. Notice que …

## Ce qu'on a bâti
…
```

Une seule voie. Explications en une ligne + lien. Pas de menu d'options.

### How-to → but + contrat

```markdown
## How to …
Ce guide montre comment … (but réel).

## Quand l'utiliser
…

## Étapes
1. …
2. Si …, alors …

## Voir aussi
- Référence : …
- Pourquoi : …
```

### Référence → description consultable

```markdown
## `nom`
**Quoi :** …
**Signature / champs :** …
**Comportement :** …
**Exemple :** `…`
```

Austère. Pas de « pourquoi on a choisi… » ici → lien *About*.

### Explication → *About* + connexions

```markdown
## About …
### Contexte
### Pourquoi
### Alternatives
### Liens
```

## Avant → Après (structure)

**Avant** (tout mélangé) :

> Pour démarrer il faut d'abord cloner le repo puis installer les deps avec npm install ensuite on peut lancer le serveur de développement via npm run dev mais attention il faut Node 20 sinon ça plante et aussi regarde le fichier .env.example…

**Après** :

```markdown
## Démarrer en local

**Prérequis :** Node 20+

1. Cloner le repo
2. `npm install`
3. Copier `.env.example` → `.env`
4. `npm run dev`
```

## Pattern « ancre + détail »

1. Ligne d'ancre scannable (titre ou **gras**).
2. 1–3 phrases max de détail.
3. Exemple ou commande en `code` si pertinent.

## Pattern « décision rapide »

Quand le lecteur doit choisir :

```markdown
| Situation | Action |
|---|---|
| Premier setup | Suivre **Installer** |
| Déjà installé | Aller à **Lancer** |
| Ça casse | Section **Dépannage** |
```

## Pattern « status emoji » (docs ops / runbooks)

- ✅ Fait / OK
- ⚠️ Attention / limite
- ❌ Ne pas faire
- 🔁 À répéter

Un emoji = un statut. Pas de décoration.

## Pattern « TL;DR en haut »

Pour les docs longues (> ~40 lignes utiles) :

```markdown
## TL;DR
- But : …
- Action : `…`
- Si bloqué : …
```

## Préservation

- Ne pas inventer de commandes, d'URLs ou de versions absentes de la source.
- Garder les noms propres, chemins et IDs **identiques**.
- Si une info manque pour clarifier : le signaler dans le diagnostic, pas la fabriquer.
