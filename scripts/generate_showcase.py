from pathlib import Path
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

PROJECTS = [
    {
        "id": "01",
        "name": "Agentex Platform",
        "repo": "agentix-platform",
        "url": "https://github.com/saadali122gb/agentix-platform",
        "tag": "RAG AGENTS • GUARDRAILS",
        "desc": "RAG agents, guardrails & multi-user flow",
        "accent": "#00f2fe",
        "accent2": "#4facfe",
        "dur": "3.2s",
        "delay": "0.0s",
        "col": 0,
        "row": 0,
        "spark": "M 0,8 Q 20,2 40,8 T 80,6"
    },
    {
        "id": "02",
        "name": "MoveOn CRM",
        "repo": "CRM",
        "url": "https://github.com/saadali122gb/CRM",
        "tag": "CRM PIPELINE • RBAC",
        "desc": "Lead routing, BANT pipeline & RBAC",
        "accent": "#10b981",
        "accent2": "#34d399",
        "dur": "3.7s",
        "delay": "0.4s",
        "col": 1,
        "row": 0,
        "spark": "M 0,9 Q 20,3 40,7 T 80,5"
    },
    {
        "id": "03",
        "name": "Taxi Dispatcher",
        "repo": "Taxi-Dispatcher",
        "url": "https://github.com/saadali122gb/Taxi-Dispatcher",
        "tag": "REAL-TIME • SOCKET.IO",
        "desc": "Socket.io matching, routing & JWT auth",
        "accent": "#f59e0b",
        "accent2": "#fbbf24",
        "dur": "3.4s",
        "delay": "0.8s",
        "col": 0,
        "row": 1,
        "spark": "M 0,6 Q 20,11 40,4 T 80,8"
    },
    {
        "id": "04",
        "name": "Hexa AI",
        "repo": "Hexa-AI",
        "url": "https://github.com/saadali122gb/Hexa-AI",
        "tag": "OAUTH 2.0 • AI OUTREACH",
        "desc": "Gmail OAuth 2.0 & AI outreach automation",
        "accent": "#a855f7",
        "accent2": "#c084fc",
        "dur": "3.9s",
        "delay": "1.2s",
        "col": 1,
        "row": 1,
        "spark": "M 0,8 Q 20,3 40,9 T 80,6"
    },
    {
        "id": "05",
        "name": "MoveOn Resumator",
        "repo": "MoveOn",
        "url": "https://github.com/saadali122gb/MoveOn",
        "tag": "ATS ENGINE • PUPPETEER",
        "desc": "ATS resume engine & Puppeteer PDFs",
        "accent": "#f43f5e",
        "accent2": "#fb7185",
        "dur": "3.3s",
        "delay": "1.6s",
        "col": 0,
        "row": 2,
        "spark": "M 0,5 Q 20,11 40,4 T 80,7"
    },
    {
        "id": "06",
        "name": "Cora AI Assistant",
        "repo": "Cora-AI-Assisstant-By-MoveOn-AI",
        "url": "https://github.com/saadali122gb/Cora-AI-Assisstant-By-MoveOn-AI",
        "tag": "CONVERSATIONAL AI",
        "desc": "Conversational AI & workflow automation",
        "accent": "#0ea5e9",
        "accent2": "#38bdf8",
        "dur": "3.8s",
        "delay": "2.0s",
        "col": 1,
        "row": 2,
        "spark": "M 0,9 Q 20,4 40,8 T 80,5"
    },
    {
        "id": "07",
        "name": "Orion Dispatch",
        "repo": "Orion-Dispatch-Truck-Dispatch-",
        "url": "https://github.com/saadali122gb/Orion-Dispatch-Truck-Dispatch-",
        "tag": "FLEET OPS • DISPATCH",
        "desc": "Truck dispatch, fleet & load scheduling",
        "accent": "#f97316",
        "accent2": "#fb923c",
        "dur": "3.5s",
        "delay": "0.3s",
        "col": 0,
        "row": 3,
        "spark": "M 0,7 Q 20,2 40,9 T 80,6"
    },
    {
        "id": "08",
        "name": "Rawana Cargo",
        "repo": "Rawana-Cargo-For-Truck-Logistics-",
        "url": "https://github.com/saadali122gb/Rawana-Cargo-For-Truck-Logistics-",
        "tag": "FREIGHT LOGISTICS • GPS",
        "desc": "Freight logistics & shipment tracking",
        "accent": "#84cc16",
        "accent2": "#a3e635",
        "dur": "4.1s",
        "delay": "0.7s",
        "col": 1,
        "row": 3,
        "spark": "M 0,9 Q 20,3 40,8 T 80,6"
    },
    {
        "id": "09",
        "name": "Data Saver",
        "repo": "Data-Saver-By-Moveon-AI",
        "url": "https://github.com/saadali122gb/Data-Saver-By-Moveon-AI",
        "tag": "CHROME EXTENSION",
        "desc": "Chrome lead extractor & tracking tool",
        "accent": "#6366f1",
        "accent2": "#818cf8",
        "dur": "3.2s",
        "delay": "1.1s",
        "col": 0,
        "row": 4,
        "spark": "M 0,6 Q 20,10 40,4 T 80,7"
    },
    {
        "id": "10",
        "name": "Connector",
        "repo": "Connector-by-moveon",
        "url": "https://github.com/saadali122gb/Connector-by-moveon",
        "tag": "WEBHOOKS • API PIPELINES",
        "desc": "API bridge, webhooks & data pipelines",
        "accent": "#d946ef",
        "accent2": "#e879f9",
        "dur": "3.6s",
        "delay": "1.5s",
        "col": 1,
        "row": 4,
        "spark": "M 0,8 Q 20,3 40,9 T 80,5"
    },
    {
        "id": "11",
        "name": "FixGhar",
        "repo": "Service-Provider-Company-Fix-Ghar-",
        "url": "https://github.com/saadali122gb/Service-Provider-Company-Fix-Ghar-",
        "tag": "SERVICE MARKETPLACE",
        "desc": "Service marketplace & booking platform",
        "accent": "#14b8a6",
        "accent2": "#2dd4bf",
        "dur": "3.4s",
        "delay": "0.5s",
        "col": 0,
        "row": 5,
        "spark": "M 0,7 Q 20,11 40,4 T 80,8"
    },
    {
        "id": "12",
        "name": "FixGuard Security",
        "repo": "Fixguard-Security-LTD",
        "url": "https://github.com/saadali122gb/Fixguard-Security-LTD",
        "tag": "SECURITY OPS PORTAL",
        "desc": "Security ops & client management portal",
        "accent": "#ef4444",
        "accent2": "#f87171",
        "dur": "3.9s",
        "delay": "0.9s",
        "col": 1,
        "row": 5,
        "spark": "M 0,8 Q 20,3 40,9 T 80,6"
    },
    {
        "id": "13",
        "name": "Healthcare Entry",
        "repo": "Health-Care-Data-Entry-Software",
        "url": "https://github.com/saadali122gb/Health-Care-Data-Entry-Software",
        "tag": "CLINICAL RECORDS • EHR",
        "desc": "Medical records & structured data system",
        "accent": "#06b6d4",
        "accent2": "#22d3ee",
        "dur": "3.7s",
        "delay": "1.3s",
        "col": 0,
        "row": 6,
        "spark": "M 0,6 Q 20,10 40,3 T 80,7"
    },
    {
        "id": "14",
        "name": "PC Antivirus",
        "repo": "Anti-Virus-Software-For-PC",
        "url": "https://github.com/saadali122gb/Anti-Virus-Software-For-PC",
        "tag": "SYSTEM SECURITY",
        "desc": "System security & file scanner utility",
        "accent": "#3b82f6",
        "accent2": "#60a5fa",
        "dur": "3.3s",
        "delay": "1.7s",
        "col": 1,
        "row": 6,
        "spark": "M 0,9 Q 20,4 40,8 T 80,6"
    }
]

