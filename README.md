<div align="center">

<!-- Hero Banner Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,14,24,36&height=220&section=header&text=PRUTHVI%20JADHAV&fontSize=52&fontColor=ffffff&animation=twinkling&desc=Embedded%20Systems%20%E2%80%A2%20Modern%20C%2B%2B%20%E2%80%A2%20Autonomous%20Robotics&descSize=18&descAlign=50&descAlignY=64" width="100%"/>

<!-- Dynamic Animated Typing Subheader -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&duration=3000&pause=1000&color=22D3EE&center=true&vCenter=true&width=750&lines=Embedded+Systems+%26+Firmware+Architect;Low-Level+C%2B%2B17%2F20+%26+FreeRTOS+Specialist;Upstream+Contributor+%40+NVIDIA+%C2%B7+Espressif+%C2%B7+Arduino;Autonomous+Robotics+%26+CUDA+Compute+Engineer" alt="Typing SVG" />
</a>

<br><br>

<!-- Contact & Social Badges -->
<a href="https://www.linkedin.com/in/pruthvi-jadhav-28767a309/"><img src="https://img.shields.io/badge/LinkedIn-0A101F?style=for-the-badge&logo=linkedin&logoColor=22D3EE" alt="LinkedIn"/></a>&nbsp;
<a href="mailto:jadhavpruthvi828@gmail.com"><img src="https://img.shields.io/badge/Email-0A101F?style=for-the-badge&logo=gmail&logoColor=22D3EE" alt="Email"/></a>&nbsp;
<a href="https://github.com/pruthvi828"><img src="https://img.shields.io/badge/GitHub-0A101F?style=for-the-badge&logo=github&logoColor=22D3EE" alt="GitHub"/></a>&nbsp;
<img src="https://img.shields.io/badge/System_Status-100%25_Operational-06B6D4?style=for-the-badge&logo=statuspage&logoColor=white" alt="Status"/>

<br><br>

<!-- GitHub Trophy Showcase -->
<a href="https://github.com/ryo-ma/github-profile-trophy">
  <img src="https://github-profile-trophy.vercel.app/?username=pruthvi828&theme=tokyonight&no-frame=true&no-bg=true&margin-w=4&row=1&column=7" alt="GitHub Trophies" />
</a>

<br><br>

