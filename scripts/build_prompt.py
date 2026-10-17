#!/usr/bin/env python3
"""Génère les versions "prompt unique" de la skill pour les LLM qui ne lisent pas le format Agent Skills.

Sorties :
  dist/moi-aussi-mais-en-mieux.md  : prompt complet (SKILL.md + annexes), à coller ou joindre
  dist/moi-aussi-mais-en-mieux.zip : skill zippée pour Claude.ai
  dist/gpt-instructions.txt         : instructions courtes pour un Custom GPT (limite 8000 caractères),
                                      le fichier complet étant joint en "Knowledge"

Usage : python3 scripts/build_prompt.py
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "moi-aussi-mais-en-mieux"
DIST = ROOT / "dist"

ANNEXES = [
    ("A", "surenchere.md", "Catalogue de surenchère"),
]


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S).lstrip()


def demote_headings(text: str) -> str:
    # "# Titre" -> "### Titre", etc., pour imbriquer les annexes sous "## Annexe"
    return re.sub(r"^(#+) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", text, flags=re.M)


def build_full() -> str:
    body = strip_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))
    body = body.replace(
        "Avant de commencer, lis `references/surenchere.md` (archétypes de posts et techniques de surenchère).",
        "Les archétypes de posts et les techniques de surenchère sont en annexe A.",
    )
    body = body.replace("`references/surenchere.md`", "l'annexe A")

    header = (
        "<!-- Fichier généré par scripts/build_prompt.py à partir de skills/moi-aussi-mais-en-mieux/. "
        "Ne pas modifier à la main. -->\n\n"
        "> Usage : colle ce texte comme instructions système (ChatGPT, Gemini Gem, Le Chat, Claude Project, "
        "API...) ou joins-le à la conversation.\n\n"
    )
    parts = [header, body.rstrip(), "\n"]
    for letter, filename, title in ANNEXES:
        content = strip_frontmatter((SKILL / "references" / filename).read_text(encoding="utf-8"))
        content = re.sub(r"\A# .*\n+", "", content)  # retire le titre H1 d'origine
        parts.append(f"\n## Annexe {letter} : {title}\n\n{demote_headings(content).rstrip()}\n")
    return "".join(parts)


GPT_INSTRUCTIONS = """Tu es "Moi aussi, mais en mieux", le collègue qui a toujours vécu la même chose que l'auteur d'un post, en plus fort.

Ta méthode complète est dans le fichier joint moi-aussi-mais-en-mieux.md. Avant chaque réponse, applique-la intégralement : vérification de la cible, mécanique de valorisation, surenchère en trois crans, limites, adaptation à la plateforme et format de sortie.

Règles qui priment sur tout :
- Tu parodies la mécanique de mise en valeur du post, jamais la personne. Pas de remarque sur son physique, son âge, son origine, sa santé, sa famille ou son employeur. Pas de nom de l'auteur dans la sortie.
- Les exploits inventés sont attribués à l'utilisateur (le "je"), jamais à l'auteur. Aucun fait plausible impliquant une vraie personne ou une vraie organisation.
- Hors périmètre : drames réels (deuil, maladie, burn-out, licenciement), réussites sincères et modestes, posts d'aide ou d'alerte.
- Premier degré apparent : pas de "lol", pas de "je plaisante".
- Slack et Teams : niveau subtil par défaut, l'auteur est un collègue.
- Réponds dans la langue du post. Pas de tiret cadratin.
"""


def main() -> None:
    DIST.mkdir(exist_ok=True)
    full = build_full()
    (DIST / "moi-aussi-mais-en-mieux.md").write_text(full, encoding="utf-8")
    (DIST / "gpt-instructions.txt").write_text(GPT_INSTRUCTIONS, encoding="utf-8")
    with zipfile.ZipFile(DIST / "moi-aussi-mais-en-mieux.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file():
                z.write(f, Path("moi-aussi-mais-en-mieux") / f.relative_to(SKILL))
    assert len(GPT_INSTRUCTIONS) < 8000, "Les instructions GPT dépassent 8000 caractères"
    print(f"dist/moi-aussi-mais-en-mieux.md : {len(full)} caractères")
    print(f"dist/gpt-instructions.txt        : {len(GPT_INSTRUCTIONS)} caractères")


if __name__ == "__main__":
    main()
