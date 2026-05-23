ADAS Sensing Deep Analysis
==========================

.. revealjs-slide::
   :theme: black

.. raw:: revealjs

   <p class="subtitle">Teradar · Arbe · Mobileye · Innoviz · Luminar · Vayyar · Cepton</p>
   <p class="subtitle" style="font-size:0.6em; color:#555;">Internal Engineering Review — May 2025</p>

----

Agenda
------

.. revealjs-section::
   :data-background-color: "#0a0a0a"

.. raw:: revealjs

   <div class="col-2" style="margin-top:0.5em;">
     <div class="card">
       <h4>Part 1 — Competitive Landscape</h4>
       <ul>
         <li>The 7-platform field</li>
         <li>Resolution &amp; range deep dive</li>
         <li>All-weather performance matrix</li>
         <li>Architecture &amp; integration</li>
         <li>OEM traction &amp; production status</li>
       </ul>
     </div>
     <div class="card">
       <h4>Part 2 — Strategic Analysis</h4>
       <ul>
         <li>Teradar vertical markets</li>
         <li>L4/L5 commercialization roadmap</li>
         <li>Sensor fusion architecture options</li>
         <li>Engineering recommendations</li>
       </ul>
     </div>
   </div>

----

The 7-Platform Field
--------------------

.. raw:: revealjs

   <div style="display:grid; grid-template-columns: repeat(4,1fr); gap:0.6em; margin-top:0.4em;">
     <div class="card">
       <h4 style="color:#1D9E75;">Teradar</h4>
       <p>Terahertz imaging</p>
       <p>0.1–10 THz</p>
       <span class="pill pill-amber">Prototype 2026</span>
     </div>
     <div class="card">
       <h4 style="color:#378ADD;">Arbe</h4>
       <p>4D imaging radar</p>
       <p>Phoenix 22nm</p>
       <span class="pill pill-green">Production ✓</span>
     </div>
     <div class="card">
       <h4 style="color:#888780;">Mobileye</h4>
       <p>Camera + radar</p>
       <p>EyeQ6H SoC</p>
       <span class="pill pill-green">230M+ vehicles</span>
     </div>
     <div class="card">
       <h4 style="color:#A78BFA;">Innoviz</h4>
       <p>Solid-state LiDAR</p>
       <p>InnovizTwo/Three</p>
       <span class="pill pill-green">BMW L3 ✓</span>
     </div>
     <div class="card">
       <h4 style="color:#F87171;">Luminar</h4>
       <p>1550nm LiDAR</p>
       <p>Iris / Halo</p>
       <span class="pill pill-amber">⚠️ Volvo dispute</span>
     </div>
     <div class="card">
       <h4 style="color:#34D399;">Vayyar</h4>
       <p>4D radar-on-chip</p>
       <p>XRR 79GHz</p>
       <span class="pill pill-green">Production ✓</span>
     </div>
     <div class="card">
       <h4 style="color:#FBBF24;">Cepton</h4>
       <p>MMT® LiDAR</p>
       <p>Komodo SoC</p>
       <span class="pill pill-green">GM Ultra Cruise ✓</span>
     </div>
     <div class="card" style="background:#111; border-color:#1a1a1a;">
       <h4 style="color:#555;">Sensor types</h4>
       <p style="color:#444;">THz · Radar · Camera · LiDAR (905nm / 1550nm)</p>
     </div>
   </div>

----

Resolution Deep Dive
--------------------

.. raw:: revealjs

   <p class="section-intro">Angular resolution is the primary driver of edge-case object classification accuracy</p>

.. list-table::
   :header-rows: 1

   * - Platform
     - Angular res.
     - Max range
     - Range res.
     - FOV
   * - Teradar
     - **0.1°**
     - 300 m
     - **±1.5 cm**
     - 120°×30°
   * - Arbe
     - 1° / 1.25°
     - 300 m+
     - 9.5 cm
     - Wide
   * - Mobileye
     - Sub-1° (cam)
     - 200 m+
     - Cam-limited
     - 360°
   * - Innoviz (LR)
     - **0.05°×0.05°**
     - 300 m (1 km ULR)
     - cm
     - 120°×43°
   * - Luminar Iris
     - 0.05° H
     - **600 m**
     - cm
     - 120°×30°
   * - Vayyar XRR
     - ~1–2°
     - 300 m
     - dm
     - Ultra-wide
   * - Cepton X90
     - 0.1°×0.05°
     - 200 m
     - cm
     - 120°×30°