svg_width = 960
card_w = 436
card_h = 130
start_x = [34, 490]
start_y = 232
row_gap = 16
svg_height = start_y + (7 * card_h) + (6 * row_gap) + 64

defs = []

defs.append('''
  <!-- Clip Path for wave chart: strictly confines drawing inside chart box -->
  <clipPath id="chartClip">
    <rect x="0" y="0" width="454" height="114" rx="4"/>
  </clipPath>
''')

defs.append('''
  <!-- Transparent Background Pattern -->
  <pattern id="techGrid" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#1e293b" stroke-width="0.75" opacity="0.35"/>
    <circle cx="24" cy="24" r="0.75" fill="#334155" opacity="0.4"/>
  </pattern>
''')

defs.append('''
  <!-- Ambient Glows with transparent fades -->
  <radialGradient id="topGlow" cx="50%" cy="0%" r="50%">
    <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.12"/>
    <stop offset="45%" stop-color="#6366f1" stop-opacity="0.04"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
  </radialGradient>
''')

defs.append('''
  <!-- Chart Gradients -->
  <linearGradient id="waveFillGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.28"/>
    <stop offset="70%" stop-color="#00f2fe" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#00f2fe" stop-opacity="0"/>
  </linearGradient>

  <linearGradient id="waveStrokeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#38bdf8"/>
    <stop offset="30%" stop-color="#00f2fe"/>
    <stop offset="65%" stop-color="#818cf8"/>
    <stop offset="100%" stop-color="#38bdf8"/>
  </linearGradient>

  <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
    <stop offset="30%" stop-color="#00f2fe" stop-opacity="0.35"/>
    <stop offset="50%" stop-color="#a855f7" stop-opacity="0.8"/>
    <stop offset="70%" stop-color="#00f2fe" stop-opacity="0.35"/>
    <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
  </linearGradient>

  <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#0e1726" stop-opacity="0.85"/>
    <stop offset="100%" stop-color="#080d17" stop-opacity="0.85"/>
  </linearGradient>
''')

