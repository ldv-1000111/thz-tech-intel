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
     - 2,304 virtual channels; Chinese OEM serial production win; NVIDIA DRIVE integration
   * - **Mobileye**
     - Camera + radar fusion (EyeQ6H)
     - $1.9B 2025 revenue; $24.5B pipeline; VW robotaxi; Mentee Robotics acquisition
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

Resolution & Range: Engineering Deep Dive
------------------------------------------

Understanding ADAS sensor resolution requires distinguishing two fundamentally different
and independent metrics that are frequently conflated in marketing materials.

Range Resolution
~~~~~~~~~~~~~~~~

Range resolution is the ability to separate two objects at **different distances along
the same radial line** — can the sensor distinguish a car at 36.0 m from a car at
36.095 m? It is governed exclusively by the transmitted signal bandwidth:

.. code-block:: text

   ΔR = c / (2B)

   where:
     ΔR = range resolution (metres)
     c  = speed of light (3 × 10⁸ m/s)
     B  = swept bandwidth (Hz)

Bandwidth is the **only** variable. Target distance, transmit power, and antenna size
have no effect on range resolution. This is a hard physical law derived from the
Fourier uncertainty principle: a signal occupying bandwidth B cannot resolve time
differences shorter than 1/B, corresponding to a range difference of c/(2B).

In FMCW automotive radar, bandwidth equals the chirp sweep range (f_stop − f_start).
The wider the frequency sweep, the finer the range resolution.

Angular (Cross-Range) Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Angular resolution is the ability to separate two objects at the **same distance but
different lateral positions** — can the sensor distinguish a cyclist from a car 1 metre
to its left at 200 m range? It is governed by the antenna aperture:

.. code-block:: text

   θ ≈ λ / D

   where:
     θ = angular resolution (radians)
     λ = wavelength (metres)
     D = effective aperture diameter (metres)

Lateral separability at range R:

.. code-block:: text

   lateral separation = R × tan(θ) ≈ R × θ  (small angle approximation)

At Arbe's 1° angular resolution, lateral separability degrades linearly with range:

.. code-block:: text

   100 m  →  1.7 m lateral separation required to resolve two objects
   200 m  →  3.5 m
   300 m  →  5.2 m

At Teradar's 0.1° angular resolution, these figures are 10× finer at every range.

Physical vs Synthetic Aperture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Physical aperture** is the actual antenna size. A 77 GHz radar (λ ≈ 3.9 mm) achieving
0.1° angular resolution would require a 220 cm physical antenna — impossible on a vehicle.

**Synthetic aperture (MIMO)** simulates a larger effective aperture by combining signals
from multiple spatially distributed antenna elements:

.. code-block:: text

   virtual channels = N_TX × N_RX

Each unique TX-RX pair has a different spatial baseline, synthesising a larger effective
aperture than the physical hardware occupies. Arbe's 48 TX × 48 RX array creates 2,304
virtual channels and achieves 1° angular resolution from a bumper-mounted device. Angular
resolution improvement scales with aperture size — doubling virtual channels improves
angular resolution by only √2, not ×2.

At THz frequencies (~300 GHz, λ ≈ 1 mm), the same physical aperture produces
proportionally finer angular resolution than 77 GHz radar. The shorter wavelength means
fewer virtual channels are needed to achieve the same effective aperture — a fundamental
physics advantage of operating at higher carrier frequency, not an engineering achievement.

Sensor Resolution Comparison
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 18 21 16 25 20

   * - Platform
     - Angular resolution
     - Max range
     - Range resolution
     - FOV (H × V)
   * - Teradar
     - **0.1°** (inferred MIMO)
     - 300 m
     - **±1.5 cm** (implies ~10 GHz BW)
     - 120° × 30°
   * - Arbe Robotics
     - 1° az / 1.25° el
     - 300 m+
     - 9.5 cm @ 36 m (1.6 GHz BW)
     - Wide (configurable)
   * - Mobileye
     - Sub-1° (camera)
     - 200 m+
     - Camera-limited
     - 360° surround
   * - Innoviz (InnovizTwo LR)
     - **0.05° × 0.05°**
     - 300 m (ULR: 1 km)
     - cm-level (pulsed ToF)
     - 120° × 43°
   * - Luminar Iris
     - 0.05° H
     - **600 m**
     - cm-level (pulsed ToF)
     - 120° × 30°
   * - Vayyar XRR
     - ~1–2°
     - 300 m
     - dm-level
     - Ultra-wide
   * - Cepton Vista-X90
     - 0.1° × 0.05°
     - 200 m
     - cm-level (pulsed ToF)
     - 120° × 30°

