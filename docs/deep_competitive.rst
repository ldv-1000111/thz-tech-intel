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
     - 2,304 virtual channels; Chinese OEM serial production; NVIDIA DRIVE integration
   * - **Mobileye**
     - Camera + radar + LiDAR fusion (EyeQ6H)
     - $1.9B 2025 revenue; in-house imaging radar (SOP 2028); closed vertical stack
   * - **Innoviz**
     - Solid-state LiDAR (InnovizTwo/Three)
     - 0.05° resolution; $55M 2025 revenue; Top-5 OEM L3 SOP 2027; dual ecosystem
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

Resolution & Range: Engineering Deep Dive
------------------------------------------

Understanding ADAS sensor resolution requires distinguishing two fundamentally different
and independent metrics that are frequently conflated in marketing materials.

Range Resolution
~~~~~~~~~~~~~~~~

Range resolution is the ability to separate two objects at **different distances along
the same radial line**. It is governed exclusively by the transmitted signal bandwidth:

.. code-block:: text

   ΔR = c / (2B)

   where:
     ΔR = range resolution (metres)
     c  = speed of light (3 × 10⁸ m/s)
     B  = swept bandwidth (Hz)

Bandwidth is the **only** variable. Target distance, transmit power, and antenna size
have no effect. This is a hard physical law derived from the Fourier uncertainty
principle: a signal occupying bandwidth B cannot resolve time differences shorter
than 1/B, corresponding to a range difference of c/(2B).

In FMCW automotive radar, bandwidth equals the chirp sweep range (f_stop − f_start).

Angular (Cross-Range) Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Angular resolution is the ability to separate two objects at the **same distance but
different lateral positions**. It is governed by the effective antenna aperture:

.. code-block:: text

   θ ≈ λ / D

   where:
     θ = angular resolution (radians)
     λ = wavelength (metres)
     D = effective aperture diameter (metres)

Lateral separability at range R:

.. code-block:: text

   lateral separation ≈ R × θ  (small angle approximation)

At 1° angular resolution (Arbe), lateral separability at range:

.. code-block:: text

   100 m  →  1.7 m lateral separation required
   200 m  →  3.5 m
   300 m  →  5.2 m

At 0.5° (Mobileye), these figures halve. At 0.1° (Teradar), they are 10× finer.

Physical vs Synthetic Aperture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Physical aperture** is the actual antenna size. A 77 GHz radar (λ ≈ 3.9 mm) achieving
0.1° angular resolution would require a 220 cm physical antenna — impossible on a vehicle.

**Synthetic aperture (MIMO)** simulates a larger effective aperture by combining signals
from multiple spatially distributed antenna elements:

.. code-block:: text

   virtual channels = N_TX × N_RX

Each unique TX-RX pair has a different spatial baseline, synthesising a larger effective
aperture than the physical hardware occupies. Angular resolution improvement scales with
aperture size — doubling virtual channels improves angular resolution by only √2, not ×2.

At THz frequencies (~300 GHz, λ ≈ 1 mm), the same physical aperture produces
proportionally finer angular resolution than 77 GHz radar — a fundamental physics
advantage of operating at higher carrier frequency.

Dynamic Range — the Long-Range Detection Factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dynamic range is the ratio between the largest and smallest signal the radar can process
simultaneously. It determines the ability to detect weak distant returns in the presence
of strong nearby returns — the critical capability for detecting a small hazard at 300 m
while a truck passes at 20 m.

.. code-block:: text

   Dynamic range of 60 dB  = 1,000,000 : 1 signal power ratio
   Dynamic range of 100 dB = 10,000,000,000 : 1 signal power ratio

The 40 dB gap between standard automotive radar (60 dB) and Mobileye's imaging radar
(100 dB) represents a 10,000× difference in simultaneous signal discrimination. This
is what enables detection of a tyre on the highway at 230 m while simultaneously
processing truck returns at 20 m — without receiver saturation masking distant objects.

.. note::
   Dynamic range improves long-range **detection sensitivity** but does not affect
   range **resolution**. Two objects separated by 9 cm in depth at 300 m still cannot
   be resolved regardless of dynamic range — only bandwidth governs that.

Side-lobe suppression (−40 dBc) is the complementary metric: it determines how much
energy the radar antenna leaks into unintended angular directions. High side lobes create
ghost targets in cluttered environments (tunnels, construction zones, dense traffic).
Mobileye's −40 dBc vs the industry-typical ~−20 dBc represents a 100× improvement in
spurious target rejection.

----