for p in PROJECTS:
    defs.append(f'''
  <linearGradient id="cardGrad_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#0b1120" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#070b14" stop-opacity="0.85"/>
  </linearGradient>
  <linearGradient id="beamGrad_{p['id']}" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{p['accent']}" stop-opacity="0"/>
    <stop offset="50%" stop-color="{p['accent2']}" stop-opacity="1"/>
    <stop offset="100%" stop-color="{p['accent']}" stop-opacity="0"/>
  </linearGradient>
''')

defs_content = "\n".join(defs)

styles = '''
  <style>
    .font-sans {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, "Helvetica Neue", sans-serif;
    }
    .font-mono {
      font-family: "JetBrains Mono", "SF Mono", Consolas, "Fira Code", monospace;
    }
    .card-item {
      cursor: pointer;
    }
    .card-box {
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .card-item:hover .card-box {
      stroke: #00f2fe !important;
      stroke-width: 1.5px !important;
      fill-opacity: 0.95 !important;
      filter: drop-shadow(0 8px 24px rgba(0, 0, 0, 0.6));
    }
    .card-item:hover .card-title {
      fill: #ffffff !important;
    }
    .card-item:hover .action-btn {
      fill: #1e293b !important;
      stroke-opacity: 0.9 !important;
    }
  </style>
'''

