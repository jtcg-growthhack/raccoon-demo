#!/usr/bin/env python3
"""demos.json から各社の全画面デモページと一覧ページを生成する。
使い方: python3 _tools/build.py   （demo-site/ 直下で実行）"""
import html, json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "_tools/template.html").read_text()
demos = json.loads((root / "_tools/demos.json").read_text())

for d in demos:
    page = (tpl.replace("{{NAME}}", html.escape(d["name"]))
               .replace("{{COLOR}}", d.get("color") or "#142572")
               .replace("{{SITE_KEY}}", d["site_key"]))
    out = root / d["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)

items = "\n".join(f'<li><a href="{d["slug"]}/">{html.escape(d["name"])} 向け</a></li>' for d in demos)
(root / "index.html").write_text(f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Raccoon AI デモ</title><link rel="icon" href="favicon.svg" type="image/svg+xml">
<style>body{{margin:0;padding:32px 16px;background:#fff;font-family:"Noto Sans JP",system-ui,sans-serif;color:#222}}a{{color:#142572}}li{{margin:6px 0}}</style></head>
<body><h1 style="font-size:20px">Raccoon AI デモ</h1><ul>
{items}
</ul></body></html>
""")
print(f"built {len(demos)} demo pages")