Sensor Resolution & Performance Comparison
--------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 16 14 16 14 14 8

   * - Platform
     - Angular res.
     - Max range
     - Range res.
     - Dynamic range
     - Side lobes
     - FOV
   * - Teradar
     - **0.1°** (inferred)
     - 300 m
     - **±1.5 cm** (~10 GHz BW)
     - Not disclosed
     - Not disclosed
     - 120°×30°
   * - Arbe Phoenix
     - 1° / 1.25°
     - 300 m+
     - 9.5 cm @ 36 m
     - ~60 dB (industry std)
     - Not published
     - Wide
   * - Mobileye Imaging Radar
     - **<0.5°**
     - **315 m**
     - Not published (77 GHz FMCW)
     - **100 dB**
     - **−40 dBc**
     - **170°**
   * - Innoviz InnovizTwo LR
     - **0.05°×0.05°**
     - 300 m (ULR: 1 km)
     - cm (pulsed ToF)
     - N/A (LiDAR)
     - N/A
     - 120°×43°
   * - Luminar Iris
     - 0.05° H
     - **600 m**
     - cm (pulsed ToF)
     - N/A (LiDAR)
     - N/A
     - 120°×30°
   * - Vayyar XRR
     - ~1–2°
     - 300 m
     - dm-level
     - Not published
     - Not published
     - Ultra-wide
   * - Cepton Vista-X90
     - 0.1°×0.05°
     - 200 m
     - cm (pulsed ToF)
     - N/A (LiDAR)
     - N/A
     - 120°×30°

.. note::
   **Teradar disclosure gap.** The whitepapers state performance outputs only. The ~10 GHz
   bandwidth is back-calculated from ΔR = c/(2B). MIMO/synthetic aperture use is inferred
   — the only physically plausible mechanism to achieve 0.1° at chip scale. Carrier
   frequency (~300 GHz), TX/RX channel count, points-per-frame, dynamic range, and
   side-lobe levels are not published. Standard pre-production disclosure behaviour.
   OEM engineering teams should request full architecture disclosure during evaluation.

   **Mobileye range resolution gap.** Mobileye does not publish a bandwidth or range
   resolution figure for its imaging radar. The 77 GHz FMCW architecture means the same
   ΔR = c/(2B) physics apply — range resolution is bandwidth-limited regardless of
   dynamic range. The 315 m detection range and 100 dB dynamic range are detection
   sensitivity figures, not depth resolution figures.

----

Bandwidth and Range Resolution: Carrier Frequency Effect
----------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 20 20 20

   * - Sensor
     - Carrier
     - Bandwidth used
     - Range resolution
     - Notes
   * - Conventional 77 GHz radar
     - 77 GHz
     - ~500 MHz
     - ~30 cm
     - Long-range chirp mode
   * - Arbe Phoenix
     - 77 GHz
     - ~1.6 GHz
     - ~9.5 cm
     - Short-range mode only
   * - Mobileye Imaging Radar
     - 77 GHz (FMCW)
     - Not disclosed
     - Not disclosed
     - Detection to 315 m; ΔR physics same as Arbe
   * - 77 GHz theoretical limit
     - 77 GHz
     - 5 GHz (full band)
     - ~3 cm
     - Not achieved in practice
   * - Teradar MTE
     - ~300 GHz (inferred)
     - ~10 GHz (inferred)
     - ~1.5 cm
     - Back-calculated from spec
   * - LiDAR (Innoviz/Luminar)
     - ~200 THz
     - N/A (pulsed ToF)
     - cm-level
     - Time-of-flight physics

.. warning::
   Arbe's 9.5 cm range resolution applies **only** in its short-range wide-bandwidth
   chirp mode. In long-range mode (300 m detection), a narrower bandwidth chirp is used,
   yielding approximately 30–75 cm range resolution. Fine range resolution and maximum
   detection range cannot be achieved simultaneously in a single chirp configuration.
   This applies equally to Mobileye's 77 GHz FMCW radar — the 315 m detection range
   is achieved with a narrow-bandwidth long-range chirp whose range resolution is
   not published but is subject to the same physics.

----

Highway Autonomy: Binding Constraints Analysis
------------------------------------------------

At highway speeds, three distinct physical constraints determine L4/L5 viability.
They are independent and must each be satisfied simultaneously.

**Constraint 1 — Angular resolution at range**

