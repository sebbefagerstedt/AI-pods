# Rendering episodes on your own computer

Turning a script into an MP3 costs no Claude credits if you run it yourself. Claude writes the scripts, which is what uses credits; your computer does the slow part.

## Where the time goes

Episode 9 (29.6 minutes of audio) took about 5.5 hours in the cloud, on a machine with no graphics card:

| Step | Time | Can be cut? |
|---|---|---|
| Generating the speech | about 2.3 h | A graphics card makes it much faster. |
| Retakes when the check finds a problem | about 2.5 h | Yes: `--takes 1` keeps the first take. |
| Checking the finished file | about 40 min | Yes: skip it and just listen. |

With `--takes 1`, you'll sometimes hear a line in the other host's voice, a short gap or a garbled word. VibeVoice also sometimes adds faint background music; retakes don't fix that either.

## What you need

- A Mac with Apple silicon (M1 or later, 16 GB of memory or more), or a PC with an Nvidia graphics card (8 GB or more) running Linux. On Windows, use WSL (Windows Subsystem for Linux). Without either, it still works on the CPU, just slowly.
- About 15 GB of free disk space: about 5 GB of Python packages and 6 GB of voice models, downloaded on the first run.
- Git, ffmpeg and uv (a Python installer).

The Mac and Nvidia paths haven't been tested yet, only the CPU one. If something fails, paste the error to Claude.

## Setup (once)

On a Mac, in Terminal (install [Homebrew](https://brew.sh) first if you don't have it):

```sh
brew install git ffmpeg uv
```

On Linux or WSL:

```sh
sudo apt install git ffmpeg
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, on either:

```sh
git clone https://github.com/sebbefagerstedt/AI-pods.git
cd AI-pods
bash tools/setup.sh
```

Once the repo is private, `git clone` asks you to sign in to GitHub.

## Test it

Render the short sample conversation (about a minute):

```sh
.venv/bin/python tools/render.py samples/sample.md samples/test.mp3 --takes 1
```

The first run downloads the models, so give it a while. The log shows how long each segment took, for example `[1/1] 60 s of audio, 90 s so far`. Divide the seconds so far by the seconds of audio to see how many times slower than real time your computer is. The cloud machine is about 4.7.

## Render an episode

```sh
.venv/bin/python tools/render.py episodes/02-machine-learning/script.md episodes/02-machine-learning/02-machine-learning.mp3 --takes 1 --title "Episode 2: Machine learning"
```

Use the episode's real folder name. Leave the computer on and awake while it runs (on a Mac, prefix the command with `caffeinate -i`). If it stops, run the same command again: it picks up from the last finished segment.

Drop `--takes 1` for the cloud's quality: up to three takes per segment when the check finds a problem.

Afterwards, put the MP3 in the repo:

```sh
git add episodes && git commit -m "Render episode 2" && git push
```

Or just copy the MP3 to your phone.