.. note::
   **Teradar disclosure gap.** The whitepapers state performance outputs only. The ~10 GHz
   bandwidth is back-calculated from ΔR = c/(2B). MIMO/synthetic aperture use is inferred
   — it is the only physically plausible mechanism to achieve 0.1° at chip scale at
   ~300 GHz. Carrier frequency (~300 GHz), TX/RX channel count, and points-per-frame are
   not published. This is standard pre-production disclosure behaviour. OEM engineering
   teams should request full architecture disclosure during evaluation.

----

Bandwidth and Range Resolution: Carrier Frequency Effect
----------------------------------------------------------

Higher carrier frequency enables wider absolute bandwidth at the same fractional sweep,
directly driving range resolution improvement:

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
     - Short-range chirp mode only
   * - 77 GHz theoretical limit
     - 77 GHz
     - 5 GHz (full band)
     - ~3 cm
     - Not achieved in practice
   * - Teradar MTE
     - ~300 GHz (inferred)
     - ~10 GHz (inferred)
     - ~1.5 cm
     - Published spec; BW back-calculated
   * - LiDAR (Innoviz/Luminar)
     - ~200 THz
     - N/A (pulsed ToF)
     - cm-level
     - Time-of-flight, not FMCW

.. warning::
   Arbe's 9.5 cm range resolution applies **only** in its short-range wide-bandwidth
   chirp mode. In long-range mode (300 m detection), a narrower bandwidth chirp is used,
   yielding approximately 30–75 cm range resolution — comparable to conventional radar.
   Fine range resolution and maximum detection range cannot be achieved simultaneously
   in a single chirp configuration. Multi-mode chirp scheduling is a fundamental
   limitation of FMCW radar at 77 GHz.

----

Highway Autonomy: The Angular Resolution Constraint
-----------------------------------------------------

At highway speeds, **angular resolution is the binding constraint** for L4/L5 perception
— not range resolution. At 130 km/h (~36 m/s) with 300 m detection range, approximately
8 seconds of reaction time is available. The critical question is not depth accuracy —
it is **lateral object separability**: can the sensor resolve a motorcyclist from an
adjacent truck at 250 m?

Arbe's 1° angular resolution at 300 m requires 5.2 m of lateral separation to resolve
two objects. Adjacent lane vehicles may merge into a single radar return. This is a
category constraint of 77 GHz FMCW physics — not specific to Arbe. Doubling virtual
channels to 4,608 would improve angular resolution by only √2 (~0.7°), at doubled
cost and power.

**Where Arbe excels at highway speeds** is velocity resolution and stationary object
detection — precise Doppler separation of dozens of simultaneous targets, and reliable
detection of stopped vehicles or road debris that conventional radar misses entirely.

For L4/L5 highway autonomy, 77 GHz radar alone is insufficient as a primary sensor.
It must be fused with a high-resolution sensor (LiDAR at 0.05° or THz at 0.1°).
This is precisely the architecture the Arbe/NVIDIA partnership is designed to enable.

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

The full stack runs on NVIDIA's DRIVE Hyperion autonomous driving reference platform.
The value to OEMs is pre-validated integration across all three layers, significantly
reducing integration engineering overhead.

**CES 2025:** Radar-based free space mapping demonstration on DRIVE AGX Orin.

**CES 2026:** Live AI-based Occupancy Grid demo with Perciv AI; direct LiDAR performance
comparison demonstrating Arbe's all-weather advantage in degraded visibility conditions.

**What this partnership is not:**

- Not exclusive — NVIDIA Hyperion simultaneously supports Innoviz LiDAR and other vendors
- Not a production contract — it is a reference platform integration and go-to-market tool
- Not equity-backed — no investment component disclosed
- Not a replacement for OEM design wins — it accelerates the path to them

The strategic logic: OEMs building on NVIDIA DRIVE Hyperion (increasingly common for
L3+ architectures) receive Arbe's radar pre-integrated, shortening the sensor evaluation
to production programme timeline.

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