# 1. GRAPHICAL DASHBOARD SECTION (CONTRIBUTION CURVE + METRIC GAUGES)
graphical_section_svg = '''
  <!-- SECTION A: CONTRIBUTION & ACTIVITY WAVEFORM (GRAPHICAL CHART) -->
  <g transform="translate(34, 20)">
    <!-- Container Card (Transparent glass) -->
    <rect x="0" y="0" width="490" height="172" rx="12" fill="#080c16" fill-opacity="0.8" stroke="#1a273f" stroke-width="1"/>
    
    <!-- Header -->
    <g transform="translate(18, 22)">
      <circle cx="0" cy="0" r="3" fill="#00f2fe"/>
      <text x="10" y="3.5" class="font-mono" font-size="10.5" font-weight="700" fill="#f8fafc" letter-spacing="1">
        CONTRIBUTION &amp; DISPATCH VELOCITY
      </text>
      <text x="450" y="3.5" text-anchor="end" class="font-mono" font-size="9" fill="#38bdf8">
        PEAK: 38 COMMITS/DAY
      </text>
    </g>

    <!-- Chart Drawing Area (Strictly Clipped with #chartClip) -->
    <g transform="translate(18, 38)" clip-path="url(#chartClip)">
      <!-- Grid Lines (Subtle) -->
      <g opacity="0.35">
        <line x1="0" y1="20" x2="454" y2="20" stroke="#1e293b" stroke-dasharray="2 3"/>
        <line x1="0" y1="45" x2="454" y2="45" stroke="#1e293b" stroke-dasharray="2 3"/>
        <line x1="0" y1="68" x2="454" y2="68" stroke="#1e293b" stroke-dasharray="2 3"/>
        <line x1="0" y1="90" x2="454" y2="90" stroke="#1e293b"/>
      </g>

      <!-- Underneath Gradient Fill (Bounded cubic bezier) -->
      <path d="M 0,90 L 0,80 C 15,80 30,45 45,45 C 60,45 75,75 90,75 C 105,75 120,35 135,35 C 150,35 165,70 180,70 C 195,70 215,20 230,20 C 245,20 265,65 280,65 C 295,65 315,30 330,30 C 345,30 365,72 380,72 C 405,72 430,55 454,55 L 454,90 Z" 
            fill="url(#waveFillGrad)"/>
      
      <!-- Main Glowing Wave Stroke -->
      <path d="M 0,80 C 15,80 30,45 45,45 C 60,45 75,75 90,75 C 105,75 120,35 135,35 C 150,35 165,70 180,70 C 195,70 215,20 230,20 C 245,20 265,65 280,65 C 295,65 315,30 330,30 C 345,30 365,72 380,72 C 405,72 430,55 454,55" 
            fill="none" stroke="url(#waveStrokeGrad)" stroke-width="2.6" stroke-linecap="round"/>

      <!-- Glowing Data Nodes at Wave Peaks (Strictly bounded) -->
      <circle cx="45" cy="45" r="3" fill="#f8fafc" stroke="#00f2fe" stroke-width="1.8"/>
      <circle cx="135" cy="35" r="3" fill="#f8fafc" stroke="#00f2fe" stroke-width="1.8"/>

      <!-- Node 3 (Highest Peak at 230,20) -->
      <circle cx="230" cy="20" r="3.8" fill="#f8fafc" stroke="#00f2fe" stroke-width="2.2"/>
      <circle cx="230" cy="20" r="7.5" fill="#00f2fe" opacity="0.35">
        <animate attributeName="r" values="4;9;4" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.5;0;0.5" dur="2s" repeatCount="indefinite"/>
      </circle>

      <circle cx="330" cy="30" r="3" fill="#f8fafc" stroke="#818cf8" stroke-width="1.8"/>
      <circle cx="90" cy="75" r="2.2" fill="#38bdf8"/>
      <circle cx="180" cy="70" r="2.2" fill="#00f2fe"/>
      <circle cx="280" cy="65" r="2.2" fill="#818cf8"/>
      <circle cx="380" cy="72" r="2.2" fill="#38bdf8"/>
      <circle cx="454" cy="55" r="2.5" fill="#00f2fe"/>
    </g>

    <!-- Timeline Days below curve -->
    <g transform="translate(18, 148)" class="font-mono" font-size="8.5" fill="#64748b">
      <text x="0" y="0">DAY 01</text>
      <text x="80" y="0">DAY 07</text>
      <text x="160" y="0">DAY 14</text>
      <text x="230" y="0">DAY 21 (PEAK)</text>
      <text x="320" y="0">DAY 28</text>
      <text x="454" y="0" text-anchor="end">CURRENT</text>
    </g>
  </g>

  <!-- SECTION B: PERFORMANCE METRIC GAUGES & LANGUAGE DISTRIBUTION -->
  <g transform="translate(538, 20)">
    <rect x="0" y="0" width="388" height="172" rx="12" fill="#080c16" fill-opacity="0.8" stroke="#1a273f" stroke-width="1"/>
    
    <!-- Title -->
    <g transform="translate(18, 22)">
      <circle cx="0" cy="0" r="3" fill="#10b981"/>
      <text x="10" y="3.5" class="font-mono" font-size="10.5" font-weight="700" fill="#f8fafc" letter-spacing="1">
        ENGINEERING QUALITY &amp; AUDIT GAUGES
      </text>
    </g>

    <!-- 4 Circular Score Gauges -->
    <g transform="translate(16, 42)">
      <!-- Gauge 1: Performance -->
      <g transform="translate(36, 26)">
        <circle cx="0" cy="0" r="22" fill="none" stroke="#162238" stroke-width="3.5"/>
        <circle cx="0" cy="0" r="22" fill="none" stroke="#00f2fe" stroke-width="3.5"
                stroke-dasharray="138.2" stroke-dashoffset="4.1" stroke-linecap="round" transform="rotate(-90)"/>
        <text x="0" y="4" text-anchor="middle" class="font-mono" font-size="11.5" font-weight="800" fill="#f8fafc">97</text>
        <text x="0" y="36" text-anchor="middle" class="font-sans" font-size="8.5" font-weight="600" fill="#94a3b8">Performance</text>
      </g>

      <!-- Gauge 2: Security/RBAC -->
      <g transform="translate(126, 26)">
        <circle cx="0" cy="0" r="22" fill="none" stroke="#162238" stroke-width="3.5"/>
        <circle cx="0" cy="0" r="22" fill="none" stroke="#10b981" stroke-width="3.5"
                stroke-dasharray="138.2" stroke-dashoffset="0" stroke-linecap="round" transform="rotate(-90)"/>
        <text x="0" y="4" text-anchor="middle" class="font-mono" font-size="11.5" font-weight="800" fill="#f8fafc">100</text>
        <text x="0" y="36" text-anchor="middle" class="font-sans" font-size="8.5" font-weight="600" fill="#94a3b8">Security/RBAC</text>
      </g>

      <!-- Gauge 3: Architecture -->
      <g transform="translate(216, 26)">
        <circle cx="0" cy="0" r="22" fill="none" stroke="#162238" stroke-width="3.5"/>
        <circle cx="0" cy="0" r="22" fill="none" stroke="#a855f7" stroke-width="3.5"
                stroke-dasharray="138.2" stroke-dashoffset="2.7" stroke-linecap="round" transform="rotate(-90)"/>
        <text x="0" y="4" text-anchor="middle" class="font-mono" font-size="11.5" font-weight="800" fill="#f8fafc">98</text>
        <text x="0" y="36" text-anchor="middle" class="font-sans" font-size="8.5" font-weight="600" fill="#94a3b8">Architecture</text>
      </g>

      <!-- Gauge 4: Real-Time Sockets -->
      <g transform="translate(306, 26)">
        <circle cx="0" cy="0" r="22" fill="none" stroke="#162238" stroke-width="3.5"/>
        <circle cx="0" cy="0" r="22" fill="none" stroke="#f59e0b" stroke-width="3.5"
                stroke-dasharray="138.2" stroke-dashoffset="0" stroke-linecap="round" transform="rotate(-90)"/>
        <text x="0" y="4" text-anchor="middle" class="font-mono" font-size="11.5" font-weight="800" fill="#f8fafc">100</text>
        <text x="0" y="36" text-anchor="middle" class="font-sans" font-size="8.5" font-weight="600" fill="#94a3b8">Real-Time Sync</text>
      </g>
    </g>

    <!-- Language & Stack Distribution Bar -->
    <g transform="translate(18, 126)">
      <text x="0" y="-4" class="font-mono" font-size="8.5" font-weight="700" fill="#64748b" letter-spacing="0.5">
        STACK DISTRIBUTION
      </text>
      <rect x="0" y="4" width="352" height="7" rx="3.5" fill="#1e293b"/>
      <rect x="0" y="4" width="134" height="7" rx="3.5" fill="#38bdf8"/>
      <rect x="136" y="4" width="98" height="7" rx="2" fill="#00f2fe"/>
      <rect x="236" y="4" width="76" height="7" rx="2" fill="#a855f7"/>
      <rect x="314" y="4" width="38" height="7" rx="2" fill="#10b981"/>

      <g transform="translate(0, 24)" class="font-mono" font-size="8" fill="#94a3b8">
        <circle cx="4" cy="-3" r="3" fill="#38bdf8"/><text x="11" y="0">TypeScript 38%</text>
        <circle cx="100" cy="-3" r="3" fill="#00f2fe"/><text x="107" y="0">Python 28%</text>
        <circle cx="190" cy="-3" r="3" fill="#a855f7"/><text x="197" y="0">.NET 22%</text>
        <circle cx="270" cy="-3" r="3" fill="#10b981"/><text x="277" y="0">GIS/SQL 12%</text>
      </g>
    </g>
  </g>
'''

