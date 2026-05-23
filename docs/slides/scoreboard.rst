Teradar Technology Scoreboard
==============================

.. revealjs-slide::
   :theme: black

.. raw:: revealjs

   <p class="subtitle">Teradar vs. Arbe Robotics vs. Mobileye — May 2025</p>

----

The Sensing Gap
---------------

.. revealjs-section::
   :data-background-color: "#0a0a0a"

.. raw:: revealjs

   <p class="section-intro">Why existing sensors fall short for next-gen ADAS and autonomy</p>

.. revealjs-fragments::

   - **1.3M** road fatalities per year globally
   - **22%** occur in adverse weather / low visibility
   - Cameras fail in fog, glare, and darkness
   - Radar is weather-robust but coarse in resolution
   - LiDAR degrades in rain and dust — and is expensive

.. revealjs-notes::

   Current ADAS sensors each solve part of the problem.
   The goal is a single sensor category that solves all of it.

----

The Three Contenders
--------------------

.. raw:: revealjs

   <div class="col-2" style="grid-template-columns: 1fr 1fr 1fr; gap: 1em; margin-top: 0.5em;">
     <div class="card">
       <h4 style="color: #1D9E75;">Teradar</h4>
       <p>Terahertz imaging</p>
       <p>0.1–10 THz band</p>
       <p>Solid-state CMOS chip</p>
       <p style="color: #888; margin-top: 0.5em;">Prototype 2026 · Volume 2028</p>
     </div>
     <div class="card">
       <h4 style="color: #378ADD;">Arbe Robotics</h4>
       <p>4D imaging radar</p>
       <p>48×48 TX/RX channels</p>
       <p>Phoenix chipset</p>
       <p style="color: #888; margin-top: 0.5em;">Serial production Q4 2025</p>
     </div>
     <div class="card">
       <h4 style="color: #888780;">Mobileye</h4>
       <p>Camera + radar fusion</p>
       <p>EyeQ6H SoC</p>
       <p>REM mapping + RSS</p>
       <p style="color: #888; margin-top: 0.5em;">230M+ vehicles deployed</p>
     </div>
   </div>

----

Resolution & Range
------------------

.. raw:: revealjs

   <p class="section-intro">Higher resolution = safer object classification at distance</p>

.. list-table::
   :header-rows: 1

   * - Metric
     - Teradar
     - Arbe Robotics
     - Mobileye
   * - Angular resolution
     - **0.1°**
     - 1° az / 1.25° el
     - Sub-1° (camera)
   * - Max detection range
     - 300 m
     - 300 m+
     - 200 m+
   * - Range resolution
     - ±1.5 cm
     - 9.5 cm @ 36 m
     - Camera-limited
   * - Point cloud density
     - High (THz)
     - 2K ultra-HD 4D
     - N/A

.. revealjs-notes::

   Teradar's 0.1° angular resolution is 10x finer than Arbe.
   In practice this matters most for small object detection at long range —
   pedestrians, cyclists, debris — especially in edge cases.

----

All-Weather Performance
-----------------------

.. raw:: revealjs

   <p class="section-intro">The critical differentiator for L4/L5 deployment at scale</p>

.. list-table::
   :header-rows: 1

   * - Condition
     - Teradar
     - Arbe
     - Mobileye
   * - Rain / fog / snow
     - ✅ Excellent
     - ✅ Excellent
     - ⚠️ Degraded
   * - Glare / direct sun
     - ✅ Immune
     - ✅ Immune
     - ⚠️ Limited
   * - Night / low light
     - ✅ Full
     - ✅ Full
     - ⚠️ Reduced
   * - Dust / sand
     - ✅ Penetrates
     - ✅ Penetrates
     - ❌ Fails

.. revealjs-notes::

   Mobileye's camera-first approach is its primary weather Achilles heel.
   Both Teradar and Arbe solve this — through THz physics and radar physics
   respectively.

----

Object & Material Detection
----------------------------

.. raw:: revealjs

   <p class="section-intro">What the sensor can tell you about what it sees</p>

.. list-table::
   :header-rows: 1

   * - Capability
     - Teradar
     - Arbe
     - Mobileye
   * - Material fingerprinting
     - ✅ THz spectral ID
     - ❌
     - ❌
   * - Stationary object detection
     - ✅ Yes
     - ✅ Yes (key diff.)
     - ⚠️ Camera-dependent
   * - Vulnerable road users
     - ✅ All weather
     - ✅ All weather
     - ⚠️ Clear only
   * - 4D imaging (x/y/z + velocity)
     - ✅ Yes
     - ✅ Yes
     - ⚠️ Partial

----

System Integration
------------------