.. note::
   Luminar's 1550 nm wavelength has better fog penetration than 905 nm LiDAR (Innoviz,
   Cepton) due to lower atmospheric scattering at longer wavelengths. All LiDAR degrades
   in heavy precipitation. THz and radar platforms (Teradar, Arbe, Vayyar) have full
   all-weather immunity — a physics advantage, not an engineering one.

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
     - **$1,894M**
     - Nasdaq: MBLY · $1.8B cash
   * - Innoviz
     - ~$300M+
     - $40M direct — Feb 2025
     - **$55M**
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
   January 2026. Do not commit to new Luminar programmes until acquisition closes.

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
     - 5 US/EU OEMs + 3 Tier-1s (undisclosed)
     - L2–L5
     - Win targeted 2028
   * - Arbe
     - Chinese state OEM (Hirain LRR610 L4); European OEM (L3 data collection); AI compute co.
     - L3–L4
     - Serial production China; RFI stage EU/US
   * - Mobileye
     - VW (L2++/L3/robotaxi), Mahindra, major US OEM, 50+ others
     - L2–L4
     - Mass production · 230M+ vehicles
   * - Innoviz
     - BMW Series 7 L3, VW ADMT ID. Buzz, Top-5 OEM (L3 SOP 2027), Mobileye Drive
     - L3–L4
     - Series production; SOP ramp 2026–2027
   * - Luminar
     - Volvo EX90/ES90 (terminated); Mercedes-Benz (status unclear)
     - L3
     - **Disrupted** — Chapter 11
   * - Vayyar
     - Multiple undisclosed OEMs; Euro NCAP validated
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
     - Arbe: Hirain LRR610 serial production (China L4). Innoviz: InnovizThree launch.
       Luminar: Chapter 11 filing; Volvo termination. Mobileye: imaging radar L3 design win.
       Teradar: stealth exit; $150M Series B; CES 2026 debut.
   * - Q1–Q2 2026
     - Mobileye: VW/MOIA robotaxi pre-series production. Innoviz: Top-5 OEM SOP discussions.
       Luminar/MicroVision: Halo B-sample (Q2). Arbe: new CEO; multi-market pivot.
       Innoviz ULR 1 km range launched April 2026.
   * - 2026
     - Teradar: prototype availability US and Europe. Arbe: 4 OEM design-in target (Western).
       Mobileye: 37M+ IQ unit guidance. Innoviz: Fabrinet high-volume line ramping.
   * - 2027
     - Innoviz: Top-5 OEM L3 programme SOP. Mobileye: Chauffeur L3 production ramp.
       IEC/FDA THz medical regulatory groundwork. Vayyar: 4D radar market scaling.
   * - 2028
     - Teradar: global high-volume production. Arbe: Western automotive production
       (contingent on 2026 design wins). Industry THz ADAS deployment expected.
   * - 2028+
     - Luminar (MicroVision): next-gen vehicle programmes (deferred). Full L4/L5 ODD
       expansion across surviving platforms.

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
       No incumbent holds meaningful THz automotive patents — window is 2025–2028.
   * - Arbe
     - Moderate · disclosed chipset IP
     - 4D FMCW signal processing; 2,304-channel virtual aperture synthesis;
       ultra-high resolution imaging radar; automotive MIMO architectures
   * - Mobileye
     - Very strong · decades of IP
     - Computer vision ADAS; RSS safety model (patented — potential ISO standard);
       EyeQ SoC architecture; REM mapping; imaging radar; sensor fusion
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
   software stack even if they source sensors elsewhere. This is a software moat that
   extends beyond hardware competition.

----

Engineering Recommendations
----------------------------

**Immediate (now):**
Arbe (radar backbone — all-weather, velocity accuracy, stationary object detection)
+ Innoviz (LiDAR — 0.05° angular resolution at range) + Mobileye (software stack,
mapping, single-ECU integration). Covers all binding constraints available today.

**Medium-term (2026–2028):**
Add Teradar as the THz sensing layer. The Teradar + Arbe pairing provides the strongest
available redundancy argument for L4/L5 regulatory approval — THz and 77 GHz radar
share no physical failure modes. Teradar's 0.1° angular resolution and material
fingerprinting will improve edge-case object classification at range.

**Remove from consideration:**
Luminar — until MicroVision acquisition closes and a confirmed OEM roadmap exists.

**Watch list:**
Vayyar for cost-sensitive L2+ platforms prioritising sensor consolidation.
Cepton/Koito for GM-ecosystem vehicles where Ultra Cruise supply chain is established.
