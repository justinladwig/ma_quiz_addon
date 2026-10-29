# Music Assistant Quiz – test add-on repository

Home Assistant add-on repository to test the Music Quiz **Title Reveal** game before it is
proposed upstream.

## Install

1. In Home Assistant go to **Settings → Add-ons → Add-on Store**, open the ⋮ menu,
   choose **Repositories** and add `https://github.com/justinladwig/music-assistant-quiz-addon`.
2. Install **Music Assistant (Quiz Test)**. Stop the official Music Assistant add-on first,
   both cannot run at the same time.

## How the image is built

The add-on does not build anything on your Home Assistant device. The workflow in
`.github/workflows/build.yml` builds the image on GitHub Actions and pushes it to
`ghcr.io/justinladwig/music-assistant-quiz:<version>`:

1. builds the frontend wheel from `justinladwig/frontend` (branch `music-quiz-title-reveal`),
2. builds the server wheel from `justinladwig/server` (branch `music-quiz-title-reveal`),
3. builds the image with the server's own `Dockerfile` and installs the custom frontend on top.

The sources are set in `sources.env`.

## Publishing a new test build

1. Push new commits to the server and/or frontend branch.
2. Raise `version` in `music_assistant_quiz/config.yaml` (and add a `CHANGELOG.md` entry).
3. Push. The workflow builds the image tagged with that version (takes a while, arm64 is
   emulated), then Home Assistant offers the update.

The workflow can also be started by hand under **Actions → Build add-on image → Run workflow**.

After the very first build, open the package `music-assistant-quiz` on your GitHub profile
(**Packages**), go to **Package settings** and set the visibility to **Public**, otherwise
Home Assistant cannot pull the image.
