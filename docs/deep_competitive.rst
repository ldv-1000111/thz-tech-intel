Deep Competitive Analysis: ADAS Sensing Landscape
==================================================

.. note::
   Last updated: May 2026. An interactive slide deck of this analysis is available at
   :doc:`/slides/deep_analysis`.

This document provides a comprehensive engineering-level comparison of seven sensing
platforms competing in the ADAS and L4/L5 automotive autonomy space. Coverage spans
technical specifications, all-weather performance, OEM traction, financial health,
technology roadmaps, and IP positioning — as of May 2026.

----

The Seven Platforms
-------------------

.. list-table::
   :header-rows: 1
   :widths: 18 18 64

   * - Company
     - Technology
     - Key differentiator
   * - **Teradar**
     - Terahertz imaging (0.1–10 THz)
     - Only THz platform; 20× radar resolution; material fingerprinting; $150M Series B
   * - **Arbe Robotics**
     - 4D imaging radar (77 GHz)
     - 2,304 virtual channels; Chinese OEM serial production win; pivoting to defense/robotaxi
   * - **Mobileye**
     - Camera + radar fusion (EyeQ6H)
     - $1.9B 2025 revenue; $24.5B pipeline; VW robotaxi; acquiring Mentee Robotics
   * - **Innoviz**
     - Solid-state LiDAR (InnovizTwo/Three)
     - 0.05° resolution; $55M 2025 revenue; Top-5 OEM L3 SOP 2027; NVIDIA Hyperion
   * - **Luminar**
     - 1550 nm LiDAR (Iris/Halo)
     - Filed Chapter 11 Dec 2025; assets acquired by MicroVision; Halo IP preserved
   * - **Vayyar**
     - 4D imaging radar-on-chip (79 GHz)
     - $296M raised; $1B valuation; single chip replaces 20+ sensors; in-cabin + ADAS
   * - **Cepton (Koito)**
     - MMT® mirrorless LiDAR
     - Fully acquired by Koito Jan 2025; GM Ultra Cruise; 37 patents; Tier-1 secured

----

Financial Snapshot
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 22 22 22 16

   * - Company
     - Total funding raised
     - Latest round
     - 2025 revenue
     - Status
   * - Teradar
     - **$175M** (PitchBook)
     - $150M Series B — Nov 2025
     - Pre-revenue
     - Private · stealth exit
   * - Arbe Robotics
     - ~$200M+ (public)
     - $18.5M direct offering — Feb 2026
     - ~$1–2M (NRE)
     - Nasdaq: ARBE · $52M cash
   * - Mobileye
     - Public (Intel spinoff)
     - —
     - **$1,894M** (+15% YoY)
     - Nasdaq: MBLY · $1.8B cash
   * - Innoviz
     - ~$300M+
     - $40M registered direct — Feb 2025
     - **$55M** (>2× 2024)
     - Nasdaq: INVZ · ~$95M NRE pipeline
   * - Luminar
     - $306M
     - Bankruptcy DIP financing
     - ~$67–74M (revised down)
     - **Chapter 11** filed Dec 2025
   * - Vayyar
     - **$296M**
     - $108M Series E — Jun 2022
     - Undisclosed (private)
     - Private · $1B valuation
   * - Cepton (Koito)
     - $226M
     - Acquired by Koito — Jan 2025
     - Undisclosed (Koito subsidiary)
     - Private · Koito subsidiary

.. warning::
   Luminar filed for Chapter 11 bankruptcy in December 2025 following the Volvo contract
   termination and an SEC investigation. MicroVision agreed to acquire Luminar's LiDAR
   assets in January 2026. The Halo IP and OEM development contracts are the primary
   assets under negotiation.

----

OEM Design Wins & Production Contracts
---------------------------------------

Teradar
~~~~~~~