At 130 km/h, 8 seconds of reaction time is available at 300 m. The question is whether
the sensor can laterally separate close objects at that range:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Sensor
     - Angular res.
     - Lateral sep. @ 200 m
     - Lateral sep. @ 300 m
   * - Teradar
     - 0.1°
     - 0.35 m
     - 0.52 m
   * - Mobileye Imaging Radar
     - <0.5°
     - <1.75 m
     - <2.6 m
   * - Arbe Phoenix
     - 1°
     - 3.5 m
     - 5.2 m
   * - Innoviz / Luminar
     - 0.05°
     - 0.17 m
     - 0.26 m

**Constraint 2 — Long-range detection sensitivity**

Ability to detect small objects (tyre debris, pedestrian) at 200–315 m against a
cluttered background of large vehicles. Governed by dynamic range and side-lobe
suppression — not angular resolution or bandwidth.

Mobileye's 100 dB dynamic range and −40 dBc side-lobe suppression make it the
strongest 77 GHz radar for this constraint. Arbe's ~60 dB dynamic range is
industry-standard but 10,000× lower simultaneous signal discrimination.

**Constraint 3 — Range (depth) resolution at long range**

Ability to separate two objects at the same angle but different depths at 200–300 m.
Governed purely by chirp bandwidth. All 77 GHz FMCW radars (Arbe, Mobileye,
Vayyar) are subject to the same physics — achievable range resolution at 300 m
is approximately 30–75 cm in long-range chirp modes. Only THz (Teradar, ~1.5 cm)
and LiDAR (Innoviz/Luminar, cm-level ToF) resolve this constraint.

**Summary:**

.. list-table::
   :header-rows: 1
   :widths: 28 18 18 18 18

   * - Sensor
     - Angular sep.
     - Detection sensitivity
     - Range res. @ 300 m
     - Highway L4 viability
   * - Teradar
     - ✅ Best (0.1°)
     - ❓ Not disclosed
     - ✅ Best (~1.5 cm)
     - High (if specs confirmed)
   * - Mobileye Imaging Radar
     - ✅ Good (<0.5°)
     - ✅ Best (100 dB)
     - ⚠️ Not disclosed (77 GHz)
     - Good (within EyeQ only)
   * - Arbe Phoenix
     - ⚠️ Limited (1°)
     - ⚠️ Standard (~60 dB)
     - ⚠️ ~30–75 cm @ 300 m
     - Fusion required
   * - Innoviz / Luminar
     - ✅ Best (0.05°)
     - ✅ Excellent
     - ✅ cm-level
     - ⚠️ Weather-limited

----

Mobileye Imaging Radar: Architecture Deep Dive
------------------------------------------------

Mobileye's imaging radar has been in development since 2018 — seven years of proprietary
R&D — and achieved its first OEM nomination in May 2025 with SOP targeted for 2028.
Key architectural details:

**Hardware:**

- Proprietary RFIC (Radio Frequency Integrated Circuit) components — not third-party
- Dedicated radar SoC with 11 TOPS of on-chip compute — all processing on-chip,
  no dependency on NVIDIA DRIVE AGX or external GPU
- Massive MIMO TX/RX architecture — 1,500+ virtual channels
- 170° field of view — the widest published FOV in automotive radar
- −40 dBc side-lobe suppression — 100× better than industry ~−20 dBc
- 100 dB dynamic range — 10,000× wider than industry standard 60 dB
- 20 frames per second processing rate

**Integration within Mobileye stack:**

The imaging radar is not a standalone product. It is designed exclusively as a redundancy
layer within Mobileye's closed EyeQ ecosystem:

- **Surround ADAS:** EyeQ6H + 5 cameras + multiple Mobileye radars (hands-off, eyes-on)
- **Chauffeur L3:** 4× EyeQ6H + cameras + imaging radar + front LiDAR (Innoviz)
- **Drive L4:** EyeQ Ultra + cameras + imaging radar + surround LiDAR (Innoviz)

This is the critical architectural distinction: Mobileye's radar is a **sensor within
a closed system**, not a standalone sensor available to OEMs independently. An OEM
cannot buy Mobileye's imaging radar without buying the entire EyeQ stack.

**What Mobileye radar does not disclose:**

- Chirp bandwidth and derived range resolution
- Carrier frequency (implied 77 GHz FMCW from architecture description)
- Detection range in adverse weather (fog, heavy rain)
- Performance in long-range mode vs short-range mode separately

----

Arbe / NVIDIA Partnership: Technical Details
---------------------------------------------

The partnership is a **software and compute integration**, not a co-development or
equity arrangement. The structure is a three-way stack:

