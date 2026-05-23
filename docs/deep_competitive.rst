Deep Competitive Analysis: ADAS Sensing Landscape
==================================================

.. note::
   An interactive slide deck of this analysis is available at
   :doc:`/slides/deep_analysis`.

This document provides a comprehensive engineering-level comparison of six
sensing platforms competing in the ADAS and L4/L5 autonomy space, covering
resolution, weather performance, architecture, OEM traction, and production
readiness as of May 2025.

----

The Six Platforms
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Company
     - Technology
     - Key differentiator
   * - **Teradar**
     - Terahertz imaging (0.1–10 THz)
     - Only THz platform; material fingerprinting; 0.1° resolution; multi-vertical
   * - **Arbe Robotics**
     - 4D imaging radar (77 GHz)
     - 2,304 virtual channels; serial production; NVIDIA partnership
   * - **Mobileye**
     - Camera + radar fusion (EyeQ6H)
     - 230M+ vehicles; REM mapping; RSS safety model
   * - **Innoviz**
     - Solid-state LiDAR (InnovizTwo / Three)
     - 0.05° resolution; BMW L3 series production; 300 m range
   * - **Luminar**
     - 1550 nm LiDAR (Iris / Halo)
     - 600 m range; Volvo EX90 production (now disputed); Halo 2026
   * - **Vayyar**
     - 4D imaging radar (79 GHz)
     - Single-chip multi-range 0–300 m; replaces 20+ sensors; in-cabin + ADAS
   * - **Cepton**
     - MMT® LiDAR (mirrorless)
     - GM Ultra Cruise; largest LiDAR production award to date; Koito Tier-1

----

Resolution & Range Comparison
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 20 20 20 18

   * - Platform
     - Angular resolution
     - Max range
     - Range resolution
     - FOV (H × V)
   * - Teradar
     - **0.1°**
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
     - 0.05° (H)
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

.. note::
   Innoviz InnovizTwo ULR (launched April 2026) extends to 1 km at
   667 pts/deg² — the highest published long-range LiDAR spec to date.

----

All-Weather Performance
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 22 16 16 16 16 14

   * - Platform
     - Rain/fog/snow
     - Dust/sand
     - Glare/sun
     - Night
     - Basis
   * - Teradar
     - ✅ Excellent
     - ✅ Excellent
     - ✅ Immune
     - ✅ Full
     - THz physics
   * - Arbe Robotics
     - ✅ Excellent
     - ✅ Excellent
     - ✅ Immune
     - ✅ Full
     - Radar physics
   * - Mobileye
     - ⚠️ Degraded
     - ❌ Fails
     - ⚠️ Limited
     - ⚠️ Reduced
     - Camera-dependent
   * - Innoviz
     - ⚠️ Partial
     - ⚠️ Partial
     - ✅ Resilient
     - ✅ Full
     - 905 nm MEMS LiDAR
   * - Luminar
     - ⚠️ Partial
     - ⚠️ Partial
     - ✅ Resilient
     - ✅ Full
     - 1550 nm (better fog)
   * - Vayyar
     - ✅ Excellent
     - ✅ Excellent
     - ✅ Immune
     - ✅ Full
     - Radar physics
   * - Cepton
     - ⚠️ Partial
     - ⚠️ Partial
     - ✅ Resilient
     - ✅ Full
     - MMT® LiDAR

.. note::
   Luminar's 1550 nm wavelength has better fog penetration than 905 nm
   LiDAR (Innoviz, Cepton) but still degrades in heavy precipitation.
   Radar-based platforms (Teradar, Arbe, Vayyar) are uniquely immune.

----

Architecture & Integration
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 25 25 28

   * - Platform
     - Sensor type
     - Key chip / module
     - Integration notes
   * - Teradar
     - Solid-state THz CMOS
     - Modular THz Engine (MTE)
     - Behind-fascia; no cleaning; ISO 26262 / SAE 21434
   * - Arbe Robotics
     - Solid-state 4D radar
     - Phoenix 22 nm CMOS
     - Behind bumper/fascia; ASIL-D; NVIDIA AI partnership
   * - Mobileye
     - Camera + radar
     - EyeQ6H SoC
     - Single ECU; REM + RSS; 19M EyeQ6H committed
   * - Innoviz
     - MEMS solid-state LiDAR
     - InnovizTwo / Three chip
     - Roof / windshield; ASIL-B(D); InnovizAPP perception
   * - Luminar
     - Rotating 1550 nm LiDAR
     - Iris / Halo ASIC
     - Roof dome; Halo: behind-windshield; <10 W
   * - Vayyar
     - 4D radar-on-chip
     - XRR RFIC (79 GHz)
     - Single chip replaces 20+ sensors; 0–300 m multi-range
   * - Cepton
     - MMT® mirrorless LiDAR
     - Komodo SoC + Vista-X90
     - Fascia / headlamp / roof; frictionless; low power

----

