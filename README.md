<div align="center">

# Hi, I'm Pruthvi Jadhav 👋
### **Embedded Systems & Firmware Engineer | Low-Level C++ • RTOS • Robotics**

<!-- Badges Row -->
<a href="https://www.linkedin.com/in/pruthvi-jadhav-28767a309/"><img src="https://img.shields.io/badge/LinkedIn-0A101F?style=for-the-badge&logo=linkedin&logoColor=22D3EE" alt="LinkedIn"/></a>&nbsp;
<a href="mailto:jadhavpruthvi828@gmail.com"><img src="https://img.shields.io/badge/Email-0A101F?style=for-the-badge&logo=gmail&logoColor=22D3EE" alt="Email"/></a>&nbsp;
<a href="https://github.com/pruthvi828"><img src="https://img.shields.io/badge/GitHub-0A101F?style=for-the-badge&logo=github&logoColor=22D3EE" alt="GitHub"/></a>&nbsp;
<a href="https://pruthvi828.github.io/tars-maze-navigation/"><img src="https://img.shields.io/badge/Live_Studio-60_FPS_Demo-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Live Demo"/></a>

<br><br>

```cpp
#include <iostream>

struct SystemsEngineer {
    const char* name = "Pruthvi Jadhav";
    const char* focus = "Embedded Systems, Low-Level C++, Real-Time Firmware & Autonomous Robotics";
    const char* primary_targets[4] = {"ESP32-S3/C6/P4", "ARM Cortex-M (STM32)", "FreeRTOS", "OpenCV"};
};
```

---

</div>

## 📌 Core Engineering Profile

I specialize in **low-level C++, hardware abstraction layers (HAL), real-time multitasking (FreeRTOS), and autonomous pathfinding algorithms**.

