#!/usr/bin/env python3
"""Build the curated category and workflow pages.

The catalog is data-driven so navigation and tool-card structure cannot drift.
Run this script after editing CATEGORIES, TOOLS, or WORKFLOWS.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
VERIFIED = "2026-07-07"

CATEGORIES = [
    ("Username", "Username discovery and identity correlation across public services."),
    ("Email", "Email account discovery, reputation checks, and breach-aware triage."),
    ("Phone", "Number parsing, carrier context, and public footprint discovery."),
    ("Telegram", "Telegram client research and public-channel collection."),
    ("Discord", "Authorized export and preservation of accessible Discord content."),
    ("Steam", "Steam identifiers, public profiles, and ecosystem metadata."),
    ("Gaming", "Cross-platform gaming profiles, achievements, and account pivots."),
    ("Social Media", "Collection and analysis of public social-platform content."),
    ("Images", "Metadata inspection, hashing, and visual-evidence triage."),
    ("Documents", "Document metadata, embedded-object, and sanitization analysis."),
    ("Domains", "DNS, subdomain, certificate, and external-asset discovery."),
    ("IP", "Network attribution context and authorized service discovery."),
    ("GEOINT", "Geospatial analysis, map data, and location corroboration."),
    ("SOCMINT", "Structured research into public social interactions and identities."),
    ("HUMINT", "Ethical interview support, research notes, and source corroboration."),
    ("OPSEC", "Researcher compartmentation, transport privacy, and data protection."),
    ("AI", "Local language, transcription, and extraction assistance for analysts."),
    ("Infrastructure", "Authorized exposure mapping and web-service reconnaissance."),
    ("Misc", "General-purpose OSINT frameworks and extensible research consoles."),
]

TOOLS = {
    "Username": [
        {
            "name": "Sherlock", "description": "Checks a username across a large catalog of social networks and public services.",
            "platform": "Linux, macOS, Windows; Python; Docker", "repo": "https://github.com/sherlock-project/sherlock", "site": "https://sherlockproject.xyz/", "license": "MIT", "status": "Maintained",
            "install": "pipx install sherlock-project", "example": "sherlock --print-found --csv analyst_handle", "sources": "Public profile URLs on supported websites.",
            "pros": "Broad site coverage; machine-readable output; active test ecosystem.", "limits": "False positives remain possible; rate limits and site changes affect results; existence does not establish ownership.",
        },
        {
            "name": "Maigret", "description": "Searches usernames across sites and produces structured reports with profile-derived identifiers.",
            "platform": "Linux, macOS, Windows; Python; Docker", "repo": "https://github.com/soxoj/maigret", "site": "https://maigret.readthedocs.io/", "license": "MIT", "status": "Maintained",
            "install": "pipx install maigret", "example": "maigret analyst_handle --json simple", "sources": "Public profiles, username pages, and identifiers exposed by supported sites.",
            "pros": "Multiple report formats; recursive identifier extraction; configurable site database.", "limits": "Large scans create noise; some targets require cookies or regional access; matches need manual validation.",
        },
    ],
    "Email": [
        {
            "name": "Holehe", "description": "Tests whether an email address is associated with supported services through public account-recovery behavior.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/megadose/holehe", "site": "https://github.com/megadose/holehe", "license": "GPL-3.0", "status": "Community",
            "install": "pipx install holehe", "example": "holehe subject@example.com --only-used", "sources": "Public registration and account-recovery responses from supported services.",
            "pros": "Focused account-discovery signal; simple CLI; service modules are inspectable.", "limits": "May trigger rate limits or notifications; service behavior changes frequently; a hit is not proof of control.",
        },
        {
            "name": "h8mail", "description": "Correlates email addresses with locally supplied or authorized breach and intelligence sources.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/khast3x/h8mail", "site": "https://github.com/khast3x/h8mail", "license": "MIT", "status": "Community",
            "install": "pipx install h8mail", "example": "h8mail -t subject@example.com -q case-001.csv", "sources": "Local breach files and configured third-party APIs for which the analyst has lawful access.",
            "pros": "Supports local datasets; CSV output; useful for controlled enrichment pipelines.", "limits": "Data provenance and legality vary; stale breach data can mislead; API sources require separate credentials and terms review.",
        },
    ],
    "Phone": [
        {
            "name": "PhoneInfoga", "description": "Performs phone-number parsing and open-web reconnaissance without claiming subscriber identification.",
            "platform": "Linux, macOS, Windows; Go binary; Docker", "repo": "https://github.com/sundowndev/phoneinfoga", "site": "https://sundowndev.github.io/phoneinfoga/", "license": "GPL-3.0", "status": "Maintained",
            "install": "docker pull sundowndev/phoneinfoga:latest", "example": "docker run --rm sundowndev/phoneinfoga scan -n '+12025550123'", "sources": "Numbering-plan metadata and generated public-web search pivots.",
            "pros": "Normalizes international numbers; reproducible CLI; does not depend on a private subscriber database.", "limits": "Cannot prove a person's ownership; search results can be stale; use a reserved example number in demonstrations.",
        },
        {
            "name": "libphonenumber", "description": "Google's library for parsing, formatting, and validating international phone-number structures.",
            "platform": "Java, C++, JavaScript; community ports for other languages", "repo": "https://github.com/google/libphonenumber", "site": "https://github.com/google/libphonenumber", "license": "Apache-2.0", "status": "Maintained",
            "install": "# JavaScript port\nnpm install google-libphonenumber", "example": "node -e \"const p=require('google-libphonenumber').PhoneNumberUtil.getInstance(); console.log(p.parse('+12025550123'))\"", "sources": "International numbering plans and metadata distributed with the library.",
            "pros": "Mature normalization logic; multi-language support; useful before querying other sources.", "limits": "Validity means structurally possible, not assigned or owned; metadata may lag numbering-plan changes.",
        },
    ],
    "Telegram": [
        {
            "name": "Telethon", "description": "Python client library for the Telegram API, suitable for authorized, reproducible public-channel collection.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/LonamiWebs/Telethon", "site": "https://docs.telethon.dev/", "license": "MIT", "status": "Maintained",
            "install": "python -m pip install telethon", "example": "python -m telethon.sync", "sources": "Telegram entities and messages accessible to the authenticated account through the official API.",
            "pros": "Asynchronous API; documented entity model; supports controlled exports.", "limits": "Requires Telegram API credentials; account access and collection must comply with law and platform terms; private content is out of scope without authorization.",
        },
        {
            "name": "Telegram Phone Number Checker", "description": "Bellingcat utility that checks whether phone numbers are connected to visible Telegram accounts under the operator's contact-discovery settings.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/bellingcat/telegram-phone-number-checker", "site": "https://github.com/bellingcat/telegram-phone-number-checker", "license": "MIT", "status": "Experimental",
            "install": "git clone https://github.com/bellingcat/telegram-phone-number-checker.git\ncd telegram-phone-number-checker\npython -m pip install -r requirements.txt", "example": "python telegram-phone-number-checker.py --help", "sources": "Telegram contact-discovery results visible to the authenticated research account.",
            "pros": "Open implementation; batch-oriented research workflow; produced by an established investigations team.", "limits": "Results depend on privacy settings and contacts; bulk use can expose subjects or the research account; review current upstream instructions before use.",
        },
    ],
    "Discord": [
        {
            "name": "DiscordChatExporter", "description": "Exports channels and direct-message histories that the authenticated account is authorized to access.",
            "platform": "Windows GUI; cross-platform CLI via .NET or Docker", "repo": "https://github.com/Tyrrrz/DiscordChatExporter", "site": "https://github.com/Tyrrrz/DiscordChatExporter", "license": "MIT", "status": "Maintained",
            "install": "docker pull tyrrrz/discordchatexporter:stable", "example": "docker run --rm tyrrrz/discordchatexporter:stable --help", "sources": "Discord messages, attachments, threads, and channel metadata visible to the authorized account.",
            "pros": "Multiple export formats; attachment support; useful for evidence preservation.", "limits": "Authentication handling is sensitive; collection may conflict with platform terms; exports contain personal data and require strict access controls.",
        },
        {
            "name": "Discord History Tracker", "description": "Browser-based viewer and tracking utility for preserving accessible Discord message history.",
            "platform": "Modern web browser; desktop viewer", "repo": "https://github.com/chylex/Discord-History-Tracker", "site": "https://dht.chylex.com/", "license": "MIT", "status": "Community",
            "install": "# Download a release from the repository; verify its checksum before use.", "example": "# Follow the upstream browser or desktop instructions for an authorized test server.", "sources": "Messages and metadata visible in Discord to the operator.",
            "pros": "Local history viewer; searchable archives; transparent source code.", "limits": "Browser injection and account-token handling carry risk; platform changes may break capture; use only where collection is authorized.",
        },
    ],
    "Steam": [
        {
            "name": "SteamKit", "description": "A .NET library for interacting with the Steam network and public Steam services.",
            "platform": ".NET on Linux, macOS, and Windows", "repo": "https://github.com/SteamRE/SteamKit", "site": "https://github.com/SteamRE/SteamKit/wiki", "license": "LGPL-2.1", "status": "Maintained",
            "install": "dotnet add package SteamKit2", "example": "dotnet new console -n SteamResearch\ncd SteamResearch\ndotnet add package SteamKit2", "sources": "Steam network data exposed to the authenticated client and public Steam endpoints.",
            "pros": "Mature protocol implementation; typed .NET API; suitable for repeatable research tooling.", "limits": "Requires custom development; authenticated collection must respect Steam rules; public profiles may be incomplete or private.",
        },
        {
            "name": "SteamDB Browser Extension", "description": "Adds SteamDB context and public metadata directly to Steam store and community pages.",
            "platform": "Chromium- and Firefox-based browsers", "repo": "https://github.com/SteamDatabase/BrowserExtension", "site": "https://steamdb.info/extension/", "license": "MIT", "status": "Maintained",
            "install": "# Install only from the official browser-store links on the project website.", "example": "# Open a public Steam store or community page after installation.", "sources": "Public Steam pages and SteamDB metadata.",
            "pros": "Low-friction context; open-source extension; useful for manual verification.", "limits": "Not a bulk collector; SteamDB is an independent service; displayed data can change after capture.",
        },
    ],
    "Gaming": [
        {
            "name": "PlayTracker", "description": "Cross-platform gaming profile and statistics service with public user, game, and attribute search.",
            "platform": "Web; Windows desktop companion", "repo": "TODO — no public source repository identified.", "site": "https://playtracker.net/", "license": "Proprietary service", "status": "Active",
            "install": "# No installation is required for public web search.", "example": "https://playtracker.net/search/", "sources": "Linked public gaming profiles and platform-derived game, achievement, and activity data.",
            "pros": "Cross-platform correlation; public search; unified profile context.", "limits": "Some data requires an account or subscription; estimates are not primary-source facts; linked accounts may be self-asserted.",
        },
        {
            "name": "Exophase", "description": "Public cross-platform achievement and gaming-profile search spanning major console and PC ecosystems.",
            "platform": "Web", "repo": "TODO — no public source repository identified.", "site": "https://www.exophase.com/", "license": "Proprietary service", "status": "Active",
            "install": "# No installation is required.", "example": "https://www.exophase.com/search/", "sources": "Public PSN, Xbox, Steam, GOG, Epic, Nintendo, and other linked gaming profiles.",
            "pros": "Wide platform coverage; achievements provide useful temporal context; public profile pages are easy to cite.", "limits": "Coverage depends on privacy and synchronization; identical handles are not identity proof; platform availability changes.",
        },
    ],
    "Social Media": [
        {
            "name": "Instaloader", "description": "Downloads accessible Instagram posts, profiles, metadata, and comments for reproducible research.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/instaloader/instaloader", "site": "https://instaloader.github.io/", "license": "MIT", "status": "Maintained",
            "install": "pipx install instaloader", "example": "instaloader --no-videos --no-compress-json public_profile", "sources": "Public Instagram profiles and content accessible to the operator's session.",
            "pros": "Metadata-rich output; resumable downloads; filename controls aid evidence handling.", "limits": "Instagram changes and rate limits cause breakage; authentication raises account risk; private content requires legitimate access.",
        },
        {
            "name": "twscrape", "description": "Python library and CLI for collecting publicly accessible X/Twitter search, user, and timeline results.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/vladkens/twscrape", "site": "https://github.com/vladkens/twscrape", "license": "MIT", "status": "Community",
            "install": "python -m pip install twscrape", "example": "twscrape search 'from:example since:2026-01-01' --limit 20", "sources": "Publicly accessible X/Twitter web and API responses available to configured accounts.",
            "pros": "Structured output; asynchronous collection; useful search primitives.", "limits": "Requires account configuration; platform enforcement and schema changes are frequent; comply with terms and minimize collection.",
        },
    ],
    "Images": [
        {
            "name": "ExifTool", "description": "Reads, writes, and compares metadata across a wide range of image and media formats.",
            "platform": "Linux, macOS, Windows; Perl; standalone packages", "repo": "https://github.com/exiftool/exiftool", "site": "https://exiftool.org/", "license": "Artistic-1.0 or GPL-1.0-or-later", "status": "Maintained",
            "install": "# Debian/Ubuntu\nsudo apt install libimage-exiftool-perl", "example": "exiftool -G1 -a -s evidence.jpg", "sources": "Embedded EXIF, IPTC, XMP, maker-note, filesystem, and container metadata.",
            "pros": "Exceptional format coverage; preserves duplicate tags; stable machine-readable output.", "limits": "Metadata may be stripped, spoofed, or inherited; never treat a single tag as conclusive location or authorship evidence.",
        },
        {
            "name": "ImageHash", "description": "Python library for perceptual image hashes used to find near-duplicates and transformed variants.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/JohannesBuchner/imagehash", "site": "https://pypi.org/project/ImageHash/", "license": "BSD-2-Clause", "status": "Maintained",
            "install": "python -m pip install ImageHash", "example": "python -c \"from PIL import Image; import imagehash; print(imagehash.phash(Image.open('evidence.jpg')))\"", "sources": "Local raster images and frames extracted from media.",
            "pros": "Fast similarity screening; several hash algorithms; simple integration.", "limits": "Hash distance is not semantic proof; crops and heavy edits can evade matching; thresholds require dataset-specific testing.",
        },
    ],
    "Documents": [
        {
            "name": "oletools", "description": "Analyzes Microsoft Office and OLE files for metadata, macros, embedded objects, and suspicious structures.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/decalage2/oletools", "site": "https://github.com/decalage2/oletools/wiki", "license": "BSD-2-Clause", "status": "Maintained",
            "install": "pipx install oletools", "example": "oleid evidence.docx\nolevba evidence.docm", "sources": "OLE, OOXML, RTF, macro, property, and embedded-object structures.",
            "pros": "Purpose-built analyzers; readable reports; strong triage value.", "limits": "Potentially malicious documents need isolated handling; findings require interpretation; does not safely render document content.",
        },
        {
            "name": "MAT2", "description": "Inspects and removes metadata from common file formats while exposing what was found.",
            "platform": "Linux; Python", "repo": "https://0xacab.org/jvoisin/mat2", "site": "https://0xacab.org/jvoisin/mat2", "license": "LGPL-3.0-or-later", "status": "Maintained",
            "install": "# Debian/Ubuntu\nsudo apt install mat2", "example": "mat2 --show evidence.pdf", "sources": "Metadata in supported documents, images, audio, archives, and office formats.",
            "pros": "Clear inspection mode; supports sanitized copies; integrates with desktop workflows.", "limits": "Sanitization can change files and signatures; preserve an original first; not every proprietary metadata field is supported.",
        },
    ],
    "Domains": [
        {
            "name": "OWASP Amass", "description": "Performs external asset discovery using DNS, certificates, APIs, and graph-based correlation.",
            "platform": "Linux, macOS, Windows; Go; Docker", "repo": "https://github.com/owasp-amass/amass", "site": "https://owasp.org/www-project-amass/", "license": "Apache-2.0", "status": "Maintained",
            "install": "go install github.com/owasp-amass/amass/v4/...@master", "example": "amass enum -passive -d example.com", "sources": "DNS, certificate transparency, search APIs, public datasets, and configured data sources.",
            "pros": "Strong source fusion; graph model; passive mode supports low-impact discovery.", "limits": "Active modes can touch target infrastructure; API keys change coverage; discovered names require DNS and ownership validation.",
        },
        {
            "name": "Subfinder", "description": "Discovers valid subdomains from passive online sources with a pipeline-friendly CLI.",
            "platform": "Linux, macOS, Windows; Go; Docker", "repo": "https://github.com/projectdiscovery/subfinder", "site": "https://docs.projectdiscovery.io/tools/subfinder/overview", "license": "MIT", "status": "Maintained",
            "install": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest", "example": "subfinder -silent -d example.com -o subdomains.txt", "sources": "Passive APIs, certificate transparency, public datasets, and search services.",
            "pros": "Fast; configurable providers; clean text and JSON output.", "limits": "Completeness depends on API credentials; wildcard DNS and stale records create noise; authorization is still required for follow-on probing.",
        },
    ],
    "IP": [
        {
            "name": "Nmap", "description": "Network mapper for authorized host discovery, service identification, and carefully scoped enumeration.",
            "platform": "Linux, macOS, Windows", "repo": "https://github.com/nmap/nmap", "site": "https://nmap.org/", "license": "Nmap Public Source License", "status": "Maintained",
            "install": "# Debian/Ubuntu\nsudo apt install nmap", "example": "nmap -sV --version-light 192.0.2.10", "sources": "Direct network responses from explicitly authorized hosts and services.",
            "pros": "Mature service detection; XML output; extensive documentation.", "limits": "Active scanning is observable and may be unlawful without permission; detection is probabilistic; use documentation-reserved addresses in examples.",
        },
        {
            "name": "ZMap", "description": "High-speed internet scanner designed for controlled research with explicit scope and rate governance.",
            "platform": "Linux, macOS, BSD", "repo": "https://github.com/zmap/zmap", "site": "https://zmap.io/", "license": "Apache-2.0", "status": "Maintained",
            "install": "# Debian/Ubuntu\nsudo apt install zmap", "example": "zmap --dryrun -p 443 192.0.2.0/24", "sources": "Direct responses to researcher-defined network probes.",
            "pros": "Reproducible high-volume methodology; denylist support; structured output.", "limits": "Internet-scale use has substantial legal, ethical, and operational risk; never run without authorization, exclusions, rate controls, and abuse handling.",
        },
    ],
    "GEOINT": [
        {
            "name": "QGIS", "description": "Desktop geographic information system for layering, transforming, and analyzing geospatial evidence.",
            "platform": "Linux, macOS, Windows", "repo": "https://github.com/qgis/QGIS", "site": "https://qgis.org/", "license": "GPL-2.0-or-later", "status": "Maintained",
            "install": "# Debian/Ubuntu\nsudo apt install qgis", "example": "qgis evidence-locations.geojson", "sources": "GeoJSON, KML, raster imagery, vector layers, databases, and web map services.",
            "pros": "Powerful spatial analysis; broad format support; reproducible projects and styles.", "limits": "Source accuracy and licensing vary; projections can distort results; project files should preserve source and transformation notes.",
        },
        {
            "name": "Overpass Turbo", "description": "Interactive web interface for querying and visualizing OpenStreetMap data through the Overpass API.",
            "platform": "Web; JavaScript", "repo": "https://github.com/tyrasd/overpass-turbo", "site": "https://overpass-turbo.eu/", "license": "MIT", "status": "Maintained",
            "install": "# No installation is required for the hosted interface.", "example": "[out:json];node[amenity=pharmacy](around:500,51.5074,-0.1278);out;", "sources": "OpenStreetMap nodes, ways, relations, tags, and geometry available through Overpass.",
            "pros": "Fast query prototyping; map visualization; export to common geospatial formats.", "limits": "OpenStreetMap is community-maintained and uneven; public instances enforce limits; timestamps reflect map edits, not necessarily real-world events.",
        },
    ],
    "SOCMINT": [
        {
            "name": "Social Analyzer", "description": "Correlates a username or name across supported social and public-web sources with multiple analysis modes.",
            "platform": "Linux, macOS, Windows; Python; Node.js; Docker", "repo": "https://github.com/qeeqbox/social-analyzer", "site": "https://github.com/qeeqbox/social-analyzer", "license": "MIT", "status": "Community",
            "install": "python -m pip install social-analyzer", "example": "social-analyzer --username analyst_handle --metadata --top 100", "sources": "Public profile endpoints and search results across supported websites.",
            "pros": "Broad query modes; JSON output; useful for initial lead generation.", "limits": "Coverage breadth increases false positives; automated requests can be blocked; all identity links require corroboration.",
        },
        {
            "name": "snscrape", "description": "Collectors for public social-network content that produce structured items for downstream analysis.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/JustAnotherArchivist/snscrape", "site": "https://github.com/JustAnotherArchivist/snscrape", "license": "GPL-3.0", "status": "Community",
            "install": "pipx install snscrape", "example": "snscrape --jsonl reddit-search 'example query' > results.jsonl", "sources": "Public content from the collectors currently supported by the installed version.",
            "pros": "Streaming JSON Lines; composable CLI; no private-data claim.", "limits": "Individual collectors frequently break after platform changes; verify current upstream support; collection may be restricted by terms or law.",
        },
    ],
    "HUMINT": [
        {
            "name": "SpiderFoot", "description": "Automates open-source collection and entity correlation to prepare and corroborate lawful research leads.",
            "platform": "Linux, macOS, Windows; Python; Docker", "repo": "https://github.com/smicallef/spiderfoot", "site": "https://www.spiderfoot.net/", "license": "MIT", "status": "Maintained",
            "install": "docker pull spiderfoot/spiderfoot", "example": "docker run -p 5001:5001 spiderfoot/spiderfoot", "sources": "Configured public APIs, DNS, web pages, threat-intelligence feeds, and search sources.",
            "pros": "Entity graph; modular sources; useful for pre-interview fact checking.", "limits": "Automation can amplify incorrect associations; API terms differ; it is not a substitute for consent, source evaluation, or human judgment.",
        },
        {
            "name": "Joplin", "description": "End-to-end encrypted note application suitable for structured interview notes and source logs.",
            "platform": "Linux, macOS, Windows, Android, iOS; terminal", "repo": "https://github.com/laurent22/joplin", "site": "https://joplinapp.org/", "license": "AGPL-3.0-or-later", "status": "Maintained",
            "install": "# Install a signed release from the official website or platform store.", "example": "# Create a case notebook with separate source, claim, and verification notes.", "sources": "Analyst-authored notes, attachments, web clips, and imported Markdown.",
            "pros": "Local-first; encryption support; Markdown export helps case portability.", "limits": "Encryption does not replace endpoint security; interview records may be highly sensitive; access, retention, and consent rules must be defined first.",
        },
    ],
    "OPSEC": [
        {
            "name": "Tor", "description": "An anonymity network and client for separating research traffic from ordinary network identity.",
            "platform": "Linux, macOS, Windows, Android", "repo": "https://gitlab.torproject.org/tpo/core/tor", "site": "https://www.torproject.org/", "license": "BSD-3-Clause", "status": "Maintained",
            "install": "# Prefer Tor Browser from the official website and verify its signature.", "example": "# Confirm the connection only through the Tor Project check page.", "sources": "Network transport; Tor does not itself provide OSINT data sources.",
            "pros": "Separates destination traffic from the origin IP; mature threat documentation; open source.", "limits": "Does not provide complete anonymity; browser behavior, logins, downloads, and endpoint compromise can deanonymize a researcher.",
        },
        {
            "name": "VeraCrypt", "description": "Creates encrypted volumes for protecting case material at rest.",
            "platform": "Linux, macOS, Windows", "repo": "https://github.com/veracrypt/VeraCrypt", "site": "https://www.veracrypt.fr/", "license": "Apache-2.0 and TrueCrypt License 3.0", "status": "Maintained",
            "install": "# Download a signed release from the official website and verify it.", "example": "veracrypt --text --create case-container.hc", "sources": "Local files and block devices selected by the investigator.",
            "pros": "Strong at-rest encryption; cross-platform volumes; supports keyfiles and hidden volumes.", "limits": "Mounted data is exposed to the endpoint; forgotten credentials are unrecoverable; local law and organizational key-management rules apply.",
        },
    ],
    "AI": [
        {
            "name": "Ollama", "description": "Runs supported language and vision models locally for extraction, classification, and analyst-assisted review.",
            "platform": "Linux, macOS, Windows; Docker", "repo": "https://github.com/ollama/ollama", "site": "https://ollama.com/", "license": "MIT", "status": "Maintained",
            "install": "# Follow the signed installer instructions on the official website.\nollama pull gemma3", "example": "ollama run gemma3 'Extract claims and uncertainties from this public text.'", "sources": "Analyst-supplied local text, images for supported models, and model files.",
            "pros": "Local processing can reduce disclosure; scriptable API; broad model ecosystem.", "limits": "Models hallucinate and reproduce bias; model licenses vary; outputs require source-grounded human verification.",
        },
        {
            "name": "Whisper", "description": "OpenAI speech-recognition model and reference code for local transcription and language identification.",
            "platform": "Linux, macOS, Windows; Python; GPU optional", "repo": "https://github.com/openai/whisper", "site": "https://github.com/openai/whisper", "license": "MIT", "status": "Maintained",
            "install": "python -m pip install -U openai-whisper", "example": "whisper interview.wav --model turbo --output_format json", "sources": "Local audio and video converted through FFmpeg-supported formats.",
            "pros": "Multilingual transcription; timestamped output; can run locally.", "limits": "Names, numbers, and low-quality audio are error-prone; consent and recording law matter; transcriptions must be checked against audio.",
        },
    ],
    "Infrastructure": [
        {
            "name": "Nuclei", "description": "Template-based scanner for authorized, reproducible checks against known infrastructure conditions.",
            "platform": "Linux, macOS, Windows; Go; Docker", "repo": "https://github.com/projectdiscovery/nuclei", "site": "https://docs.projectdiscovery.io/tools/nuclei/overview", "license": "MIT", "status": "Maintained",
            "install": "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest", "example": "nuclei -u https://example.com -severity info -rl 1", "sources": "Direct responses from explicitly authorized web and network targets, interpreted through selected templates.",
            "pros": "Versioned templates; structured output; rate and scope controls.", "limits": "Active scanning can affect systems and trigger alerts; templates can produce false positives or unsafe requests; obtain permission first.",
        },
        {
            "name": "httpx", "description": "Probes authorized HTTP services and records status, titles, technologies, TLS, and response metadata.",
            "platform": "Linux, macOS, Windows; Go; Docker", "repo": "https://github.com/projectdiscovery/httpx", "site": "https://docs.projectdiscovery.io/tools/httpx/overview", "license": "MIT", "status": "Maintained",
            "install": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest", "example": "printf 'https://example.com\\n' | httpx -json -title -status-code", "sources": "Direct HTTP and TLS responses from analyst-supplied, authorized targets.",
            "pros": "Pipeline-friendly; rich JSON output; configurable retries and rates.", "limits": "It sends network traffic; technology detection is heuristic; redirects and virtual hosting can create attribution mistakes.",
        },
    ],
    "Misc": [
        {
            "name": "Recon-ng", "description": "Modular reconnaissance framework with workspaces, structured records, and exportable results.",
            "platform": "Linux, macOS, Windows; Python", "repo": "https://github.com/lanmaster53/recon-ng", "site": "https://github.com/lanmaster53/recon-ng/wiki", "license": "GPL-3.0", "status": "Community",
            "install": "git clone https://github.com/lanmaster53/recon-ng.git\ncd recon-ng\npython -m pip install -r REQUIREMENTS", "example": "./recon-ng -w case-001", "sources": "Public and credentialed APIs selected through separately installed modules.",
            "pros": "Case workspaces; modular design; repeatable exports.", "limits": "Modules vary in maintenance and legal terms; API keys are sensitive; framework output needs source-level validation.",
        },
        {
            "name": "OSINT Framework", "description": "A navigable taxonomy of OSINT resources organized by starting data type and investigative objective.",
            "platform": "Web", "repo": "https://github.com/lockfale/OSINT-Framework", "site": "https://osintframework.com/", "license": "MIT", "status": "Community",
            "install": "# No installation is required for the hosted website.", "example": "https://osintframework.com/", "sources": "Curated links to third-party services and research resources.",
            "pros": "Fast discovery by pivot type; broad coverage; source tree is public.", "limits": "A catalog is not validation; third-party links and business models change; evaluate every resource before submitting data.",
        },
    ],
}

WORKFLOWS = {
    "Username Investigation": [
        ("Define the identifier", "Record exact spelling, capitalization, separators, observed URL, collection time, and the source that exposed the handle."),
        ("Search across services", "Run two independent username tools, then manually validate high-value results. Treat display-name matches separately from exact handles."),
        ("Check historical presence", "Review lawful web archives and cached search results. Record capture dates; do not imply that an archived profile is still controlled by the same person."),
        ("Compare visual signals", "Compare avatars with perceptual hashes and manual inspection. Note reused crops, backgrounds, and upload timing without treating similarity as identity proof."),
        ("Cross-reference attributes", "Compare self-disclosed names, locations, links, writing patterns, and activity windows. Require at least two independent signals for an identity hypothesis."),
        ("Map relationships", "Record public interactions only when they materially support the question. Avoid bulk collection of unrelated contacts."),
        ("Document and preserve", "Save URLs, timestamps, screenshots, raw exports, tool versions, and hashes. Separate observations from analytical judgments."),
    ],
    "Telegram Investigation": [
        ("Set scope and account safety", "Define whether the target is a public channel, group, message, or visible account. Use a dedicated research account and document platform and legal constraints."),
        ("Resolve entities", "Record canonical usernames, numeric IDs when lawfully available, invite links, display names, and entity type. Expect usernames and titles to change."),
        ("Collect public content", "Use an authorized API client for bounded date ranges. Preserve message IDs, timestamps, forwards, edits, media references, and reply relationships."),
        ("Trace provenance", "Follow forward headers and cited links to the earliest accessible source. Distinguish original publication from redistribution."),
        ("Analyze media and location", "Hash media, inspect metadata safely, compare frames, and test geographic claims against independent map or imagery evidence."),
        ("Assess networks", "Map channels, administrators only when public, mentions, forwards, and shared links. Do not infer coordination from a single overlap."),
        ("Preserve evidence", "Export raw API records, media hashes, collection code, account context, and UTC timestamps. Note deletions or inaccessible items without attempting unauthorized recovery."),
    ],
    "Email Investigation": [
        ("Normalize the address", "Preserve the original string, normalize the domain conservatively, check for aliases, and avoid provider-specific transformations unless documented."),
        ("Validate infrastructure", "Inspect domain registration context, MX records, SPF, DKIM selectors when known, and DMARC. Do not send probing mail without authorization."),
        ("Discover public exposure", "Search exact-address variants, public documents, commits, account-recovery signals, and lawful breach sources. Record query and source dates."),
        ("Inspect message evidence", "When a message is provided, preserve it in RFC 5322 form and analyze the full header chain, authentication results, attachments, and URLs in isolation."),
        ("Correlate identities", "Compare usernames, public profiles, organization references, and historical documents. An address alone is not reliable proof of a current owner."),
        ("Assess risk", "Classify confirmed compromise exposure separately from spam reputation, spoofing, or mere appearance in an old dataset."),
        ("Report minimally", "Redact unnecessary personal data and breach content. Cite public sources, uncertainty, and lawful-access basis."),
    ],
    "Phone Investigation": [
        ("Normalize the number", "Convert to E.164 with the correct region assumption. Preserve the submitted format and document any inferred country code."),
        ("Check numbering context", "Determine structural validity, country, possible type, and numbering-plan context. Do not equate validity with assignment."),
        ("Search public references", "Search quoted international and national formats, public business listings, documents, and self-published profiles."),
        ("Review messaging visibility", "Use only ordinary contact-discovery behavior that is lawful and visible to the research account. Avoid invasive enumeration or notification-generating checks."),
        ("Correlate cautiously", "Compare names, avatars, business records, usernames, and timestamps. Recycled numbers make historical matches especially fragile."),
        ("Check temporal validity", "Record when each association was observed and whether the source describes a historical or current contact."),
        ("Preserve and redact", "Store the canonical number in restricted case notes and redact it from broad reports unless essential."),
    ],
    "Image Investigation": [
        ("Preserve the original", "Save the highest-quality available file without re-encoding. Calculate SHA-256 and record acquisition URL, time, and method."),
        ("Inspect safely", "Identify the actual file type, dimensions, color profile, embedded previews, and metadata in an isolated environment."),
        ("Generate derivatives", "Create documented crops, frames, contrast variants, and perceptual hashes. Never overwrite the original."),
        ("Search for earlier copies", "Use multiple reverse-image engines and search distinctive visual elements. Prioritize the earliest verifiable publication, not the first search result."),
        ("Geolocate", "Extract signs, terrain, shadows, architecture, weather, road markings, and landmarks; test each clue against independent geospatial sources."),
        ("Chronolocate", "Compare upload history, weather, sun position, construction state, vegetation, and event context. State time ranges rather than false precision."),
        ("Report confidence", "List supporting and contradicting observations, transformation history, source URLs, hashes, and confidence level."),
    ],
    "Domain Investigation": [
        ("Canonicalize scope", "Record the registrable domain, IDNA form, wildcard behavior, authorized boundaries, and investigation time window."),
        ("Collect passive DNS context", "Query current DNS, certificate transparency, passive sources, and web archives before any active probing."),
        ("Enumerate names", "Use at least two passive subdomain sources, deduplicate, resolve, and flag wildcard-derived results."),
        ("Inspect web history", "Review archived pages, redirects, favicons, analytics identifiers, and public documents. Preserve dates because ownership and content change."),
        ("Map dependencies", "Identify mail, CDN, hosting, nameserver, certificate, and third-party service relationships without assuming common ownership."),
        ("Validate ownership claims", "Corroborate with official sites, public filings, DNS control evidence, or signed statements; shared infrastructure is weak evidence."),
        ("Package evidence", "Export DNS answers with TTL and timestamp, certificate records, screenshots, raw tool output, and a scope statement."),
    ],
    "Infrastructure Investigation": [
        ("Obtain authorization", "Define targets, ports, dates, rate limits, excluded systems, data handling, and an abuse contact before sending traffic."),
        ("Establish passive inventory", "Collect DNS, certificates, routing, public cloud references, and known hostnames. Track source and observation time."),
        ("Resolve and classify", "Resolve hostnames, account for CDNs and shared hosting, and separate owned systems from third-party dependencies."),
        ("Probe conservatively", "Start with low-rate HTTP and service identification. Use explicit input lists and stop on instability or scope ambiguity."),
        ("Validate findings", "Reproduce important observations manually, capture raw responses, and distinguish a technology hint from a confirmed exposure."),
        ("Assess change over time", "Compare current results with authorized prior snapshots while accounting for dynamic addresses and ephemeral cloud assets."),
        ("Report responsibly", "Provide evidence, affected asset, timestamp, severity rationale, reproduction limits, and remediation channel; never publish exploitable details prematurely."),
    ],
    "Company Investigation": [
        ("Identify the legal entity", "Resolve exact legal names, jurisdictions, registration numbers, trading names, and official domains. Avoid merging similarly named entities."),
        ("Collect first-party claims", "Archive official sites, reports, filings, policies, press releases, and verified accounts with publication dates."),
        ("Map corporate structure", "Trace parents, subsidiaries, directors, beneficial ownership where lawfully public, and historical name changes through authoritative registries."),
        ("Analyze operations", "Review locations, hiring, procurement, technology, patents, shipping, and infrastructure while separating claims from observed evidence."),
        ("Assess people links", "Use professional and public sources proportionately. Do not collect unrelated family or private contact information."),
        ("Cross-check adverse claims", "Seek primary records, responses from the subject, and independent confirmation. Preserve the difference between allegation, proceeding, and finding."),
        ("Build a sourced timeline", "Record events in UTC where possible, cite archived primary sources, and mark gaps, conflicts, and confidence."),
    ],
    "Person Investigation": [
        ("Define necessity and scope", "Write the legitimate purpose, legal basis, target identifiers, excluded sensitive data, retention period, and stop conditions."),
        ("Disambiguate identity", "Start with high-quality known facts and build hypotheses. Never merge records solely on a common name, face, username, or location."),
        ("Collect self-published data", "Prioritize official biographies, public professional pages, authored work, verified accounts, and consented records."),
        ("Corroborate public records", "Use authoritative registries and publications appropriate to the jurisdiction; record access dates and correction mechanisms."),
        ("Build a bounded timeline", "Include only events relevant to the question, with evidence and uncertainty. Account for time zones and historical identifier reuse."),
        ("Test contradictions", "Actively search for disconfirming evidence, alternative people, parody accounts, stale records, and manipulated media."),
        ("Minimize the report", "Exclude doxxing-enabling details, unrelated associates, credentials, and intimate data. Separate fact, inference, and unknowns."),
    ],
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def page_link(folder: str, name: str) -> str:
    return f"../{folder}/{name.replace(' ', '%20')}.md"


def nav(folder: str, ordered_names: list[str], index: int) -> str:
    previous = ordered_names[index - 1] if index else ordered_names[-1]
    following = ordered_names[(index + 1) % len(ordered_names)]
    return (
        f"[Previous: {previous}]({page_link(folder, previous)}) · "
        f"[Next: {following}]({page_link(folder, following)}) · "
        "[Back to README](../README.md)"
    )


def tool_card(tool: dict[str, str], category: str) -> str:
    anchor = slug(tool["name"])
    return f"""<a id=\"{anchor}\"></a>
