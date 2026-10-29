# Music Assistant (Quiz Test)

Test build of Music Assistant that adds the **Title Reveal** game to the Music Quiz plugin:
the title of the playing song is shown as letter placeholders, more letters are uncovered
while the song plays, small typos are accepted and earlier correct guesses score more points.

## Before you start

- **Stop the official Music Assistant add-on** while this one runs. Both use the host
  network and the same ports (8095, 8097, Sendspin), so they cannot run at the same time.
- This add-on keeps its own data. You set up Music Assistant from scratch here; your
  library and settings in the official add-on are left untouched.
- This is a self-built image, so Music Assistant reports it as an unsupported installation,
  and providers that rely on the credentials bundled into official releases may not work.

## Connecting Spotify (and other providers that need credentials)

Official releases ship shared credentials for some providers; this build cannot. Without
them, adding Spotify fails with "client_id not present". Use your own Spotify app instead:

1. Open the [Spotify developer dashboard](https://developer.spotify.com/dashboard) and
   create an app.
2. Add the redirect URI `https://music-assistant.io/callback`, tick **Web API** and save.
3. Copy the app's **Client ID** into the add-on option **Spotify client ID** and restart
   the add-on. Then add the Spotify provider in Music Assistant as usual.

Other providers can get their credentials through **Extra app variables** as `name=value`.

## Testing the quiz

1. Enable the **Music Quiz** plugin under Settings → Providers.
2. Open the Music Quiz, pick **Title Reveal**, select some music and create the game.
3. Scan the QR code with a phone to join as a guest. Choose remote playback to have
   every guest listen on their own device through Sendspin.
