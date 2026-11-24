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
        "row": 0
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
        "row": 0
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
        "row": 1
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
        "row": 1
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
        "row": 2
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
        "row": 2
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
        "row": 3
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
        "row": 3
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
        "row": 4
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
        "row": 4
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
        "row": 5
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
        "row": 5
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
        "row": 6
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
        "row": 6
    }
]

svg_width = 960
svg_height = 1320
card_w = 436
card_h = 126
start_x = [34, 490]
start_y = 246
row_gap = 16

# Build Gradients & Defs
defs = []

defs.append('''
  <!-- Background Pattern -->
  <pattern id="techGrid" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#121a2d" stroke-width="0.7" opacity="0.65"/>
    <circle cx="24" cy="24" r="0.75" fill="#1e293b" opacity="0.8"/>
  </pattern>
''')

defs.append('''
  <!-- Radial Lighting Glows -->
  <radialGradient id="topAura" cx="50%" cy="0%" r="55%">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.16"/>
    <stop offset="40%" stop-color="#6366f1" stop-opacity="0.06"/>
    <stop offset="100%" stop-color="#05070c" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="sideAura" cx="90%" cy="50%" r="45%">
    <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#05070c" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="bottomAura" cx="10%" cy="95%" r="40%">
    <stop offset="0%" stop-color="#a855f7" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#05070c" stop-opacity="0"/>
  </radialGradient>
''')

defs.append('''
  <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
    <stop offset="25%" stop-color="#38bdf8" stop-opacity="0.3"/>
    <stop offset="50%" stop-color="#818cf8" stop-opacity="0.85"/>
    <stop offset="75%" stop-color="#38bdf8" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
  </linearGradient>
  
  <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="70%" stop-color="#e2e8f0"/>
    <stop offset="100%" stop-color="#94a3b8"/>
  </linearGradient>

  <linearGradient id="dividerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#1e293b" stop-opacity="0.2"/>
    <stop offset="15%" stop-color="#38bdf8" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#818cf8" stop-opacity="0.4"/>
    <stop offset="85%" stop-color="#38bdf8" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#1e293b" stop-opacity="0.2"/>
  </linearGradient>

  <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#131c2e" stop-opacity="0.95"/>
    <stop offset="100%" stop-color="#0a101d" stop-opacity="0.95"/>
  </linearGradient>
''')

