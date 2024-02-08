<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<h1 align="center">Youtube Playlist Organizer</h1>

  <p align="center">
  This is a small python script that creates a youtube playlist.
    <br />
    <a href="https://github.com/aaron-kristopher/youtube-playlist-organizer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/aaron-kristopher/youtube-playlist-organizer/issues">Report Bug</a>
    ·
    <a href="https://github.com/aaron-kristopher/youtube-playlist-organizer/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#to-fix">To Fix</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

**YouTube Playlist Organizer for TV Series**

This project helps you easily create and manage playlists for TV series on YouTube.
It's designed to be a user-friendly tool for anyone who wants to ditch the frustrating
autoplay shuffle and watch their favorite series in chronological order.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Before diving into the world of automated TV series playlist, let's ensure you
have the necessary tools.

### Prerequisites

-   **Python 3:** This project is built using [Python 3](https://www.python.org/downloads/)
-   **Python Virtual Environment:** Using a virtual environment keeps your script's
    dependencies isolated and avoids conflicts with other system libraries. Watch this
    video for setting it up in [Windows](https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer), and this for [Mac and Linux](https://www.youtube.com/watch?v=Kg1Yvry_Ydk&ab_channel=CoreySchafer)
-   **Required Libraries:** Install the Python libraries listed in the `requirements.txt`
    file. This include the Google API Client Library for Python, essential for interacting
    with the YouTube Data API.
-   **YouTube Data API Key:** You'll need a free YouTube Data API v3 key to
    authenticate your script and access video information. - Once you have your own API Key, don't forget to set it in your environment variables.
    You can put it in your `~/.bash_profile` or `~/.profile` on Mac and Linux.

        ```bash
        export SECRET_API_KEY="YOUR_SECRET_API_KEY"
        ```

### Installation

1. Get a free API Key at [Google Cloud API Library](https://console.cloud.google.com/apis/library?project=kinetic-axle-411403)
2. Clone the repo
    ```sh
    git clone https://github.com/aaron-kristopher/youtube-playlist-organizer.git
    ```
3. Install pip packages
    ```sh
    pip install google-api-python-client
    ```
4. Enter your API in `api_client.py`
    ```python
    SECRET_API_KEY = "ENTER YOUR API";
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Currently, the program sorts an existing playlist in ascending order. This assumes
that the playlist you provide it is public and has episode numbers. The program
creates a new playlist with the videos sorted.

> NOTE: The program is still in development and is not yet finished

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
inclued
## Roadmap

-   [x] Automatic Episode Retrieval
-   [x] Chronological Ordering
-   [x] Video Filtering for None Episodic Videos
-   [x] Custom Playlist Creation
-   [ ] New Features...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TO FIX -->

## To Fix

-   [ ] Remove Duplicate Episodes
-   [ ] Track Last Episode Before Quota
-   [ ] Continue From Last Episode

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

This project is still under development. Contributions are what make the open
source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and
create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Aaron Lim - aaron.lim.cstr@gmail.com

Project Link: [https://github.com/aaron-kristopher/youtube-playlist-organizer](https://github.com/aaron-kristopher/youtube-playlist-organizer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[license-shield]: https://img.shields.io/github/license/aaron-kristopher/youtube-playlist-organizer.svg?style=for-the-badge
[license-url]: https://github.com/aaron-kristopher/youtube-playlist-organizer/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/aaron-lim-88a478259/