.. code-block:: text

   Layer 1  Arbe Phoenix radar chipset
            2,304-channel point cloud · 20,000+ detections/frame · all-weather

   Layer 2  NVIDIA DRIVE AGX Orin compute platform
            AI inference on the dense radar point cloud

   Layer 3  Perciv AI software
            AI-based Occupancy Grid — detailed spatial map of vehicle surroundings

The full stack runs on NVIDIA's DRIVE Hyperion autonomous driving reference platform,
reducing OEM integration engineering overhead significantly.

**CES 2025:** Radar-based free space mapping on DRIVE AGX Orin.

**CES 2026:** Live AI-based Occupancy Grid demo; direct LiDAR performance comparison
demonstrating Arbe's all-weather advantage in degraded visibility.

**What this partnership is not:**

- Not exclusive — NVIDIA Hyperion simultaneously supports Innoviz LiDAR and others
- Not a production contract — a reference platform integration and go-to-market tool
- Not equity-backed — no investment component disclosed
- Not relevant to Mobileye EyeQ OEMs — Mobileye runs its own radar on its own silicon

**How Arbe and Mobileye radar relate:**

They do not compete directly in the same architecture. Mobileye radar is exclusively
for EyeQ-based vehicles (closed system, SOP 2028). Arbe radar is exclusively for
NVIDIA DRIVE-based vehicles and independent OEM stacks (available now in China,
Western SOP 2028–2030). An OEM must choose between the two ecosystems at the
vehicle platform design stage — sensor selection is downstream of that decision.

----

The Two Compute Ecosystem Split
---------------------------------

The most important strategic context for evaluating all sensor companies is the
fundamental split between two incompatible compute ecosystems:

.. code-block:: text

   MOBILEYE EyeQ ECOSYSTEM (closed vertical integration)
   ├── Compute:  Mobileye EyeQ SoC family (not NVIDIA)
   ├── Cameras:  Mobileye-specified
   ├── Radar:    Mobileye Imaging Radar (in-house, SOP 2028)
   ├── LiDAR:    Innoviz (Chauffeur/Drive only)
   ├── Software: Mobileye closed stack (perception, REM, RSS)
   └── Sensors not in scope: Arbe, Vayyar, Teradar, Cepton

   NVIDIA DRIVE ECOSYSTEM (open platform)
   ├── Compute:  DRIVE Orin (254 TOPS) / Thor (2,000 TOPS)
   ├── Cameras:  OEM/Tier-1 choice
   ├── Radar:    Arbe Phoenix (DRIVE-integrated via NVIDIA partnership)
   ├── LiDAR:    Innoviz (Hyperion 8) / others
   ├── Software: OEM or Tier-1 built on DRIVE OS + TensorRT
   └── Flexibility: Full sensor substitution, higher integration effort

Innoviz is the only sensor company present in **both** ecosystems — Mobileye Drive
(as primary LiDAR) and NVIDIA Hyperion 8 (as validated sensor option). This is
what makes Innoviz the most strategically positioned sensor supplier in the field.

----

All-Weather Performance
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 13 13 13 13 14

   * - Platform
     - Rain/fog
     - Dust
     - Glare/sun
     - Night
     - Physics basis
   * - Teradar
     - ✅ Full
     - ✅ Full
     - ✅ Immune
     - ✅ Full
     - THz wave penetration
   * - Arbe
     - ✅ Full
     - ✅ Full
     - ✅ Immune
     - ✅ Full
     - 77 GHz radar physics
   * - Mobileye Imaging Radar
     - ✅ Full
     - ✅ Full
     - ✅ Immune
     - ✅ Full
     - 77 GHz radar physics
   * - Mobileye (cameras only)
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
     - 905 nm LiDAR
   * - Luminar
     - ⚠️ Better
     - ⚠️ Partial
     - ✅ Resilient
     - ✅ Full
     - 1550 nm LiDAR
   * - Vayyar
     - ✅ Full
     - ✅ Full
     - ✅ Immune
     - ✅ Full
     - 77 GHz radar physics
   * - Cepton
     - ⚠️ Partial
     - ⚠️ Partial
     - ✅ Resilient
     - ✅ Full
     - MMT® LiDAR

.. note::
   Mobileye's all-weather performance characterisation now requires qualification by
   product. Mobileye Chauffeur and Drive (with imaging radar) have full all-weather
   radar coverage. Mobileye Surround ADAS and SuperVision (cameras + limited radar)
   remain weather-constrained. The imaging radar changes Mobileye's weather profile
   but only for its L3/L4 products, not its high-volume L2 ADAS business.