.. raw:: revealjs

   <div class="col-2" style="grid-template-columns: 1fr 1fr 1fr; gap: 1em; margin-top: 0.3em;">
     <div class="card">
       <h4 style="color: #1D9E75;">Teradar</h4>
       <ul>
         <li>CMOS chip-scale solid-state</li>
         <li>No moving parts, no waveguides</li>
         <li>Mounts behind fascia</li>
         <li>ISO 26262 / SAE 21434</li>
         <li>L2 → L5 support</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color: #378ADD;">Arbe Robotics</h4>
       <ul>
         <li>22 nm CMOS chipset</li>
         <li>ASIL-D compliant</li>
         <li>NVIDIA AI partnership (CES 2026)</li>
         <li>Installs behind bumper/fascia</li>
         <li>L2+ → L5 support</li>
       </ul>
     </div>
     <div class="card">
       <h4 style="color: #888780;">Mobileye</h4>
       <ul>
         <li>EyeQ6H SoC (single ECU)</li>
         <li>REM + RSS software stack</li>
         <li>ISO 26262 / Euro NCAP</li>
         <li>19M+ EyeQ6H systems committed</li>
         <li>L2+ → L3 (Surround ADAS)</li>
       </ul>
     </div>
   </div>

----

Production Readiness
--------------------

.. raw:: revealjs

   <p class="section-intro">Where is each company on the deployment timeline?</p>

.. list-table::
   :header-rows: 1

   * - Milestone
     - Teradar
     - Arbe
     - Mobileye
   * - Current status
     - Pre-production testing
     - Serial production
     - Mass market
   * - Prototype / pilot
     - US & Europe, 2026
     - HiRain LRR610, Q4 2025
     - Decades of deployment
   * - High-volume
     - 2028
     - Now (via Tier-1s)
     - 230M+ vehicles (2025)
   * - Cost vs. LiDAR
     - Lower (CMOS)
     - Lower (radar)
     - Lower (camera-first)

----

Key Takeaways
-------------

.. revealjs-section::
   :data-background-color: "#0a1a0f"

.. raw:: revealjs

   <div class="col-2" style="margin-top: 0.5em;">
     <div class="card">
       <h4>Where Teradar leads</h4>
       <ul>
         <li>Finest angular resolution (0.1°)</li>
         <li>Only platform with THz material fingerprinting</li>
         <li>Tightest range resolution (±1.5 cm)</li>
         <li>Multi-vertical: auto, defense, health, security</li>
       </ul>
     </div>
     <div class="card">
       <h4>Where Arbe leads</h4>
       <ul>
         <li>Most production-ready weather-robust sensor today</li>
         <li>NVIDIA AI partnership for highway autonomy</li>
         <li>Stationary object detection (radar first)</li>
         <li>Proven Tier-1 integration pipeline</li>
       </ul>
     </div>
   </div>

.. raw:: revealjs

   <div class="card" style="margin-top: 1em; border-color: #333;">
     <h4 style="color: #888780;">Where Mobileye leads</h4>
     <p>Software maturity (REM, RSS), OEM trust, and unmatched deployment scale —
     but weather performance remains its primary vulnerability.</p>
   </div>

----

Roadmap
-------

.. raw:: revealjs

   <p class="section-intro">Path to Automotive Sensing 2.0</p>

.. list-table::
   :header-rows: 1

   * - Year
     - Milestone
   * - Q4 2025
     - Arbe/HiRain LRR610 enters serial production
   * - 2026
     - Teradar prototypes available in US & Europe
   * - 2027
     - Regulatory groundwork for THz automotive (US DOT, Euro NCAP)
   * - 2028
     - Teradar global high-volume availability; industry deployment expected
   * - 2028+
     - THz medical systems (IEC/FDA); broader Teradar verticals

----

Thank You
---------

.. revealjs-section::
   :data-background-color: "#050f0a"

.. raw:: revealjs

   <p style="font-size: 1.1em; color: #1D9E75; margin-bottom: 0.5em;">
     Teradar Technology Intelligence
   </p>
   <p style="font-size: 0.7em; color: #666;">
     Analysis based on Teradar whitepapers (ADAS, Advanced Autonomy, Defense,
     Healthcare, Security) and public data from Arbe Robotics and Mobileye.
   </p>
   <p style="font-size: 0.65em; color: #444; margin-top: 1.5em;">
     Built with sphinx-revealjs 3.2.1 · reveal.js 5.2.1 · Hosted on ReadTheDocs
   </p>

.. revealjs-notes::

   Full documentation and competitive analysis available at the main docs site.
   This presentation is part of the Teradar Technology Intelligence hub.