for p in PROJECTS:
    defs.append(f'''
  <linearGradient id="cardGrad_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#0d1424" stop-opacity="0.92"/>
    <stop offset="100%" stop-color="#070a12" stop-opacity="0.96"/>
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
    @keyframes pulseAura {
      0%, 100% { opacity: 0.8; }
      50% { opacity: 0.4; }
    }
    @keyframes sweepGlow {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(200%); }
    }
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
      stroke: #38bdf8 !important;
      stroke-width: 1.5px !important;
      fill: #0f182c !important;
      filter: drop-shadow(0 6px 20px rgba(0, 0, 0, 0.6));
    }
    .card-item:hover .card-title {
      fill: #ffffff !important;
    }
    .card-item:hover .action-btn {
      fill: #1e293b !important;
      stroke-opacity: 0.9 !important;
    }
    .social-btn {
      transition: all 0.25s ease;
      cursor: pointer;
    }
    .social-btn:hover rect {
      fill: #1a253c !important;
      stroke: #38bdf8 !important;
    }
    .social-btn:hover text {
      fill: #38bdf8 !important;
    }
  </style>
'''

header_svg = '''
  <!-- TOP STATUS PILL -->
  <g transform="translate(34, 28)">
    <rect x="0" y="0" width="310" height="26" rx="13" fill="#0c1220" stroke="#1f2c47" stroke-width="1"/>
    <!-- Animated Status Dot -->
    <circle cx="16" cy="13" r="3.5" fill="#10b981"/>
    <circle cx="16" cy="13" r="3.5" fill="#10b981" opacity="0.6">
      <animate attributeName="r" values="3.5;8;3.5" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0.7" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="28" y="17" class="font-mono" font-size="9.5" font-weight="600" fill="#94a3b8" letter-spacing="1">
      FULL-STACK &amp; AI SYSTEMS PORTFOLIO
    </text>
  </g>

  <!-- LIVE TIME/NODE BADGE (RIGHT) -->
  <g transform="translate(712, 28)">
    <rect x="0" y="0" width="214" height="26" rx="13" fill="#0c1220" stroke="#1f2c47" stroke-width="1"/>
    <circle cx="14" cy="13" r="3" fill="#38bdf8"/>
    <text x="24" y="17" class="font-mono" font-size="9.5" font-weight="500" fill="#64748b" letter-spacing="0.5">
      NODE: GCUL // 14 SERVICES
    </text>
  </g>

  <!-- MAIN NAME & TITLES -->
  <g transform="translate(34, 82)">
    <text x="0" y="0" class="font-sans" font-size="33" font-weight="800" fill="url(#titleGrad)" letter-spacing="-0.6">
      Rana Saad Ali Khan
    </text>
    
    <!-- Subtitle -->
    <text x="0" y="27" class="font-sans" font-size="14.5" font-weight="500" fill="#94a3b8">
      Full-Stack Software Developer <tspan fill="#38bdf8">•</tspan> MERN <tspan fill="#38bdf8">•</tspan> .NET <tspan fill="#38bdf8">•</tspan> Python <tspan fill="#38bdf8">•</tspan> AI Agents <tspan fill="#38bdf8">•</tspan> Real-Time Systems
    </text>
    
    <!-- Academic & Specialization Badges -->
    <g transform="translate(0, 42)">
      <!-- Degree Badge -->
      <rect x="0" y="0" width="260" height="24" rx="6" fill="#0d1527" stroke="#1e2c4a" stroke-width="1"/>
      <text x="10" y="16" class="font-mono" font-size="10" font-weight="600" fill="#38bdf8">
        🎓 B.S. Remote Sensing &amp; GIS @ GCUL
      </text>

      <!-- Focus Badge -->
      <rect x="270" y="0" width="254" height="24" rx="6" fill="#0d1527" stroke="#1e2c4a" stroke-width="1"/>
      <text x="280" y="16" class="font-mono" font-size="10" font-weight="600" fill="#a855f7">
        ⚡ Production RAG &amp; Real-Time Pipelines
      </text>
    </g>
  </g>

  <!-- SOCIAL / CONTACT BUTTONS (STRICT: NO WEBSITE LINK) -->
  <g transform="translate(34, 168)">
    <!-- GitHub Link -->
    <a xlink:href="https://github.com/saadali122gb" href="https://github.com/saadali122gb" target="_blank" rel="noopener noreferrer" class="social-btn">
      <rect x="0" y="0" width="154" height="32" rx="7" fill="url(#btnGrad)" stroke="#1f2c47" stroke-width="1"/>
      <!-- GitHub Icon -->
      <path d="M16 8C11.58 8 8 11.58 8 16c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 24 16c0-4.42-3.58-8-8-8z" fill="#f8fafc"/>
      <text x="32" y="20.5" class="font-sans" font-size="12" font-weight="600" fill="#f8fafc">GitHub</text>
      <text x="80" y="20.5" class="font-mono" font-size="10.5" fill="#64748b">/saadali122gb</text>
    </a>

    <!-- LinkedIn Link -->
    <a xlink:href="https://www.linkedin.com/in/saad-rana-64a285320/" href="https://www.linkedin.com/in/saad-rana-64a285320/" target="_blank" rel="noopener noreferrer" class="social-btn">
      <g transform="translate(164, 0)">
        <rect x="0" y="0" width="168" height="32" rx="7" fill="url(#btnGrad)" stroke="#1f2c47" stroke-width="1"/>
        <!-- LinkedIn Icon -->
        <path d="M12 9a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm-1.75 3h3.5V22h-3.5V12zm6.25 0h3.35v1.44h.05c.47-.88 1.6-1.82 3.3-1.82 3.53 0 4.18 2.32 4.18 5.34V22h-3.5v-4.52c0-1.08-.02-2.47-1.5-2.47-1.51 0-1.74 1.18-1.74 2.39V22h-3.5v-10h-.64z" fill="#38bdf8"/>
        <text x="32" y="20.5" class="font-sans" font-size="12" font-weight="600" fill="#f8fafc">LinkedIn</text>
        <text x="88" y="20.5" class="font-mono" font-size="10.5" fill="#64748b">/saad-rana</text>
      </g>
    </a>

    <!-- Email Link -->
    <a xlink:href="mailto:saadali122gb@gmail.com" href="mailto:saadali122gb@gmail.com" target="_blank" rel="noopener noreferrer" class="social-btn">
      <g transform="translate(342, 0)">
        <rect x="0" y="0" width="220" height="32" rx="7" fill="url(#btnGrad)" stroke="#1f2c47" stroke-width="1"/>
        <!-- Mail Icon -->
        <path d="M10 8h12c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H10c-1.1 0-2-.9-2-2V10c0-1.1.9-2 2-2zm0 2v.51L16 14.2l6-3.69V10H10zm12 12V13l-5.46 3.36c-.33.2-.74.2-1.08 0L10 13v9h12z" fill="#f43f5e"/>
        <text x="30" y="20.5" class="font-sans" font-size="12" font-weight="600" fill="#f8fafc">Email</text>
        <text x="70" y="20.5" class="font-mono" font-size="10.5" fill="#64748b">saadali122gb@gmail.com</text>
      </g>
    </a>
  </g>

  <!-- SECTION DIVIDER WITH SUBTLE ANIMATED SCAN BEAM -->
  <g transform="translate(34, 222)">
    <line x1="0" y1="0" x2="892" y2="0" stroke="#162238" stroke-width="1"/>
    <!-- Animated Light Runner on Divider -->
    <rect x="0" y="-1" width="140" height="2" fill="url(#scanlineGrad)">
      <animate attributeName="x" values="0;752;0" dur="6s" repeatCount="indefinite"/>
    </rect>
    <text x="0" y="-8" class="font-mono" font-size="9" font-weight="700" fill="#475569" letter-spacing="1.5">
      FEATURED REPOSITORIES &amp; SYSTEMS ARCHITECTURE
    </text>
    <text x="892" y="-8" text-anchor="end" class="font-mono" font-size="9" font-weight="600" fill="#38bdf8" letter-spacing="0.8">
      14 ACTIVE PROJECTS ↗
    </text>
  </g>
'''

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
      <!-- Card Base Rect -->
      <rect class="card-box" x="0" y="0" width="{card_w}" height="{card_h}" rx="10" 
            fill="url(#cardGrad_{cid})" stroke="#172236" stroke-width="1"/>

      <!-- Ambient Card Inner Glow -->
      <rect x="1" y="1" width="{card_w - 2}" height="32" rx="9" fill="{accent}" opacity="0.04"/>

      <!-- Top Border Accent Track -->
      <rect x="0" y="0" width="{card_w}" height="2" rx="1" fill="{accent}" opacity="0.22"/>

      <!-- Top Kinetic Light Runner (SMIL Animated) -->
      <rect x="0" y="0" width="90" height="2" fill="url(#beamGrad_{cid})" opacity="0.95">
        <animate attributeName="x" values="0;{card_w - 90};0" dur="{dur}" begin="{delay}" repeatCount="indefinite"/>
      </rect>

      <!-- Left Vertical Indicator Tab -->
      <rect x="0" y="18" width="3" height="24" rx="1.5" fill="{accent}"/>

      <!-- CARD HEADER: Index, Title & Live Status Indicator -->
      <g transform="translate(18, 24)">
        <!-- Index Number -->
        <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" fill="{accent}" opacity="0.9">
          {cid}
        </text>
        <!-- Project Title -->
        <text class="card-title font-sans" x="24" y="0.5" font-size="15.5" font-weight="700" fill="#f8fafc">
          {escape(p['name'])}
        </text>

        <!-- Live Pulse Indicator (Top Right) -->
        <g transform="translate(390, -4)">
          <circle cx="0" cy="0" r="3.5" fill="{accent}"/>
          <circle cx="0" cy="0" r="3.5" fill="{accent}" opacity="0.7">
            <animate attributeName="r" values="3.5;10;3.5" dur="{dur}" begin="{delay}" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.7;0;0.7" dur="{dur}" begin="{delay}" repeatCount="indefinite"/>
          </circle>
        </g>
      </g>

      <!-- CATEGORY / TAG BADGE -->
      <g transform="translate(18, 42)">
        <rect x="0" y="0" width="{len(p['tag']) * 6.8 + 14}" height="19" rx="4.5" 
              fill="{accent}" fill-opacity="0.1" stroke="{accent}" stroke-opacity="0.3" stroke-width="0.8"/>
        <text x="7" y="13" class="font-mono" font-size="9" font-weight="700" fill="{accent}" letter-spacing="0.6">
          {escape(p['tag'])}
        </text>
      </g>

      <!-- DESCRIPTION -->
      <text x="18" y="85" class="font-sans" font-size="12.2" font-weight="400" fill="#94a3b8">
        {escape(p['desc'])}
      </text>

      <!-- FOOTER ROW: Repo Path & Action Link -->
      <g transform="translate(18, 110)">
        <!-- Repo Path Snippet -->
        <text x="0" y="0" class="font-mono" font-size="10" fill="#475569">
          saadali122gb/{p['repo'][:22]}
        </text>

        <!-- Action Pill (Right) -->
        <g transform="translate(300, -12)">
          <rect class="action-btn" x="0" y="0" width="100" height="20" rx="5" 
                fill="#0d1424" stroke="{accent}" stroke-opacity="0.4" stroke-width="0.8"/>
          <text x="50" y="13.5" text-anchor="middle" class="font-sans" font-size="10" font-weight="600" fill="#e2e8f0">
            View Repo ↗
          </text>
        </g>
      </g>
    </a>
  </g>
'''
    cards_svg.append(card_str)

cards_content = "\n".join(cards_svg)

footer_y = 1260
footer_svg = f'''
  <!-- FOOTER STATUS CONSOLE -->
  <g transform="translate(34, {footer_y})">
    <rect x="0" y="0" width="892" height="38" rx="8" fill="#080c16" stroke="#162238" stroke-width="1"/>
    
    <!-- Status Terminal Dot -->
    <circle cx="18" cy="19" r="4" fill="#10b981"/>
    <circle cx="18" cy="19" r="4" fill="#10b981" opacity="0.5">
      <animate attributeName="r" values="4;8;4" dur="2.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    
    <text x="32" y="23" class="font-mono" font-size="10" font-weight="600" fill="#64748b">
      SYSTEM MATRIX ONLINE <tspan fill="#334155">//</tspan> ALL 14 REPOSITORIES ACTIVE
    </text>

    <!-- Center Architecture Tags -->
    <text x="446" y="23" text-anchor="middle" class="font-mono" font-size="9.5" fill="#475569">
      MERN • .NET • PYTHON • FASTAPI • DOCKER • SPATIAL GIS • LLM GUARDRAILS
    </text>

    <!-- Right Profile Link -->
    <a xlink:href="https://github.com/saadali122gb" href="https://github.com/saadali122gb" target="_blank" rel="noopener noreferrer">
      <text x="874" y="23" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8">
        @saadali122gb ↗
      </text>
    </a>
  </g>
'''

scanline_svg = '''
  <!-- Subtle Ambient Scanline traversing vertically -->
  <line x1="0" y1="0" x2="960" y2="0" stroke="url(#scanlineGrad)" stroke-width="1.2" opacity="0.18">
    <animate attributeName="y1" values="0;1320;0" dur="10s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="0;1320;0" dur="10s" repeatCount="indefinite"/>
  </line>
'''

full_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
     viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%"
     style="background: #05070c; text-rendering: geometricPrecision; shape-rendering: geometricPrecision;">
  <defs>
{defs_content}
  </defs>

{styles}

  <!-- BACKGROUND RECT & GRID -->
  <rect width="{svg_width}" height="{svg_height}" fill="#05070c"/>
  <rect width="{svg_width}" height="{svg_height}" fill="url(#techGrid)"/>

  <!-- AMBIENT LIGHTING OVERLAYS -->
  <rect width="{svg_width}" height="600" fill="url(#topAura)"/>
  <rect width="{svg_width}" height="{svg_height}" fill="url(#sideAura)"/>
  <rect width="{svg_width}" height="{svg_height}" fill="url(#bottomAura)"/>

{scanline_svg}

{header_svg}

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
print(f"Generated and validated {svg_file} successfully!")