```
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  PRUTHVI JADHAV // LOW-LEVEL SYSTEMS & AUTONOMOUS ROBOTICS ENGINEER                          ║
║  Core: Modern C++17/20 · FreeRTOS · ESP32-S3/C6/P4 · Hardware HAL · OpenCV · CUDA · Kinematics║
║  Telemetry: Upstream Contributor @ NVIDIA · Espressif · Arduino · OpenCV                     ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## ⚡ About & Engineering Focus

I build deterministic, memory-efficient systems at the boundary between hardware and software. My work focuses on **low-level C++, hardware abstraction layers (HAL), real-time multitasking (FreeRTOS), CUDA compute, and autonomous pathfinding algorithms**.

- 🔬 **Firmware & Low-Level Architecture:** Interrupt Service Routines (ISRs), race-free concurrency, lockless ring buffers, DMA pipelines, and peripheral driver design (I2C, SPI, UART, RMII Ethernet).
- 🏎️ **Autonomous Robotics & Kinematics:** Real-time motion planning, trajectory smoothing, dynamic flood-fill, and sensor fusion algorithms designed for microcontrollers with strict deterministic execution constraints.
- 🌐 **Upstream Open Source:** Active contributor to **[NVIDIA](https://github.com/NVIDIA/cuda-samples)**, **[Espressif Systems](https://github.com/espressif/arduino-esp32)**, **[Arduino](https://github.com/arduino/ArduinoCore-API)**, and the **[OpenCV Foundation](https://github.com/opencv/opencv)**.

---

## 🚀 Upstream Open-Source Contributions

<table>
  <thead>
    <tr>
      <th width="35%">Repository</th>
      <th width="45%">Pull Request & Technical Solution</th>
      <th width="20%">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <b><a href="https://github.com/NVIDIA/cuda-samples">NVIDIA/cuda-samples</a></b><br/>
        <sub>⭐ 18.2k+ • Official NVIDIA CUDA Samples</sub>
      </td>
      <td>
        <b><a href="https://github.com/NVIDIA/cuda-samples/pull/462">PR #462</a>: <code>fix(test-runner): fix executable discovery and path resolution on Windows</code></b><br/>
        <sub>Resolved Win32 <code>CreateProcess</code> path execution failures (<code>WinError 2</code>) across sample test runners and fixed binary discovery on Windows (Fixes #453).</sub>
      </td>
      <td>
        <img src="https://img.shields.io/badge/PR-In_Review-yellow?style=flat-square&logo=github"/>
      </td>
    </tr>
    <tr>
      <td>
        <b><a href="https://github.com/espressif/arduino-esp32">espressif/arduino-esp32</a></b><br/>
        <sub>⭐ 14.5k+ • Official ESP32 Core</sub>
      </td>
      <td>
        <b><a href="https://github.com/espressif/arduino-esp32/pull/12911">PR #12911</a>: <code>feat(timer): add std::function and lambda callback support</code></b><br/>
        <sub>Engineered modern C++ lambda capture callbacks for <code>timerAttachInterrupt()</code>. Eliminated critical ISR use-after-free race conditions and prevented uninitialized heap memory leaks across ESP32-S3, C6, and P4.</sub>
      </td>
      <td>
        <img src="https://img.shields.io/badge/PR-Passing_CI-success?style=flat-square&logo=githubactions&logoColor=white"/><br/>
        <img src="https://img.shields.io/badge/Wokwi-Verified-blue?style=flat-square"/>
      </td>
    </tr>
    <tr>
      <td>
        <b><a href="https://github.com/espressif/arduino-esp32">espressif/arduino-esp32</a></b><br/>
        <sub>⭐ 14.5k+ • Official ESP32 Core</sub>
      </td>
      <td>
        <b><a href="https://github.com/espressif/arduino-esp32/pull/12928">PR #12928</a>: <code>fix(periman): correct ETHERNET_MCD typo to ETHERNET_MDC</code></b><br/>
        <sub>Aligned Peripheral Manager (<code>periman</code>) with IEEE 802.3 Ethernet Management Data Clock specification with zero-regression backward-compatible aliasing (Closes #12876).</sub>
      </td>
      <td>
        <img src="https://img.shields.io/badge/PR-In_Review-yellow?style=flat-square&logo=github"/>
      </td>
    </tr>
    <tr>
      <td>
        <b><a href="https://github.com/espressif/arduino-esp32">espressif/arduino-esp32</a></b><br/>
        <sub>⭐ 14.5k+ • Official ESP32 Core</sub>
      </td>
      <td>
        <b><a href="https://github.com/espressif/arduino-esp32/pull/12929">PR #12929</a>: <code>fix(partitions): correct littlefs partition subtype in large_littlefs_32MB.csv</code></b><br/>
        <sub>Corrected partition table definitions, enabling out-of-the-box LittleFS VFS mounting for commercial 32MB flash modules (Closes #12898).</sub>
      </td>
      <td>
        <img src="https://img.shields.io/badge/PR-In_Review-yellow?style=flat-square&logo=github"/>
      </td>
    </tr>
    <tr>
      <td>
        <b><a href="https://github.com/arduino/ArduinoCore-API">arduino/ArduinoCore-API</a></b><br/>
        <sub>⭐ 1.2k+ • Official Arduino Core API</sub>
      </td>
      <td>
        <b><a href="https://github.com/arduino/ArduinoCore-API/pull/282">PR #282</a>: <code>fix(IPAddress): remove redundant condition in fromString6</code></b><br/>
        <sub>Eliminated tautological pointer conditions in IPv6 parser state machine and extended Catch2 unit test coverage for consecutive colon validations (Fixes #249).</sub>
      </td>
      <td>
        <img src="https://img.shields.io/badge/PR-In_Review-yellow?style=flat-square&logo=github"/>
      </td>
    </tr>
    <tr>
      <td>
        <b><a href="https://github.com/opencv/opencv">opencv/opencv</a></b><br/>
        <sub>⭐ 78.5k+ • Computer Vision Library</sub>
      </td>
      <td>
        <b><a href="https://github.com/opencv/opencv/pull/29978">PR #29978</a>: <code>doc(js_tutorials): fix broken precompiled opencv.js download URLs</code></b><br/>
        <sub>Resolved precompiled WebAssembly distribution endpoints across official OpenCV 4.x and 5.x documentation pipelines (Fixes #29818).</sub>
      </td>
      <td>
        <img src="https://img.shields.io/badge/PR-In_Review-yellow?style=flat-square&logo=github"/>
      </td>
    </tr>
  </tbody>
</table>

---

## 🛠️ Technical Arsenal

<div align="center">

<!-- Skill Icons Badges -->
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=c,cpp,python,linux,arduino,cmake,git,githubactions,vscode,opencv&theme=dark" alt="Tech Stack Icons" />
</a>

<br><br>

| Domain | Technologies, Frameworks & Protocols |
|---|---|
| **Core Languages** | `C (C99/C11)` &bull; `Modern C++ (C++17/20)` &bull; `Python 3.10+` &bull; `ARM Assembly` |
| **Embedded & RTOS** | `FreeRTOS` &bull; `ESP-IDF` &bull; `Arduino Core` &bull; `STM32 HAL / LL Drivers` &bull; `CMSIS` |
| **Hardware & Peripherals** | `ESP32-S3 / C6 / P4` &bull; `STM32 Cortex-M` &bull; `CAN / TWAI` &bull; `RMII Ethernet` &bull; `SPI` &bull; `I2C` &bull; `UART` &bull; `DMA` &bull; `KiCad PCB` |
| **Robotics & Algorithms** | `Modified Flood-Fill` &bull; `A* Search` &bull; `45° Diagonal Smoothing` &bull; `OpenCV Vision` &bull; `Sensor Fusion (ToF/IMU)` |
| **Toolchains & DevOps** | `CMake` &bull; `GDB / JTAG Debugging` &bull; `Git` &bull; `GitHub Actions CI/CD` &bull; `Wokwi Simulation` &bull; `VS Code` |

</div>

---

<div align="center">

## 🐍 Contribution Activity Stream

<img src="./github-snake.svg" width="100%" alt="GitHub Snake Animation"/>

<br><br>

## 📊 Telemetry & Activity Matrix

<table border="0">
  <tr>
    <td width="50%">
      <img src="https://github-readme-stats.vercel.app/api?username=pruthvi828&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&bg_color=0D1117&title_color=22D3EE&text_color=E2E8F0&icon_color=38BDF8" width="100%" alt="GitHub Stats" />
    </td>
    <td width="50%">
      <img src="https://github-readme-streak-stats.herokuapp.com/?user=pruthvi828&theme=tokyonight&hide_border=true&background=0D1117&ring=22D3EE&fire=38BDF8&currStreakLabel=22D3EE" width="100%" alt="GitHub Streak" />
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=pruthvi828&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=22D3EE&text_color=E2E8F0" width="100%" alt="Top Languages" />
    </td>
  </tr>
</table>

<br/>

<!-- Footer Wave Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,14,24,36&height=120&section=footer" width="100%"/>

*Engineered with precision by **Pruthvi Jadhav** &bull; Always open to discussing low-level systems, firmware, and robotics engineering.*

</div>