# 2. SECTION DIVIDER
divider_svg = '''
  <!-- SECTION DIVIDER WITH MOVING LIGHT PULSE -->
  <g transform="translate(34, 210)">
    <line x1="0" y1="0" x2="892" y2="0" stroke="#162238" stroke-width="1"/>
    <!-- Animated Light Runner on Divider -->
    <rect x="0" y="-1" width="160" height="2" fill="url(#scanlineGrad)">
      <animate attributeName="x" values="0;732;0" dur="5.5s" repeatCount="indefinite"/>
    </rect>
    <text x="0" y="-8" class="font-mono" font-size="9" font-weight="700" fill="#475569" letter-spacing="1.5">
      FEATURED PRODUCTION ARCHITECTURES // 14 DEPLOYMENTS
    </text>
    <text x="892" y="-8" text-anchor="end" class="font-mono" font-size="9" font-weight="600" fill="#00f2fe" letter-spacing="0.8">
      ACTIVE CODEBASES ↗
    </text>
  </g>
'''

# 3. ENHANCED 14 PROJECT CARDS
cards_svg = []
for p in PROJECTS:
    cx = start_x[p['col']]
    cy = start_y + (p['row'] * (card_h + row_gap))
    accent = p['accent']
    accent2 = p['accent2']
    cid = p['id']
    dur = p['dur']
    delay = p['delay']

    card_str = f'''
  <!-- CARD {cid}: {p['name']} -->
  <g transform="translate({cx}, {cy})" class="card-item">
    <a xlink:href="{p['url']}" href="{p['url']}" target="_blank" rel="noopener noreferrer">
      <!-- Card Base Box (Semi-transparent glass) -->
      <rect class="card-box" x="0" y="0" width="{card_w}" height="{card_h}" rx="10" 
            fill="url(#cardGrad_{cid})" stroke="#172236" stroke-width="1"/>

      <!-- Ambient Glow on card top -->
      <rect x="1" y="1" width="{card_w - 2}" height="32" rx="9" fill="{accent}" opacity="0.04"/>

      <!-- Top Border Accent Track -->
      <rect x="0" y="0" width="{card_w}" height="2" rx="1" fill="{accent}" opacity="0.22"/>

      <!-- Top Kinetic Light Runner (SMIL Animated) -->
      <rect x="0" y="0" width="90" height="2" fill="url(#beamGrad_{cid})" opacity="0.95">
        <animate attributeName="x" values="0;{card_w - 90};0" dur="{dur}" begin="{delay}" repeatCount="indefinite"/>
      </rect>

      <!-- Cyber Corner Brackets -->
      <path d="M 6,14 L 6,6 L 14,6" fill="none" stroke="{accent}" stroke-width="1.2" opacity="0.6"/>
      <path d="M {card_w - 6},{card_h - 14} L {card_w - 6},{card_h - 6} L {card_w - 14},{card_h - 6}" 
            fill="none" stroke="{accent}" stroke-width="1.2" opacity="0.6"/>

      <!-- Left Vertical Indicator Tab -->
      <rect x="0" y="18" width="3" height="26" rx="1.5" fill="{accent}"/>

      <!-- CARD HEADER: Index, Title & Live Telemetry Equalizer -->
      <g transform="translate(18, 24)">
        <!-- Index Number -->
        <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" fill="{accent}" opacity="0.9">
          [{cid}]
        </text>
        <!-- Project Title -->
        <text class="card-title font-sans" x="32" y="0.5" font-size="15.5" font-weight="700" fill="#f8fafc">
          {escape(p['name'])}
        </text>

        <!-- Mini Live Activity Equalizer (Graphical Bars) -->
        <g transform="translate(352, -10)">
          <rect x="0" y="0" width="2.5" height="12" rx="1" fill="{accent}" opacity="0.75">
            <animate attributeName="height" values="6;14;6" dur="1.6s" begin="{delay}" repeatCount="indefinite"/>
            <animate attributeName="y" values="3;0;3" dur="1.6s" begin="{delay}" repeatCount="indefinite"/>
          </rect>
          <rect x="5" y="0" width="2.5" height="14" rx="1" fill="{accent}" opacity="0.95">
            <animate attributeName="height" values="14;5;14" dur="1.9s" begin="{delay}" repeatCount="indefinite"/>
            <animate attributeName="y" values="0;4;0" dur="1.9s" begin="{delay}" repeatCount="indefinite"/>
          </rect>
          <rect x="10" y="0" width="2.5" height="9" rx="1" fill="{accent}" opacity="0.8">
            <animate attributeName="height" values="4;13;4" dur="1.4s" begin="{delay}" repeatCount="indefinite"/>
            <animate attributeName="y" values="5;0;5" dur="1.4s" begin="{delay}" repeatCount="indefinite"/>
          </rect>
          <!-- Pulse Dot -->
          <circle cx="24" cy="7" r="3.5" fill="{accent}"/>
          <circle cx="24" cy="7" r="3.5" fill="{accent}" opacity="0.6">
            <animate attributeName="r" values="3.5;8;3.5" dur="{dur}" begin="{delay}" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.7;0;0.7" dur="{dur}" begin="{delay}" repeatCount="indefinite"/>
          </circle>
        </g>
      </g>

      <!-- CATEGORY / TAG BADGE & MINI SPARKLINE -->
      <g transform="translate(18, 43)">
        <rect x="0" y="0" width="{len(p['tag']) * 6.7 + 14}" height="19" rx="4.5" 
              fill="{accent}" fill-opacity="0.1" stroke="{accent}" stroke-opacity="0.3" stroke-width="0.8"/>
        <text x="7" y="13" class="font-mono" font-size="9" font-weight="700" fill="{accent}" letter-spacing="0.6">
          {escape(p['tag'])}
        </text>

        <!-- Mini Telemetry Sparkline Curve (Bounded) -->
        <g transform="translate({card_w - 146}, 4)" opacity="0.55">
          <path d="{p['spark']}" fill="none" stroke="{accent}" stroke-width="1.4" stroke-linecap="round"/>
        </g>
      </g>

      <!-- DESCRIPTION -->
      <text x="18" y="87" class="font-sans" font-size="12.2" font-weight="400" fill="#94a3b8">
        {escape(p['desc'])}
      </text>

      <!-- FOOTER ROW: Repo Path & Action Link -->
      <g transform="translate(18, 114)">
        <!-- Repo Path Snippet -->
        <text x="0" y="0" class="font-mono" font-size="10" fill="#475569">
          saadali122gb/{p['repo'][:22]}
        </text>

        <!-- Action Pill (Right) -->
        <g transform="translate(300, -13)">
          <rect class="action-btn" x="0" y="0" width="100" height="21" rx="5" 
                fill="#0d1424" stroke="{accent}" stroke-opacity="0.4" stroke-width="0.8"/>
          <text x="50" y="14" text-anchor="middle" class="font-sans" font-size="10" font-weight="600" fill="#e2e8f0">
            LAUNCH REPO ↗
          </text>
        </g>
      </g>
    </a>
  </g>
'''
    cards_svg.append(card_str)

