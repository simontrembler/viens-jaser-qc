# Diátaxis (référence opérationnelle)

Source : [diataxis.fr](https://diataxis.fr/start-here/). Cadre pragmatique — pas un plan à imposer d'en haut.

## Les quatre types

| Type            | Besoin                                      | Question                            | Analogie                                |
|-----------------|---------------------------------------------|-------------------------------------|-----------------------------------------|
| **Tutorial**    | Apprendre (étude + action)                  | « Tu peux m'enseigner à… ? »        | Leçon de cuisine avec un enfant         |
| **How-to**      | Atteindre un but (travail + action)         | « Comment je… ? »                   | Recette / manuel clinique               |
| **Référence**   | Faits pour travailler (travail + cognition) | « Qu'est-ce que… ? »                | Étiquette nutritionnelle / carte marine |
| **Explication** | Comprendre (étude + cognition)              | « Pourquoi… ? » / « Parle-moi de… » | Essai / discussion de fond              |

### Tutorial

- Leçon pratique : le lecteur **fait** sous guidance.
- Succès = expérience d'apprentissage fiable, pas le produit parfait.
- Résultats visibles tôt et souvent ; narrative de l'attendu (« tu devrais voir… »).
- Minimiser l'explication ; lier vers une page *explanation*.
- Une voie, pas d'options ; concret ; « nous » (tutor + learner).
- Voir [Tutorials](https://diataxis.fr/tutorials/).

### How-to

- Directions vers un **but réel** déjà compétent.
- Perspective utilisateur / projet humain — pas « voici les boutons de l'outil ».
- Action (et jugement) seulement ; pas d'enseignement ni de digression théorique.
- Adaptable au monde réel ; forks OK (`si X, alors Y`).
- Titre exact : *How to integrate…* (pas *Integrating…* ambigu).
- Voir [How-to guides](https://diataxis.fr/how-to-guides/).

### Référence

- Description neutre, austère, consultable — on ne « lit » pas, on **consulte**.
- Structure alignée sur la machine (modules → classes → méthodes).
- Patterns standards ; exemples illustratifs OK, pas d'essai.
- Voir [Reference](https://diataxis.fr/reference/).

### Explication

- Contexte, *why*, connexions, perspectives — lecture « au calme ».
- Titres du genre *About…* / *Background…*.
- Opinion et alternatives possibles ; borner le sujet.
- Ne pas absorber howto / référence / tutoriel.
- Voir [Explanation](https://diataxis.fr/explanation/).

## Distinctions critiques (où ça casse)

### Tutorial ≠ How-to

Même forme (étapes), besoins opposés : **étude** vs **travail**.
Les confondre est le mélange le plus fréquent et le plus coûteux.
Détail : [tutorials-how-to](https://diataxis.fr/tutorials-how-to/).

|                | Tutorial                       | How-to                   |
|----------------|--------------------------------|--------------------------|
| But            | Compétence de base / confiance | Tâche correctement faite |
| Cadre          | Contrôlé, sûr, rejouable       | Monde réel               |
| Responsabilité | L'auteur/tuteur                | L'utilisateur            |
| Choix          | Une ligne                      | Branches possibles       |
| Complexité     | Peut être avancé               | Peut être basique        |

### Référence ≠ Explication

Les deux = cognition ; **travail** vs **étude**.
Si on le lirait « au boulot pour un fait » → référence.
Si on le lirait « pour réfléchir / pourquoi » → explication.
Détail : [reference-explanation](https://diataxis.fr/reference-explanation/).

## Workflow Diátaxis (processus)

Ne pas créer quatre dossiers vides. Améliorer de l'intérieur :

1. Prendre un morceau devant soi.
2. L'évaluer (besoin ? type ? langage ?).
3. Choisir **une** action qui améliore.
4. La faire (commit / publier).
5. Répéter.

Voir [how-to-use-diataxis](https://diataxis.fr/how-to-use-diataxis/) et [map](https://diataxis.fr/map/).

## Comment docs-claires compose avec Diátaxis

1. **Type d'abord** (boussole) → calibre quoi garder / sortir / lier.
2. **Clarté ensuite** → titres, rythme, gras, listes, emojis de scan.
3. Le formatage sert le type :
   - Tutorial / how-to → listes d'actions, attentes concrètes
   - Référence → tableaux, listes sèches, exemples courts
   - Explication → prose structurée, sous-titres *About*, liens croisés