<details>
<summary><strong>{tool['name']}</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | {tool['name']} |
| **Description** | {tool['description']} |
| **Category** | {category} |
| **Platform** | {tool['platform']} |
| **Repository** | {f'[{tool["repo"]}]({tool["repo"]})' if tool['repo'].startswith('http') else tool['repo']} |
| **Official website** | [{tool['site']}]({tool['site']}) |
| **License** | {tool['license']} |
| **Status** | {tool['status']} |
| **Last verified** | {VERIFIED} |

**Installation**

```text
{tool['install']}
```

**Quick example**

```text
{tool['example']}
```

**Supported sources**

{tool['sources']}

**Pros**

{tool['pros']}

**Limitations**

{tool['limits']}

</details>
"""


def build_categories() -> None:
    folder = ROOT / "categories"
    folder.mkdir(exist_ok=True)
    names = [name for name, _ in CATEGORIES]
    for index, (name, scope) in enumerate(CATEGORIES):
        tools = TOOLS[name]
        toc_tools = "\n".join(f"  - [{tool['name']}](#{slug(tool['name'])})" for tool in tools)
        cards = "\n".join(tool_card(tool, name) for tool in tools)
        content = f"""# {name}

{nav('categories', names, index)}

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

{scope}

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
{toc_tools}
- [Quality controls](#quality-controls)
- [Related workflows](#related-workflows)
<!-- toc:end -->

## Scope

Use this category to generate and test leads, not to declare identity or attribution from a single match. Define the research question, collection boundary, and retention rule before opening a tool.

## Investigation approach

1. Preserve the input exactly as received and record its source.
2. Normalize only in a separate working copy and document every transformation.
3. Start with passive or locally processed sources.
4. Validate important results manually against the primary source.
5. Record UTC timestamps, URLs, tool versions, queries, and uncertainty.
6. Minimize personal data and stop when the research question is answered.

## Tools

The entries below are curated starting points, not endorsements. Verify current upstream documentation and release signatures before installation.

{cards}
## Quality controls

- Corroborate identity or ownership with at least two independent signals.
- Distinguish a tool result, an observed fact, and an analytical inference.
- Preserve raw output before filtering or transforming it.
- Re-run time-sensitive checks before publication.
- Document negative results; they describe coverage, not absence.

## Related workflows

Use the closest procedural guide in the [workflow index](../README.md#workflows). When no exact workflow exists, combine the relevant collection steps with the evidence-preservation requirements in [CONTRIBUTING](../CONTRIBUTING.md#evidence-and-safety-standard).

---

{nav('categories', names, index)}
"""
        (folder / f"{name}.md").write_text(content, encoding="utf-8")


def build_workflows() -> None:
    folder = ROOT / "workflows"
    folder.mkdir(exist_ok=True)
    names = list(WORKFLOWS)
    for index, name in enumerate(names):
        steps = WORKFLOWS[name]
        toc_steps = "\n".join(f"- [{i}. {title}](#{i}-{slug(title)})" for i, (title, _) in enumerate(steps, 1))
        sections = []
        for i, (title, body) in enumerate(steps, 1):
            sections.append(f"""## {i}. {title}

{body}

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.
""")
        content = f"""# {name}

{nav('workflows', names, index)}

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
{toc_steps}
- [Evidence package](#evidence-package)
- [Stop conditions](#stop-conditions)
<!-- toc:end -->

## Outcome

Produce a reproducible, source-grounded case record that separates observations from inferences and contains only information necessary to answer the stated question.

## Before collection

| Control | Required record |
| --- | --- |
| Purpose | One-sentence research question and intended user of the result |
| Authority | Consent, policy, contract, or legal basis |
| Scope | Included identifiers, sources, dates, and explicit exclusions |
| Safety | Account, device, network, and sensitive-data handling plan |
| Retention | Storage location, access list, review date, and deletion rule |

{"\n".join(sections)}
## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

{nav('workflows', names, index)}
"""
        (folder / f"{name}.md").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    build_categories()
    build_workflows()
    print(f"Built {len(CATEGORIES)} category pages and {len(WORKFLOWS)} workflow pages.")