* ⚡ **Upstream Open Source:** Active contributor to **[Espressif Systems](https://github.com/espressif/arduino-esp32)** (ESP32 core HAL) and **[OpenCV](https://github.com/opencv/opencv)**.
* 🏎️ **Robotics Engine:** Author of **[TARS-MazeNav](https://github.com/pruthvi828/tars-maze-navigation)** — an autonomous navigation engine featuring 45° diagonal kinematics, zero dynamic heap allocation, and <2KB static RAM memory footprint.
* 🔍 **Firmware Depth:** Interrupt Service Routines (ISRs), race-free concurrency, DMA buffers, hardware timer lifecycle, and peripheral driver development (I2C, SPI, UART, RMII Ethernet).

---

## 🚀 Upstream Open-Source Contributions

### 🔹 [Espressif Systems (`espressif/arduino-esp32`)](https://github.com/espressif/arduino-esp32) — *14.5k+ ⭐*
* **[PR #12911](https://github.com/espressif/arduino-esp32/pull/12911) — `feat(timer): add std::function and lambda callback support`**  
  *Engineered modern C++ lambda callback support for `timerAttachInterrupt()`. Eliminated critical ISR use-after-free race conditions and prevented uninitialized heap memory leaks across ESP32-S3, C6, and P4.*
* **[PR #12928](https://github.com/espressif/arduino-esp32/pull/12928) — `fix(periman): correct ETHERNET_MCD typo to ETHERNET_MDC`**  
  *Aligned Peripheral Manager (`periman`) with IEEE 802.3 Ethernet Management Data Clock specification while providing zero-regression backward compatibility.*
* **[PR #12929](https://github.com/espressif/arduino-esp32/pull/12929) — `fix(partitions): correct littlefs partition subtype in large_littlefs_32MB.csv`**  
  *Corrected partition table definitions, enabling out-of-the-box LittleFS VFS mounting for commercial 32MB flash modules.*

### 🔹 [OpenCV Foundation (`opencv/opencv`)](https://github.com/opencv/opencv) — *78.5k+ ⭐*
* **[PR #29978](https://github.com/opencv/opencv/pull/29978) — `doc(js_tutorials): fix broken precompiled opencv.js download URLs`**  
  *Resolved precompiled WebAssembly distribution endpoints across official OpenCV 4.x and 5.x documentation pipelines.*

---

## 💻 Featured Technical Projects

<table>
  <tr>
    <td width="60%">
      <h3>🏁 TARS-MazeNav — Autonomous Micromouse Engine</h3>
      <p>High-performance autonomous maze exploration and kinematics engine written in <b>C++ and Python</b> with real-time 60 FPS simulation studio.</p>
      <ul>
        <li><b>Modified Flood-Fill:</b> Dynamic Manhattan potential field recalculation with directional momentum bias.</li>
        <li><b>45° Diagonal Kinematics:</b> Smooth trajectory compression with trapezoidal acceleration profiling (<i>v<sub>max</sub> = 3.5 m/s, a = 12 m/s²</i>).</li>
        <li><b>Embedded Firmware:</b> Zero dynamic heap allocation operating under strict <b>&lt; 2 KB static RAM</b> on ESP32/STM32.</li>
      </ul>
      <p>
        <a href="https://pruthvi828.github.io/tars-maze-navigation/"><b>👉 Launch Live 60 FPS Interactive Studio</b></a> &bull;
        <a href="https://github.com/pruthvi828/tars-maze-navigation"><b>View Source Code</b></a>
      </p>
    </td>
    <td width="40%" align="center">
      <img src="https://img.shields.io/badge/60%20FPS-Canvas%20Simulation-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white" /><br/><br/>
      <img src="https://img.shields.io/badge/Target-ESP32%20%7C%20STM32-red?style=for-the-badge" /><br/><br/>
      <img src="https://img.shields.io/badge/Memory-%3C2KB%20Static%20RAM-34d399?style=for-the-badge" />
    </td>
  </tr>
</table>

---

## 🛠️ Technical Arsenal

<div align="center">

| Domain | Technologies & Frameworks |
|---|---|
| **Languages** | ![C](https://img.shields.io/badge/C-00599C?style=flat&logo=c&logoColor=white) ![C++](https://img.shields.io/badge/C++17/20-00599C?style=flat&logo=c%2B%2B&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![ARM Assembly](https://img.shields.io/badge/ARM_Assembly-0091BD?style=flat&logo=arm&logoColor=white) |
| **Embedded & RTOS** | ![FreeRTOS](https://img.shields.io/badge/FreeRTOS-34d399?style=flat) ![ESP-IDF](https://img.shields.io/badge/ESP--IDF-E7352C?style=flat&logo=espressif&logoColor=white) ![Arduino Core](https://img.shields.io/badge/Arduino_Core-00979D?style=flat&logo=arduino&logoColor=white) ![STM32 HAL](https://img.shields.io/badge/STM32_HAL-03234B?style=flat&logo=stmicroelectronics&logoColor=white) |
| **Hardware & Peripherals** | `ESP32-S3/C6/P4` &bull; `STM32 Cortex-M` &bull; `I2C` &bull; `SPI` &bull; `UART` &bull; `RMII Ethernet` &bull; `CAN/TWAI` &bull; `DMA` &bull; `KiCad PCB` |
| **Robotics & Vision** | `Modified Flood-Fill` &bull; `A* Search` &bull; `45° Diagonal Smoothing` &bull; `OpenCV` &bull; `ToF/IR Sensor Fusion` |
| **Developer Tools** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) ![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat&logo=cmake&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white) |

</div>

---

<div align="center">

### 📊 GitHub Activity

<img src="https://github-readme-stats.vercel.app/api?username=pruthvi828&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" width="48%" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=pruthvi828&layout=compact&theme=tokyonight&hide_border=true" width="48%" />

<br/>

*Engineered with precision by **Pruthvi Jadhav** &bull; Always open to firmware, systems, and robotics opportunities.*

</div>