Teradar emerged from stealth in November 2025 with its $150M Series B and confirmed
active collaborations with five leading automotive OEMs in the US and Europe, plus three
Tier-1 suppliers. The company targets its first vehicle production program win by 2028.
Investors include Lockheed Martin Ventures, Capricorn Investment Group, The Engine
Ventures (MIT), IBEX Investors, and VXI Capital.

Arbe Robotics
~~~~~~~~~~~~~

Arbe's most significant recent win is a serial-production order from a state-owned Chinese
automaker, which selected Hirain Technologies' LRR610 radar — powered by Arbe's
ultra-high-definition chipset — for an L4 autonomous vehicle program. In Western markets,
three leading OEMs are in active RFI processes for eyes-off/hands-off functionality,
with selections expected in 2026 and production targeted for 2028–2030. A premium European
OEM is conducting data collection for an L3 program using Arbe-based radar. Arbe has also
received development kit orders from a leading AI computing company for full-stack AV
software development. However, in December 2025, Arbe disclosed it does not expect to
secure a previously anticipated European OEM strategic program award in the near term,
reflecting lengthening OEM decision timelines.

Mobileye
~~~~~~~~

Mobileye enters 2026 with the strongest OEM position in the field. Key 2025–2026 wins:

- **New high-volume Surround ADAS program** with a major US OEM
- **Mahindra SuperVision and Surround ADAS** design wins (Q1 2026)
- **VW Group EyeQ6H Supervision L2++ and Chauffeur L3** programs in active development
- **VW/MOIA ID.Buzz robotaxi** pre-series production kicked off at Hanover plant (Mar 2026)
- **8-year forward revenue pipeline of $24.5B** — a 42% increase since 2022

The EyeQ6 high-chip platform secured its first two major programs with two of the world's
largest automakers including Volkswagen. Mobileye's in-house imaging radar achieved its
first design win in Q2 2025 as an enabler of highway-speed L3 eyes-off performance.

Innoviz
~~~~~~~

Innoviz has become a key Tier-1 LiDAR supplier across multiple platforms:

- **BMW Series 7** — InnovizOne L3 in series production since March 2024
- **VW ADMT ID. Buzz AD** — InnovizTwo Long-Range selected as primary LiDAR
- **Mobileye Drive AV platform** — InnovizTwo chosen as key sensor (disclosed Q4 2024)
- **NVIDIA Hyperion 8 platform** — InnovizTwo integrated and offered to OEMs
- **Top-5 global passenger OEM** — Statement of Development Work signed June 2025 for
  an L3 global production program; SOP targeted 2027; production agreement in discussion
- **$95M NRE pipeline** with payments 2025–2027; H1 2025 revenues exceeded all of 2024

Luminar
~~~~~~~

Luminar's OEM position collapsed following the Volvo contract termination in November 2025.
Prior to bankruptcy, Luminar held production contracts with Volvo (EX90/ES90) and a
multi-billion dollar Mercedes-Benz agreement for next-generation vehicle lines. Those
programs are now in flux following the Chapter 11 filing. MicroVision's acquisition of
Luminar's LiDAR assets may preserve the Mercedes relationship, though no confirmation
has been made as of May 2026.

Vayyar
~~~~~~

Vayyar holds production-ready ADAS and in-cabin sensor positions with multiple undisclosed
OEMs. The company's XRR platform supports Euro NCAP 2023 requirements across nine ADAS
protocols. Vayyar claims its 2–4 external sensors plus one in-cabin sensor can provide up
to 35% of a vehicle's Euro NCAP points for a 5-star rating — a compelling cost reduction
argument for mass-market OEM adoption.

Cepton (Koito)
~~~~~~~~~~~~~~

Cepton was fully acquired by Koito Manufacturing in January 2025, securing the Tier-1
supply chain for the GM Ultra Cruise program — the largest ADAS LiDAR production contract
in the industry. Ultra Cruise spans multiple GM vehicle models across Cadillac and other
brands, with Koito providing full assembly, test, and calibration. Honda has also adopted
elements of the Super Cruise / Ultra Cruise ecosystem. Cepton filed 37 patents, now held
by Koito.