----

Financial Snapshot
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 22 22 22 16

   * - Company
     - Total funding
     - Latest round
     - 2025 revenue
     - Status
   * - Teradar
     - $175M
     - $150M Series B — Nov 2025
     - Pre-revenue
     - Private · 62 employees
   * - Arbe
     - ~$200M+
     - $18.5M direct — Feb 2026
     - ~$1–2M
     - Nasdaq: ARBE · $52M cash
   * - Mobileye
     - Public
     - —
     - **$1,894M** (+15% YoY)
     - Nasdaq: MBLY · $1.8B cash
   * - Innoviz
     - ~$300M+
     - $40M direct — Feb 2025
     - **$55M** (>2× 2024)
     - Nasdaq: INVZ · $95M NRE pipeline
   * - Luminar
     - $306M
     - DIP bankruptcy financing
     - ~$67–74M
     - **Chapter 11** Dec 2025
   * - Vayyar
     - $296M
     - $108M Series E — Jun 2022
     - Undisclosed
     - Private · $1B valuation
   * - Cepton (Koito)
     - $226M
     - Acquired Jan 2025
     - Koito-consolidated
     - Koito subsidiary

.. warning::
   Luminar filed Chapter 11 in December 2025. MicroVision agreed to acquire LiDAR assets
   January 2026. Do not commit to new Luminar programmes until acquisition closes and a
   confirmed roadmap is available.

----

OEM Design Win Tracker
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 18 42 20 20

   * - Company
     - Confirmed programmes
     - Autonomy level
     - Production status
   * - Teradar
     - 5 US/EU OEMs + 3 Tier-1s (undisclosed); Lockheed Martin Ventures investor
     - L2–L5
     - Production win targeted 2028
   * - Arbe
     - Chinese state OEM via Hirain LRR610 (L4); European OEM L3 data collection;
       AI compute co. dev kits; European OEM strategic award not expected near-term
     - L3–L4
     - Serial production China; RFI stage EU/US
   * - Mobileye
     - VW (L2++/L3/robotaxi), Mahindra (SuperVision + Surround), major US OEM
       (Surround), 50+ others; imaging radar first OEM nomination May 2025 (SOP 2028)
     - L2–L4
     - Mass production · 230M+ vehicles
   * - Innoviz
     - BMW Series 7 L3, VW ADMT ID. Buzz, Top-5 OEM (L3 SOP 2027),
       Mobileye Drive, NVIDIA Hyperion 8
     - L3–L4
     - Series production; SOP ramp 2026–2027
   * - Luminar
     - Volvo EX90/ES90 (terminated Nov 2025); Mercedes-Benz (status unclear)
     - L3
     - **Disrupted** — Chapter 11
   * - Vayyar
     - Multiple undisclosed OEMs; Euro NCAP validated; 35% NCAP points from
       2–4 external + 1 in-cabin sensors
     - L2–L3
     - Production-ready · deployed
   * - Cepton (Koito)
     - GM Ultra Cruise (Cadillac +); Honda (Super Cruise ecosystem)
     - L2+
     - Series production

----

Technology Roadmap Timeline
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 14 86

   * - Period
     - Milestones
   * - Q4 2025
     - Arbe: Hirain LRR610 serial production (China L4). Innoviz: InnovizThree launch
       (35% cost cut). Luminar: Chapter 11; Volvo termination. Teradar: stealth exit;
       $150M Series B; CES 2026 debut.
   * - Q1–Q2 2026
     - Mobileye: VW/MOIA robotaxi pre-series production; Mahindra SuperVision win.
       Innoviz: ULR 1 km range launched April 2026; Top-5 OEM SOP discussions.
       Luminar/MicroVision: Halo B-sample (Q2). Arbe: new CEO Ram Machness (Apr 2026);
       multi-market pivot to defense/robotaxi/off-road.
   * - 2026
     - Teradar: prototype availability US and Europe. Arbe: 4 OEM design-in target
       (Western). Mobileye: 37M+ IQ unit guidance; imaging radar OEM development.
       Innoviz: Fabrinet high-volume line ramping.
   * - 2027
     - Innoviz: Top-5 OEM L3 SOP. Mobileye: Chauffeur L3 production ramp with VW.
       IEC/FDA THz medical regulatory groundwork. Vayyar: 4D radar market scaling.
   * - 2028
     - Teradar: global high-volume production target. Arbe: Western automotive
       production contingent on 2026 design wins. Mobileye imaging radar SOP.
       Industry THz ADAS deployment expected.
   * - 2028+
     - Luminar (MicroVision): next-gen vehicle programmes (deferred).
       Full L4/L5 ODD expansion across surviving platforms.