cards_content = "\n".join(cards_svg)

# 4. FOOTER BAR
footer_y = svg_height - 52
footer_svg = f'''
  <!-- FOOTER STATUS CONSOLE (Transparent) -->
  <g transform="translate(34, {footer_y})">
    <rect x="0" y="0" width="892" height="36" rx="8" fill="#080c16" fill-opacity="0.8" stroke="#162238" stroke-width="1"/>
    
    <!-- Status Terminal Dot -->
    <circle cx="18" cy="18" r="4" fill="#10b981"/>
    <circle cx="18" cy="18" r="4" fill="#10b981" opacity="0.5">
      <animate attributeName="r" values="4;8;4" dur="2.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    
    <text x="32" y="22" class="font-mono" font-size="9.5" font-weight="700" fill="#64748b">
      SYSTEM MATRIX ONLINE <tspan fill="#334155">//</tspan> 14 PRODUCTION ARCHITECTURES VERIFIED
    </text>

    <!-- Center Architecture Tags -->
    <text x="446" y="22" text-anchor="middle" class="font-mono" font-size="9" fill="#475569">
      MERN • .NET CORE • FASTAPI • DOCKER • REAL-TIME SOCKETS • SPATIAL GIS
    </text>

    <!-- Right Profile Link -->
    <a xlink:href="https://github.com/saadali122gb" href="https://github.com/saadali122gb" target="_blank" rel="noopener noreferrer">
      <text x="874" y="22" text-anchor="end" class="font-mono" font-size="9.5" font-weight="700" fill="#00f2fe">
        @saadali122gb ↗
      </text>
    </a>
  </g>
'''