----

Technology Roadmaps
--------------------

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Company
     - 2025–2028 roadmap
   * - Teradar
     - Prototype availability US/Europe 2026; Modular Terahertz Engine (MTE) targeting
       L2–L5; defense (US Army SBIR Phase II completed); healthcare THz imaging; global
       high-volume production 2028. CES 2026 debut followed stealth exit Nov 2025.
   * - Arbe
     - Pivoting strategy to defense, robotaxi, robotruck, and off-road markets for shorter
       adoption cycles. Automotive Western OEM wins remain 2028–2030 target. New CEO
       appointed to manage multi-market expansion. 2026 adjusted EBITDA loss guided at
       ($28M)–($31M).
   * - Mobileye
     - EyeQ6H Surround ADAS scaling to high-volume 2026 (37M+ IQ units guided); Chauffeur
       L3 with VW ramping; Drive AV robotaxi expanding with MOIA; acquisition of Mentee
       Robotics (humanoid) extending into Physical AI. Imaging radar maturing for L3 eyes-off.
   * - Innoviz
     - InnovizThree launched Dec 2025 (35% cost reduction vs InnovizTwo); InnovizTwo ULR
       (1 km range) launched Apr 2026 for infrastructure/robotaxi; SOP ramp 2026–2027 for
       BMW/VW; Top-5 OEM L3 program SOP 2027; InnovizSMART for industrial launched 2025;
       Fabrinet high-volume line operational.
   * - Luminar
     - Halo ASIC tape-out completed Q4 2025; low-volume Halo prototype line launched Q1 2026;
       Halo B-sample delivery targeted Q2 2026. MicroVision acquisition targets preservation
       of Halo IP and continuing OEM development contracts. Future vehicle programs TBD
       pending asset sale resolution.
   * - Vayyar
     - XRR multi-range platform (0–300 m, single chip) in production; targeting 60 GHz
       in-cabin + 79 GHz ADAS dual-deployment on same vehicle platform. 4D imaging radar
       market projected at $1.2B by 2030 (MarketsandMarkets). No major new funding
       since $108M Series E in 2022.
   * - Cepton (Koito)
     - Under Koito ownership, Cepton is focused on GM Ultra Cruise scaling and potential
       expansion to additional GM/Honda models. Komodo SoC and Vista-X120 Plus represent
       the current product line. Koito's global Tier-1 infrastructure enables international
       deployment beyond North America.

----

Patent Landscape & IP Positioning
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 30 52

   * - Company
     - IP position
     - Key areas
   * - Teradar
     - Strong · $175M raised for IP development
     - THz chip architecture; solid-state THz imaging; on-chip TX/RX antenna arrays;
       material spectral fingerprinting; automotive THz fusion algorithms
   * - Arbe
     - Moderate · publicly disclosed chipset IP
     - 4D radar signal processing; 2,304-channel virtual aperture synthesis;
       ultra-high resolution imaging radar; MIMO radar architectures
   * - Mobileye
     - Very strong · decades of camera/CV patents
     - Computer vision for ADAS; RSS (Responsibility Sensitive Safety) — patented
       safety model; EyeQ SoC architecture; REM (Road Experience Management) mapping;
       imaging radar; sensor fusion
   * - Innoviz
     - Strong · MEMS LiDAR patents
     - MEMS scanning LiDAR; solid-state LiDAR beam steering; point cloud processing;
       LiDAR perception software (InnovizAPP); automotive-grade LiDAR packaging
   * - Luminar
     - Strong but at risk · bankruptcy may fragment IP
     - 1550 nm LiDAR receiver technology; Halo ASIC architecture; 5 custom silicon chips;
       behind-windshield integration methods; automotive LiDAR cost reduction IP
   * - Vayyar
     - Strong · multi-vertical radar-on-chip patents
     - 4D radar-on-chip integration; MIMO antenna arrays; in-cabin occupant detection;
       multi-range single-chip radar (0–300 m); vital sign detection; automotive radar fusion
   * - Cepton (Koito)
     - 37 patents · now Koito-owned
     - MMT® mirrorless, rotation-free LiDAR mechanism; frictionless optical scanning;
       behind-fascia/headlamp LiDAR integration; Komodo SoC processing architecture