OEM Traction & Production Status
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 35 43

   * - Platform
     - OEM / Tier-1 partnerships
     - Production status
   * - Teradar
     - Major OEMs & Tier-1s (US + Europe, undisclosed)
     - Pre-production testing; prototype 2026; volume 2028
   * - Arbe Robotics
     - HiRain (NVIDIA partnership, CES 2026)
     - Serial production Q4 2025 (LRR610)
   * - Mobileye
     - BMW, VW, Ford, GM, Nissan, 50+ OEMs
     - Mass market; 230M+ vehicles through 2025
   * - Innoviz
     - BMW (InnovizOne L3 Series 7), VW ADMT (ID. Buzz AD)
     - Series production; InnovizThree announced Dec 2025
   * - Luminar
     - Volvo EX90/ES90 (Iris); Mercedes-Benz (next-gen)
     - ⚠️ Volvo ended relationship Nov 2025; Halo initial 2026
   * - Vayyar
     - Multiple OEMs (undisclosed); Euro NCAP validated
     - Production-ready XRR; deployed in-cabin & ADAS
   * - Cepton (now Koito)
     - GM Ultra Cruise (Koito Tier-1); Honda (via Super Cruise)
     - Series production; largest LiDAR award to date; acquired by Koito 2023

----

Teradar Vertical Markets
-------------------------

Teradar's THz platform is uniquely positioned across four verticals, each
leveraging the same core sensor architecture.

Automotive ADAS
~~~~~~~~~~~~~~~

The primary commercial application. Teradar's Modular THz Engine (MTE)
targets L2–L5 vehicles as a replacement or complement to LiDAR:

- **Sub-millimeter resolution** at 300 m — 10× finer than imaging radar
- **All-weather** performance camera and LiDAR cannot match
- **Material fingerprinting** enables pedestrian vs. debris classification
- **ISO 26262 / SAE 21434** compliant; encrypted signal processing

Defense
~~~~~~~

Teradar's solid-state, low-SWAP-C design translates directly to military use:

- **UGV navigation** — drop-in LiDAR replacement for autonomous ground vehicles
  in Human-Machine Integrated Formations (HMIF)
- **Manned DVE** — degraded visual enhancement for Army/Marine Corps tactical
  vehicles in dust, fog, and rain
- **Counter-sUAS** — 4D imaging detects low-RCS plastic-bodied FPV drones
  that radar misses and EO/IR cannot range

Healthcare
~~~~~~~~~~

Teradar's MTE, adapted from automotive-grade sensing, has direct medical potential:

- **Non-ionizing imaging** — safe for repeated use; no DNA disruption
- **THz tissue contrast** — cancerous tissue's higher water content creates
  distinctive reflectivity patterns detectable at sub-mm resolution
- **Skin cancer detection** — in vivo studies confirm tumor margin visualization
- **Market:** $7.9B global skin cancer diagnostics opportunity; IEC/FDA
  regulatory groundwork underway for first THz medical systems by 2027

Security
~~~~~~~~

THz's material penetration and spectral fingerprinting directly enable:

- **Airport / stadium screening** — non-ionizing body scanning; >90% explosive
  detection sensitivity in field tests
- **Port cargo inspection** — distinguishes organic/inorganic substances
  without physical contact
- **Mail security** — 100% in-line non-destructive THz-AI package inspection

----

L4/L5 Autonomy Commercialization Roadmap
-----------------------------------------

Key challenges blocking L4/L5 at scale:

- **Weather robustness** — camera + LiDAR degrade in the 22% of accidents
  that happen in adverse conditions
- **Edge case handling** — novel scenarios not seen in training data
- **Sensor cost** — LiDAR historically too expensive for mass deployment
- **Redundancy** — regulatory bodies require diverse sensing modalities

How each platform addresses these:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Platform
     - L4/L5 readiness assessment
   * - Teradar
     - Highest technical ceiling (resolution + weather + fingerprinting);
       pre-production — not yet deployable at scale. Critical gap-filler
       when available 2026–2028.
   * - Arbe Robotics
     - Best available weather-robust high-resolution sensor in production today.
       NVIDIA partnership positions it as the radar backbone for highway L4.
   * - Mobileye
     - Software and mapping maturity (REM, RSS) is unmatched but camera-first
       architecture limits ODD in adverse weather. Needs radar/THz complement.
   * - Innoviz
     - Best LiDAR resolution in production (0.05°); BMW L3 proven; ULR at 1 km
       opens new use cases. Weather limitation remains the core LiDAR weakness.
   * - Luminar
     - 1550 nm gives best-in-class fog performance for LiDAR; Volvo dispute
       is a significant commercial risk signal for the platform.
   * - Vayyar
     - Strong for cost-sensitive L2+ / L3 deployments; single-chip replaces
       sensor arrays. Resolution insufficient for L4/L5 primary sensing alone.
   * - Cepton
     - GM Ultra Cruise is the largest LiDAR L2+ deployment. Koito acquisition
       secures Tier-1 supply chain. Weather limitation same as all LiDAR.

----

Engineering Recommendations
----------------------------

For an internal engineering team evaluating sensor architecture for L4/L5:

1. **Near-term (2025–2026):** Deploy Arbe (radar backbone) + Innoviz
   (LiDAR high-resolution) + Mobileye (software/mapping) as the primary
   sensor fusion stack. This covers weather robustness, resolution, and
   ODD mapping today.

2. **Medium-term (2026–2028):** Integrate Teradar as the THz layer.
   Its material fingerprinting and 0.1° resolution will elevate object
   classification and reduce false positives in edge cases — particularly
   for VRU protection and adverse weather scenarios.

3. **Watch list:** Luminar Halo (2026 availability, behind-windshield
   form factor) and Vayyar for cost-sensitive platforms where sensor
   count reduction is a priority.

4. **Redundancy design:** Teradar + Arbe provides a genuinely diverse
   sensing pair (THz + radar) that satisfies regulatory redundancy
   requirements without overlapping physics — no shared failure mode.
