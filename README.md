# PwLaunch

An Ableton Live 10 remote script to be used with a Novation Launchpad mk2

## Development

_This assumes one knows how to add a remote script to the ableton live remote
scripts directory_

Create a file named `config.json` in the home directory. Put the following
contents in it:

```json
{
  "width": 1,
  "height": 1
}
```

Replace `PwLaunch.py:33` with the correct path to you home directory. The line
is as follows: `/users/berry/config.json`

Replace `PyLaunch.py:46` with the correct path to your home directory. The line
is as follows: `/users/berry/pwlaunch.txt`

To see the logs, open a terminal window an return

```bash
$ tail -f pwlaunch.txt
```

## Resources

[Unofficial API docs](https://julienbayle.studio/PythonLiveAPI_documentation/Live10.0.2.xml)
[Remote Script Repos](https://github.com/gluon/AbletonLive10_MIDIRemoteScripts)
