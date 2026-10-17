<h1 align="center">Moi aussi, mais en mieux</h1>

<p align="center"><em>Il s'est levé à 5 h. Toi, à 3 h 47.</em></p>

Une skill satirique qui s'approprie n'importe quel post où l'auteur se met en valeur, et le surpasse avec la même mécanique, poussée un cran trop loin. LinkedIn, X, Reddit, Discord, Slack, Teams : partout où quelqu'un raconte à quel point il est formidable, tu l'es davantage.

Fonctionne avec **Claude, ChatGPT / Codex, Gemini, Mistral Le Chat, Cursor, Copilot** et tout LLM capable de suivre des instructions. Pas besoin de recherche web.

*English speakers: see [In English](#in-english) below. The skill answers in the language of the post.*

## Exemple

Post d'origine :
> Ce matin, mon fils de 6 ans m'a demandé pourquoi je travaillais.
> J'ai mis 10 minutes à répondre.
> Ce jour-là, j'ai compris ce qu'était le leadership.

Commentaire généré :
> Tellement vrai.
> Ma fille de 14 mois m'a regardé hier pendant que je préparais mon comité de direction.
> Elle n'a rien dit.
> Elle n'a pas besoin de parler pour me faire comprendre que ma roadmap Q3 manquait d'ambition.
> Je l'ai refaite le soir même. Elle a validé en recrachant sa compote.
> Ce jour-là, j'ai compris que le leadership commence avant le langage.

## Ce que ça fait

1. Repère la mécanique de valorisation du post et son **unité de mesure de l'ego** : l'heure du réveil, l'âge de l'enfant qui donne des leçons, le prestige de l'offre refusée.
2. Reprend la même structure et les mêmes codes, puis fait monter l'unité de mesure : un cran plausible, un cran douteux, un cran absurde, toujours avec le même sérieux.
3. Adapte le commentaire à la plateforme : 280 caractères pour X, TL;DR pour Reddit, lignes courtes pour Discord, niveau subtil par défaut pour Slack et Teams.

Sorties : un commentaire prêt à poster, un post miroir sur demande, et un **indice de surenchère** de 1/10 (on peut encore te croire sérieux) à 10/10 (même l'auteur va comprendre).

Trois niveaux : `subtil`, `assumé` (défaut), `délirant`. Mode `variantes` : un commentaire par niveau.

## Installation

### Installation universelle (agents de code)

```bash
npx skills add GregoryBabonaux/moi-aussi-mais-en-mieux
```

Installe la skill dans l'agent de ton choix : Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Cline, OpenCode...

### Installation manuelle

| Outil | Commande |
|---|---|
| Claude Code | `cp -r skills/moi-aussi-mais-en-mieux ~/.claude/skills/` |
| Codex CLI | `cp -r skills/moi-aussi-mais-en-mieux ~/.agents/skills/` |
| Autres agents Agent Skills | copier le dossier dans leur répertoire de skills |

### Claude.ai / app Claude

Télécharge [`dist/moi-aussi-mais-en-mieux.zip`](dist/moi-aussi-mais-en-mieux.zip) (bouton *Download raw file* sur GitHub), puis ajoute-le dans Paramètres > Skills.

### ChatGPT (Custom GPT)

1. Créer un GPT, coller le contenu de `dist/gpt-instructions.txt` dans *Instructions*.
2. Joindre `dist/moi-aussi-mais-en-mieux.md` dans *Knowledge*.

Sans GPT : colle `dist/moi-aussi-mais-en-mieux.md` au début de la conversation, puis ton post.

### Gemini (Gem), Mistral Le Chat (Agent), Claude Project, API, autres

Utilise le contenu de `dist/moi-aussi-mais-en-mieux.md` comme instructions système.

## Utilisation

```
Moi aussi mais en mieux : [texte du post]
Surenchère délirante sur ce post Reddit : [capture d'écran]
Trois variantes pour ce message Slack : [texte]
Fais-moi un post miroir de celui-ci : [texte]
```

Tu peux donner des éléments vrais sur toi (métier, parcours) : la surenchère part de ton profil réel, ce qui la rend plus crédible au premier cran.

## Les règles du jeu

- **On parodie la mécanique, pas la personne.** Aucune remarque sur le physique, l'âge, l'origine, la santé, la famille ou l'employeur de l'auteur. Son nom n'apparaît jamais.
- **Les exploits inventés sont les tiens**, jamais attribués à l'auteur.
- **Aucun fait plausible impliquant une vraie personne ou entreprise.** "J'ai refusé Google trois fois, dont une avant sa création" passe. "Le DRH de Google m'a appelé hier" ne passe pas.
- **Hors périmètre** : drames réels (deuil, maladie, burn-out, licenciement), réussites sincères et modestes, posts d'aide ou d'alerte.
- **Slack et Teams** : l'auteur est un collègue et le message reste dans l'historique de l'entreprise. La skill passe en niveau subtil par défaut et te le signale.

## Voir aussi

[Contre-argument Anything](https://github.com/GregoryBabonaux/contre-argument-anything) : la skill qui donne tort à n'importe quel post, avec des sources.

## Structure du repo

```
├── skills/moi-aussi-mais-en-mieux/    # la skill, format Agent Skills
│   ├── SKILL.md
│   └── references/surenchere.md       # archétypes de posts, techniques de surenchère
├── dist/                              # versions générées, ne pas éditer
│   ├── moi-aussi-mais-en-mieux.md     # prompt unique (tous LLM)
│   ├── gpt-instructions.txt           # instructions courtes pour Custom GPT
│   └── moi-aussi-mais-en-mieux.zip    # skill zippée pour Claude.ai
└── scripts/build_prompt.py            # régénère dist/ depuis skills/
```

## Contribuer

Modifie uniquement `skills/moi-aussi-mais-en-mieux/`, puis :

```bash
python3 scripts/build_prompt.py
npx skills-ref validate ./skills/moi-aussi-mais-en-mieux
```

Les nouveaux archétypes de posts sont les bienvenus dans `references/surenchere.md`.

## In English

A satirical skill that takes any self-congratulatory post (LinkedIn, X, Reddit, Discord, Slack, Teams) and outdoes its author with the exact same mechanics, pushed one notch too far. They woke up at 5 am? You woke up at 3:47.

- Agent Skills compatible tools: `npx skills add GregoryBabonaux/moi-aussi-mais-en-mieux`
- ChatGPT, Gemini, Le Chat, any LLM: use `dist/moi-aussi-mais-en-mieux.md` as system instructions.

Rules: parody the bragging, never the person; invented feats belong to you, not the author; real tragedies and sincere achievements are off limits.

## Avertissement

C'est de la satire. Si tu postes le commentaire généré, tu en assumes la paternité, y compris devant tes collègues.

## Licence

MIT
