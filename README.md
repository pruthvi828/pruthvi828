<div align="center">

# Hi, I'm Pruthvi Jadhav 👋
### **Embedded Systems & Firmware Engineer | Low-Level C++ • RTOS • Robotics**

[![GitHub followers](https://img.shields.io/github/followers/spidyy19?label=Follow&style=social)](https://github.com/spidyy19)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com)
[![Email](https://img.shields.io/badge/Email-jadhavpruthvi826%40gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:jadhavpruthvi828@gmail.com)

```cpp
#include <iostream>

struct Engineer {
    const char* name = "Pruthvi Jadhav";
    const char* focus = "Embedded Systems, Low-Level C++, RTOS, Autonomous Robotics";
    const char* primary_targets[3] = {"ESP32-S3/C6/P4", "ARM Cortex-M (STM32)", "FreeRTOS"};
};
```

---

</div>

## 📌 About Me

I am a systems-focused engineering student specializing in **low-level C++, real-time embedded firmware, and autonomous robotics navigation**.

- 🔭 **Core Focus:** Hardware Abstraction Layers (HAL), Interrupt Service Routines (ISRs), FreeRTOS memory management, and deterministic embedded pathfinding.
- ⚡ **Upstream Open Source:** Active contributor to **[Espressif Systems](https://github.com/espressif/arduino-esp32)** (ESP32 core HAL) and **[OpenCV](https://github.com/opencv/opencv)**.
- 🏎️ **Robotics Engine:** Creator of **[TARS-MazeNav](https://github.com/pruthvi828/tars-maze-navigation)** — an autonomous navigation engine with 45° diagonal kinematics and embedded C++ firmware (<2KB static RAM).
- 💬 **Ask me about:** C++17/C++20, ISR race conditions, peripheral drivers (I2C/SPI/UART/RMII), and potential field pathfinding.

---

## 🚀 Open Source Contributions

### 🔹 [Espressif Systems (`espressif/arduino-esp32`)](https://github.com/espressif/arduino-esp32) — *14.5k+ ⭐*
* **[PR #12931](https://github.com/espressif/arduino-esp32/pull/12931) — `fix(zigbee): zero-initialize report_attr_cmd and set manuf_code in endpoint report helpers`**  
  *Fixed uninitialized stack memory defect in Zigbee C++ HAL across 12 endpoint classes (`ZigbeeAnalog`, `ZigbeeTempSensor`, etc.), explicitly assigning standard `manuf_code` to eliminate non-deterministic payload behavior.*
* **[PR #12911](https://github.com/espressif/arduino-esp32/pull/12911) — `feat(timer): add std::function and lambda callback support`**  
  *Engineered modern C++ lambda callback support for `timerAttachInterrupt()`. Resolved critical ISR use-after-free race conditions and eliminated uninitialized heap memory leaks across ESP32-S3, C6, and P4.*
* **[PR #12928](https://github.com/espressif/arduino-esp32/pull/12928) — `fix(periman): correct ETHERNET_MCD typo to ETHERNET_MDC`**  
  *Aligned Peripheral Manager (`periman`) with IEEE 802.3 Ethernet Management Data Clock specification while providing zero-regression backward compatibility.*
* **[PR #12929](https://github.com/espressif/arduino-esp32/pull/12929) — `fix(partitions): correct littlefs partition subtype in large_littlefs_32MB.csv`**  
  *Fixed filesystem partition table definitions, enabling seamless out-of-the-box LittleFS VFS mounting for 32MB flash modules.*

### 🔹 [NVIDIA (`NVIDIA/cuda-samples`)](https://github.com/NVIDIA/cuda-samples) — *6.4k+ ⭐*
* **[PR #462](https://github.com/NVIDIA/cuda-samples/pull/462) — `fix(deviceQuery): fix invalid Python print formatting syntax in post-build script`**  
  *Fixed invalid string formatting syntax in Python utility script under `1_Utilities/deviceQuery/`.*

### 🔹 [Arduino Foundation (`arduino/ArduinoCore-API`)](https://github.com/arduino/ArduinoCore-API) — *1.2k+ ⭐*
* **[PR #282](https://github.com/arduino/ArduinoCore-API/pull/282) — `fix(IPAddress): remove redundant condition in fromString6`**  
  *Optimized C++ IPv6 parsing logic by removing tautological bounds checks in core IP address manipulation routines.*

### 🔹 [OpenCV Foundation (`opencv/opencv`)](https://github.com/opencv/opencv) — *78.5k+ ⭐*
* **[PR #29978](https://github.com/opencv/opencv/pull/29978) — `doc(js_tutorials): fix broken precompiled opencv.js download URLs`**  
  *Resolved precompiled WebAssembly distribution endpoints across official OpenCV 4.x/5.x documentation pipelines.*

---

## 💻 Featured Projects

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
| **Hardware & Peripherals** | `ESP32-S3/C6/P4` &bull; `STM32 Cortex-M` &bull; `I2C` &bull; `SPI` &bull; `UART` &bull; `RMII Ethernet` &bull; `CAN/TWAI` &bull; `DMA` |
| **Robotics & Vision** | `Modified Flood-Fill` &bull; `A* Search` &bull; `45° Diagonal Smoothing` &bull; `OpenCV` &bull; `ToF/IR Sensor Fusion` |
| **Developer Tools** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) ![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat&logo=cmake&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white) |

</div>

---

<div align="center">

### 📊 GitHub Activity

<img src="https://github-readme-stats.vercel.app/api?username=spidyy19&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" width="48%" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=spidyy19&layout=compact&theme=tokyonight&hide_border=true" width="48%" />

<br/>

*Designed & engineered by **Pruthvi Jadhav** &bull; Always open to discussing low-level systems, firmware, and robotics opportunities.*

</div>
