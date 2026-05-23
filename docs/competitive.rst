Competitive Analysis
====================

This page summarises the technology scoreboard comparing Teradar against
two leading ADAS sensing companies: **Arbe Robotics** (4D imaging radar)
and **Mobileye** (camera + radar fusion).

.. note::
   A full interactive presentation of this analysis is available at
   :doc:`/slides/scoreboard`.

Company Profiles
----------------

Teradar
~~~~~~~
Teradar is pioneering a new sensing category using terahertz imaging.
Its Modular Terahertz Engine (MTE) is built on proprietary TX, RX, and
core processing chips produced on high-volume silicon processes, with
antennas integrated directly in chip design — no waveguides, no moving parts.

Prototypes are available in the US and Europe in 2026, with global
high-volume availability planned for 2028.

Arbe Robotics
~~~~~~~~~~~~~
Arbe (Nasdaq: ARBE) produces the Phoenix 4D imaging radar chipset, featuring
a 48×48 TX/RX antenna array (2,304 virtual channels) capable of up to 300 m
point cloud range. Its HiRain LRR610 module entered serial production in Q4 2025,
making Arbe the most production-ready of the three on the radar/THz side.

Arbe's key differentiator is reliable detection of stationary objects — a
notorious weak spot for conventional 77 GHz radar.

Mobileye
~~~~~~~~
Mobileye (Nasdaq: MBLY) is the established market leader, with approximately
230 million vehicles built with its EyeQ technology through 2025. Its
EyeQ6H-powered Surround ADAS system uses cameras and radar for hands-free,
eyes-on driving up to 81 mph.

Mobileye's strength is software maturity: REM crowdsourced mapping,
Responsibility Sensitive Safety (RSS), and a deep OEM integration ecosystem.
Its limitation is camera-centric perception that degrades in adverse weather.

Scoreboard Summary
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 24 24 24

   * - Dimension
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
   * - Rain / fog / snow
     - Excellent
     - Excellent
     - Degraded
   * - Glare / direct sun
     - Immune
     - Immune
     - Limited
   * - Material fingerprinting
     - Yes (THz unique)
     - No
     - No
   * - Stationary object detection
     - Yes
     - Yes
     - Camera-dependent
   * - Autonomy level support
     - L2 → L5
     - L2+ → L5
     - L2+ → L3
   * - Production readiness
     - Prototype 2026
     - Serial production now
     - 230M+ vehicles
   * - Cost vs. LiDAR
     - Lower (CMOS scale)
     - Lower (radar)
     - Lower (camera-first)

Key Takeaways
-------------

- Teradar holds the **resolution advantage** (0.1° vs Arbe's 1°) and is the
  only platform with THz material fingerprinting.
- Arbe is the **most production-ready** weather-robust sensing solution available
  today, with serial production in place and an NVIDIA AI partnership announced
  at CES 2026.
- Mobileye leads on **software maturity and deployment scale** but is exposed
  to weather-related perception failure — the exact gap Teradar and Arbe address.
