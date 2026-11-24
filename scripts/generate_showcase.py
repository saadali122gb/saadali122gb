from pathlib import Path

PROJECTS = [
    ("Agentex Platform", "RAG agents, guardrails & multi-user flow", "https://github.com/saadali122gb/agentix-platform", "#38bdf8"),
    ("MoveOn CRM", "Lead routing, BANT pipeline & RBAC", "https://github.com/saadali122gb/CRM", "#22c55e"),
    ("Taxi Dispatcher", "Socket.io matching, routing & JWT auth", "https://github.com/saadali122gb/Taxi-Dispatcher", "#f59e0b"),
    ("Hexa AI", "Gmail OAuth 2.0 & AI outreach automation", "https://github.com/saadali122gb/Hexa-AI", "#a855f7"),
    ("MoveOn Resumator", "ATS resume engine & Puppeteer PDFs", "https://github.com/saadali122gb/MoveOn", "#ec4899"),
    ("Cora AI Assistant", "Conversational AI & workflow automation", "https://github.com/saadali122gb/Cora-AI-Assisstant-By-MoveOn-AI", "#06b6d4"),
    ("Orion Dispatch", "Truck dispatch, fleet & load scheduling", "https://github.com/saadali122gb/Orion-Dispatch-Truck-Dispatch-", "#eab308"),
    ("Rawana Cargo", "Freight logistics & shipment tracking", "https://github.com/saadali122gb/Rawana-Cargo-For-Truck-Logistics-", "#10b981"),
    ("Data Saver", "Chrome lead extractor & tracking tool", "https://github.com/saadali122gb/Data-Saver-By-Moveon-AI", "#6366f1"),
    ("Connector", "API bridge, webhooks & data pipelines", "https://github.com/saadali122gb/Connector-by-moveon", "#f97316"),
    ("FixGhar", "Service marketplace & booking platform", "https://github.com/saadali122gb/Service-Provider-Company-Fix-Ghar-", "#14b8a6"),
    ("FixGuard Security", "Security ops & client management portal", "https://github.com/saadali122gb/Fixguard-Security-LTD", "#8b5cf6"),
    ("Healthcare Entry", "Medical records & structured data system", "https://github.com/saadali122gb/Health-Care-Data-Entry-Software", "#ef4444"),
    ("PC Antivirus", "System security & file scanner utility", "https://github.com/saadali122gb/Anti-Virus-Software-For-PC", "#84cc16"),
]

COLS = 2
CARD_W = 430
CARD_H = 112
GAP_X = 24
GAP_Y = 20
PAD_X = 16
PAD_Y = 18

rows = (len(PROJECTS) + COLS - 1) // COLS
total_w = PAD_X * 2 + COLS * CARD_W + (COLS - 1) * GAP_X
total_h = PAD_Y * 2 + rows * CARD_H + (rows - 1) * GAP_Y

blocks = []
for idx, (title, desc, url, accent) in enumerate(PROJECTS):
    r = idx // COLS
    c = idx % COLS
    x = PAD_X + c * (CARD_W + GAP_X)
    y = PAD_Y + r * (CARD_H + GAP_Y)
    delay = round(idx * 0.14, 2)

    blocks.append(f"""
  <a href="{url}" target="_blank">
    <g transform="translate({x}, {y})">
      <rect width="{CARD_W}" height="{CARD_H}" rx="14" fill="#0b0f17" stroke="#1e293b" stroke-width="1.5"/>
      <rect x="0" y="14" width="4" height="{CARD_H - 28}" rx="2" fill="{accent}">
        <animate attributeName="opacity" values="0.35;1;0.35" dur="2.8s" begin="{delay}s" repeatCount="indefinite"/>
      </rect>
      <circle cx="{CARD_W - 22}" cy="24" r="5" fill="{accent}">
        <animate attributeName="r" values="4;7;4" dur="2.2s" begin="{delay}s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.9;0.3;0.9" dur="2.2s" begin="{delay}s" repeatCount="indefinite"/>
      </circle>
      <text x="20" y="32" fill="#f8fafc" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="16" font-weight="700">{title}</text>
      <text x="20" y="60" fill="#94a3b8" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="12.5">{desc}</text>
      <text x="20" y="88" fill="{accent}" font-family="monospace" font-size="11.5">github.com/saadali122gb -></text>
    </g>
  </a>""")

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{total_h}" viewBox="0 0 {total_w} {total_h}">
  <defs>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#111827" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="{total_w}" height="{total_h}" rx="18" fill="#05070c"/>
  <rect width="{total_w}" height="{total_h}" rx="18" fill="url(#grid)" opacity="0.85"/>
  {"".join(blocks)}
</svg>
"""

out_dir = Path("assets")
out_dir.mkdir(exist_ok=True)
(out_dir / "projects-showcase.svg").write_text(svg, encoding="utf-8")
