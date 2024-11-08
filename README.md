# Just a little game of snake

This is a little game of snake written in Python. I wanted to make a small, self-contained program to practice common conventions and scripting across multiple files. This project originated when I was playing around with GPT Engineer, and wanted to test the prompt results and polish up my process for git commits. The original results were very bare-bones and did not function, but gave me an opportunity to improve my review and debug skills, as I was able to treat the original result as if it were code written by a different person. The code has been significantly overhauled and I consider it to be written by myself, not AI-generated code. I got to learn the library pygame and interact with graphics elements! Overall, this was an interesting project, taking pre-written code and identifying bugs, cleaning up repetition, reworking logic, etc. 

Also, the game itself is kind of fun.

## Getting Started
* The game should be able to run through a terminal window, and theoretically should automatically run if opened from the containing folder. 
* The "snake" (represented by green blocks) will automatically start moving upon the game running.

How to play:
Navigate the snake "head" to "eat" the red "pellets" to score points (maybe excessive quoting here, but I'm not going to pretend this game is any more visually complicated than solid blocks of color, haha). Game over will occur if you navigate the snake "head" so that it runs into any part of it's body. Running into a wall will halt movement.

Controls:
* Movement = Arrow keys
* If you trigger game over, restart with "R" or quit with "Q"


### Dependencies

* Python 3.11.4
* The pygame module

### Bugs & Future Updates

* BUG: Once the snake has grown longer than 2 segments, game over will occur if you navigate the "head" backwards into the first segment of the body. In the future, I hope to update this so that no action occurs; for example, the "head" should only have 3 directions of movement, rather than a 4th that automatically fails.
* At some point I want to add venv to this game so it doesn't require dependencies.

## Version History

* 0.1
    * Initial and probably only release

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg

## Acknowledgments

* [gpt-engineer](https://github.com/AntonOsika/gpt-engineer)
