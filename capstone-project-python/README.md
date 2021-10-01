<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Companion README</h3>

  <p align="center">
    The readme for the Companion (Client Side Python Application)
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This application is supposed to run on the computer of a player, ideally a coach who has an overview of all players of the team.
It is important to keep it running while a game is ongoing, since it takes care of reading in data from the game screen.

### Built With

* [Python](https://www.python.org/)
* [TKinter](https://docs.python.org/3/library/tkinter.html)
* [OBS](https://obsproject.com/)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.x installation
* PIP package installer and virtualenv with virtualenv wrapper -> [windows](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/), [mac](https://medium.com/@viviennediegoencarnacion/managing-python-virtual-environments-on-mac-using-pyenv-5fdd34951fcd)
* TFOD API -> https://towardsdatascience.com/how-to-install-tensorflow-2-object-detection-api-on-windows-2eef9b7ae869
* Latest OBS version with the virtual camera plugin -> https://obsproject.com/

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Mayson12381/Capstone-Project.git
   ```
2. Install libraries (inside virtualenv)
   ```sh
   pip install -r requirements.txt
   ```
3. Setup OBS and virtualcam with this video

* https://youtu.be/uMo2eyu5zk4

4. Check the installation with the following command:
   ```sh
   py helper_modules\video_processor.py test_camera_id
   ```

5. Add the firebase service account file to the *helper_modules* folder



<!-- USAGE EXAMPLES -->
## Usage

To have a practical tutorial on how to get the software up and running, I've recored a video outlining these steps ->



<!-- TEST EXAMPLES -->
## Test

- Testing
   ```sh
   python -m unittest discover -s tests
   ```

- Testing with coverage
   ```sh
   coverage run -m unittest discover -s tests
   ```

- Viewing reports on coverage
   ```sh
   coverage report
   ```



<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch with the **'comp' prefix** (`git checkout -b comp/feature/new-feature`)
3. Commit your Changes considering the **git guidelines** (`git commit -m ':sparkles: [comp] - feat: New Feature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
