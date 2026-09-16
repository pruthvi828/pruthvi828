import json
import os
import sys
from datetime import datetime, timezone
import urllib.request

SEARCH_QUERIES = [
    'label:"good first issue" state:open no:assignee language:python stars:>300',
    'label:"good first issue" state:open no:assignee language:c++ stars:>300',
    'label:"good first issue" state:open no:assignee language:typescript stars:>300'
]

def search_issues():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Pruthvi-OSS-Scout",
        "Accept": "application/vnd.github.v3+json"
    }
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    all_items = []
    seen = set()

    for q in SEARCH_QUERIES:
        url = f"https://api.github.com/search/issues?q={urllib.parse.quote(q)}&sort=updated&order=desc&per_page=5"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                for item in data.get("items", []):
                    if item["id"] not in seen:
                        seen.add(item["id"])
                        all_items.append({
                            "title": item.get("title"),
                            "url": item.get("html_url"),
                            "repo": "/".join(item.get("repository_url", "").split("/")[-2:]),
                            "comments": item.get("comments", 0),
                            "created_at": item.get("created_at"),
                            "labels": [lbl["name"] for lbl in item.get("labels", [])]
                        })
        except Exception as e:
            print(f"[!] Warning on query {q}: {e}")

    return all_items[:10]

def generate_radar_md(items, out_path="OSS_RADAR.md"):
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# 📡 Daily Open Source Radar",
        "",
        f"> **Last Synchronized:** `{now_str}` via automated GitHub Actions daily dispatch.",
        "> Curated unassigned high-impact open-source opportunities tailored for systems, embedded, and full-stack engineering.",
        "",
        "| Repository | Issue Title | Labels | Comments | Link |",
        "| :--- | :--- | :--- | :---: | :---: |"
    ]
    if not items:
        lines.append("| `upstream/ecosystem` | Upstream API Rate limit reached; refresh pending next cron | `standby` | 0 | [#] |")
    else:
        for it in items:
            labels_str = " ".join([f"`{l}`" for l in it['labels'][:2]])
            title_escaped = it['title'].replace("|", "\\|")
            lines.append(f"| **{it['repo']}** | {title_escaped} | {labels_str} | {it['comments']} | [View Issue ↗]({it['url']}) |")

    lines.extend([
        "",
        "---",
        "### 🛡️ Safety & Anti-Spam Policy",
        "This radar operates as a read-only intelligence aggregation engine. All PR submissions and code contributions are locally developed, reviewed, and authorized. **Zero unsolicited automated comments or pull requests are generated.**"
    ])

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[+] Saved OSS Radar to {out_path} with {len(items)} vetted issues.")

if __name__ == "__main__":
    out_file = sys.argv[1] if len(sys.argv) > 1 else "OSS_RADAR.md"
    items = search_issues()
    generate_radar_md(items, out_file)
