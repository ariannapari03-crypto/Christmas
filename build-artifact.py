"""Genera artifact-claude.html (anteprima su claude.ai) da index.html (sito su GitHub Pages)."""
import re, pathlib
src = pathlib.Path("index.html").read_text(encoding="utf-8")
body = src.split("<!--APP-START-->", 1)[1].split("<!--APP-END-->", 1)[0]
body = re.sub(r"<!--FIREBASE-START-->.*?<!--FIREBASE-END-->\n", "", body, flags=re.S)
body = body.replace("</head>\n<body>\n", "")
pathlib.Path("artifact-claude.html").write_text(body.strip() + "\n", encoding="utf-8")
print("artifact-claude.html aggiornato")
