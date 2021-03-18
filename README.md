<!--
Using thr Best-README-Template
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/luis-gustta/adbtv/">
    <img src="images/adbtv21.png" alt="Logo" width="277" height="264">
  </a>


  <h3 align="center">ADB Python Module</h3>

  <p align="center">
    An easy way to control Android (TV) devices remotely using Python
    <br />
    <br />
    <a href="https://github.com/luis-gustta/adbtv/">Examples</a>
    ·
    <a href="https://github.com/luis-gustta/adbtv/issues">Report Bug</a>
    ·
    <a href="https://github.com/luis-gustta/adbtv/issues">Request Feature</a>
  </p>

</p>



<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## About The Project

Like any project, this one have started to solve a simple problem,
<h6 align="center">"How can I integrate my AndroidTV with smart home applications, without using Google Home"</h6> So here it is, a simple solution (or kind of), just using Python and Google's Android Debug Bridge. Of course is possible to use this to control any android device, not just the ones running AndroidTV. Using a device like a Raspberry Pi, you can easily control a lot of Android devices with Alexa, for example, and create routines; since Alexa is not natively compatible (yet?!) with AndroidTV and Chromecast devices.

<!-- GETTING STARTED -->
## Getting Started

Clone this project and you're done:

  ```sh
  git clone https://github.com/luis-gustta/adbtv.git
  ```

Using `pip`:
  ```sh
python -m pip install adbtv
  ```
or:
  ```sh
python -m pip install git+https://github.com/luis-gustta/adbtv.git
  ```
### Prerequisites

The following modules are requirements to AdbTV:

* **`os`**  <font size="2">and</font> **`time`**

* **`typing`**:
  ```sh
  python3 -m pip install typing
  ```

#### **ADB:**

Also, you (of course) must have ADB installed. 

**Windows users:**

If you're using Windows, you can download it from:
[https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools).

**Linux users:**

If you're using Linux, you can download it using:

* **Debian-based Linux:**
  ```sh
  sudo apt install android-tools-adb
  ```

* **Fedora/SUSE-based Linux:**
  ```sh
  sudo yum install android-tools
  ```

## Usage

This module was built to be simple and intuitive, every function have a little "documentation" and is very easy to use. Here's an example:

```python
import adbtv as adb

adb.connect('ip','port')
adb.shell_cmd('echo hello world')
```

Because the main focus of this module is to control AndroidTV systems, most commands have been optimized for this. Another example:

```python
import adbtv as adb

adb.connect('ip','port')
adb.launch_app('NETFLIX')
```

_More examples about usage can be found under the [examples](https://github.com/luis-gustta/adbtv/examples) folder._


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Luis Gustavo - lang.gaiato@ufrgs.br

Project Link: [https://github.com/luis-gustta/adbtv/](https://github.com/luis-gustta/adbtv/)



<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [ADB](https://developer.android.com/studio/command-line/adb)
* [Imgbot](https://imgbot.net/docs/)
* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/luis-gustta/adbtv.svg?style=for-the-badge
[contributors-url]: https://github.com/luis-gustta/adbtv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/luis-gustta/adbtv.svg?style=for-the-badge
[forks-url]: https://github.com/luis-gustta/adbtv/network/members
[stars-shield]: https://img.shields.io/github/stars/luis-gustta/adbtv.svg?style=for-the-badge
[stars-url]: https://github.com/luis-gustta/adbtv/stargazers
[issues-shield]: https://img.shields.io/github/issues/luis-gustta/adbtv.svg?style=for-the-badge
[issues-url]: https://github.com/luis-gustta/adbtv/issues
[license-shield]: https://img.shields.io/github/license/luis-gustta/adbtv.svg?style=for-the-badge
[license-url]: https://github.com/luis-gustta/adbtv/master/LICENSE.txt