----

Resolution & Range Comparison
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 20 18 18 18

   * - Platform
     - Angular resolution
     - Max range
     - Range resolution
     - FOV (H × V)
   * - Teradar
     - **0.1°** native THz
     - 300 m
     - ±1.5 cm
     - 120° × 30°
   * - Arbe Robotics
     - 1° az / 1.25° el
     - 300 m+
     - 9.5 cm @ 36 m
     - Wide (configurable)
   * - Mobileye
     - Sub-1° (camera)
     - 200 m+
     - Camera-limited
     - 360° surround
   * - Innoviz (InnovizTwo LR)
     - **0.05° × 0.05°**
     - 300 m (ULR: 1 km)
     - cm-level
     - 120° × 43°
   * - Luminar Iris
     - 0.05° H
     - **600 m**
     - cm-level
     - 120° × 30°
   * - Vayyar XRR
     - ~1–2° (radar-class)
     - 300 m
     - dm-level
     - Ultra-wide
   * - Cepton Vista-X90
     - 0.1° × 0.05°
     - 200 m
     - cm-level
     - 120° × 30°

----

All-Weather Performance
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 18 14 14 14 14 14

   * - Platform
     - Rain/fog
     - Dust
     - Glare/sun
     - Night
     - Physics basis
   * - Teradar
     - ✅
     - ✅
     - ✅
     - ✅
     - THz wave penetration
   * - Arbe
     - ✅
     - ✅
     - ✅
     - ✅
     - Radar physics
   * - Mobileye
     - ⚠️
     - ❌
     - ⚠️
     - ⚠️
     - Camera-dependent
   * - Innoviz
     - ⚠️
     - ⚠️
     - ✅
     - ✅
     - 905 nm LiDAR
   * - Luminar
     - ⚠️ (better)
     - ⚠️
     - ✅
     - ✅
     - 1550 nm LiDAR
   * - Vayyar
     - ✅
     - ✅
     - ✅
     - ✅
     - Radar physics
   * - Cepton
     - ⚠️
     - ⚠️
     - ✅
     - ✅
     - MMT® LiDAR

----

Engineering Recommendations
----------------------------

For an internal engineering team evaluating sensor architecture for L4/L5 ADAS as of
mid-2026:

**Immediate (now):**
Deploy Arbe (radar backbone) + Innoviz (LiDAR resolution layer) + Mobileye
(software/mapping/ECU). This stack covers weather robustness, angular resolution, ODD
mapping, and functional safety today. Innoviz's Fabrinet production line and NVIDIA
Hyperion integration make it the most accessible high-resolution LiDAR option.

**Medium-term (2026–2028):**
Integrate Teradar as the THz sensing layer when prototypes become available. Its
material fingerprinting and 0.1° resolution will elevate object classification accuracy
and reduce false positives in edge cases. The Teradar + Arbe redundancy pair (THz +
radar — entirely different physics, no shared failure mode) is the strongest available
argument for L4/L5 regulatory approval.

**Remove from consideration:**
Luminar — bankruptcy proceedings and asset fragmentation make program commitment
inadvisable until MicroVision acquisition closes and future OEM roadmap is confirmed.

**Watch list:**
Vayyar for cost-sensitive L2+ platforms where sensor consolidation (replacing 20+
sensors with 2–4 XRR chips) is a priority. Cepton/Koito for GM-ecosystem vehicles
where the Ultra Cruise supply chain is already established.