----

Patent Landscape & IP Positioning
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 30 52

   * - Company
     - IP position
     - Key patent areas
   * - Teradar
     - Strong · greenfield THz
     - THz chip architecture; solid-state THz imaging; on-chip TX/RX antennas;
       material spectral fingerprinting; automotive THz fusion.
       **No incumbent holds meaningful THz automotive patents — window is 2025–2028.**
   * - Arbe
     - Moderate · disclosed chipset IP
     - 4D FMCW signal processing; 2,304-channel virtual aperture synthesis;
       ultra-high resolution imaging radar; automotive MIMO architectures
   * - Mobileye
     - **Very strong · 2,000+ patents**
     - Computer vision ADAS; RSS safety model (patented — potential ISO standard);
       EyeQ SoC; REM mapping; imaging radar RFIC architecture (patents US12123937,
       US11747457 covering multi-static distributed radar aperture synthesis);
       side-lobe suppression techniques; 100 dB dynamic range radar architecture
   * - Innoviz
     - Strong · MEMS LiDAR
     - MEMS scanning LiDAR; solid-state beam steering; point cloud processing;
       InnovizAPP perception software; automotive-grade LiDAR packaging
   * - Luminar
     - Strong but at risk
     - 1550 nm LiDAR receiver; Halo ASIC (5 custom chips); behind-windshield
       integration; LiDAR cost reduction IP. Bankruptcy may fragment ownership.
   * - Vayyar
     - Strong · multi-vertical
     - 4D radar-on-chip integration; MIMO antenna arrays; in-cabin occupant detection;
       multi-range single-chip radar; vital sign detection
   * - Cepton (Koito)
     - 37 patents · Koito-owned
     - MMT® mirrorless LiDAR mechanism; frictionless optical scanning;
       behind-fascia/headlamp integration; Komodo SoC architecture

.. note::
   **Mobileye RSS patent risk.** The Responsibility Sensitive Safety (RSS) model defines
   a mathematical framework for assigning fault in AV incidents. If RSS becomes an ISO
   standard (actively pursued by Mobileye), it could lock OEMs into Mobileye's broader
   software stack even if they source sensors elsewhere.

   **Mobileye imaging radar IP.** Patent US11747457 discloses a multi-static radar system
   with spatially distributed units synthesising a larger aperture across the vehicle.
   Combined with US12123937 (compact transmitter with digital-to-analog converters and
   analog beamforming), Mobileye holds a growing imaging radar IP position that will
   constrain third-party radar suppliers attempting to match the 100 dB / −40 dBc
   performance within the same architectural approach.

----

Engineering Recommendations
----------------------------

**Immediate (now):**
Arbe (radar backbone — all-weather, velocity accuracy, stationary object detection,
available in production) + Innoviz (LiDAR — 0.05° angular resolution at range,
in production) + Mobileye EyeQ6H (software stack, mapping, single-ECU integration,
$1.9B revenue platform). This covers all binding constraints available today.

**Medium-term (2026–2028):**
Add Teradar as the THz sensing layer when prototypes are available (2026) and
production is confirmed (2028). The Teradar + Arbe pairing provides the strongest
available redundancy argument for L4/L5 regulatory approval — THz and 77 GHz radar
share no physical failure modes. Teradar's 0.1° angular resolution and material
fingerprinting will improve edge-case object classification at long range in ways
no 77 GHz radar can match regardless of dynamic range or channel count.

**If building on Mobileye EyeQ stack:**
Mobileye's imaging radar (SOP 2028) becomes the natural radar choice — integrated,
validated, and economically bundled within the EyeQ ecosystem. Arbe is not in scope
for EyeQ-based vehicles. Innoviz remains in scope for Chauffeur and Drive tiers only.

**If building on NVIDIA DRIVE platform:**
Arbe (radar) + Innoviz (LiDAR) + Teradar (THz, from 2026/2028) is the recommended
stack. Mobileye's imaging radar is not available outside the EyeQ ecosystem.

**Remove from consideration:**
Luminar — until MicroVision acquisition closes and a confirmed OEM roadmap exists.

**Watch list:**
Vayyar for cost-sensitive L2+ platforms prioritising sensor consolidation (replacing
20+ sensors with 2–4 XRR chips). Cepton/Koito for GM-ecosystem vehicles.
