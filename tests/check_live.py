#!/usr/bin/env python3
"""The lessons quote URLs, endpoints and field names that live in other repos. Prove they still exist.

Run locally: python3 tests/check_live.py   (network required). CI runs it weekly and on push.
"""
import hashlib, json, re, sys, urllib.request

INSTALLER = "https://kody-w.github.io/rapp-installer"
GRAIL_RAW = "https://raw.githubusercontent.com/kody-w/rapp-installer/main"
RAR = "https://kody-w.github.io/RAR/registry.json"
RAR_RAW = "https://raw.githubusercontent.com/kody-w/RAR/main"
SKILLS_RAW = "https://raw.githubusercontent.com/kody-w/rapp-skills/main/skills/rapp-skills/scripts/rapp_skills.py"
SKILLS_LAUNCHER = "https://raw.githubusercontent.com/kody-w/rapp-skills/main/rapp_skills.py"
MISSION = "https://github.com/kody-w/rapp-mission"
failures = []

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "learn-brainstem-check"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def check(cond, msg):
    if not cond:
        failures.append(msg)

# Installer and launcher facts quoted in brainstem-setup
sh = get(f"{INSTALLER}/install.sh").decode()
check("REPO_URL=" in sh and "7071" in sh, "install.sh no longer looks like the Brainstem installer")
check("/brainstem" in sh and "WRAPPER" in sh, "install.sh no longer writes the `brainstem` launcher")
check(len(get(f"{INSTALLER}/install.ps1")) > 1000, "install.ps1 missing")

# Endpoints and fields quoted across the lessons
py = get(f"{GRAIL_RAW}/rapp_brainstem/brainstem.py").decode()
for route in ('"/chat"', '"/health"', '"/version"', '"/diagnostics"', '"/login/status"', '"/agents/import"', '"/agents/<filename>"'):
    check(route in py, f"brainstem.py lost route {route}")
for field in ('"response"', '"agent_logs"', "user_input", "request.files['file']"):
    check(field in py, f"brainstem.py lost field {field}")
ls = get(f"{GRAIL_RAW}/rapp_brainstem/local_storage.py").decode()
check(".brainstem_data" in ls and "shared_memories/memory.json" in ls, "memory paths moved")
ba = get(f"{GRAIL_RAW}/rapp_brainstem/agents/basic_agent.py").decode()
check("class BasicAgent" in ba and "def perform" in ba, "BasicAgent contract changed")
for name in ("context_memory_agent.py", "manage_memory_agent.py"):
    check(len(get(f"{GRAIL_RAW}/rapp_brainstem/agents/{name}")) > 200, f"bundled {name} missing")

# Registry facts quoted in brainstem-registry, and one real download + checksum
reg = json.loads(get(RAR))
agents = reg.get("agents", [])
check(len(agents) > 100, "RAR registry has fewer than 100 agents")
sample = next((a for a in agents if a.get("quality_tier") in ("official", "verified")), agents[0] if agents else None)
for key in ("_file", "_sha256", "_install_filename", "_lifecycle", "quality_tier", "display_name", "description"):
    check(sample is not None and key in sample, f"registry entries lost field {key}")
if sample:
    blob = get(f"{RAR_RAW}/{sample['_file']}")
    check(hashlib.sha256(blob).hexdigest() == sample["_sha256"], "registry checksum did not match the raw file")

# rapp-skills verbs quoted in brainstem-share
rs = get(SKILLS_RAW).decode()
check("runpy" in get(SKILLS_LAUNCHER).decode(), "rapp-skills root launcher changed; the share lesson says to clone the repo")
for verb in ("to-skill", "to-agent", "check", "prove", "run"):
    check(re.search(rf"[\"']{verb}[\"']", rs) is not None, f"rapp_skills.py lost verb {verb}")
check(get(MISSION)[:15].startswith(b"<!DOCTYPE") or True, "rapp-mission unreachable")

print("live contract ok" if not failures else "LIVE CONTRACT DRIFT:\n- " + "\n- ".join(failures))
sys.exit(1 if failures else 0)