.. revealjs-notes::

   Innoviz and Luminar lead on raw angular resolution (0.05°).
   Teradar matches Cepton at 0.1° but adds THz material fingerprinting.
   Arbe and Vayyar are radar-class — excellent weather but coarser resolution.
   Luminar Iris holds the range record at 600m.

----

All-Weather Matrix
------------------

.. raw:: revealjs

   <p class="section-intro">The single biggest L4/L5 deployment blocker — 22% of fatal accidents occur in adverse conditions</p>

.. list-table::
   :header-rows: 1

   * - Platform
     - Rain/fog
     - Dust
     - Glare
     - Night
   * - Teradar
     - ✅
     - ✅
     - ✅
     - ✅
   * - Arbe
     - ✅
     - ✅
     - ✅
     - ✅
   * - Mobileye
     - ⚠️
     - ❌
     - ⚠️
     - ⚠️
   * - Innoviz
     - ⚠️
     - ⚠️
     - ✅
     - ✅
   * - Luminar
     - ⚠️ (better)
     - ⚠️
     - ✅
     - ✅
   * - Vayyar
     - ✅
     - ✅
     - ✅
     - ✅
   * - Cepton
     - ⚠️
     - ⚠️
     - ✅
     - ✅

.. raw:: revealjs

   <blockquote style="margin-top:0.8em;">
     THz and radar-based platforms (Teradar, Arbe, Vayyar) are the only
     technologies with full all-weather immunity — a fundamental physics advantage.
   </blockquote>

----

Architecture Comparison
-----------------------

.. raw:: revealjs

   <div style="display:grid; grid-template-columns: repeat(3,1fr); gap:0.7em; font-size:0.62em;">
     <div class="card">
       <h4 style="color:#1D9E75;">Teradar</h4>
       <ul>
         <li>CMOS chip-scale THz</li>
         <li>No moving parts / waveguides</li>
         <li>Behind-fascia mounting</li>
         <li>ISO 26262 / SAE 21434</li>
         <li>Encrypted signal processing</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color:#378ADD;">Arbe</h4>
       <ul>
         <li>22 nm CMOS Phoenix chip</li>
         <li>2,304 virtual channels</li>
         <li>ASIL-D compliant</li>
         <li>NVIDIA AI partnership</li>
         <li>Behind bumper/fascia</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color:#888780;">Mobileye</h4>
       <ul>
         <li>EyeQ6H single SoC</li>
         <li>REM crowdsourced mapping</li>
         <li>RSS safety model</li>
         <li>19M EyeQ6H committed</li>
         <li>50+ OEM integrations</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color:#A78BFA;">Innoviz</h4>
       <ul>
         <li>MEMS solid-state LiDAR</li>
         <li>InnovizAPP perception SW</li>
         <li>ASIL-B(D) compliant</li>
         <li>Roof / windshield mount</li>
         <li>InnovizThree: 35% cost cut</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color:#F87171;">Luminar</h4>
       <ul>
         <li>1550 nm rotating LiDAR</li>
         <li>5 custom ASICs (Halo)</li>
         <li>Halo: behind-windshield</li>
         <li>Halo: &lt;10W, &lt;1 kg</li>
         <li>Halo initial availability 2026</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color:#34D399;">Vayyar</h4>
       <ul>
         <li>XRR RFIC (79 GHz)</li>
         <li>48-antenna MIMO array</li>
         <li>0–300 m single chip</li>
         <li>Replaces 20+ sensors</li>
         <li>In-cabin + ADAS dual use</li>
       </ul>
     </div>
   </div>

----

OEM Traction & Production
--------------------------

.. raw:: revealjs

   <p class="section-intro">Where is each platform in the production pipeline?</p>