scanline_svg = f'''
  <!-- Subtle Ambient Scanline traversing vertically -->
  <line x1="0" y1="0" x2="960" y2="0" stroke="url(#scanlineGrad)" stroke-width="1.2" opacity="0.16" pointer-events="none">
    <animate attributeName="y1" values="0;{svg_height};0" dur="10s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="0;{svg_height};0" dur="10s" repeatCount="indefinite"/>
  </line>
'''

# ENTIRE SVG WITH FULLY TRANSPARENT BACKGROUND
full_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
     viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%"
     style="background: transparent; text-rendering: geometricPrecision; shape-rendering: geometricPrecision;">
  <defs>
{defs_content}
  </defs>

{styles}

  <!-- TRANSPARENT GRID PATTERN OVERLAY -->
  <rect width="{svg_width}" height="{svg_height}" fill="url(#techGrid)" pointer-events="none"/>

  <!-- AMBIENT LIGHTING OVERLAYS -->
  <rect width="{svg_width}" height="500" fill="url(#topGlow)" pointer-events="none"/>

{scanline_svg}

{graphical_section_svg}

{divider_svg}

{cards_content}

{footer_svg}
</svg>'''

# Save to destination
out_dir = Path("assets")
out_dir.mkdir(exist_ok=True)
svg_file = out_dir / "projects-showcase.svg"
svg_file.write_text(full_svg, encoding="utf-8")

# Validate XML
ET.fromstring(full_svg)
print(f"Generated and validated {svg_file} successfully! (Dimensions: {svg_width}x{svg_height})")
