<div align="center">

# Hi, I'm Pruthvi Jadhav 👋

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&duration=2800&pause=800&color=38BDF8&center=true&vCenter=true&width=700&lines=Embedded+Systems+%26+Firmware+Engineer;Low-Level+C%2B%2B+%E2%80%A2+FreeRTOS+%E2%80%A2+ARM+Cortex-M;Upstream+Contributor+to+Espressif%2C+NVIDIA+%26+OpenCV" alt="Typing Header" />
</a>

<br/><br/>

[![GitHub followers](https://img.shields.io/github/followers/spidyy19?label=Followers&style=for-the-badge&color=0284c7&logo=github)](https://github.com/spidyy19)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)
[![Email](https://img.shields.io/badge/Email-jadhavpruthvi828%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jadhavpruthvi828@gmail.com)
[![Location](https://img.shields.io/badge/Location-India-FF9933?style=for-the-badge&logo=googlemaps&logoColor=white)](#)

<br/>

```cpp
#include <iostream>

struct SystemsEngineer {
    const char* name          = "Pruthvi Jadhav";
    const char* domain        = "Embedded Firmware, Real-Time Systems & Autonomous Robotics";
    const char* core_stack    = "C++17/20, FreeRTOS, ESP-IDF, STM32 HAL, CUDA";
    const char* open_source   = "Espressif Systems (arduino-esp32), NVIDIA, Arduino, OpenCV";
};
```

---

### 🏆 GitHub Trophies

<img src="https://github-profile-trophy.vercel.app/?username=spidyy19&theme=tokyonight&no-frame=true&no-bg=true&column=6" width="100%" />

</div>

---

## 📌 About Me

I am a systems-focused engineer specializing in **low-level C++, real-time embedded firmware, and deterministic robotics navigation**.

* ⚡ **Upstream Open Source:** Active contributor to core HAL and drivers for **Espressif Systems** (`arduino-esp32`), **NVIDIA** (`cuda-samples`), **Arduino** (`ArduinoCore-API`), and **OpenCV**.
* 🏎️ **Autonomous Robotics:** Creator of **[TARS-MazeNav](https://github.com/pruthvi828/tars-maze-navigation)** — an embedded micromouse navigation engine (<2KB static RAM) with 45° diagonal kinematics and 60 FPS Web Studio.
* 🔭 **Core Specialties:** Interrupt Service Routines (ISRs), FreeRTOS concurrency & memory safety, peripheral drivers (I2C/SPI/UART/RMII/CAN), and potential field pathfinding algorithms.

---

## 🚀 Upstream Open Source Contributions

<table>
  <thead>
    <tr>
      <th>Organization / Repo</th>
      <th>Pull Request</th>
      <th>Status</th>
      <th>Technical Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Espressif Systems</b><br/><code>espressif/arduino-esp32</code><br/><i>14.5k+ ⭐</i></td>
      <td><a href="https://github.com/espressif/arduino-esp32/pull/12931"><b>PR #12931</b></a><br/><code>fix(zigbee): zero-init report_attr_cmd</code></td>
      <td><img src="https://img.shields.io/badge/Status-Review-yellow?style=flat-square" /></td>
      <td>Fixed uninitialized stack memory defect across 12 C++ Zigbee endpoint classes (<code>ZigbeeAnalog</code>, <code>ZigbeeTempSensor</code>), enforcing standard manufacturer code assignment.</td>
    </tr>
    <tr>
      <td><b>Espressif Systems</b><br/><code>espressif/arduino-esp32</code><br/><i>14.5k+ ⭐</i></td>
      <td><a href="https://github.com/espressif/arduino-esp32/pull/12911"><b>PR #12911</b></a><br/><code>feat(timer): std::function callbacks</code></td>
      <td><img src="https://img.shields.io/badge/Status-Review-yellow?style=flat-square" /></td>
      <td>Engineered modern C++ lambda callback support for <code>timerAttachInterrupt()</code>, resolving ISR use-after-free race conditions across ESP32-S3/C6/P4.</td>
    </tr>
    <tr>
      <td><b>Espressif Systems</b><br/><code>espressif/arduino-esp32</code><br/><i>14.5k+ ⭐</i></td>
      <td><a href="https://github.com/espressif/arduino-esp32/pull/12929"><b>PR #12929</b></a><br/><code>fix(partitions): LittleFS subtype</code></td>
      <td><img src="https://img.shields.io/badge/Status-Review-yellow?style=flat-square" /></td>
      <td>Corrected partition table definitions in <code>large_littlefs_32MB.csv</code>, enabling out-of-the-box LittleFS VFS mounting for 32MB flash modules.</td>
    </tr>
    <tr>
      <td><b>NVIDIA</b><br/><code>NVIDIA/cuda-samples</code><br/><i>6.4k+ ⭐</i></td>
      <td><a href="https://github.com/NVIDIA/cuda-samples/pull/462"><b>PR #462</b></a><br/><code>fix(deviceQuery): python formatting</code></td>
      <td><img src="https://img.shields.io/badge/Status-Review-yellow?style=flat-square" /></td>
      <td>Fixed invalid string formatting syntax error in Python post-build utility under <code>1_Utilities/deviceQuery/</code>.</td>
    </tr>
    <tr>
      <td><b>Arduino Foundation</b><br/><code>arduino/ArduinoCore-API</code><br/><i>1.2k+ ⭐</i></td>
      <td><a href="https://github.com/arduino/ArduinoCore-API/pull/282"><b>PR #282</b></a><br/><code>fix(IPAddress): IPv6 tautology</code></td>
      <td><img src="https://img.shields.io/badge/Status-Review-yellow?style=flat-square" /></td>
      <td>Optimized core C++ IPv6 parsing logic by removing tautological bounds checks in <code>fromString6()</code>.</td>
    </tr>
    <tr>
      <td><b>OpenCV Foundation</b><br/><code>opencv/opencv</code><br/><i>78.5k+ ⭐</i></td>
      <td><a href="https://github.com/opencv/opencv/pull/29978"><b>PR #29978</b></a><br/><code>doc(js): fix opencv.js URLs</code></td>
      <td><img src="https://img.shields.io/badge/Status-Review-yellow?style=flat-square" /></td>
      <td>Resolved precompiled WebAssembly distribution endpoints across official OpenCV 4.x/5.x documentation pipelines.</td>
    </tr>
  </tbody>
</table>

---

## 💻 Featured Projects

<table>
  <tr>
    <td width="65%">
      <h3>🏁 TARS-MazeNav — Autonomous Micromouse Engine</h3>
      <p>High-performance autonomous maze exploration and kinematics engine written in <b>C++ and Python</b> with real-time 60 FPS simulation studio.</p>
      <ul>
        <li><b>Modified Flood-Fill:</b> Dynamic Manhattan potential field recalculation with directional momentum bias.</li>
        <li><b>45° Diagonal Kinematics:</b> Smooth trajectory compression with trapezoidal acceleration profiling (<i>v<sub>max</sub> = 3.5 m/s, a = 12 m/s²</i>).</li>
        <li><b>Embedded Firmware:</b> Zero dynamic heap allocation operating under strict <b>&lt; 2 KB static RAM</b> on ESP32/STM32.</li>
        <li><b>Web Audio SFX:</b> Integrated in-browser Web Audio synthesizer & particle explosion engine.</li>
      </ul>
      <p>
        <a href="https://pruthvi828.github.io/tars-maze-navigation/"><b>👉 Launch Live 60 FPS Interactive Studio</b></a> &bull;
        <a href="https://github.com/pruthvi828/tars-maze-navigation"><b>View Source Code</b></a>
      </p>
    </td>
    <td width="35%" align="center">
      <img src="https://img.shields.io/badge/60%20FPS-Canvas%20Studio-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white" /><br/><br/>
      <img src="https://img.shields.io/badge/Target-ESP32%20%7C%20STM32-red?style=for-the-badge" /><br/><br/>
      <img src="https://img.shields.io/badge/Memory-%3C2KB%20Static%20RAM-34d399?style=for-the-badge" />
    </td>
  </tr>
</table>

---

## 🛠️ Technical Arsenal

<div align="center">

| Category | Technologies & Tools |
| :--- | :--- |
| **Languages** | ![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white) ![C++](https://img.shields.io/badge/C++17/20-00599C?style=flat-square&logo=c%2B%2B&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![ARM Assembly](https://img.shields.io/badge/ARM_Assembly-0091BD?style=flat-square&logo=arm&logoColor=white) |
| **Embedded & RTOS** | ![FreeRTOS](https://img.shields.io/badge/FreeRTOS-34d399?style=flat-square) ![ESP-IDF](https://img.shields.io/badge/ESP--IDF-E7352C?style=flat-square&logo=espressif&logoColor=white) ![Arduino Core](https://img.shields.io/badge/Arduino_Core-00979D?style=flat-square&logo=arduino&logoColor=white) ![STM32 HAL](https://img.shields.io/badge/STM32_HAL-03234B?style=flat-square&logo=stmicroelectronics&logoColor=white) |
| **Peripherals & Protocols** | `ESP32-S3/C6/P4` &bull; `STM32 Cortex-M` &bull; `I2C` &bull; `SPI` &bull; `UART` &bull; `RMII Ethernet` &bull; `CAN/TWAI` &bull; `Zigbee ZCL` &bull; `DMA` |
| **Robotics & Vision** | `Modified Flood-Fill` &bull; `A* Search` &bull; `45° Diagonal Kinematics` &bull; `OpenCV` &bull; `Sensor Fusion` |
| **Developer Tools** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat-square&logo=cmake&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) |

</div>

---

<div align="center">

### 📊 GitHub Metrics & Analytics Infographic (`lowlighter/metrics`)

<p align="center">
  <img src="https://metrics.lecoq.io/spidyy19?template=classic&base=header%2C+activity%2C+community%2C+repositories%2C+metadata&config_timezone=Asia%2FKolkata" width="100%" alt="GitHub Metrics Infographic" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=spidyy19&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" width="49%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=spidyy19&theme=tokyonight&hide_border=true" width="49%" />
</p>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=spidyy19&layout=compact&theme=tokyonight&hide_border=true" width="50%" />

<br/><br/>

*Architected & engineered by **Pruthvi Jadhav** &bull; Open to systems firmware, C++, and autonomous robotics engineering opportunities.*

</div>