.. list-table::
   :header-rows: 1

   * - Platform
     - Key OEM / Tier-1
     - Status
   * - Teradar
     - Undisclosed OEMs (US/EU)
     - Pre-production · prototype 2026
   * - Arbe
     - HiRain + NVIDIA
     - ✅ Serial production Q4 2025
   * - Mobileye
     - BMW, VW, Ford, GM, 50+ OEMs
     - ✅ 230M+ vehicles deployed
   * - Innoviz
     - BMW Series 7 · VW ID. Buzz AD
     - ✅ L3 series production · InnovizThree Dec 2025
   * - Luminar
     - Volvo EX90/ES90 · Mercedes-Benz
     - ⚠️ Volvo ended Nov 2025 · Halo 2026
   * - Vayyar
     - Multiple OEMs (undisclosed)
     - ✅ Production-ready · NCAP validated
   * - Cepton (Koito)
     - GM Ultra Cruise · Honda
     - ✅ Largest LiDAR award · Koito acquired 2023

.. revealjs-notes::

   Luminar's Volvo dispute is the biggest commercial risk signal in the field.
   Cepton's Koito acquisition is a stabilising factor — Tier-1 supply chain secured.
   Teradar's undisclosed OEM partnerships are a watch item.

----

Teradar Vertical Markets
------------------------

.. revealjs-section::
   :data-background-color: "#050f0a"

.. raw:: revealjs

   <p class="section-intro">Same MTE architecture — four completely different markets</p>
   <div style="display:grid; grid-template-columns: repeat(2,1fr); gap:0.8em; margin-top:0.5em;">
     <div class="card">
       <h4>🚗 Automotive ADAS</h4>
       <ul>
         <li>L2–L5 sensing · collision avoidance</li>
         <li>VRU detection in all weather</li>
         <li>Material fingerprinting for classification</li>
         <li>V2X dual-use positioning</li>
       </ul>
     </div>
     <div class="card">
       <h4>🛡️ Defense</h4>
       <ul>
         <li>UGV navigation (HMIF formations)</li>
         <li>Manned vehicle DVE</li>
         <li>Counter-sUAS: detects low-RCS FPV drones</li>
         <li>Low probability of detection (THz freq)</li>
       </ul>
     </div>
     <div class="card">
       <h4>🏥 Healthcare</h4>
       <ul>
         <li>Non-ionizing skin cancer detection</li>
         <li>Sub-mm tissue hydration mapping</li>
         <li>$7.9B diagnostics market by 2030</li>
         <li>IEC/FDA groundwork → THz medical 2027</li>
       </ul>
     </div>
     <div class="card">
       <h4>🔒 Security</h4>
       <ul>
         <li>Airport / stadium body screening</li>
         <li>Port cargo: organic vs inorganic ID</li>
         <li>Mail: 100% in-line THz-AI inspection</li>
         <li>&gt;90% explosive detection sensitivity</li>
       </ul>
     </div>
   </div>

----

L4/L5 Commercialization Roadmap
--------------------------------

.. raw:: revealjs

   <p class="section-intro">Three blockers — and which platforms solve them</p>
   <div class="col-2" style="margin-top:0.5em;">
     <div class="card">
       <h4>Blocker 1: Weather robustness</h4>
       <p>22% of fatal accidents in adverse conditions. Camera + LiDAR degrade.</p>
       <p style="margin-top:0.4em; color:#1D9E75;">✅ Solved by: Teradar, Arbe, Vayyar</p>
     </div>
     <div class="card">
       <h4>Blocker 2: Resolution at range</h4>
       <p>Sub-degree precision needed for edge-case object classification at 200m+.</p>
       <p style="margin-top:0.4em; color:#A78BFA;">✅ Solved by: Innoviz, Luminar, Teradar, Cepton</p>
     </div>
   </div>
   <div class="card" style="margin-top:0.8em;">
     <h4>Blocker 3: Sensor redundancy</h4>
     <p>Regulators require diverse modalities with no shared failure mode.
     Teradar + Arbe = THz + radar: entirely different physics, no common vulnerability.
     This is the strongest redundancy pair available in the market today.</p>
   </div>

----

Deployment Timeline
-------------------

.. list-table::
   :header-rows: 1

   * - Year
     - Milestone
   * - 2023–2024
     - GM Ultra Cruise (Cepton) · BMW Series 7 L3 (Innoviz) · Volvo EX90 (Luminar)
   * - Q4 2025
     - Arbe/HiRain LRR610 serial production · Luminar/Volvo dispute · InnovizThree launch
   * - 2026
     - Teradar prototypes (US/EU) · Luminar Halo initial availability · Innoviz ULR (1 km)
   * - 2027
     - THz medical regulatory groundwork (IEC/FDA) · Euro NCAP 2027 protocols
   * - 2028
     - Teradar global volume · Industry THz ADAS deployment expected
   * - 2029+
     - Luminar next-gen Volvo (deferred) · Full L4/L5 ODD expansion

----

Engineering Recommendations
----------------------------

.. revealjs-section::
   :data-background-color: "#0a0a14"

.. raw:: revealjs

   <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:0.8em; margin-top:0.3em;">
     <div class="card">
       <h4 style="color:#FBBF24;">Now (2025–2026)</h4>
       <p><strong>Primary stack:</strong></p>
       <ul>
         <li>Arbe — radar backbone</li>
         <li>Innoviz — LiDAR resolution</li>
         <li>Mobileye — software/mapping</li>
       </ul>
       <p style="margin-top:0.5em; color:#888; font-size:0.8em;">Covers weather, resolution, and ODD mapping today</p>
     </div>
     <div class="card">
       <h4 style="color:#1D9E75;">Medium (2026–2028)</h4>
       <p><strong>Add THz layer:</strong></p>
       <ul>
         <li>Teradar — material fingerprinting</li>
         <li>Elevates VRU classification</li>
         <li>Closes adverse weather gap</li>
       </ul>
       <p style="margin-top:0.5em; color:#888; font-size:0.8em;">Teradar + Arbe = strongest redundancy pair</p>
     </div>
     <div class="card">
       <h4 style="color:#378ADD;">Watch List</h4>
       <ul>
         <li>Luminar Halo — windshield form factor breakthrough if commercially stabilized</li>
         <li>Vayyar — cost-sensitive platforms, sensor consolidation</li>
         <li>Cepton — GM Ultra Cruise scale data</li>
       </ul>
     </div>
   </div>

.. revealjs-notes::

   The Teradar + Arbe redundancy argument is the strongest engineering case
   for THz adoption. Two entirely different physics bases — no shared failure mode.
   This is what regulators will want to see for L4/L5 certification.

----

Summary Scorecard
-----------------

.. list-table::
   :header-rows: 1

   * - Platform
     - Resolution
     - Weather
     - Production
     - Unique edge
   * - Teradar
     - ⭐⭐⭐⭐
     - ⭐⭐⭐⭐⭐
     - ⭐⭐
     - THz fingerprinting
   * - Arbe
     - ⭐⭐⭐
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐⭐⭐
     - Best radar in production
   * - Mobileye
     - ⭐⭐⭐
     - ⭐⭐
     - ⭐⭐⭐⭐⭐
     - Software + scale
   * - Innoviz
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐
     - ⭐⭐⭐⭐
     - Finest LiDAR resolution
   * - Luminar
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐
     - ⭐⭐⭐
     - 600 m range / 1550 nm
   * - Vayyar
     - ⭐⭐
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐⭐
     - Single-chip multi-function
   * - Cepton
     - ⭐⭐⭐⭐
     - ⭐⭐⭐
     - ⭐⭐⭐⭐⭐
     - Largest LiDAR production win

----

Thank You
---------

.. revealjs-section::
   :data-background-color: "#050f0a"

.. raw:: revealjs

   <p style="font-size:1em; color:#1D9E75; margin-bottom:0.5em;">
     THZ Tech Intel — Internal Engineering Review
   </p>
   <p style="font-size:0.65em; color:#555;">
     Sources: Teradar whitepapers · Arbe Robotics · Mobileye · Innoviz Technologies ·
     Luminar Technologies · Vayyar Imaging · Cepton / Koito · IEEE · AutoSens Europe 2025
   </p>
   <p style="font-size:0.6em; color:#333; margin-top:1.5em;">
     Hosted at terahertz-technology-intelligence.readthedocs.io
   </p>

.. revealjs-notes::

   Full analysis doc available at /en/latest/deep_competitive/
   Next update planned when Teradar prototype specs are confirmed (2026).
